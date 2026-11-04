import cv2
from pyzbar.pyzbar import decode
import numpy as np

def read_qr_code(image_path):
    # Load the image using OpenCV
    code = cv2.imread(image_path)

    # Convert the image to a bytes-like object
    # code = cv2.imencode('.png', code)[1].tobytes()

    # Decode the QR code
    barcodes = decode(code)

    for barcode in barcodes:
        # Get the data from the QR code
        data = barcode.data.decode('utf-8').strip().split()
        # print(data)
        
        if len(data) == 2:
            try:
                num1 = int(data[0])
                num2 = int(data[1])
                divide = float(num1/num2)
                divide = format(divide, ".2f")
                # divide = float(num1/num2).round(2)
                # print(num1, num2)
                # print(f"{num1}/{num2}=", divide, sep='')
                text = []
                text.append(str(num1)+" "+str(num2))
                text.append(f"{num1}/{num2}="+divide)
                # print(text)
            except ValueError:
                print("Invalid input. Please ensure the QR code contains two numbers separated by a space.")
        else:
            print("Invalid input. Please ensure the QR code contains at least two numbers separated by a space.")
        print(text)
        return(text)

# Test the function


window = np.ones((512, 512, 3), dtype=np.uint8) * 255


# read_qr_code('QRcode.png')

font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(window, read_qr_code('QRcode.png')[0], (25, 30), font, 1.0, (0, 0, 0), 2)

cv2.putText(window, read_qr_code('QRcode.png')[1], (25, 60), font, 1.0, (0, 0, 0), 2)



cv2.imshow("img", window)
cv2.waitKey(0)
cv2.destroyAllWindows()





# # Create a font object
# font = cv2.FONT_HERSHEY_SIMPLEX

# # Add text to the image
# cv2.putText(img, 'Hello World!', (10, 20), font, 1.0,
#             (0, 0, 255), 2)