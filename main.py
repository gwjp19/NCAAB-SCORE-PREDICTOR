from stat_stuff import mean, sd_pop, fgaa1mean, fgaa1_sd_pop, fd1mean, fd1_sd_pop, fc1mean, fc1_sd_pop, tv1mean, tv1_sd_pop, tvf1mean, tvf1_sd_pop, orb1mean, orb1_sd_pop, drb1mean, drb1_sd_pop, drba1mean, drba1_sd_pop, orba1mean, orba1_sd_pop, name1, name2
import numpy as np
z_values = []
while len(z_values) <10000:
  z=np.random.normal(0,1)
  if -3 <= z <= 3:
    z_values.append(z)
#///////////
sim_fga1 =[]
for z in z_values:
  pfga1 = mean + (sd_pop * z)
  sim_fga1.append(pfga1)
n=len(sim_fga1)
fga1_mean = sum(sim_fga1) / n
print("Simulated FGA Average is: " + str(fga1_mean))
#//////////
sim_fgaa1 =[]
for z in z_values:
  pfgaa1 = fgaa1mean + (fgaa1_sd_pop * z)
  sim_fgaa1.append(pfgaa1)
fgaa1n=len(sim_fgaa1)
fgaa1_mean = sum(sim_fgaa1) / fgaa1n
print("Simulated FGAA Average is: " + str(fgaa1_mean))
#///////////
sim_fd1 =[]
for z in z_values:
  pfd1 = fd1mean + (fd1_sd_pop * z)
  sim_fd1.append(pfd1)
fd1n=len(sim_fd1)
fd1_mean = sum(sim_fd1) / fd1n
print("Simulated Fouls Drawn Average is: " + str(fd1_mean))
#///////////
sim_fc1 =[]
for z in z_values:
  pfc1 = fc1mean + (fc1_sd_pop * z)
  sim_fc1.append(pfc1)
fc1n=len(sim_fc1)
fc1_mean = sum(sim_fc1) / fc1n
print("Simulated Fouls Drawn Average is: " + str(fc1_mean))
#///////////
sim_tv1 =[]
for z in z_values:
  ptv1 = tv1mean + (tv1_sd_pop * z)
  sim_tv1.append(ptv1)
tv1n=len(sim_tv1)
tv1_mean = sum(sim_tv1) / tv1n
print("Simulated Fouls Drawn Average is: " + str(tv1_mean))
#///////////
sim_tvf1 =[]
for z in z_values:
  ptvf1 = tvf1mean + (tvf1_sd_pop * z)
  sim_tvf1.append(ptvf1)
tvf1n=len(sim_tvf1)
tvf1_mean = sum(sim_tvf1) / tvf1n
print("Simulated Fouls Drawn Average is: " + str(tvf1_mean))
#///////////
sim_orb1 =[]
for z in z_values:
  porb1 = orb1mean + (orb1_sd_pop * z)
  sim_orb1.append(porb1)
orb1n=len(sim_orb1)
orb1_mean = sum(sim_orb1) / orb1n
print("Simulated Fouls Drawn Average is: " + str(orb1_mean))
#///////////
sim_orba1 =[]
for z in z_values:
  porba1 = orba1mean + (orba1_sd_pop * z)
  sim_orba1.append(porba1)
orba1n=len(sim_orba1)
orba1_mean = sum(sim_orba1) / orba1n
print("Simulated Fouls Drawn Average is: " + str(orba1_mean))
#///////////
sim_drb1 =[]
for z in z_values:
  pdrb1 = drb1mean + (drb1_sd_pop * z)
  sim_drb1.append(drb1)
drb1n=len(sim_drb1)
drb1_mean = sum(sim_drb1) / drb1n
print("Simulated Fouls Drawn Average is: " + str(drb1_mean))
#///////////
sim_drba1 =[]
for z in z_values:
  pdrba1 = drba1mean + (drba1_sd_pop * z)
  sim_drba1.append(drba1)
drba1n=len(sim_drba1)
drba1_mean = sum(sim_drba1) / drba1n
print("Simulated Fouls Drawn Average is: " + str(drba1_mean))
#///////////

#TEAM 2 //////////////

