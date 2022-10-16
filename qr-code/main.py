import pyqrcode

''' 
first, install pyqrcode: `pip install pyqrcode`
after running the code: 
'''

# Generate QR-Code with a value (message, link)
code_message = "https://github.com/TomazWill"
my_qrcode = pyqrcode.create(code_message)
print(f"[QR-CODE] Message: {code_message}")

# Create and Save SVG file with QR-Code inside
file_name = "myqr.svg"
my_qrcode.svg(file_name, scale = 6)
print(f"[QR-CODE] Created: {file_name}")
