import requests
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render


def profile_view(request):
    access_token = request.session.get("access_token")
    if not access_token:
        messages.error(request, "You must login to access this page.")
        return redirect("request_code")

    api_url = f"{settings.API_BASE_URL}/users/profile/"
    headers = {"Authorization": f"Bearer {access_token}"}

    if request.method == "POST":
        invite_code = request.POST.get("invite_code")
        activate_url = f"{settings.API_BASE_URL}/users/activate_invite_code/"
        try:
            response = requests.post(
                activate_url, json={"invite_code": invite_code}, headers=headers
            )
            if response.status_code == 200:
                messages.success(request, "Referral code activated successfully!")
            else:
                error_message = response.json().get(
                    "message", "Error activating referral code."
                )
                messages.error(request, error_message)
        except requests.exceptions.RequestException:
            messages.error(
                request, "Could not activate referral code. Please try again."
            )
        return redirect("profile")

    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            user_data = response.json().get("data", {})
            return render(request, "profile.html", {"user": user_data})
        else:
            messages.error(request, "Failed to load profile information.")
            return redirect("request_code")
    except requests.exceptions.RequestException:
        messages.error(request, "Could not load profile. Please try again later.")
        return redirect("request_code")


def request_code_view(request):
    error = None

    if request.method == "POST":
        phone_number = request.POST.get("phone_number")
        api_url = f"{settings.API_BASE_URL}/auth/request_code/"
        try:
            response = requests.post(api_url, data={"phone_number": phone_number})
            response.raise_for_status()
            request.session["phone_number"] = phone_number
            messages.success(request, "Authorization code sent successfully!")
            return redirect("verify_code")
        except requests.exceptions.RequestException as e:
            try:
                error = e.response.json().get("message", "An error occurred.")
            except (ValueError, AttributeError):
                error = "An unknown error occurred."

    return render(request, "request_code.html", {"error": error})


def verify_code_view(request):
    phone_number = request.session.get("phone_number", "")
    error_message = None

    if request.method == "POST":
        code = request.POST.get("code")
        api_url = f"{settings.API_BASE_URL}/auth/verify_code/"
        try:
            response = requests.post(
                api_url, data={"phone_number": phone_number, "code": code}
            )
            if response.status_code == 200:
                data = response.json()
                request.session["access_token"] = data.get("access_token")
                messages.success(request, "You have been logged in successfully.")
                return redirect("profile")
            else:
                error_message = response.json().get(
                    "error", "Invalid code. Please try again."
                )
        except requests.exceptions.RequestException:
            error_message = "Connection error. Please try again later."

    return render(
        request,
        "verify_code.html",
        {"phone_number": phone_number, "error": error_message},
    )


def logout_view(request):
    request.session.flush()
    messages.success(request, "You have been logged out successfully.")
    return redirect("request_code")
