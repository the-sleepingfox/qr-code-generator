import qrcode
from io import BytesIO
from django.core.files import File

def generate_qr_code(text):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    buffer = BytesIO()
    img.save(buffer, 'PNG')
    return File(buffer, name='qr_code.png')
