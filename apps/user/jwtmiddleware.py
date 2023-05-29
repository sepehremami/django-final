from rest_framework_simplejwt.authentication import JWTStatelessUserAuthentication



class JWtMiddleaare:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    