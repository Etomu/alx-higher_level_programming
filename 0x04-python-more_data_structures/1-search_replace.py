earch_replace(my_list, search, replace):

    return list(map(lambda e: replace if e == search else e, my_list))
