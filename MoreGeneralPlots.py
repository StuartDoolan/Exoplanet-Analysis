import numpy as np
import matplotlib.pyplot as plt
import collections
plt.close('all')


import random
rMass = random.sample(xrange(100), 60)
things=[]
for i in range(60):
    if rMass[i]<30:
        things.append(random.randint(1,2))
    elif rMass[i]<60:
        things.append(random.randint(1,3))
    else:
        things.append(3)

my_xticks = np.array(('','Thing 1', 'Thing 2', 'Thing 3', ''))
fig1= plt.figure()
ax1 = fig1.add_subplot(111)
plt.xticks([0,1, 2, 3, 4], my_xticks)
plt.plot(things,rMass,"bo")
fig1.suptitle('Which Category of Thing Stuff Falls Into', fontsize = 17)
ax1.set_xlim(0, 4)
ax1.set_xlabel('Things', fontsize = 16)
ax1.set_ylabel('Stuff', fontsize = 16)
plt.show()