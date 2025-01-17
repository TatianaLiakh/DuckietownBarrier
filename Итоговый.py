
import cv2
import pyzbar.pyzbar as pyzbar
import serial
ser = serial.Serial('/dev/ttyACM0')#вставить name в ()
cap = cv2.VideoCapture(0)#захват камеры
font = cv2.FONT_HERSHEY_PLAIN#размер текста
value = b'c'
ser.write(value)#отправка value на ком.порт
codes = list(map(int, input().split()))#разрешенные номера
while True:
    rat, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    decodedObjects = pyzbar.decode(gray)
    for obj in decodedObjects:
        data = obj.data.decode('utf-8')
        cv2.putText(gray, data, (50, 50), font, 2, (255, 0, 0), 2)
        if (data == 'Open') or (data in str(codes)):
            value = b'o'
            ser.write(value)
        elif data == 'Close':
            value = b'c'
            ser.write(value)
    cv2.imshow("Frame", gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
