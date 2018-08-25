import os
from Parse_Annotation import parse_annotation

labels = ['RBC', 'WBC', 'Platelet']

for ann_file in os.listdir('Testing/Annotations'):
    ann_dir = 'Testing/Annotations/' + ann_file
    ground_truths, labels = parse_annotation(ann_dir, labels)
    print(ann_file, labels)
