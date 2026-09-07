from statistics import mean, sd_pop
import munpy as np
z_values = []
while len(z_values) <10000:
  z=np.random.normal(0,1)
  if -3 <= z <= 3:
    z_values.append(z)

sim_fga1 =[]
for z in z values:
  pfga = mean + (sd_pop * z)
  sim_.fga1.append(pfga)


