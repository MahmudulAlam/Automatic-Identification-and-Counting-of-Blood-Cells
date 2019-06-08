import os
from parse_annotation import parse_annotation

labels = ['RBC', 'WBC', 'Platelet']

for ann_file in os.listdir('Dataset/Testing/Annotations'):
    ann_dir = 'Dataset/Testing/Annotations/' + ann_file
    ground_truths, labels = parse_annotation(ann_dir, labels)
    print(ann_file, labels)
