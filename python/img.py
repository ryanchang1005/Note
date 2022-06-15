from io import BytesIO
from PIL import Image, ImageOps
from django.core.files import File
def handle_image_file(file):
    # 檢查content_type
    if file.content_type not in ['image/jpeg', 'image/png']:
        raise Exception(f'檔案不符({file.content_type})')

    # 檢查檔案大小
    max_size = 10 * 1024 * 1024  # 10MB
    if file.size > max_size:
        raise Exception(f'檔案太大({file.size})')
    
    # 讀圖片
    img = Image.open(BytesIO(file.read()))
    img = img.convert('RGB')  # 轉成RGB(JPG只有RGB)(PNG會有RGBA)
    img = ImageOps.exif_transpose(img)  # 解決圖片內建旋轉問題
    
    # 等比例縮放圖片尺寸
    (width, height) = img.size
    while width > 1024.0 or height > 1024.0:
        width *= 0.9
        height *= 0.9
    img = img.resize((int(width), int(height)))

    # save
    output_io = BytesIO()
    img.save(output_io, 'JPEG', quality=70)
    new_file = File(output_io, 'uploaded.jpg')
    
    # 避免上傳S3時錯誤
    # https://stackoverflow.com/questions/51468132/baddigest-when-calling-the-putobject-operation-s3-boto
    new_file.seek(0)
    
    return new_file