def count_all(txt):
    """
    Given a function that takes a string and calculates the number of letters and digits within it.
    Return the result in a dictionary.
    Args:
        txt(str): count letters and digits
    Returns:
        dict: dictionary with letters and digits
    """
    data={}
    i=0
    l=0
    d=0
    while i < len(txt):
        if txt[i].isdigit():
            d+=1
        if txt[i].isalpha():
            l+=1
        i+=1
    data['LETTERS']=l
    data['DIGITS']=d
    return data
print(count_all('python foundations 2022'))