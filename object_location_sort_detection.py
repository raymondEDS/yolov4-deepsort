#t={'cell phone': 254.51778822734013}
#d1 = {'a': 1, 'b': 9, 'c': 4}
#method taken from https://stackabuse.com/how-to-sort-dictionary-by-value-in-python/
def sort_dict_by_location (dict):
    ''' Takes in a dictionary from object_tracker.py with {class_name:x_axis_midpoint} and sorts each class by their midpoint then
    compares to see if the class name is in alphabetical order.
    '''
    sorted_values = sorted(dict.values(),reverse=True) # Sort the dict into order of which object occur on screen
    object_location_dict = {}

    for i in sorted_values:
        for k in dict.keys():
            if dict[k] == i:
                object_location_dict[k] = dict[k]
                break

    if list(object_location_dict.keys()) ==sorted(list(dict.keys())): #check to see if items are sorted alphabetical order 
        return True
    else:
        return False


def sort_two_dict_by_elements(size_dict,loc_dict):

    sorted_size = sorted(size_dict.values(),reverse=True) #sort dict of your object order by size

    sorted_object_size_dict = {} #this is the order you want your objects in
    for i in sorted_size:
        for k in size_dict.keys():
            if size_dict[k] == i:
                sorted_object_size_dict[k] = size_dict[k]
                break

    sort_by_location = sorted(loc_dict.values(),reverse=True) #sort dict into order of which object occur on screen

    object_location_dict = {} #this is the order your objects are in

    for i in sort_by_location:
        for k in loc_dict.keys():
            if loc_dict[k] == i:
                object_location_dict[k] = loc_dict[k]
                break


    if list(object_location_dict.keys()) == list(sorted_object_size_dict.keys()):
        return True
    else:
        return False

#{'1': 13844.911917633293, '3': 8853.188246161952, '7': 4300.153398944917}


#print(sort_dict(d1))