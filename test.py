import os
import cv2
import time
from utils import iou
from scipy import spatial
from darkflow.net.build import TFNet

options = {'model': 'cfg/tiny-yolo-voc-3c.cfg',
           'load': 3750,
           'threshold': 0.1,
           'gpu': 0.7}

tfnet = TFNet(options)

avg_time = 0
pred_bb = []  # predicted bounding box
pred_cls = []  # predicted class
pred_conf = []  # predicted class confidence

directory = 'dataset/Testing/Images/'

for file_name in os.listdir(directory):
    tic = time.time()
    image = cv2.imread(directory + file_name)
    output = tfnet.return_predict(image)

    rbc = 0
    wbc = 0
    platelets = 0

    cell = []
    cls = []
    conf = []

    record = []
    tl_ = []
    br_ = []
    iou_ = []
    iou_value = 0

    for prediction in output:
        label = prediction['label']
        confidence = prediction['confidence']

        tl = (prediction['topleft']['x'], prediction['topleft']['y'])
        br = (prediction['bottomright']['x'], prediction['bottomright']['y'])

        if label == 'RBC' and confidence < .5:
            continue
        if label == 'WBC' and confidence < .25:
            continue
        if label == 'Platelets' and confidence < .25:
            continue

        # clearing up spurious platelets
        if label == 'Platelets':
            if record:
                tree = spatial.cKDTree(record)
                index = tree.query(tl)[1]
                iou_value = iou(tl + br, tl_[index] + br_[index])
                iou_.append(iou_value)

            if iou_value > 0.1:
                continue

            record.append(tl)
            tl_.append(tl)
            br_.append(br)

        # image = cv2.rectangle(image, tl, br,color, 2)
        center_x = int((tl[0] + br[0]) / 2)
        center_y = int((tl[1] + br[1]) / 2)
        center = (center_x, center_y)

        if label == 'RBC':
            color = (255, 0, 0)
            rbc = rbc + 1
        if label == 'WBC':
            color = (0, 255, 0)
            wbc = wbc + 1
        if label == 'Platelets':
            color = (0, 0, 255)
            platelets = platelets + 1

        radius = int((br[0] - tl[0]) / 2)
        image = cv2.circle(image, center, radius, color, 2)
        font = cv2.FONT_HERSHEY_COMPLEX
        image = cv2.putText(image, label, (center_x - 15, center_y + 5), font, .5, color, 1)
        cell.append([tl[0], tl[1], br[0], br[1]])

        if label == 'RBC':
            cls.append(0)
        if label == 'WBC':
            cls.append(1)
        if label == 'Platelets':
            cls.append(2)

        conf.append(confidence)

    pred_bb.append(cell)
    pred_cls.append(cls)
    pred_conf.append(conf)
    cv2.imwrite('output/' + file_name, image)
    toc = time.time()
    avg_time = avg_time + (toc - tic) * 1000

avg_time = avg_time / 60

print('Mean time: {0:.5}'.format(avg_time), 'ms')
print('All Done!')
