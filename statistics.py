print(fga1_list)
n = len(fga1_list)
mean = sum(fga1_list) / n
squarred_diff = [(x-men) ** 2 for x in fga1_list]
variance_pop = sum(squared_dif) / n
sd_op = variance_pop ** 0.5
