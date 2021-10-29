
from rest_framework.request import Request
from rest_framework.decorators import (
    api_view as function_base_api,
    action as class_base_api,
    permission_classes
)
import functools

from datetime import datetime
from . import messages, exceptions
from django.http import JsonResponse
from django.db import connection, reset_queries
from django.core.paginator import Paginator

from rest_framework import viewsets
from rest_framework import serializers

PAGE_SIZE = 10
PAGE_SIZE_MAX = 40


class EmptySerializer(serializers.Serializer):
    pass


def paginate_data(request, data):
    page = int(request.data.get("page", 1))
    page_size = int(request.data.get("page_size", PAGE_SIZE))

    # Handle page_size = 'all'
    # page_size = 0 for get all
    if page_size == 0:
        page_size = len(data) + 1
    elif page_size < 0:
        raise exceptions.InvalidArgumentException(messages.NEGATIVE_PAGE_SIZE)
    elif page_size > PAGE_SIZE_MAX:
        raise ValueError(messages.OVER_PAGE_SIZE_MAX + PAGE_SIZE_MAX)

    paginator = Paginator(data, page_size)

    total_pages = paginator.num_pages

    if int(total_pages) < page:
        page_number = page
        content = []
    else:
        current_page = paginator.page(page)
        page_number = current_page.number
        content = current_page.object_list

    total = paginator.count

    response_data = {
        "totalRows": total,
        "totalPages": total_pages,
        "currentPage": page_number,
        "content": content,
        "pageSize": page_size,
    }

    return response_data


class ResponseHandler:
    @classmethod
    def handle(cls, data=None, error_code=0, message=messages.SUCCESS) -> JsonResponse:
        return JsonResponse(
            data={
                "data": data,
                "error_code": error_code,
                "message": message,
                "current_time": datetime.now(),
            }
        )


class ExceptionHandler:
    @classmethod
    def _get_code_and_message(cls, exception: Exception) -> set:
        print('Exceptions: ', exception)

        default_message = (500, messages.CONTACT_ADMIN_FOR_SUPPORT)
        switcher = {
            exceptions.ValidationException: (400, str(exception)),
            exceptions.InvalidArgumentException: (400, str(exception)),
            exceptions.NotFoundException: (404, str(exception)),
            exceptions.AuthenticationException: (401, str(exception)),
            exceptions.NetworkException: (500, str(exception)),
            Exception: (500, str(exception))
        }

        return switcher.get(type(exception), default_message)

    @classmethod
    def handle(cls, exception: Exception) -> JsonResponse:
        error_code, message = cls._get_code_and_message(exception)

        return JsonResponse(
            data={
                "data": None,
                "error_code": error_code,
                "message": message,
                "current_time": datetime.now(),
            }
        )


# Calculate query time and number of query statement
def query_debugger(func):
    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        reset_queries()

        start_queries = len(connection.queries)
        result = func(*args, **kwargs)
        end_queries = len(connection.queries)

        print("Function : " + func.__name__)
        print("Number of Queries : {}".format(end_queries - start_queries))
        return result

    return inner_func


def get_request_data(request: Request):

    if request.method.upper() == 'POST':
        data = request.data
        files = request.FILES
        return data, request.FILES
    else:
        data = request.query_params
        return data, None


def api_view(
    methods,
    url_path,
    exception_handler=True,
    paginate=False,
    schema_param=None,
    query_debug=True,
    permissions=[]
):
    def outer(func):
        api_decor = class_base_api(
            methods=methods, url_path=url_path, detail=False)

        @functools.wraps(func)
        def inner(instance, request, *args, **kwargs):
            print(func)
            try:
                api_function = func
                if query_debug:
                    api_function = query_debugger(api_function)
                if permissions:
                    api_function = permission_classes(permissions)(api_function)
                if schema_param:
                    ...  # swagger hasn't been implemented
                data = api_function(instance, request, *args, **kwargs)
                if paginate:
                    data = paginate_data(data, request)
                return ResponseHandler.handle(data)
            except Exception as exception:
                if exception_handler:
                    return ExceptionHandler.handle(exception)
                raise exception
        return api_decor(inner)
    return outer


class AbstractView(viewsets.GenericViewSet):
    serializer_class = EmptySerializer
