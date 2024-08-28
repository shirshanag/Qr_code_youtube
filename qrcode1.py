import qrcode as qr
img=qr.create("https://www.youtube.com/")
img.save("qr_youtube.png")
