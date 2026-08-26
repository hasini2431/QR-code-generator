import qrcode
from PIL import Image

# -------------------------
# QR CODE GENERATOR
# -------------------------

data = input("Enter text or URL: ")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=5
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(
    fill_color="black",
    back_color="white"
).convert('RGB')

# Add Logo (optional)
try:
    logo = Image.open(r"C:\Users\sathw\OneDrive\Desktop\python\logo.png")

    qr_width, qr_height = img.size

    logo_size = qr_width // 4
    logo = logo.resize((logo_size, logo_size))

    pos = (
        (qr_width - logo_size) // 2,
        (qr_height - logo_size) // 2
    )

    img.paste(logo, pos)

except FileNotFoundError:
    print("logo.png not found. QR generated without logo.")

img.save(r"C:\Users\sathw\OneDrive\Desktop\custom_qr.png")

print("QR Code Saved as custom_qr.png")
print(" ")
hello 