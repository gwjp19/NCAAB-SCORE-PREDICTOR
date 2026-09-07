from Data_inputs import fga1_list
n = len(fga1_list)
mean = sum(fga1_list) / n
squarred_diff = [(x-mean) ** 2 for x in fga1_list]
variance_pop = sum(squared_diff) / n
sd_pop = variance_pop ** 0.5
