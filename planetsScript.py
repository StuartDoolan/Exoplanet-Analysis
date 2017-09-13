import numpy as np
import matplotlib.pyplot as plt
import collections
plt.close('all')

# read in planets file and dick about with plots
f = open('/Users/stuartdoolan/Documents/Accelerate Internship/planets-reduced-data-set.csv', 'r')


#read in data from file
filecontents = f.readlines()
f.close()


# skip through header lines starting with '#'
filestart = 0
while 1:
    if filecontents[filestart][0] == '#':
        filestart += 1
    else:
        break

exonumber = len(filecontents)
planetdata = [[0 for x in range(5)] for y in range(exonumber-1)]

#probably cheating but it works
for i in range(exonumber-1):
    thisline = []
    lines = filecontents[filestart+i].split(',')
    for entry in lines:
            thisline.append(entry.strip())
    planetdata[i] = thisline
planetdata = np.array(planetdata)
header = planetdata[0]
planetdata = np.delete(planetdata, (0), axis=0)
planetdataT = np.array(zip(*planetdata))

Planet_letter = planetdataT[2]
Disc_method = planetdataT[3]
no_planets = planetdataT[4]
Orb_Per = np.array(planetdataT[5])
Eccentricity = planetdataT[6]
Inclination = planetdataT[7]
Distance = planetdataT[8]
Equil_Temp = planetdataT[11]
Mass= planetdataT[12]
Radius = planetdataT[13]
YrDiscovered = planetdataT[14]
Discovery_Facility = planetdataT[15]
Rad_Vel = planetdata[16]



no_Disc = Disc_method
for i in range(len(no_Disc)):
    if no_Disc[i] =='Transit':
           no_Disc[i] = 1
           no_Disc[i] = int(no_Disc[i])
    elif no_Disc[i] =='Radial Velocity':
            no_Disc[i] = 2 
            no_Disc[i] = int(no_Disc[i])
    elif no_Disc[i] =='Microlensing':
            no_Disc[i] = 3
            no_Disc[i] = int(no_Disc[i])
    else: no_Disc[i] = 4
int_Disc = [int(x) for x in no_Disc]
int_Disc = np.array(int_Disc)
int_Disc = np.reshape(int_Disc,len(int_Disc))

## Account for empty data points in mass by defining a reduced version of each
## Also remove 'Other' values
rMass = []
mDisc = []
for i in range(len(Mass)):
    if Mass[i] != '' and int_Disc[i]!=4:
        rMass.append(Mass[i])
        mDisc.append(int_Disc[i])



## Account for empty Radius                        
rRadius = []
rDisc = []
for i in range(len(Radius)):
    if Radius[i] != ''and int_Disc[i]!=4:
        rRadius.append(Radius[i])
        rDisc.append(int_Disc[i])
        
## Number of planets
rNoPlanets = []
npDisc = []
for i in range(len(no_planets)):
    if no_planets[i] != ''and int_Disc[i]!=4:
        rNoPlanets.append(no_planets[i])
        npDisc.append(int_Disc[i])

##Orbital Period
rOrbPer = []
opDisc = []
for i in range(len(Orb_Per)):
    if Orb_Per[i] !=''and int_Disc[i]!=4:
        rOrbPer.append(Orb_Per[i])
        opDisc.append(int_Disc[i])

##Distance
rDistance = []
dDisc = []
for i in range (len(Distance)):
    if Distance[i] != ''and int_Disc[i]!=4:
        rDistance.append(Distance[i])
        dDisc.append(int_Disc[i])
        
        
## Equilibrium Temperature
rTemp = []
tDisc = []
for i in range(len(Equil_Temp)):
    if Equil_Temp[i] != ''and int_Disc[i]!=4:
        rTemp.append(Equil_Temp[i])
        tDisc.append(int_Disc[i])
        
        
#set up pie. Cut out 'Other' and find percentages of transit, RadVel and Microlensing
#dumb, but makes list
pDisc = []
for i in range(len(int_Disc)):
        pDisc.append(int_Disc[i])
percTransit = (pDisc.count(1)*100/len(int_Disc))
percRV = (pDisc.count(2)*100/len(int_Disc))
percMicro = (pDisc.count(3)*100/len(int_Disc))
percOther = (pDisc.count(4)*100/len(int_Disc))
percDisc = [percTransit, percRV, percMicro, percOther]
    
