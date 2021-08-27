from django.http import JsonResponse
from datetime import datetime
from . import messages, exceptions

class TokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    # @query_debugger
    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 401:
            return JsonResponse({
                "data": None,
                "error_code": response.status_code,
                "message": messages.EXPIRED_SESSION,
                "current_time": datetime.now(),
            })

        if response.status_code == 403:
            return JsonResponse({
                "data": None,
                "error_code": response.status_code,
                "message": messages.PERMISSION_DENIED,
                "current_time": datetime.now(),
            })

        if response.status_code == 404:
            if 'Not Found' == response.reason_phrase:
                return JsonResponse({
                    "data": None,
                    "error_code": response.status_code,
                    "message": messages.PAGE_NOT_FOUND,
                    "current_time": datetime.now(),
                })

        if response.status_code == 405:
            return JsonResponse({
                "data": None,
                "error_code": response.status_code,
                "message": response.data['detail'],
                "current_time": datetime.now(),
            })

        if response.status_code == 302:
            # Handle 302 status_code
            pass
        elif response.status_code != 200:
            return JsonResponse({
                "data": None,
                "error_code": response.status_code,
                "message": messages.CONTACT_ADMIN_FOR_SUPPORT,
                "current_time": datetime.now(),
            })

        return response

    def process_exception(self, request, exception):
        if type(exception) is exceptions.NotFoundException:
            return JsonResponse({
                "data": None,
                "error_code": 404,
                "message": str(exception),
                "current_time": datetime.now(),
            })
        elif type(exception) is exceptions.AuthenticationException:
            return JsonResponse({
                "data": None,
                "error_code": 401,
                "message": str(exception),
                "current_time": datetime.now(),
            })
