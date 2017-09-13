### Plotting survey data from exoplanet experiment
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
from itertools import cycle, islice

import pandas
plt.close('all')

# read in planets file and dick about with plots
f = open('/Users/stuartdoolan/Documents/Accelerate Internship/SurveyPythonFriendly.csv', 'r')


#read in data from file
filecontents = f.readlines()
f.close()


# skip through header line
filestart = 1


totalpupils = len(filecontents)-1
pupilinfo = [[0 for x in range(100)] for y in range(totalpupils)]

#probably cheating but it works
for i in range(totalpupils):
    thisline = []
    lines = filecontents[filestart+i].split(',')
    for entry in lines:
            thisline.append(entry.strip())
    pupilinfo[i] = thisline
pupilinfo = np.array(pupilinfo)
header = pupilinfo[0]
pupilinfo = np.delete(pupilinfo, (0), axis=0)
pupilinfoT = np.array(zip(*pupilinfo))

day = pupilinfoT[0]
date = pupilinfoT[1]
time = pupilinfoT[2]
firstname = pupilinfoT[3]
midname = pupilinfoT[4]
secondname = pupilinfoT[5]
school = pupilinfoT[6]
gender = pupilinfoT[7]
exp = pupilinfoT[8]
lexp = list(exp)
tele = pupilinfoT[9]
ltele = list(tele)
notes = pupilinfoT[10]

nogood = lexp.count('Good')
noneutral = lexp.count('Neutral')
nopoor = lexp.count('Poor')
##Plots
# horiz bar chart for experience of all pupils

opinion = ('Good', 'Neutral', 'Poor')
y_pos = np.arange(len(opinion))

fig1 =plt.figure()
blines =plt.barh(y_pos, [nogood,noneutral, nopoor], align='center', height = 0.6)
ax1 = fig1.add_subplot(111)
blines[0].set_color('c')
blines[1].set_color('c')
blines[2].set_color('c')
ax1.set_yticks(y_pos)
ax1.set_yticklabels(opinion, fontsize = 14)
ax1.invert_yaxis()  # labels read top-to-bottom
ax1.set_xlabel('Number of Pupils',fontsize = 14 )
ax1.set_title('What Was Your Experience of Astro School?', fontsize = 16)
plt.show()


##barh for telescope question

yes = ltele.count('Yes')
no = ltele.count('No')
answer = ('Yes', 'No')
ypos2 = np.arange(len(answer))

fig2 =plt.figure()
blines =plt.barh(ypos2, [yes,no], align='center', height = 0.5)
ax2 = fig2.add_subplot(111)
blines[0].set_color('c')
blines[1].set_color('c')
ax2.set_yticks(ypos2)
ax2.set_yticklabels(answer, fontsize = 14)
ax2.invert_yaxis()  # labels read top-to-bottom
ax2.set_xlabel('Number of Pupils',fontsize = 14 )
ax2.set_title('Would You Like to Take Part In Our Next Experiment?', fontsize = 16)
plt.show()

#comparing male and female good/poor/neutral

femgood = 0
fempoor = 0
femneutral = 0
malegood = 0
malepoor = 0
maleneutral = 0
fyes = 0
fno = 0
myes = 0
mno = 0

for i in range(totalpupils-1):
    if gender[i] =='Female' and exp[i] == 'Good':
        femgood =femgood+1
    if gender[i] =='Female' and exp[i] == 'Neutral':
        femneutral =femneutral+1
    if gender[i] =='Female' and exp[i] == 'Poor':
        fempoor =fempoor+1
    if gender[i] =='Male' and exp[i] == 'Good':
        malegood =malegood+1
    if gender[i] =='Male' and exp[i] == 'Neutral':
        maleneutral =maleneutral+1
    if gender[i] =='Male' and exp[i] == 'Poor':
        malepoor =malepoor+1
    
    if gender[i] =='Female' and tele[i] == 'Yes':
        fyes = fyes+1
    if gender[i] =='Female' and tele[i] == 'No':
        fno = fno+1
    
    if gender[i] =='Male' and tele[i] == 'Yes':
        myes = myes+1
    if gender[i] =='Male' and tele[i] == 'No':
        mno = mno+1

