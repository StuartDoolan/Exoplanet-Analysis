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

#Same set up as discovery method script, populate new lists with corresponding 
#nonempty planet data to be plotted 
rRadius=[]
rOrb=[]
for i in range(len(Orb_Per)):
    if Radius[i]!='' and Orb_Per[i]!='':
        rRadius.append(Radius[i])
        rOrb.append(Orb_Per[i])
        
mMass=[]
mOrb=[]
for i in range(len(Orb_Per)):
    if Mass[i]!='' and Orb_Per[i]!='':
        mMass.append(Mass[i])
        mOrb.append(Orb_Per[i])

tTemp=[]
tOrb=[]
for i in range(len(Orb_Per)):
    if Equil_Temp[i]!='' and Orb_Per[i]!='':
        tTemp.append(Equil_Temp[i])
        tOrb.append(Orb_Per[i])   

dDistance=[]
dOrb=[]
for i in range(len(Orb_Per)):
    if Distance[i]!='' and Orb_Per[i]!='':
        dDistance.append(Distance[i])
        dOrb.append(Orb_Per[i])        
        
nPlanets=[]
nOrb=[]
for i in range(len(Orb_Per)):
    if no_planets[i]!='' and Orb_Per[i]!='':
        nPlanets.append(no_planets[i])
        nOrb.append(Orb_Per[i])        


##plots
#Radius
fig1= plt.figure()
ax1 = fig1.add_subplot(111)
plt.plot(rOrb,rRadius,"bo")
fig1.suptitle('Radius of Exoplanets Against Orbital Period', fontsize = 17)
ax1.set_xlabel('Orbital Period (Earth Days)', fontsize = 16)
ax1.set_ylabel('Radius (Re)', fontsize = 16)

fig2= plt.figure()
ax2 = fig2.add_subplot(111)
plt.plot(rOrb,rRadius,"bo")
fig2.suptitle('Radius of Exoplanets Against Orbital Period With Outliers Removed', fontsize = 17)
ax2.set_xlim(0, 1000)
ax2.set_xlabel('Orbital Period (Earth Days)', fontsize = 16)
ax2.set_ylabel('Radius (Re)', fontsize = 16)

#Mass
fig3= plt.figure()
ax3 = fig3.add_subplot(111)
plt.plot(mOrb,mMass,"bo")
fig3.suptitle('Mass of Exoplanets Against Orbital Period', fontsize = 17)
ax3.set_xlabel('Orbital Period (Earth Days)', fontsize = 16)
ax3.set_ylabel('Mass (Me)', fontsize = 16)

fig4= plt.figure()
ax4 = fig4.add_subplot(111)
plt.plot(mOrb,mMass,"bo")
fig4.suptitle('Mass of Exoplanets Against Orbital Period With Outliers Removed', fontsize = 17)
ax4.set_xlim(0, 1000)
ax4.set_xlabel('Orbital Period (Earth Days)', fontsize = 16)
ax4.set_ylabel('Mass (Me)', fontsize = 16)

#Temperature
fig5= plt.figure()
ax5 = fig5.add_subplot(111)
plt.plot(tOrb,tTemp,"bo")
fig5.suptitle('Temperature of Exoplanets Against Orbital Period', fontsize = 17)
ax5.set_xlabel('Orbital Period (Earth Days)', fontsize = 16)
ax5.set_ylabel('Equilibrium Temperature (Kelvin)', fontsize = 16)

fig6= plt.figure()
ax6 = fig6.add_subplot(111)
plt.plot(tOrb,tTemp,"bo")
fig6.suptitle('Temperature Against Orbital Period With Outliers Removed', fontsize = 17)
ax6.set_xlim(0, 1000)
ax6.set_xlabel('Orbital Period (Earth Days)', fontsize = 16)
ax6.set_ylabel('Equilibrium Temperature of Exoplanet (Kelvin)', fontsize = 16)

##Distance
fig7= plt.figure()
ax7 = fig7.add_subplot(111)
plt.plot(dOrb,dDistance,"bo")
fig7.suptitle('Distance of Exoplanets Against Orbital Period', fontsize = 17)
ax7.set_xlabel('Orbital Period (Earth Days)', fontsize = 16)
ax7.set_ylabel('Distance of Exoplanet from Earth (Parsecs)', fontsize = 16)

