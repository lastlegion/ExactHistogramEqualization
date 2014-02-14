import SimpleCV
import numpy as np
import pylab as plt
def unique_rows(a):
    a = np.ascontiguousarray(a)
    unique_a = np.unique(a.view([('',a.dtype)]*a.shape[1]))
    return unique_a.view(a.dtype).reshape((unique_a.shape[0], a.shape[1]))


I = SimpleCV.Image("lena.jpg")

F2 = [[0,1,0],[1,1,1],[0,1,0]]
F2 = (1/5.0)*np.matrix(F2)
F2 = F2.tolist()
F3 = (1/9.0)*np.ones((3,3))
F3 = F3.tolist()
F4 = (1/13.0)*np.ones((5,5))
F4[0,0] = F4[1,0] = F4[0,1] = F4[0,3] = F4[0,4] = F4[1,4] = 0
F4[0,3] = F4[0,4] = F4[1,4] = F4[3,4] = F4[4,4] = F4[4,3] = 0
F4 = F4.tolist()
F5 = (1/21.0)*np.ones((5,5))
F5[0,0] = F5[4,4] = F5[0,4] = F5[4,0] = 0
F5 = F5.tolist()
F6 = (1/25.0)*np.ones((5,5))
F6 = F6.tolist()
F = [F2,F3,F4,F5,F6]
#print F

FR = np.zeros((I.width, I.height,6))

Inp = I.getGrayNumpy()
#FR = Inp.reshape(I.width*I.height,1)
FR[:,:,0] = Inp
##Apply filters
FR[:,:,0] = I.convolve(F[0]).getGrayNumpy()
for i in range(0,5):
    FR[:,:,i+1] = I.convolve(F[i]).getGrayNumpy()
FR = FR.reshape(I.width*I.height,6)
#print FR

#Ordering accuracy
n_unique = unique_rows(FR)
print n_unique
print n_unique.shape
#print FR[100:120,100:120,:]
'''
for i in range(0,6):

'''
#Lexicographic sorting
indx_o = np.lexsort((FR[:,0], FR[:,1], FR[:,2], FR[:,3], FR[:,4], FR[:,5]))
print indx_o
print indx_o.shape

#Divide sorted list into 255 parts each having M*N/255 elements
bin_size = I.width*I.height/256
'''
bins = []
for i in range(0,255):
    bins.append([indx_o[i*bin_size:i*bin_size+bin_size]])
print len(bins)
print len(bins[250][0])
print bin_size
'''
print "Bin size" 
print bin_size
#Now for each pixel find the corresponding graylevel
#Create a new vector Ieq such that it is equalized
Ieq = np.zeros((I.width*I.height,1))
for i in range(0,I.width*I.height):
    Ieq[i] = indx_o[i]/bin_size

Ieq = Ieq.reshape((I.width,I.height))
Op = SimpleCV.Image(Ieq)
Op.show()
hist = Op.histogram(255)
plt.plot(hist)
plt.show()
a=raw_input()
#print len(bins[0])
#print bins
