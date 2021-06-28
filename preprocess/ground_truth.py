import os
from preprocess.parse_annotation import parse_annotation

labels = ['RBC', 'WBC', 'Platelet']
directory = '../dataset/Testing/Annotations/'
for ann_file in os.listdir(directory):
    ann_dir = directory + ann_file
    ground_truths, labels = parse_annotation(ann_dir, labels)
    print(ann_file, labels)
