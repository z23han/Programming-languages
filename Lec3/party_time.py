def all_subset(my_list, my_subset=[]):
    if not len(my_list):
        return [my_subset]
    current_element = my_list[0]
    rest_of_list = my_list[1:]
    return all_subset(rest_of_list, my_subset+[current_element]) + \
           all_subset(rest_of_list, my_subset)

print all_subset([1,2,3,4,5])
    
