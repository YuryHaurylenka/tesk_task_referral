from django.shortcuts import redirect, render


def home_view(request):
    if request.session.get("access_token"):
        return redirect("profile")
    else:
        return redirect("request_code")


def custom_404(request, exception=None):
    return render(request, "404.html", status=404)