fig3 =plt.figure()
blines1 =plt.barh(ypos2, [fyes,fno], align='center', height = 0.30,alpha = 0.8, label = 'Female')
blines2 =plt.barh(ypos2+0.3, [myes,mno], align='center', height = 0.3, alpha = 0.8, label = 'Male')

ax3 = fig3.add_subplot(111)
blines1[0].set_color('c')
blines1[1].set_color('c')
blines2[0].set_color('b')
blines2[1].set_color('b')
ax3.set_yticks(ypos2+0.15)
ax3.set_yticklabels(answer, fontsize = 14)
ax3.invert_yaxis()  # labels read top-to-bottom
ax3.set_xlabel('Number of Pupils',fontsize = 14 )
ax3.set_title('Comparing Female and Male Interest in Next Project', fontsize = 16)
plt.legend(loc =4)
plt.show()

fig4 =plt.figure()
blines1 =plt.barh(y_pos, [femgood,femneutral, fempoor], align='center', height = 0.30,alpha = 0.8, label = 'Female')
blines2 =plt.barh(y_pos+0.3, [malegood,maleneutral, malepoor], align='center', height = 0.3, alpha = 0.8, label = 'Male')

ax4 = fig4.add_subplot(111)
blines1[0].set_color('c')
blines1[1].set_color('c')
blines1[2].set_color('c')
blines2[0].set_color('b')
blines2[1].set_color('b')
blines2[2].set_color('b')
ax4.set_yticks(y_pos+0.15)
ax4.set_yticklabels(opinion, fontsize = 14)
ax4.invert_yaxis()  # labels read top-to-bottom
ax4.set_xlabel('Number of Pupils',fontsize = 14 )
ax4.set_title('Comparing Female and Male Experience', fontsize = 16)
plt.legend(loc =4)
plt.show()

mongood= 0
monneutral = 0
monpoor = 0
monyes = 0
monno = 0
tuegood = 0
tueneutral = 0
tuepoor = 0
tueyes = 0
tueno = 0
wedgood =0
wedneutral = 0
wedpoor = 0
wedyes = 0
wedno = 0
thurgood = 0
thurneutral = 0
thurpoor = 0
thuryes = 0
thurno = 0
frigood = 0
frineutral = 0
fripoor = 0
friyes = 0
frino = 0



for i in range(totalpupils-1):
    if day[i] =='Monday' and exp[i] == 'Good':
        mongood =mongood+1
    if day[i] =='Monday' and exp[i] == 'Neutral':
        monneutral =monneutral+1
    if day[i] =='Monday' and exp[i] == 'Poor':
        monpoor =monpoor+1
    
    if day[i] =='Monday' and tele[i] == 'Yes':
        monyes =monyes+1
    if day[i] =='Monday' and tele[i] == 'No':
        monno =monno+1
    
    if day[i] =='Tuesday' and exp[i] == 'Good':
        tuegood =tuegood+1
    if day[i] =='Tuesday' and exp[i] == 'Neutral':
        tueneutral =tueneutral+1
    if day[i] =='Tuesday' and exp[i] == 'Poor':
        tuepoor =tuepoor+1
        
    if day[i] =='Tuesday' and tele[i] == 'Yes':
        tueyes =tueyes+1
    if day[i] =='Tuesday' and tele[i] == 'No':
        tueno =tueno+1
        
    if day[i] =='Wednesday' and exp[i] == 'Good':
        wedgood =wedgood+1
    if day[i] =='Wednesday' and exp[i] == 'Neutral':
        wedneutral =wedneutral+1
    if day[i] =='Wednesday' and exp[i] == 'Poor':
        wedpoor =wedpoor+1
        
    if day[i] =='Wednesday' and tele[i] == 'Yes':
        wedyes =wedyes+1
    if day[i] =='Wednesday' and tele[i] == 'No':
        wedno =wedno+1
        
    if day[i] =='Thursday' and exp[i] == 'Good':
        thurgood =thurgood+1
    if day[i] =='Thursday' and exp[i] == 'Neutral':
        thurneutral =thurneutral+1
    if day[i] =='Thursday' and exp[i] == 'Poor':
        thurpoor =thurpoor+1
        
    if day[i] =='Thursday' and tele[i] == 'Yes':
        thuryes =thuryes+1
    if day[i] =='Thursday' and tele[i] == 'No':
        thurno =thurno+1
        
    if day[i] =='Friday' and exp[i] == 'Good':
        frigood =frigood+1
    if day[i] =='Friday' and exp[i] == 'Neutral':
        frineutral =frineutral+1
    if day[i] =='Friday' and exp[i] == 'Poor':
        fripoor =fripoor+1
        
    if day[i] =='Friday' and tele[i] == 'Yes':
        friyes =friyes+1
    if day[i] =='Friday' and tele[i] == 'No':
        frino =frino+1

