import cv2
import numpy as np

# Image Path
image_path = "/Users/nitesh/Downloads/simple-shape-detection/White_background_image.png"

img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
_, threshold = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

font = cv2.FONT_HERSHEY_COMPLEX

count_triangle = 0
count_rectangle = 0
count_square = 0
count_circle = 0

for cnt in contours:
  approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
  cv2.drawContours(img, [approx], -1, (0, 255, 0), 3)
  x = approx.ravel()[0]
  y = approx.ravel()[1]

  print len(approx)
  # Detect Triangle.
  if len(approx) == 3:
    cv2.putText(img, "Triangle", (x, y), font, 1, (0))
    count_triangle += 1

  # Detect Square and Rectangle.
  elif len(approx) == 4:
    (x, y, w, h) = cv2.boundingRect(approx)

    if  ((float(w)/h)  > 0.95 and (float(w)/h)  < 1.05):
      cv2.putText(img, "Square", (x, y), font, 1, (0))
      count_square += 1
    else:
      cv2.putText(img, "Rectangle", (x, y), font, 1, (0))
      count_rectangle += 1

  # # Detect Pentagon.
  # elif len(approx) == 5:
  #   cv2.putText(img, "Pentagon", (x, y), font, 1, (0))

  # # # Detect Ellipse.
  # elif 6 < len(approx) < 15:
  #     cv2.putText(img, "Ellipse", (x, y), font, 1, (0))

  # Detect Circle.
  else:
      cv2.putText(img, "Circle", (x, y), font, 1, (0))
      count_circle += 1

print "Triangle"
print count_triangle

print "Square"
print count_square

print "Rectangle"
print count_rectangle

print "Circle"
print count_circle

cv2.imshow("shapes", img)
cv2.imshow("Threshold", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
