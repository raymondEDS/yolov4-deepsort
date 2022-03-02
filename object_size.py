t={'cell phone': 254.51778822734013}
d1 = {'a': 1, 'b': 9, 'c': 4}
#method taken from https://stackabuse.com/how-to-sort-dictionary-by-value-in-python/
def sort_dict (dict):
    sorted_values = sorted(dict.values(),reverse=True) # Sort the values
    object_location_dict = {}

    for i in sorted_values:
        for k in dict.keys():
            if dict[k] == i:
                object_location_dict[k] = dict[k]
                break

    #print(object_location_dict)
    #print(object_location_dict.keys(),sorted(list(dict.keys()),reverse=True))

    if list(object_location_dict.keys()) ==sorted(list(dict.keys())):
        return True
    else:
        return False

#print(sort_dict(d1))