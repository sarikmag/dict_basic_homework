def cities_dict(cities:list):
    """
    Given a list of cities names, Return dictionary with keys ordered by city name.
    Args:
        cities(list): list of cities names
    Returns:
        dict: dictionary with keys ordered by city name
    """
    i=0
    data={}
    while i < len(cities):
        data[i]=cities[i]
        i+=1
    return data
print(cities_dict(('Bukhara','Khiva','Namangan','Samarkand')))