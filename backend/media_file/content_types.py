SUPPORTED_VIDEO_TYPES = ['video/x-msvideo', 'application/vnd.osgeo.mapguide.package', 'video/mpeg', 'video/x-flv',
                         'video/x-m4v', 'video/mp4', 'application/mp4', 'video/quicktime', 'video/x-ms-wmv', 'video/ogg', 'video/webm', 'video/x-sgi-movie', ]

SUPPORTED_DOCUMENT_TYPES = ['application/pdf',
                            'application/msword', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                            'application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                            'application/vnd.ms-powerpoint', 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
                            'application/zip', 'application/x-7z-compressed', 'application/x-rar-compressed', ]

SUPPORTED_AUDIO_TYPES = ['audio/mpeg', 'audio/wav', 'audio/aac', ]

SUPPORTED_IMAGE_TYPES = ['image/gif', 'image/jpeg', 'image/png', 'image/svg+xml', 'image/webp', ]

OTHER_CONTENT_TYPES = ['application/json', 'text/plain', 'application/xml', 'text/xml']

SUPPORTED_CONTENT_TYPES = SUPPORTED_VIDEO_TYPES + SUPPORTED_DOCUMENT_TYPES + SUPPORTED_AUDIO_TYPES + SUPPORTED_IMAGE_TYPES + OTHER_CONTENT_TYPES
