#Generate the QR using the python qrcode module
#Coded by: Dhanush K
import qrcode


data = input("Enter the data for the QR code: ")


qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)


img = qr.make_image(fill_color="white", back_color="transparent")

img.save("qr_code.png")

print("QR code saved as qr_code.png")