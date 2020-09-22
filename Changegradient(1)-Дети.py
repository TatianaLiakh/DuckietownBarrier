import cv2
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, threshold_image = cv2.threshold(im, 127, 255, 0)
viewImage(gray_image, "Пёсик в градациях серого")
viewImage(threshold_image, "Чёрно-белый пёсик")
