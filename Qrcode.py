import numpy as np
import cv2
from BinaryToColour import line
from BinaryToColour import main

height, width = 20, 20
img = np.zeros((height, width, 3), np.uint8)

colours_Array = main(line)
print(len(colours_Array))
i = 0
for q in range(height):
    for n in range(width):
        match colours_Array[i]:
            case "BLACK":
                img[q,n] = (0,0,0)
            case "WHITE":
                img[q,n] = (255,255,255)
            case "RED":
                img[q,n] = (0,0,255)
            case "GREEN":
                img[q,n] = (0,255,0)
        i += 1 
    
resized = cv2.resize(img, (1024, 1024), 0, 0, interpolation = cv2.INTER_NEAREST)
cv2.imshow("QR", resized)
cv2.waitKey(0)