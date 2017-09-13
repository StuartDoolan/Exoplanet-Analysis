import numpy as np
import matplotlib.pyplot as plt

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
## Data for Mass Hists
trMass = []
trDisc = []
for i in range(len(Mass)):
    if Mass[i] != '' and int_Disc[i]==1:
        trMass.append(Mass[i])
        trDisc.append(int_Disc[i])
radMass = []
radDisc = []
for i in range(len(Mass)):
    if Mass[i] != '' and int_Disc[i]==2:
        radMass.append(Mass[i])
        radDisc.append(int_Disc[i])
micMass = []
micDisc = []
for i in range(len(Mass)):
    if Mass[i] != '' and int_Disc[i]==3:
        micMass.append(Mass[i])
        micDisc.append(int_Disc[i])


## Data for Radius hists                      
trRadius = []
trDisc = []
for i in range(len(Radius)):
    if Radius[i] != ''and int_Disc[i]==1:
        trRadius.append(Radius[i])
RadRadius = []
for i in range(len(Radius)):
    if Radius[i] != ''and int_Disc[i]==2:
        RadRadius.append(Radius[i])
MicroRadius = []
for i in range(len(Radius)):
    if Radius[i] != ''and int_Disc[i]==3:
        MicroRadius.append(Radius[i])



##Orbital Period
rOrbPer = []
opDisc = []
for i in range(len(Orb_Per)):
    if Orb_Per[i] !=''and int_Disc[i]==3:
        rOrbPer.append(Orb_Per[i])

##Distance
trDistance = []
for i in range (len(Distance)):
    if Distance[i] != ''and int_Disc[i]==1:
        trDistance.append(Distance[i])
RadDistance = []
for i in range (len(Distance)):
    if Distance[i] != ''and int_Disc[i]==2:
        RadDistance.append(Distance[i])
MicroDistance = []
for i in range (len(Distance)):
    if Distance[i] != ''and int_Disc[i]==3:
        MicroDistance.append(Distance[i])   
        
        
## Equilibrium Temperature
trTemp = []
for i in range(len(Equil_Temp)):
    if Equil_Temp[i] != ''and int_Disc[i]==1:
        trTemp.append(Equil_Temp[i])     
        
RadTemp = []
for i in range(len(Equil_Temp)):
    if Equil_Temp[i] != ''and int_Disc[i]==2:
        RadTemp.append(Equil_Temp[i])      

MicroTemp= []
for i in range(len(Equil_Temp)):
    if Equil_Temp[i] != ''and int_Disc[i]==3:
        MicroTemp.append(Equil_Temp[i])           

### Mass and Disc Histograms for each method
#Transit 
fig1= plt.figure()
ax1 = fig1.add_subplot(111)
ax1.hist(np.ravel(trMass).astype(np.float),bins = 25)
fig1.suptitle('Distribution of Exoplanet Mass Found By Transit', fontsize = 18)
ax1.set_xlabel('Mass (Me)', fontsize = 16)
ax1.set_ylabel('Frequency', fontsize = 16)
#plt.set_xlim(0, 4)
plt.grid()



#RadVel 
fig2= plt.figure()
ax2 = fig2.add_subplot(111)
ax2.hist(np.ravel(radMass).astype(np.float),bins = 25)
fig2.suptitle('Distribution of Exoplanet Mass Found By Radial Velocity', fontsize = 18)
ax2.set_xlabel('Mass (Me)', fontsize = 16)
ax2.set_ylabel('Frequency', fontsize = 16)
#plt.set_xlim(0, 4)
plt.grid()

#Micro
fig3= plt.figure()
ax3 = fig3.add_subplot(111)
ax3.hist(np.ravel(micMass).astype(np.float),bins = 25)
fig3.suptitle('Distribution of Exoplanet Mass Found By Microlensing', fontsize = 18)
ax3.set_xlabel('Mass (Me)', fontsize = 16)
ax3.set_ylabel('Frequency', fontsize = 16)
plt.grid()


