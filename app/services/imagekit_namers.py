import os
from django.conf import settings
from imagekit.utils import format_to_extension, suggest_extension


def source_name_as_path(generator):
    source_filename = getattr(generator.source, 'name', None)
    ext = suggest_extension(source_filename or '', generator.format)
    dir = settings.IMAGEKIT_CACHEFILE_DIR
    return os.path.normpath(os.path.join(dir,
                                         '%s%s' % (generator.get_hash(), ext)))


def hash(generator):
    format = getattr(generator, 'format', None)
    ext = format_to_extension(format) if format else ''
    return os.path.normpath(os.path.join(settings.IMAGEKIT_CACHEFILE_DIR,
                                         '%s%s' % (generator.get_hash(), ext)))
