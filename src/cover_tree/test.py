from covertreec import CoverTree

import time
import scipy as sc
import numpy as np

gt = time.time
np.random.seed(seed=3)

print('Building cover tree')

x = np.random.rand(100000, 3).astype(np.float32)
x_size = x.shape
# x *= 100
with open('train_data.bin', 'wb') as f:
    np.array(x.shape, dtype='int32').tofile(f)
    x.tofile(f)
print(x[0, 0], x[0, 1], x[1, 0])

mx = np.mean(x, 0)
dists = np.array([np.sqrt(np.dot(xv - mx, xv - mx)) for xv in x])
idx = np.argsort(-dists)
xs = x[idx]
# print sc.spatial.distance.squareform(sc.spatial.distance.pdist(x, 'euclidean'))
t = gt()
ct = CoverTree(x.T)
b_t = gt() - t
# ct.display()
print("Building time:", b_t, "seconds")
print("Test covering: ", ct.check_covering())

t = gt()
ct.cal_level2ptsidx_pts2child()
level2ptsidx = ct.ret_level2ptsidx()
pts2child = ct.ret_pts2child()
b_t = gt() - t

print("level travel time:", b_t, "seconds")

print("level2ptsidx\n", level2ptsidx)
print("pts2child\n", pts2child)

# level_points_from_idx = ct.get_level_points_idx()

# for keys in list(level_points.keys()):
#     pts = level_points[keys]
#     pts_from_idx = x[level_points_from_idx[keys]]
#     if np.all(pts == pts_from_idx):
#         print("level", keys, "all the same")
#     else:
#         print("level", keys, "find different")