daygood = [mongood, tuegood, wedgood, thurgood, frigood]
dayneutral = (monneutral, tueneutral, wedneutral, thurneutral, frineutral)
daypoor = (monpoor, tuepoor, wedpoor, thurpoor, fripoor)
dayyes = (monyes, tueyes, wedyes, thuryes, friyes)
dayno = (monno, tueno, wedno, thurno, frino)



fig5 =plt.figure()
blines1 =plt.barh(y_pos, [mongood,monneutral, monpoor], align='center', height = 0.10,alpha = 0.8, label = 'Monday')
blines2 =plt.barh(y_pos+0.1, [tuegood,tueneutral, tuepoor], align='center', height = 0.1, alpha = 0.8, label = 'Tuesday')
blines3 =plt.barh(y_pos+0.2, [wedgood,wedneutral, wedpoor], align='center', height = 0.1, alpha = 0.8, label = 'Wednesday')
blines4 =plt.barh(y_pos+0.3, [thurgood,thurneutral, thurpoor], align='center', height = 0.1, alpha = 0.8, label = 'Thursday')
blines5 =plt.barh(y_pos+0.4, [frigood,frineutral, fripoor], align='center', height = 0.1, alpha = 0.8, label = 'Friday')


Days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
ax5 = fig5.add_subplot(111)
blines1[0].set_color('c')
blines1[1].set_color('c')
blines1[2].set_color('c')
blines2[0].set_color('orange')
blines2[1].set_color('orange')
blines2[2].set_color('orange')
blines3[0].set_color('red')
blines3[1].set_color('red')
blines3[2].set_color('red')
blines4[0].set_color('blue')
blines4[1].set_color('blue')
blines4[2].set_color('blue')
blines5[0].set_color('pink')
blines5[1].set_color('pink')
blines5[2].set_color('pink')
ax5.set_yticks(y_pos+0.15)
ax5.set_yticklabels(opinion, fontsize = 14)
ax5.invert_yaxis()  # labels read top-to-bottom
ax5.set_xlabel('Number of Pupils',fontsize = 14 )
ax5.set_title('All Pupils\' Experience by Day',  fontsize = 16)
plt.legend(loc =4)
plt.show()


fig6 =plt.figure()
blines1 =plt.barh(ypos2, [monyes,monno], align='center', height = 0.10,alpha = 0.8, label = 'Monday')
blines2 =plt.barh(ypos2+0.1, [tueyes,tueno], align='center', height = 0.1, alpha = 0.8, label = 'Tuesday')
blines3 =plt.barh(ypos2+0.2, [wedyes,wedno], align='center', height = 0.1, alpha = 0.8, label = 'Wednesday')
blines4 =plt.barh(ypos2+0.3, [thuryes,thurno], align='center', height = 0.1, alpha = 0.8, label = 'Thursday')
blines5 =plt.barh(ypos2+0.4, [friyes,frino], align='center', height = 0.1, alpha = 0.8, label = 'Friday')

Days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
ax6 = fig6.add_subplot(111)
blines1[0].set_color('c')
blines1[1].set_color('c')
blines2[0].set_color('orange')
blines2[1].set_color('orange')
blines3[0].set_color('red')
blines3[1].set_color('red')
blines4[0].set_color('blue')
blines4[1].set_color('blue')
blines5[0].set_color('pink')
blines5[1].set_color('pink')
ax6.set_yticks(ypos2+0.15)
ax6.set_yticklabels(answer, fontsize = 14)
ax6.invert_yaxis()  # labels read top-to-bottom
ax6.set_xlabel('Number of Pupils',fontsize = 14 )
ax6.set_title('All Pupils\' Interest in Next Project by Day',  fontsize = 16)
plt.legend(loc =4)
plt.show()