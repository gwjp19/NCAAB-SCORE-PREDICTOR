from Data_inputs import fga1_list
n = len(fga1_list)
mean = sum(fga1_list) / n
squared_diff = [(x-mean) ** 2 for x in fga1_list]
variance_pop = sum(squared_diff) / n
sd_pop = variance_pop ** 0.5
#////////////////
from Data_inputs import fgaa1_list
fgaa1n = len(fgaa1_list)
fgaa1mean = sum(fgaa1_list) / fgaa1n
fgaa1_squared_diff = [(x-fgaa1mean) ** 2 for x in fgaa1_list]
fgaa1_variance_pop = sum(fgaa1_squared_diff2 / fgaa1n
fgaa1_sd_pop = fgaa1_variance_pop ** 0.5
#////////////////
from Data_inputs import fd1_list
fd1n = len(fd1_list)
fd1mean = sum(fd1_list) / fd1n
fd1_squared_diff = [(x-fd1mean) ** 2 for x in fd1_list]
fd1_variance_pop = sum(fd1_squared_diff) / fd1n
fd1_sd_pop = fd1_variance_pop ** 0.5
#////////////////
from Data_inputs import fc1_list
fc1n = len(fc1_list)
fc1mean = sum(fc1_list) / fc1n
fc1_squared_diff = [(x-fc1mean) ** 2 for x in fc1_list]
fc1_variance_pop = sum(fc1_squared_diff) / fc1n
fc1_sd_pop = fc1_variance_pop ** 0.5
#////////////////
