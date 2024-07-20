doris_dict = {'Science':0 , 'Math':0 , "Filipino":0 , "English":0, "PE":0}

for x in doris_dict.keys():
    doris_dict[x] = int(input(f"Enter grades for {x}:"))

ave = (sum(doris_dict.values()) / len(doris_dict))
print(doris_dict)
print(ave)