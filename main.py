from PIL import Image
import numpy as np
import scipy.misc

key1 = Image.open('key1.png')
key2 = Image.open('key2.png')
eprime = Image.open('Eprime.png')
E = Image.open('E.png')
I = Image.open('I.png')

k1_a = np.asarray(key1).copy()
k2_a = np.asarray(key2).copy()
E_a = np.asarray(E).copy()
I_a = np.asarray(I).copy()
e_a = np.asarray(eprime).copy()


data = np.zeros((120000,3),int)

e = np.zeros((120000,1),int)

for y in range(300):
    for x in range(400):
      data[y * 400 + x][0] = k1_a[y][x]
      data[y * 400 + x][1] = k2_a[y][x]
      data[y * 400 + x][2] = I_a[y][x]
      e   [y * 400 + x]    = E_a[y][x]

       
w = np.array([0,0,0]) 

maxlimit = 10
t0 = 2
t1 = 2
t2 = 2

epoch = 1
while epoch < maxlimit and abs(w[0] - t0) > 0.00001 and abs(w[1] - t1) > 0.00001 and abs(w[2] - t2) > 0.00001:
    t0 = w[0]
    t1 = w[1]
    t2 = w[2] 
    for i, x in enumerate(data): 
        a = w[0] * x[0] + w[1] * x[1] + w[2] * x[2]
        b = e[i] - a
        w = w +  0.00001 * b * x
    epoch += 1 

print(w[0] , w[1] , w[2])

ans = np.zeros((300,400),int)
      
for j in range(300):
    for i in range(400):
        ans[j][i] = (e_a[j][i] - w[0] * k1_a[j][i] - w[1] * k2_a[j][i])/w[2]
        
scipy.misc.imsave('Answer.jpg', ans)
