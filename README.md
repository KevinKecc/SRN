# SRN
Side-output Residual Network for Object Symmetry Detection in the Wild

SRN is build on Holistically-Nested Edge Detection (HED) [1] with Residual Unit (RU). RU is used to compute the residual between output image and side-output of SRN.

## Installing
1. Install prerequisites for Caffe (http://caffe.berkeleyvision.org/installation.html#prequequisites)
1. Build HED (https://github.com/s9xie/hed)
1. Copy folder `SRN` to 'example/' in HED. 

## Training
1. Download benchmark **Sym-PASCAL**
Our dataset Sym-PASCAL derived from PASCAL 2011 segmentation dataset [1].
Download：[*(BaiduYun)*](http://pan.baidu.com/s/1bXvlbK)
1. Download the Pre-trained VGG [3] model.
[*(VGG19)*](https://gist.github.com/ksimonyan/3785162f95cd2d5fee77#file-readme-md)
Copy it to 'example/SRN/'
1. Change the dataset directory of 'train_val.prototxt'
1. Change the directory of `solver.prototxt`
1. Run `solve.py`

## Testing
1. Change the dataset directory of 'SRNtest.py'
1. run 'SRNtest.py'

## Evaluation
We use the evaluation code of [3] to draw the PR curve. The code can be download [*(spb-mil)*](https://github.com/tsogkas/spb-mil)

## Pre-trained SRN model on Sym-PASCAL
[*(Pre-trained SRN model on Sym-PASCAL)*](http://pan.baidu.com/s/1eR52M2I)

## The PR curve data
[*(Sym-PASCAL)*](http://pan.baidu.com/s/1gf5GYS7)
[*(SYMMAX)*](http://pan.baidu.com/s/1i4Rbys9)
[*(WH-SYMMAX)*](http://pan.baidu.com/s/1o7UUUk6) mostly taken from http://wei-shen.weebly.com/publications.html
[*(SK506)*](http://pan.baidu.com/s/1nuMP0hz) mostly taken from http://wei-shen.weebly.com/publications.html


[1]  S. Xie and Z. Tu. Holistically-nested edge detection. In International Conference on Computer Vision, 2015
[2]  M. Everingham, L. Van Gool, C. K. I. Williams, J. Winn, and A. Zisserman. The PASCAL Visual Object Classes Challenge 2011 (VOC2011) Results. http://www.pascal-network.org/challenges/VOC/voc2011/workshop/index.html.
[3]  S. Tsogkas and I. Kokkinos. Learning-based symmetry detection in natural images. In European Conference on Computer Vision