### Radius and Disc Histograms for each method
#Transit 
fig4= plt.figure()
ax4 = fig4.add_subplot(111)
ax4.hist(np.ravel(trTemp).astype(np.float),bins = 25)
fig4.suptitle('Distribution of Exoplanet Temperature Found By Transit', fontsize = 18)
ax4.set_xlabel('Equilibrium Temperature (Kelvin)', fontsize = 16)
ax4.set_ylabel('Frequency', fontsize = 16)
#plt.set_xlim(0, 4)
plt.grid()



#RadVel 
fig5= plt.figure()
ax5 = fig5.add_subplot(111)
ax5.hist(np.ravel(RadTemp).astype(np.float),bins = 25)
fig5.suptitle('Distribution of Exoplanet Temperature Found By Radial Velocity', fontsize = 18)
ax5.set_xlabel('Equilibrium Temperature (Kelvin)', fontsize = 16)
ax5.set_ylabel('Frequency', fontsize = 16)
#plt.set_xlim(0, 4)
plt.grid()

#Micro
fig6= plt.figure()
ax6 = fig6.add_subplot(111)
ax6.hist(np.ravel(MicroTemp).astype(np.float),bins = 25)
fig6.suptitle('Distribution of Exoplanet Temperature Found By Microlensing', fontsize = 18)
ax6.set_xlabel('Equilibrium Temperature (Kelvin)', fontsize = 16)
ax6.set_ylabel('Frequency', fontsize = 16)
plt.grid()


### Radius and Disc Histograms for each method
#Transit 
fig7= plt.figure()
ax7 = fig7.add_subplot(111)
ax7.hist(np.ravel(trRadius).astype(np.float),bins = 25)
fig7.suptitle('Distribution of Exoplanet Radius Found By Transit', fontsize = 18)
ax7.set_xlabel('Radius of Exoplanet (Re)', fontsize = 16)
ax7.set_ylabel('Frequency', fontsize = 16)
plt.grid()



#RadVel 
fig8= plt.figure()
ax8 = fig8.add_subplot(111)
ax8.hist(np.ravel(RadRadius).astype(np.float),bins = 25)
fig8.suptitle('Distribution of Exoplanet Radius Found By Radial Velocity', fontsize = 18)
ax8.set_xlabel('Radius of Exoplanet (Re)', fontsize = 16)
ax8.set_ylabel('Frequency', fontsize = 16)
plt.grid()

#Micro
fig9= plt.figure()
ax9 = fig9.add_subplot(111)
ax9.hist(np.ravel(MicroRadius).astype(np.float),bins = 25)
fig9.suptitle('Distribution of Exoplanet Radius Found By Microlensing', fontsize = 18)
ax9.set_xlabel('Radius of Exoplanet (Re)', fontsize = 16)
ax9.set_ylabel('Frequency', fontsize = 16)
plt.grid()

### Distance and Disc Histograms for each method
#Transit 
fig10= plt.figure()
ax10 = fig10.add_subplot(111)
ax10.hist(np.ravel(trDistance).astype(np.float),bins = 25)
fig10.suptitle('Distribution of Exoplanet Distance Found By Transit', fontsize = 18)
ax10.set_xlabel('Distance From Earth (parsecs)', fontsize = 16)
ax10.set_ylabel('Frequency', fontsize = 16)
#plt.set_xlim(0, 4)
plt.grid()



#RadVel 
fig11= plt.figure()
ax11 = fig11.add_subplot(111)
ax11.hist(np.ravel(RadDistance).astype(np.float),bins = 25)
fig11.suptitle('Distribution of Exoplanet Distance Found By Radial Velocity', fontsize = 18)
ax11.set_xlabel('Distance From Earth (parsecs)', fontsize = 16)
ax11.set_ylabel('Frequency', fontsize = 16)
#plt.set_xlim(0, 4)
plt.grid()

#Micro
fig12= plt.figure()
ax12 = fig12.add_subplot(111)
ax12.hist(np.ravel(MicroDistance).astype(np.float),bins = 25)
fig12.suptitle('Distribution of Exoplanet Distance Found By Microlensing', fontsize = 18)
ax12.set_xlabel('Distance From Earth (parsecs)', fontsize = 16)
ax12.set_ylabel('Frequency', fontsize = 16)
plt.grid()
plt.show()