fig8= plt.figure()
ax8 = fig8.add_subplot(111)
plt.plot(dOrb,dDistance,"bo")
fig8.suptitle('Distance Against Orbital Period With Outliers Removed', fontsize = 17)
ax8.set_xlim(0, 2000)
ax8.set_ylim(0, 4000)
ax8.set_xlabel('Orbital Period (Earth Days)', fontsize = 16)
ax8.set_ylabel('Distance of Exoplanet from Earth (Parsecs)', fontsize = 16)

##Discovery Method
rOrbPer = []
opDisc = []
for i in range(len(Orb_Per)):
    if Orb_Per[i] !=''and int_Disc[i]!=4:
        rOrbPer.append(Orb_Per[i])
        opDisc.append(int_Disc[i])
        
##Disc method with Orbital Period
my_yticks = np.array(('Transit', 'Radial Velocity', ' Microlensing'))
fig9= plt.figure()
ax9 = fig9.add_subplot(111)
plt.yticks([1, 2, 3], my_yticks, rotation = 'vertical')
plt.plot(rOrbPer,opDisc,"bo")
fig9.suptitle('Orbital Period of Exoplanets With Corresponding Discovery Method', fontsize = 17)
ax9.set_ylim(0, 4)
ax9.set_ylabel('Discovery Method', fontsize = 16)
ax9.set_xlabel('Orbital Period (Earth Days)', fontsize = 16)

#Set up for discovery method hists
TrOrb = []
for i in range (len(Distance)):
    if Orb_Per[i] != ''and int_Disc[i]==1:
        TrOrb.append(Orb_Per[i])
RadOrb = []
for i in range (len(Distance)):
    if Orb_Per[i] != ''and int_Disc[i]==2:
        RadOrb.append(Orb_Per[i])
MicroOrb = []
for i in range (len(Distance)):
    if Orb_Per[i] != ''and int_Disc[i]==3:
        MicroOrb.append(Orb_Per[i])
        
### Orbital Period and Disc Histograms for each method
#Transit 
fig10= plt.figure()
ax10 = fig10.add_subplot(111)
ax10.hist(np.ravel(TrOrb).astype(np.float),bins = 25)
fig10.suptitle('Distribution of Orbital Period Found By Transit', fontsize = 18)
ax10.set_xlabel('Orbital Period of Exoplanet (Earth Days)', fontsize = 16)
ax10.set_ylabel('Frequency', fontsize = 16)
plt.grid()


#RadVel 
fig11= plt.figure()
ax11 = fig11.add_subplot(111)
ax11.hist(np.ravel(RadOrb).astype(np.float),bins = 25)
fig11.suptitle('Distribution of Orbital Period Found By Radial Velocity', fontsize = 18)
ax11.set_xlabel('Orbital Period of Exoplanet (Earth Days)', fontsize = 16)
ax11.set_ylabel('Frequency', fontsize = 16)
plt.grid()

#Micro
fig12= plt.figure()
ax12 = fig12.add_subplot(111)
ax12.hist(np.ravel(MicroOrb).astype(np.float),bins = 25)
fig12.suptitle('Distribution of Orbital Period Found By Microlensing', fontsize = 18)
ax12.set_xlabel('Orbital Period of Exoplanet (Earth Days)', fontsize = 16)
ax12.set_ylabel('Frequency', fontsize = 16)
plt.grid()

Orb2 = []
for i in range(len(Orb_Per)):
    if Orb_Per[i]!='':
        Orb2.append(Orb_Per[i])

Orb3 = np.ravel(Orb2).astype(np.float)
Orb4 = []
for i in range(len(Orb3)):
    if Orb3[i]<1000:
        Orb4.append(Orb2[i])
fig13= plt.figure()
ax13 = fig13.add_subplot(111)
ax13.hist(np.ravel(Orb4).astype(np.float),bins = 50)
fig13.suptitle('Distribution of Orbital Period', fontsize = 18)
ax13.set_xlabel('Orbital Period of Exoplanet (Earth Days)', fontsize = 16)
ax13.set_ylabel('Frequency', fontsize = 16)
plt.grid()

