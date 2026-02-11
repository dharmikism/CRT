'''
import array
arr = array.array('i',[12,45,78,36])
print(arr,type(arr))
arr.append(40)
print(arr)
arr.append(12.45)
print(arr)
'''
import numpy
arr = numpy.array([12,45,78,36])
arr1 = numpy.array([[1,2,3],
                    [4,5,6],
                    [7,8,9]])
print(arr.shape)
print(arr1.shape)
print(arr.dtype)