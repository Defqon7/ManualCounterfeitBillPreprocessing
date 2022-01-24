import cv2
import numpy as np
import matplotlib.pyplot as plt

# read in input image
banknote = cv2.imread('banknote.jpg', 1)
cv2.imshow('Original Image', banknote)
# find center of image for rotation
rows, cols, _ = banknote.shape
center = (rows // 2, cols // 2)
# ------------------------------------------------
# extract front-facing bill
# rotate image -93 degrees to straighten bill
frotation_matrix = cv2.getRotationMatrix2D(center, -93, 1.0)
frotated_bill = cv2.warpAffine(banknote, frotation_matrix, (cols, rows))
# crop front-facing bill
front_bill = frotated_bill[26:67, 21:87]
# fix sheared front-facing bill
# find corners of bill
pts1 = np.float32([[2, 0], [65, 1], [0, 40], [63, 40]])
pts2 = np.float32([[0, 0], [66, 0], [0, 41], [66, 41]])
# visualize the corner coordinates used
plt.imshow(front_bill)
plt.scatter(pts1[:, 0], pts1[:, 1], color='red', s=100)
plt.savefig('bill_coords.jpg')
plt.show()
# warp sheared bill
M = cv2.getPerspectiveTransform(pts1, pts2)
frontfacing_bill = cv2.warpPerspective(front_bill, M, (66, 41))
# show and save extracted bill
cv2.imshow('Front-Facing Bill', frontfacing_bill)
cv2.imwrite('frontfacing_bill.jpg', frontfacing_bill)
# ---------------------------------------------------------
# extract back-facing bill
# shift image
M = np.float32([[1, 0, -33], [0, 1, 0]])
shifted_backface = cv2.warpAffine(banknote, M, (cols, rows))
cv2.imshow('shifted backface', shifted_backface)
cv2.imwrite('shifted_backface.jpg', shifted_backface)
# modify center to be rotated around
bcenter = (54, 33)
# rotate image -98 degrees to straighten bill
brotation_matrix = cv2.getRotationMatrix2D(bcenter, -98, 1.0)
brotated_bill = cv2.warpAffine(shifted_backface, brotation_matrix, (cols, rows))
# crop back-facing bill
backfacing_bill = brotated_bill[13:58, 7:82]
# show and save extracted bill
cv2.imshow('Back-Facing Bill', backfacing_bill)
cv2.imwrite('backfacing_bill.jpg', backfacing_bill)
# ------------------------------------------------------------
cv2.waitKey(0)
cv2.destroyAllWindows()