LessEarth = []
NearEarth = []
AboveEarth = []
for i in range(len(Orb3)):
    if Orb3[i]<300:
        LessEarth.append(Orb3[i])
    elif Orb3[i]>430:
        AboveEarth.append(Orb3[i])
    else:
        NearEarth.append(Orb3[i])
EarthGroup = [len(LessEarth), len(NearEarth), len(AboveEarth)]

my_xticks = np.array(('Below Earth', 'Near Earth', 'Above Earth'))
fig14= plt.figure()
ax14 = fig14.add_subplot(111)
plt.xticks([1, 2, 3], my_xticks)
plt.bar([1,2,3], EarthGroup, color="blue", align = 'center')
fig14.suptitle('Orbital Period of Exoplanets Compared to Earth', fontsize = 17)
ax14.set_xlim(0, 4)
ax14.set_xlabel('Orbital Period (Grouped)', fontsize = 16)
ax14.set_ylabel('Frequency', fontsize = 16)                

LessMerc = []
NearMerc = []
AboveMerc = []
for i in range(len(Orb3)):
    if Orb3[i]<70:
        LessMerc.append(Orb3[i])
    elif Orb3[i]>96:
        AboveMerc.append(Orb3[i])
    else:
        NearMerc.append(Orb3[i])
MercGroup = [len(LessMerc), len(NearMerc), len(AboveMerc)]

my_xticks = np.array(('Below Mercury', 'Near Mercury', 'Above Mercury'))
fig15= plt.figure()
ax15 = fig15.add_subplot(111)
plt.xticks([1, 2, 3], my_xticks)
plt.bar([1,2,3], MercGroup, color="blue", align = 'center')
fig15.suptitle('Orbital Period of Exoplanets Compared to Mercury', fontsize = 17)
ax15.set_xlim(0, 4)
ax15.set_xlabel('Orbital Period (Grouped)', fontsize = 16)
ax15.set_ylabel('Frequency', fontsize = 16)    

LessNep = []
NearNep = []
AboveNep = []
for i in range(len(Orb3)):
    if Orb3[i]<48000:
        LessNep.append(Orb3[i])
    elif Orb3[i]>78000:
        AboveNep.append(Orb3[i])
    else:
        NearNep.append(Orb3[i])
NepGroup = [len(LessNep), len(NearNep), len(AboveNep)]

my_xticks = np.array(('Below Neptune', 'Near Neptune', 'Above Neptune'))
fig16= plt.figure()
ax16 = fig16.add_subplot(111)
plt.xticks([1, 2, 3], my_xticks)
plt.bar([1,2,3], NepGroup, color="blue", align = 'center')
fig16.suptitle('Orbital Period of Exoplanets Compared to Neptune', fontsize = 17)
ax16.set_xlim(0, 4)
ax16.set_xlabel('Orbital Period (Grouped)', fontsize = 16)
ax16.set_ylabel('Frequency', fontsize = 16)    

LessJup = []
NearJup = []
AboveJup = []
for i in range(len(Orb3)):
    if Orb3[i]<3440:
        LessJup.append(Orb3[i])
    elif Orb3[i]>5260:
        AboveJup.append(Orb3[i])
    else:
        NearJup.append(Orb3[i])
JupGroup = [len(LessJup), len(NearJup), len(AboveJup)]

my_xticks = np.array(('Below Jupiter', 'Near Jupiter', 'Above Jupiter'))
fig17= plt.figure()
ax17 = fig17.add_subplot(111)
plt.xticks([1, 2, 3], my_xticks)
plt.bar([1,2,3], JupGroup, color="blue", align = 'center')
fig17.suptitle('Orbital Period of Exoplanets Compared to Jupiter', fontsize = 17)
ax17.set_xlim(0, 4)
ax17.set_xlabel('Orbital Period (Grouped)', fontsize = 16)
ax17.set_ylabel('Frequency', fontsize = 16)    


Dist2 = []
for i in range(len(Distance)):
    if Distance[i]!='':
        Dist2.append(Distance[i])
Orb2 = []
for i in range(len(Orb_Per)):
    if Orb_Per[i]!='':
        Orb2.append(Orb_Per[i])
plt.show()
