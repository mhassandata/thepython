# import qrcode

# # Create the QR code object
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )

# # Add the YouTube channel URL to the QR code object
# qr.add_data("https://www.youtube.com/@PIAIC")
# qr.make(fit=True)

# # Create an image from the QR code data
# img = qr.make_image(fill_color="black", back_color="white")

# # Save the QR code image to a file
# img.save("youtube_channel_qr_code.png")

import qrcode as qr

# Create the QR code image file
img = qr.make("https://www.youtube.com/[@ID OF YOUTUBE CHANNEL]")

# Save the QR code image file
img.save("name of file.png")