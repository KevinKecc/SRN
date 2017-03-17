# SRN
This code is for the paper "Side-output Residual Network for Object Symmetry Detection in the Wild". [pdf](https://arxiv.org/abs/1703.02243)

SRN is build on Holistically-Nested Edge Detection (HED) [1] with Residual Unit (RU). RU is used to compute the residual between output image and side-output of SRN.

## Installing
1. Install prerequisites for Caffe (http://caffe.berkeleyvision.org/installation.html#prequequisites).
1. Build HED (https://github.com/s9xie/hed). Supposing the root directory of HED is `$HED`.
1. Copy the folder `SRN` to `$HED/example/`. 

## Training
1. Download benchmark **Sym-PASCAL** trainning and testing set
Our dataset Sym-PASCAL derived from PASCAL 2011 segmentation dataset [1]. The annotation and statistics are detailed in the Section 3 in our paper.
Download: [*(OneDrive)*](https://1drv.ms/u/s!AtLMd2E51FVrhRydfW0V-u-bLOgv) or [*(BaiduYun)*](http://pan.baidu.com/s/1slO0v73) 
1. Download the Pre-trained VGG [3] model.
[*(VGG19)*](https://gist.github.com/ksimonyan/3785162f95cd2d5fee77#file-readme-md)
Copy it to `$HED/example/SRN/`
1. Change the dataset path in '$HED/example/SRN/train_val.prototxt'
1. Run `solve.py` in shell (or you could use IDE like Eclipse)
```
cd $HED/example/SRN/
python solver.py
```

## Testing
1. Change the dataset path in `$HED/example/SRNtest.py`.
1. run `SRNtest.py`.


## Evaluation

We use the evaluation code of [3] to draw the PR curve. The code can be download [spb-mil](https://github.com/tsogkas/spb-mil).

**NOTE:** Before evaluation, the NMS is utilized. We use the NMS code in Piotr's [edges-master](https://github.com/pdollar/edges).

## Pre-trained SRN model on Sym-PASCAL
Pre-trained SRN model on Sym-PASCAL: [*(OneDrive)*](https://1drv.ms/u/s!AtLMd2E51FVrhR25fGZTs4NbgRXj) or [*(BaiduYun)*](http://pan.baidu.com/s/1c1Rs1xu)

## The PR curve data
Sym-PASCAL: [*(OneDrive)*](https://1drv.ms/f/s!AtLMd2E51FVrhSKfoRdUk7lSPqF7) or [*(BaiduYun)*](http://pan.baidu.com/s/1gf5GYS7)

SYMMAX: [*(OneDrive)*](https://1drv.ms/f/s!AtLMd2E51FVrhR8DjbOJtK7YV_tE) or [*(BaiduYun)*](http://pan.baidu.com/s/1i4Rbys9)

WH-SYMMAX: [*(OneDrive)*](https://1drv.ms/f/s!AtLMd2E51FVrhR8DjbOJtK7YV_tE) or [*(BaiduYun)*](http://pan.baidu.com/s/1o7UUUk6) mostly taken from http://wei-shen.weebly.com/publications.html

SK506: [*(OneDrive)*](https://1drv.ms/f/s!AtLMd2E51FVrhR8DjbOJtK7YV_tE) or [*(BaiduYun)*](http://pan.baidu.com/s/1nuMP0hz) mostly taken from http://wei-shen.weebly.com/publications.html

**Ref**

[1]  S. Xie and Z. Tu. Holistically-nested edge detection. In International Conference on Computer Vision, 2015

[2]  M. Everingham, L. Van Gool, C. K. I. Williams, J. Winn, and A. Zisserman. The PASCAL Visual Object Classes Challenge 2011 (VOC2011) Results. http://www.pascal-network.org/challenges/VOC/voc2011/workshop/index.html.

[3]  S. Tsogkas and I. Kokkinos. Learning-based symmetry detection in natural images. In European Conference on Computer Vision
