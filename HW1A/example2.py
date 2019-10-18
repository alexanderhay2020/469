from matplotlib.image import NonUniformImage
import matplotlib.pyplot as plt
import numpy as np

xedges = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
yedges = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]

x = np.zeros(100)
y = np.zeros(100)
H, xedges, yedges = np.histogram2d(x, y, bins=(xedges, yedges))
H = H.T  # Let each row list bins with common y range.

fig = plt.figure(figsize=(5, 5))
#ax = fig.add_subplot(title='imshow: square bins')
plt.imshow(H, interpolation='nearest', origin='low',
        extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]])
plt.grid()
plt.show()

# ax = fig.add_subplot(132, title='pcolormesh: actual edges',
#         aspect='equal')
# X, Y = np.meshgrid(xedges, yedges)
# ax.pcolormesh(X, Y, H)

# ax = fig.add_subplot(133, title='NonUniformImage: interpolated',
#         aspect='equal', xlim=xedges[[0, -1]], ylim=yedges[[0, -1]])
# im = NonUniformImage(ax, interpolation='bilinear')
# xcenters = (xedges[:-1] + xedges[1:]) / 2
# ycenters = (yedges[:-1] + yedges[1:]) / 2
# im.set_data(xcenters, ycenters, H)
# ax.images.append(im)
