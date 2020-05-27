from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def save_player_image(image, id, filename):
    default_storage.save('static/upload/%s/%s' % (id, filename), ContentFile(image.read()))
    return '/static/upload/%s/%s' % (id, filename)

def get_file_type(content_type):
    content_type = str(content_type)
    return '.'+content_type[content_type.find('/') + 1 : len(content_type)]