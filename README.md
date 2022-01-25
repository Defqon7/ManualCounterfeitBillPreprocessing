# Manual Pre-Processing Image for Counterfeit Bill Detection
This project manually extracts and pre-processes bills from an image to be prepared for counterfeit detection.
## Original Image
![](images/banknote.jpg)
## 1. Extract Front-Facing Bill
## 1.1 Rotate Image
```
banknote = cv2.imread('banknote.jpg', 1)
rows, cols, _ = banknote.shape
center = (rows // 2, cols // 2)
frotation_matrix = cv2.getRotationMatrix2D(center, -93, 1.0)
frotated_bill = cv2.warpAffine(banknote, frotation_matrix, (cols, rows))
```
Rotate image -93 degrees to straighten front-facing bill
![](images/rotated_front.jpg)
