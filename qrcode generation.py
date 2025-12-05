'''
import qrcode as qr
img=qr.make("https://www.linkedin.com/in/Lakshay-Dhull/")
img.save("My_LinkedIN.png")
'''
import qrcode as qr
from PIL import Image
print("\t\tWelcome to QR code generator")
a=input("\n\t\tPlease provide the URL for which you want to generate your QR code: ")
while True:
    try:
        print("\n\t\tBox size is between 1 to 40. If you have a longer url please select higher box")
        b=int(input("\n\t\tPlease enter box size of QR  Code: "))
        break
    except valueError:
        print("\n\t\tPlease enter a valid number!")
while True:
    try:
        print("Recommended border size is 4")
        c=input("\n\t\tPlease enter border size of your QR Code: ")
        break
    except valueError:
        print("\n\t\tInvalid enter a valid number!")

qrc=qr.QRCode(version=1,error_correction=qr.constants.ERROR_CORRECT_H,box_size=b,border=c)
qrc.add_data(a)
qrc.make(fit=True)
fc=input("\n\t\tPlease enter fill colour of your QR CODE: ")
bc=input("\n\t\tPlease enter background colour of your QR Code: ")
fc=fc.lower()
bc=bc.lower()
img=qrc.make_image(fill_color=fc,back_color=bc)
name=input("\n\t\tPlease enter the name of the file by which you want to save it: ")
name=name+".png"
img.save(name)
print(f"\n\t\tYour QR code by Name: {name} is saved")
