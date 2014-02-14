import SimpleCV
import numpy as np
import pylab as plt
def unique_rows(a):
    a = np.ascontiguousarray(a)
    unique_a = np.unique(a.view([('',a.dtype)]*a.shape[1]))
    return unique_a.view(a.dtype).reshape((unique_a.shape[0], a.shape[1]))


I = SimpleCV.Image("images/scene.jpg")

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
#FR[:,:,0] = I.convolve(F[0]).getGrayNumpy()
for i in range(0,5):
    FR[:,:,i+1] = I.convolve(F[i]).getGrayNumpy()
FR = FR.reshape(I.width*I.height,6)
#print FR[10:100,:]
#print FR

#Ordering accuracy
n_unique = unique_rows(FR)
#print n_unique
#print n_unique.shape
#print FR[100:120,100:120,:]

print n_unique
print n_unique.shape[0]
if(n_unique.shape[0] < I.width*I.height):
    print "Error! K=6 is not enough for this image"
'''
for i in range(0,6):

'''
FS = np.argsort(FR,0)[:,0]
bin_size = I.width*I.height/256

#Now for each pixel find the corresponding graylevel
#Create a new vector Ieq such that it is equalized


Ieq = np.zeros((I.width, I.height))
count=0
#
for i in range(0, I.width):
    for j in range(0, I.height):
        Ieq[i,j] = (FS[count])*255/float(I.width*I.height)
        count=count+1


Op = SimpleCV.Image(Ieq)
Op.show()
x = raw_input()
hist_data = Ieq.reshape(I.width*I.height,1)
plt.hist(hist_data,255)

plt.savefig("exacthist.jpg")

