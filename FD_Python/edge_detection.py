

import  cv2
image = cv2.imread('thor.jpg')
im_or = cv2.resize(image, (400, 600))
cv2.imshow('Original',im_or)
#--------------------------------------------------------
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,30,40)
im_edge = cv2.resize(edges, (400, 600))
cv2.imshow('Edges',im_edge)
#---------------------------------------------------------------
edges_high_thresh=cv2.Canny(gray,90,200)
im_e_h_t= cv2.resize(edges_high_thresh, (400, 600))
cv2.imshow('Edges_High',im_e_h_t)
#--------------------------------------------------------------
cv2.waitKey(0)
cv2.destroyAllWindows()