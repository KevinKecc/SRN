from __future__ import division
import numpy as np
import sys
caffe_root = '../../' 
sys.path.insert(0, caffe_root + 'python')
import caffe
import matplotlib.pyplot as plt
import scipy.io as scio

# make a bilinear interpolation kernel
# credit @longjon
def upsample_filt(size):
    factor = (size + 1) // 2
    if size % 2 == 1:
        center = factor - 1
    else:
        center = factor - 0.5
    og = np.ogrid[:size, :size]
    return (1 - abs(og[0] - center) / factor) * \
           (1 - abs(og[1] - center) / factor)

# set parameters s.t. deconvolutional layers compute bilinear interpolation
# N.B. this is for deconvolution without groups
def interp_surgery(net, layers):
    for l in layers:
        m, k, h, w = net.params[l][0].data.shape
        if m != k:
            print 'input + output channels need to be the same'
            raise
        if h != w:
            print 'filters need to be square'
            raise
        filt = upsample_filt(h)
        net.params[l][0].data[range(m), range(k), :, :] = filt

# base net -- follow the editing model parameters example to make
# a fully convolutional VGG16 net.
# http://nbviewer.ipython.org/github/BVLC/caffe/blob/master/examples/net_surgery.ipynb
# base_weights = '5stage-vgg.caffemodel'
base_weights = '5stage-vgg.caffemodel'

# init
caffe.set_mode_gpu()
caffe.set_device(3)

solver = caffe.SGDSolver('solver.prototxt')

# do net surgery to set the deconvolution weights for bilinear interpolation
interp_layers = [k for k in solver.net.params.keys() if 'up' in k]
interp_surgery(solver.net, interp_layers)

# copy base weights for fine-tuning
#solver.restore('dsn-full-res-3-scales_iter_29000.solverstate')
solver.net.copy_from(base_weights)

# solve straight through -- a better approach is to define a solving loop to
# 1. take SGD steps
# 2. score the model by the test net `solver.test_nets[0]`
# 3. repeat until satisfied
niter = 18000
test_interval = 200
train_fuse_loss = np.zeros(niter)
train_dsn1_loss = np.zeros(niter)
train_dsn2_loss = np.zeros(niter)
train_dsn3_loss = np.zeros(niter)
train_dsn4_loss = np.zeros(niter)
train_dsn5_loss = np.zeros(niter)


test_acc = np.zeros(int(np.ceil(niter / test_interval)))

# the main solver loop
for it in range(niter):
    solver.step(1)  # SGD by Caffe
    
    # store the train loss
    train_fuse_loss[it] = solver.net.blobs['fuse_loss'].data
    train_dsn1_loss[it] = solver.net.blobs['dsn1_loss'].data
    train_dsn2_loss[it] = solver.net.blobs['dsn2_loss'].data
    train_dsn3_loss[it] = solver.net.blobs['dsn3_loss'].data
    train_dsn4_loss[it] = solver.net.blobs['dsn4_loss'].data
    train_dsn5_loss[it] = solver.net.blobs['dsn5_loss'].data

scio.savemat('TrainLoss.mat', {'fuse_loss':train_fuse_loss, \
                               'dsn1_loss':train_dsn1_loss, \
                               'dsn2_loss':train_dsn2_loss, \
                               'dsn3_loss':train_dsn3_loss, \
                               'dsn4_loss':train_dsn4_loss, \
                               'dsn5_loss':train_dsn5_loss})


_, ax1 = plt.subplots()
ax1.plot(np.arange(niter), train_fuse_loss)
ax1.set_xlabel('iteration')
ax1.set_ylabel('train loss')
plt.show()

