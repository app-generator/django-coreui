from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File
import qrcode

def createQRCode(request, data):
    user = request.user
    qrcode_img = qrcode.make(user)
    canvas = Image.new('RGB',(290, 290), 'white')
    draw = ImageDraw.Draw(canvas)
    canvas.paste(qrcode_img)
    fname = f'qr-code-{user}.png'
    buffer = BytesIO()
    canvas.save(buffer,'PNG')
    canvas.close()