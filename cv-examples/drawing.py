import numpy as np
import cv2

width = 512
height = 512
# RGB image is 3 widthxheight matrices
img = np.zeros( (width,height,3), np.uint8 )

while (1):
	# Reset image
	img = np.zeros( (width,height,3), np.uint8 )

	# Draw a diagonal blue line with thickness of 5px
	img = cv2.line(img, (0,0), (width-1,height-1), (255,0,0), 5)
	# Draw rectangle using top-left and bottom-right corners
	rectW = 126
	img = cv2.rectangle(img, (width-rectW,0), (width,rectW), (0,255,0), 3)
	# Draw circle using center coords and radius, -1 thickness fills the shape
	img = cv2.circle(img, (width-rectW/2,rectW/2), rectW/2, (0,0,255), -1)
	# Draw ellipse using center coord, axes lengths, CCW rotation, startAngle, endAngle
	img = cv2.ellipse(img, (width/2,height/2), (100,50), 0, 0, 180, (255,255,255), -1)
	# Draw polygon using array of vertices, and True/False determines closed shape or lines
	pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
	pts = pts.reshape((-1,1,2))
	img = cv2.polylines(img, [pts], True, (0,255,255), lineType=cv2.LINE_AA)
	# Draw text using the string, bottom-left of textbox, font, size, etc
	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(img, 'OpenCV', (10,500), font, 4, (255,255,255), 20, cv2.LINE_AA)

	
	cv2.imshow('frame', img)
	# 'q' is for Quit
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
