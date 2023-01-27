import qrcode
data = input('Please enter anything you want to convert to qrcode(ie: text or links): ')
name = input('What do you want to call the QR code image: ')
try:
    img = qrcode.make(data)
    img.save(name +'.png')
    print("QR code image has been generated succussfully, please check this directory.")
except Exception as e1:
    print(e1.args)
        
        