import cv2
from pyzbar.pyzbar import decode

# Считывание изображения с QR-кодом
image = cv2.imread("QR_images/qrcode.png")

# Декодирование QR-кода
decoded_objects = decode(image)

print(decoded_objects[0].data.decode("utf-8"))