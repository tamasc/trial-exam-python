# Create a function that takes a list as a parameter,
# and returns a new list with all its element's values doubled.
# It should raise an error if the parameter is not a list.

def double_elements(input_list):
    if isinstance(input_list, list) != list:
        raise TypeError('input argument must be a list')
    doubled_list = [element*2 for element in input_list]
    return doubled_list


double_elements(3)
