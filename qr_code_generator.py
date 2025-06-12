import qrcode 

# Get data from user
data = input("Enter the text or URL you want to turn into a QR code: ")
# Create the QR code object
qr = qrcode.make(data)

# Create the QR code object
qr = qrcode.make(data)

# Save the QR code image
qr.save("my_qr_code.png")

print("QR Code generated and saved as 'my_qr_code.png'")