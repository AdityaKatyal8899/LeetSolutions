def SecondLargest(arr):
    if len(arr) < 2:
        return None
    
    l = None  #Largest Value Holder
    s_L = None  #2nd Largest Value Holder
    for i in arr:
        if l is None or i > l:  
            s_L = l
            l = i

        elif s_L is None or (i > s_L and i != l):
            s_L = i

    return s_L
