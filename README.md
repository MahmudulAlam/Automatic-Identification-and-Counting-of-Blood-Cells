# Automatic-Identification-and-Counting-of-Blood-Cells
## Dataset
We have used [Complete Blood Cell Count Dataset](https://github.com/MahmudulAlam/Complete-Blood-Cell-Count-Dataset). Download the dataset, unzip and put the Testing and Training folder in the working directory.

[![Download](https://img.shields.io/badge/download-dataset-ff69b4.svg?style=flat)](https://github.com/MahmudulAlam/Complete-Blood-Cell-Count-Dataset/archive/master.zip)

## Requirements
- [x] TensorFlow-GPU
- [x] OpenCV
- [x] Cython
- [x] Weights: Download the trained weights file for blood cell detection and put the Weights folder in the working directory.

[![Download](https://img.shields.io/badge/download-weights-brightgreen.svg?longCache=true&style=flat)](https://mega.nz/#F!2kVUnKjS!z15tM9WLfga3l1gCNSLNGw)

## Blood Cell Detection Output
<p align="center">
  <img src="https://user-images.githubusercontent.com/37298971/44617785-17eb0980-a88b-11e8-9018-c84f8be5cefa.png" width="550">
</p>

## Impact of KNN and IoU
In some cases, our model predicts the same platelet twice. To solve this problem we propose k-nearest neighbor (KNN) and intersection over union (IoU) based verification system where we find the nearest platelet of a platelet and calculate their overlap. We are allowing only 10% of overlap between two platelets. If the overlap is more than that then it will be a spurious prediction and we will ignore the prediction.

### Prediction Before Verfication 
<p align="center">
  <img src="https://user-images.githubusercontent.com/37298971/46260207-b27ede00-c504-11e8-9d00-7d7be151ee5d.jpg" width="400">
</p>

### Prediction After Verfication
<p align="center">
  <img src="https://user-images.githubusercontent.com/37298971/46260504-a268fd80-c508-11e8-9ef0-5230d00f47a3.jpg" width="400">
</p>


## Prediction on High-Resolution Image (HRI)
We have used our model to detect and count blood cells from high-resolution blood cell smear images. These test images are of the size of 3872x2592 way higher than our trained images size of 640x480. So, to match the cell size of our trained images we divide those images into grid cells and run prediction in each grid cell and then combine all the prediction results. 

### Dividing Image into Grid/Patch
<p align="center">
  <img src="https://user-images.githubusercontent.com/37298971/45962420-a39ab600-c042-11e8-975f-9b0a077f0e0f.jpg" width="700">
</p>

### Combined Output
<p align="center">
  <img src="https://user-images.githubusercontent.com/37298971/45961699-055a2080-c041-11e8-95b0-1c8ac3c8875b.jpg" width="700">
</p>

## Paper
For more detail explanation, please go through the [paper](http://ietdl.org/t/kmgztb).
