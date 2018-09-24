import cv2
from darkflow.net.build import TFNet

options = {'model': 'cfg/tiny-yolo-voc-3c.cfg',
           'load': 3750,
           'threshold': 0.15,
           'gpu': 0.7}

tfnet = TFNet(options)

C = []  # Center
R = []  # Radius
L = []  # Label

im_name = 'HRI001'
image = cv2.imread('Images/' + im_name + '.jpg')

for h in range(0, 2592, 890):
    for w in range(0, 3872, 1290):
        im = image[h:h + 890, w:w + 1290]
        output = tfnet.return_predict(im)

        RBC = 0
        WBC = 0
        Platelets = 0

        for prediction in output:
            label = prediction['label']
            confidence = prediction['confidence']
            tl = (prediction['topleft']['x'], prediction['topleft']['y'])
            br = (prediction['bottomright']['x'], prediction['bottomright']['y'])

            height, width, _ = image.shape
            center_x = int((tl[0] + br[0]) / 2)
            center_y = int((tl[1] + br[1]) / 2)
            center = (center_x + w, center_y + h)
            radius = int((br[0] - tl[0]) / 2)

            C.append(center)
            R.append(radius)
            L.append(label)

record = []

for i in range(0, len(C)):
    center = C[i]
    radius = R[i]
    label = L[i]

    if label == 'RBC':
        color = (255, 0, 0)
    elif label == 'WBC':
        color = (0, 255, 0)
    elif label == 'Platelets':
        color = (0, 0, 255)

    image = cv2.circle(image, center, radius, color, 5)
    font = cv2.FONT_HERSHEY_COMPLEX
    image = cv2.putText(image, label, (center[0] - 30, center[1] + 10), font, 1, color, 2)

cv2.imwrite('Output/' + im_name + 'out.jpg', image)
cv2.waitKey(0)
