import io
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
import os


def imageResize(file):
    img = Image.open(file)
    original_format = img.format
    original_name = os.path.splitext(file.name)[0]


    # Checking if the image is RGB
    if original_format == 'PNG':
        img = img.convert('RGBA')
        mime_type = 'image/png'
        extension = 'png'
    else:
        # Fallback for other formats (like JPEG)
        img = img.convert('RGB')
        mime_type = 'image/jpeg'
        extension = 'jpg'

    output = io.BytesIO()

    save_params = {'format': original_format}
    if original_format == 'JPEG':
        save_params['quality'] = 60
    elif original_format == 'PNG':
        save_params['optimize'] = True

    img = img.resize((img.width, img.height)) # Keep size or set new dimensions
    img.save(output, **save_params)
    output.seek(0)

    # 3. Return file with correct extension and mime type
    return InMemoryUploadedFile(
        output, 
        'ImageField', 
        f"{original_name}.{extension}", 
        mime_type, 
        len(output.getvalue()), 
        None
    )
    # Resizing and saving the Image
    # height = img.height 
    # width = img.width 
    # img = img.resize((int(width), int(height)))
    # img.save(output, format='JPEG', quality=60)
    # output.seek(0)

    # file = InMemoryUploadedFile(output, 'ImageFile', f"%s.{extension}" % file.name.split('.')[0], f'{mime_type}', len(output.getvalue()), None)

    # return file



