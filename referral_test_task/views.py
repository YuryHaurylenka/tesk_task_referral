from django.shortcuts import redirect, render


def home_view(request):
    if request.session.get("access_token"):
        return redirect("profile")
    else:
        return redirect("request_code")