####PLOTS

##Discovery method with mass
my_xticks = np.array(('','Transit', 'Radial Velocity', 'Microlensing', ''))
fig1= plt.figure()
ax1 = fig1.add_subplot(111)
plt.xticks([0,1, 2, 3, 4], my_xticks)
plt.plot(mDisc,rMass,"bo")
fig1.suptitle('Mass of Exoplanets With Corresponding Discovery Method', fontsize = 17)
ax1.set_xlim(0, 4)
ax1.set_xlabel('Discovery Method', fontsize = 16)
ax1.set_ylabel('Mass (Me)', fontsize = 16)

##Disc method with Radius
my_xticks = np.array(('Transit', 'Radial Velocity', 'Microlensing'))
fig2= plt.figure()
ax2 = fig2.add_subplot(111)
plt.xticks([1, 2, 3], my_xticks)
plt.plot(rDisc,rRadius,"bo")
fig2.suptitle('Radius of Exoplanets With Corresponding Discovery Method', fontsize = 17)
ax2.set_xlim(0, 4)
ax2.set_xlabel('Discovery Method', fontsize = 16)
ax2.set_ylabel('Radius (Re)', fontsize = 16)

##Disc method with Number of Planets
my_xticks = np.array(('Transit', 'Radial Velocity', 'Microlensing'))
fig3= plt.figure()
ax3 = fig3.add_subplot(111)
plt.xticks([1, 2, 3], my_xticks)
plt.plot(npDisc,rNoPlanets,"bo")
fig3.suptitle('Number of Exoplanets With Corresponding Discovery Method', fontsize = 17)
ax3.set_xlim(0, 4)
ax3.set_xlabel('Discovery Method', fontsize = 16)
ax3.set_ylabel('Number of Planets in Solar System', fontsize = 16)

##Disc method with Orbital Period
my_xticks = np.array(('Transit', 'Radial Velocity', 'Microlensing'))
fig4= plt.figure()
ax4 = fig4.add_subplot(111)
plt.xticks([1, 2, 3], my_xticks)
plt.plot(opDisc,rOrbPer,"bo")
fig4.suptitle('Orbital Period of Exoplanets With Corresponding Discovery Method', fontsize = 17)
ax4.set_xlim(0, 4)
ax4.set_xlabel('Discovery Method', fontsize = 16)
ax4.set_ylabel('Orbital Period (Earth Days)', fontsize = 16)

##Disc method with Distance
my_xticks = np.array(('Transit', 'Radial Velocity', 'Microlensing'))
fig5= plt.figure()
ax5 = fig5.add_subplot(111)
plt.xticks([1, 2, 3], my_xticks)
plt.plot(dDisc,rDistance,"bo")
fig5.suptitle('Distance From Earth With Corresponding Discovery Method', fontsize = 17)
ax5.set_xlim(0, 4)
ax5.set_xlabel('Discovery Method', fontsize = 16)
ax5.set_ylabel('Distance of Exoplanet From Earth (Parsecs)', fontsize = 16)

my_xticks = np.array(('Transit', 'Radial Velocity', 'Microlensing'))
fig6= plt.figure()
ax6 = fig6.add_subplot(111)
plt.xticks([1, 2, 3], my_xticks)
plt.plot(tDisc,rTemp,"bo")
fig6.suptitle('Temperature of Exoplanet With Corresponding Discovery Method', fontsize = 17)
ax6.set_xlim(0, 4)
ax6.set_xlabel('Discovery Method', fontsize = 16)
ax6.set_ylabel('Equilibrium Temperature of Exoplanet (Kelvin)', fontsize = 16)


# make a square figure and axes
plt.figure(7, figsize=(6,6))
ax = plt.axes([0.1, 0.1, 0.8, 0.8])
labels = 'Transit', 'Radial Velocity', 'Microlensing', 'Other'
plt.pie(percDisc, labels=labels,
                autopct='%1.1f%%', startangle=90)

plt.title('Exoplanet Discovery Methods', bbox={'facecolor':'0.8', 'pad':5})

radMass= []
masRad =[]
for i in range(len(Mass)):
    if Mass[i]!='' and Radius[i]!= '':
        masRad.append(Radius[i])
        radMass.append(Mass[i])
        
fig8=plt.figure()
plt.plot(masRad,radMass, 'o')
    
plt.show()