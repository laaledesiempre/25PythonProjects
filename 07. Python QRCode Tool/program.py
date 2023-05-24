import qrcode

def generate_qrcode(url="laaledesiempre's qr-coder",name="qrimg"):

    qr=qrcode.QRCode(
        version= 1,
        error_correction= qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img= qr.make_image(fill_color="black", back_color="white")
    img.save(f"{name}.png")

while True:
    print("if you want to exit, write \"exit\", else press ENTER")
    message=input()
    if message=="exit":
        break
    else:
        while True:
            try:
                name=input("Enter a name for the output image or press ENTER: ")
                url=input("Put an url or message you want to put on qr: ")
                if not name:
                    name="qrimg"
                if not url:
                    url="laaledesiempre's qr-coder"
                generate_qrcode(url,name)
                break
            except:
                print("error, something went wronh")