from stat_stuff import mean2, sd_pop2, fgaa2mean, fgaa2_sd_pop, fd2mean, fd2_sd_pop, fc2mean, fc2_sd_pop, tv2mean, tv2_sd_pop, tvf2mean, tvf2_sd_pop, orb2mean, orb2_sd_pop, drb2mean, drb2_sd_pop, drba2mean, drba2_sd_pop, orba2mean, orba2_sd_pop
#///////////
sim_fga2 =[]
for z in z_values:
  pfga2 = mean + (sd_pop2 * z)
  sim_fga2.append(pfga2)
n2=len(sim_fga2)
fga2_mean = sum(sim_fga2) / n2
print("Simulated FGA Average is: " + str(fga2_mean))
#//////////
sim_fgaa2 =[]
for z in z_values:
  pfgaa2 = fgaa2mean + (fgaa2_sd_pop * z)
  sim_fgaa2.append(pfgaa2)
fgaa2n=len(sim_fgaa2)
fgaa2_mean = sum(sim_fgaa2) / fgaa2n
print("Simulated FGAA Average is: " + str(fgaa2_mean))
#///////////
sim_fd2 =[]
for z in z_values:
  pfd2 = fd2mean + (fd2_sd_pop * z)
  sim_fd2.append(pfd2)
fd2n=len(sim_fd2)
fd2_mean = sum(sim_fd2) / fd2n
print("Simulated Fouls Drawn Average is: " + str(fd2_mean))
#///////////
sim_fc2 =[]
for z in z_values:
  pfc2 = fc2mean + (fc2_sd_pop * z)
  sim_fc2.append(pfc2)
fc2n=len(sim_fc2)
fc2_mean = sum(sim_fc2) / fc2n
print("Simulated Fouls Drawn Average is: " + str(fc2_mean))
#///////////
sim_tv2 =[]
for z in z_values:
  ptv2 = tv2mean + (tv2_sd_pop * z)
  sim_tv2.append(ptv2)
tv2n=len(sim_tv2)
tv2_mean = sum(sim_tv2) / tv2n
print("Simulated Fouls Drawn Average is: " + str(tv2_mean))
#///////////
sim_tvf2 =[]
for z in z_values:
  ptvf2 = tvf2mean + (tvf2_sd_pop * z)
  sim_tvf2.append(ptvf2)
tvf2n=len(sim_tvf2)
tvf2_mean = sum(sim_tvf2) / tvf2n
print("Simulated Fouls Drawn Average is: " + str(tvf2_mean))
#///////////
sim_orb2 =[]
for z in z_values:
  porb2 = orb2mean + (orb2_sd_pop * z)
  sim_orb2.append(porb2)
orb2n=len(sim_orb2)
orb2_mean = sum(sim_orb2) / orb2n
print("Simulated Fouls Drawn Average is: " + str(orb2_mean))
#///////////
sim_orba2 =[]
for z in z_values:
  porba2 = orba2mean + (orba2_sd_pop * z)
  sim_orba2.append(porba2)
orba2n=len(sim_orba2)
orba2_mean = sum(sim_orba2) / orba2n
print("Simulated Fouls Drawn Average is: " + str(orba2_mean))
#///////////
sim_drb2 =[]
for z in z_values:
  pdrb2 = drb2mean + (drb2_sd_pop * z)
  sim_drb2.append(drb2)
drb2n=len(sim_drb2)
drb2_mean = sum(sim_drb2) / drb2n
print("Simulated Fouls Drawn Average is: " + str(drb2_mean))
#///////////
sim_drba2 =[]
for z in z_values:
  pdrba2 = drba2mean + (drba2_sd_pop * z)
  sim_drba2.append(drba2)
drba2n=len(sim_drba2)
drba2_mean = sum(sim_drba2) / drba2n
print("Simulated Fouls Drawn Average is: " + str(drba2_mean))
#///////////

from math_stuff.py import p_possesions1, p_possesions2

print(name1+ "'s Lowest predicted possesions: ", np.min(p_possesions1))
print(name1+ "'s Average predicted possesions: ", np.mean(p_possesions1))
print(name1+ "'s Highest predicted possesions: ", np.max(p_possesions1))

print(name2+ "'s Lowest predicted possesions: ", np.min(p_possesions2))
print(name2+ "'s Average predicted possesions: ", np.mean(p_possesions2))
print(name2+ "'s Highest predicted possesions: ", np.max(p_possesions2))




