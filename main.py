import segno 
qrcode = segno.make_qr("www.theverge.com")
qrcode.save('theverge.png',scale=10)