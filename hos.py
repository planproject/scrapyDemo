import qrcode
img = qrcode.make('http://alethea.cdn.fsociaty.com/1582731418973.mp4')
with open('test.png', 'wb') as f:
    img.save(f)