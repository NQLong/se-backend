from .models import Media
from utils import messages, exceptions, validators, enums


def get_media_list(include_deleted=False):
    media_list = Media.objects.all()
    if not include_deleted:
        media_list = media_list.exclude(deleted=True)
    return media_list


def create_media(creator, size, directory, content_type, file_name, storage_type, file=None, access_url=None):
    try:
        media = Media.objects.create(
            creator=creator,
            size=size,
            directory=directory,
            content_type=content_type,
            file_name=file_name,
            file=file,
            storage_type=storage_type,
            thumbnail_size=1,
            access_url=access_url,
        )
        return media
    except Exception as exception:
        raise exceptions.ApplicationException(
            message=messages.UPLOAD_MEDIA_FAILED)
