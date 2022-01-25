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
cv2.imshow('Rotated Front-Facing Bill', frotated_bill)
```
![](images/rotated_front.jpg)
## 1.2 Crop Image
```
front_bill = frotated_bill[26:67, 21:87]
cv2.imshow('Cropped Bill', front_bill)
```
![](images/cropped_front.jpg)
## 1.3 Fix Shear in Bill
### 1.3.1 Find Corners of Bill
```
pts1 = np.float32([[2, 0], [65, 1], [0, 40], [63, 40]])
pts2 = np.float32([[0, 0], [66, 0], [0, 41], [66, 41]])
plt.imshow(front_bill)
plt.scatter(pts1[:, 0], pts1[:, 1], color='red', s=100)
plt.show()
```
![](images/dots.jpg)<br>
### 1.3.2 Warp Image to Remove Shear
```
M = cv2.getPerspectiveTransform(pts1, pts2)
frontfacing_bill = cv2.warpPerspective(front_bill, M, (66, 41))
cv2.imshow('Front-Facing Bill', frontfacing_bill)
```
![](images/frontfacing_bill.jpg)
## 2. Extract Back-Facing Bill
## 2.1 Shift Image
```
M = np.float32([[1, 0, -33], [0, 1, 0]])
shifted_backface = cv2.warpAffine(banknote, M, (cols, rows))
cv2.imshow('shifted backface', shifted_backface)
```
![](images/shifted_backface.jpg)
## 2.2 Rotate Image
![](images/Rotated_around_center.jpg)<br>
Rotating around the center causes back-facing bill to fall out of frame. Modify the rotation point.
```
bcenter = (54, 33)
brotation_matrix = cv2.getRotationMatrix2D(bcenter, -98, 1.0)
brotated_bill = cv2.warpAffine(shifted_backface, brotation_matrix, (cols, rows))
cv2.imshow('Rotated back-faced bill', brotated_bill)
```
![](images/rotated_altered_center.jpg)
## 2.3 Crop Image
```
backfacing_bill = brotated_bill[13:58, 7:82]
cv2.imshow('Cropped back-facing bill', backfacing_bill)
```
![](images/backfacing_bill.jpg)
## 3. Input → Outputs
![](images/banknote.jpg)
→
![](images/frontfacing_bill.jpg)
+
![](images/backfacing_bill.jpg)
