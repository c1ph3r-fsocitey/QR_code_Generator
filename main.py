import qrcode

link = input("please enter the link: ")
qr = qrcode.make(link)
name = input("please enter the name of the qr code image: ")
qr.show(name)
qr.save(name)
print("qr code generated and saved!")
