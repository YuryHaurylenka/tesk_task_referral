from django.conf import settings
from rest_framework.authentication import get_authorization_header
from rest_framework.exceptions import AuthenticationFailed


class AddAuthorizationHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        secure_endpoints = settings.SECURE_API_ENDPOINTS
        if any(request.path.startswith(endpoint) for endpoint in secure_endpoints):
            auth_header = get_authorization_header(request)
            if not auth_header:
                access_token = request.session.get("access_token")
                if access_token:
                    request.META["HTTP_AUTHORIZATION"] = f"Bearer {access_token}"
                else:
                    raise AuthenticationFailed(
                        "Authentication credentials were not provided."
                    )
        return self.get_response(request)
