"""
實務上Django-form上傳圖片檔案上傳至S3前的預處理
1. 檢查檔案類型'iamge/jpeg'
2. 檢查檔案大小
3. 檢查圖片旋轉資訊(iPhone圖片居多)
4. 縮小圖片此寸
5. 傳S3前檔案重置(seek 0)
"""
def _validate_image_file(file):
    if file is None:
        raise Exception('檔案不符(10)')

    # 檢查content_type
    if file.content_type not in ['image/jpeg']:
        raise Exception(f'檔案不符({file.content_type})')

    # 檢查檔案大小
    max_size = 10 * 1024 * 1024  # 10MB
    if file.size > max_size:
        raise Exception(f'檔案太大({file.size})')

    # 讀圖片
    img = Image.open(BytesIO(file.read()))

    # 解決由iPhone拍照上傳的圖片內建旋轉問題(旋轉)
    img = ImageOps.exif_transpose(img)
    
    # 此寸太大調整
    (width, height) = img.size
    while width > 600.0 or height > 600.0:
        width *= 0.9
        height *= 0.9
    img = img.resize((int(width), int(height)))

    # save
    output_io = BytesIO()
    img.save(output_io, 'JPEG', quality=70)
    new_file = File(output_io, f'{secrets.token_hex(10)}.jpg')

    # 避免上傳S3時錯誤
    # https://stackoverflow.com/questions/51468132/baddigest-when-calling-the-putobject-operation-s3-boto
    new_file.seek(0)

    return new_file

myfile = request.FILES.get('myfile', None)
ok_file = _validate_image_file(myfile)
bucket.put_object(Key='user1/myfile.jpg', Body=ok_file)