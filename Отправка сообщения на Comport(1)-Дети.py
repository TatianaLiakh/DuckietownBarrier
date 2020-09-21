import cv2
import pyzbar.pyzbar as pyzbar
import serial


#serial = serial.Serial('COM5', 9600)

cap = cv2.VideoCapture(0)


def send_to_serial(message: str):
    serial.write(message.encode('utf-8'))


def main():
    while True:
        ret, bgr_frame = cap.read()

        gray_frame = cv2.cvtColor(bgr_frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame', gray_frame)

        decoded_objects = pyzbar.decode(gray_frame)

        for decoded_object in decoded_objects:
            data = decoded_object.data.decode('utf-8')

            print(data)

            if data == 'to open':
                send_to_serial('open')
            if data == 'to_close':
                send_to_serial('close')

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    main()
