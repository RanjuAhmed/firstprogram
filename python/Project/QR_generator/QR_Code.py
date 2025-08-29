"""genaral Qr code generator"""
# import qrcode as qr
# img=qr.make("https://www.facebook.com/profile.php?id=100077733124136")
# img.save("Naim_fb_profile_QR.png")

"""genaral Qr code generator with color,hight width and etc"""

# import qrcode
# from PIL import Image

# qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4,)# qr version, error,sixe বলে দেওয়া হয়। 

# qr.add_data("https://www.facebook.com/profile.php?id=100077733124136")

# qr.make(fit=True)#সব ঠিক থাকলে create করবে

# img=qr.make_image(fill_color="black",back_color="blue")#image background create করে

# img.save("Naim_fbprofile.png")

import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=20,border=10,)

qr.add_data("https://www.facebook.com/profile.php?id=100077733124136")
qr.make(fit=True)

img=qr.make_image(fill_color="red",back_color="white")

img.save("Profile2.png")
