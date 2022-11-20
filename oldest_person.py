def oldest(people:dict):
    """
    Given a dictionary containing the names and ages of a group of people, return the name of the oldest person.
    Args:
        people(dict): parameter
    Returns:
        str: the name of the oldest person
    """
    max=0
    name=''
    for k,v in people.items():
        if v>max:
            max=v
            name=k
    return name
print(oldest({'Javohir':42,'Sharof':23,'Tolib':34}))