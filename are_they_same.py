''' Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) 
that checks whether the two arrays have the "same" elements, 
with the same multiplicities. "Same" means, here, that the elements in b are the 
elements in a squared, regardless of the order.'''



def comp(array1, array2):
    # your code
    import numpy as np
    
    array1=[num*num for num in array1]
    array1.sort()
    array1=np.array(array1)
    array2=array2
    array2.sort()
    array2=np.array(array2)
    
    return np.all((array1-array2)==[0]*len(array1))