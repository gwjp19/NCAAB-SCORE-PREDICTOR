from stat_stuff import mean, sd_pop, fgaa1mean, fgaa1_sd_pop, fd1mean, fd1_sd_pop, fc1mean, fc1_sd_pop, tv1mean, tv1_sd_pop, tvf1mean, tvf1_sd_pop, orb1mean, orb1_sd_pop, drb1mean, drb1_sd_pop, drba1mean, drba1_sd_pop, orba1mean, orba1_sd_pop
import numpy as np
z_values = []
while len(z_values) <10000:
  z=np.random.normal(0,1)
  if -3 <= z <= 3:
    z_values.append(z)

sim_fga1 =[]
for z in z_values:
  pfga = mean + (sd_pop * z)
  sim_fga1.append(pfga)
n=len(sim_fga1)
fga1_mean = sum(sim_fga1) / n
print(fga1_mean)

