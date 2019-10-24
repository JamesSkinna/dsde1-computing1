the_list = [1, 2, 3, 4, 5]
beginning = 1
end = 4
end_of_list = len(the_list)
if (end < beginning) or (beginning < 0) or (end > end_of_list):  
    raise ValueError
else: 
    new_list = the_list[beginning: end]
    new_list = new_list.reverse()
print(new_list)