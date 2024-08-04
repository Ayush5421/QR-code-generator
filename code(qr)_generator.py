import qrcode

img=qrcode.make("https://www.apple.com")
img.save("apple.png")