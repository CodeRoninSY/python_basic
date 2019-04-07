#!/usr/bin/env python
'''
    qrcode_example.py
    QR code simple generator
    N.B.: Requirement ->
        $> pip install qrcode[pil]
        Usage:
            $> qr "Some text here" > test.png

    See -> pypi.org/project/qrcode
'''

import qrcode
#from qrcode.image.pure import PymagingImage


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

data = "CodeRoninSY @2019"

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="white")

img.save("CodeRoninSY2019.png")
