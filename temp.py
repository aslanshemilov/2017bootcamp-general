import numpy as np
import matplotlib.pyplot as plt
#Carina Plot
filename1 = r'/Users/shilpakancharla/Documents/dwarfspheroidals/dSph_Carina.dat'
target_id, ra_hr, ra_min, ra_sec, dec_deg, dec_min, dec_sec, vmag, vicol, vel, 
    vel_errs, prob = np.loadtxt(filename1,unpack=True)
member = np.where(prob > 0.9)
velm = vel[member]
plt.figure(1)
plt.clf()
plt.hist(velm,50)
plt.xlabel("Radial Velocity [km/s]")
plt.ylabel("Number of stars")
plt.title("Carina: Probability Greater than 0.9")
#Fornax Plot
filename2 = r'/Users/shilpakancharla/Documents/dwarfspheroidals/dSph_Fornax.dat'
target_id, ra_hr, ra_min, ra_sec, dec_deg, dec_min, dec_sec, vmag, vicol, vel, 
    vel_errs, prob = np.loadtxt(filename2,unpack=True)
member1 = np.where(prob > 0.9)
velm1 = vel[member1]
plt.figure(2)
plt.clf()
plt.hist(velm1,50)
plt.xlabel("Radial Velocity [km/s]")
plt.ylabel("Number of stars")
plt.title("Fornax: Probability Greater than 0.9")
#Sculptor Plot
filename3 = r'/Users/shilpakancharla/Documents/dwarfspheroidals/dSph_Sculptor.dat'
target_id, ra_hr, ra_min, ra_sec, dec_deg, dec_min, dec_sec, vmag, vicol, vel, 
    vel_errs, prob = np.loadtxt(filename3,unpack=True)
member2 = np.where(prob > 0.9)
velm2 = vel[member2]
plt.figure(3)
plt.clf()
plt.hist(velm2,50)
plt.xlabel("Radial Velocity [km/s]")
plt.ylabel("Number of stars")
plt.title("Sculptor: Probability Greater than 0.9")
#Sextans Plot
filename4 = r'/Users/shilpakancharla/Documents/dwarfspheroidals/dSph_Sextans.dat'
target_id, ra_hr, ra_min, ra_sec, dec_deg, dec_min, dec_sec, vmag, vicol, vel, 
    vel_errs, prob = np.loadtxt(filename4,unpack=True)
member3 = np.where(prob > 0.9)
velm3 = vel[member3]
plt.figure(4)
plt.clf()
plt.hist(velm3,50)
plt.xlabel("Radial Velocity [km/s]")
plt.ylabel("Number of stars")
plt.title("Sextans: Probability Greater than 0.9")
#Number of Members
len(velm)
len(velm1)
len(velm2)
len(velm3) 
#Mean Line of Sight Velocity
np.mean(velm)
np.mean(velm1)
np.mean(velm2)
np.mean(velm3)
#Line of Sight
los = np.sum(((velm-np.mean(velm))**2)/len(velm))
los1 = np.sum(((velm1-np.mean(velm1))**2)/len(velm1))
los2 = np.sum(((velm2-np.mean(velm2))**2)/len(velm2))
los3 = np.sum(((velm3-np.mean(velm3))**2)/len(velm3))
#Gravitational Constant
G = 4.28e-6
#Virial Mass
M = (5*(los)*0.85)/G
M1 = (5*(los1)*2.7)/G
M2 = (5*(los2)*1.63)/G
M3 = (5*(los3)*4)/G
#Mass-to-Light Ratio
M/(4.3e5)
M1/15.5e6
M2/2.15e6
M3/5e5
