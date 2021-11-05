import re
from media_file import app_utils as media_utils
from media_file.models import Media
from media_file.content_types import SUPPORTED_CONTENT_TYPES
from media_file.serializers import BaseMediaSerializer
from utils import messages, exceptions
from utils.enums import DirectoryFile, StorageType
from utils.views import query_debugger, paginate_data, AbstractView, api_view
from rest_framework.decorators import action, parser_classes
from rest_framework import parsers
from rest_framework import permissions
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.


class MediaAPI(AbstractView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes=[parsers.MultiPartParser, parsers.FormParser]
    media_create_fields = [
        'file_name', 'description', 'directory', 'digest', 'access_url', 'size', 'content_type'
    ]

    @api_view(methods=['POST'], url_path='create', exception_handler=False)
    def create_media(self, request):
        data = request.POST.dict()
        file = request.FILES.dict().get('media', None)
        print(request.FILES)
        print(request.POST)
        creator = request.user

        media_dict = {
            k: data.get(k, None) for k in self.media_create_fields
            if data.get(k) is not None
        }

        if not file and not media_dict['access_url']:
            raise exceptions.InvalidArgumentException(
                message=messages.EMPTY_FILE)

        if not media_dict.get('file_name'):
            raise exceptions.InvalidArgumentException(
                message=messages.FILE_NAME_EMPTY)

        media_dict['creator'] = creator
        media_dict['storage_type'] = StorageType.EXTERNAL
        media_dict['directory'] = '' if not media_dict['directory'] else media_dict['directory']

        if file:
            media_dict['file'] = file
            media_dict['size'] = file.size
            media_dict['content_type'] = file.content_type
            media_dict['storage_type'] = StorageType.INTERNAL
        else:
            # Handle if user only pass access_url here
            if not media_dict['size']:
                raise exceptions.ValidationException(
                    message=messages.FILE_SIZE_EMPTY)
            if media_dict['content_type'] not in SUPPORTED_CONTENT_TYPES:
                raise exceptions.ValidationException(
                    message=messages.UNSUPPORT_CONTENT_TYPES
                )

            media_dict['storage_type'] = StorageType.EXTERNAL

        new_media = media_utils.create_media(
            **media_dict
        )
        response_data = BaseMediaSerializer(new_media).data

        return response_data


    @api_view(methods=['POST'], url_path='matrix')
    def get_media_list(self, request):
        # data = self.request_handler.handle(request)
        media_list = media_utils.get_media_list()
        response_data = BaseMediaSerializer(media_list, many=True).data
        media_by_page = paginate_data(request, response_data)
        return media_by_page


    @query_debugger
    @action(methods=['POST'], url_path='get', detail=False)
    def get_media(self, request):
        data = self.request_handler.handle(request)
        try:
            uid = data.get_body_value('uid')
            media = Media.objects.get(uid=uid)
        except:
            raise exceptions.NotFoundException(
                message=messages.MEDIA_NOT_FOUND)
        response_data = BaseMediaSerializer(media).data
        media_by_page = paginate_data(request, response_data)
        return self.response_handler.handle(data=media_by_page)

