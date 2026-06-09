# day 10 code

# numpy is a package


# list 1d
a=[1,2,3,False,"vikram"]
print(a)
print(type(a))


# array 1d
import numpy as np
arr=np.array(a)
print(arr)
print(type(arr))


# list 2d
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print(matrix[0][0])


# array 2d
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
print(arr[0,0]) # it will print first row first element



# list 2d replace 4 by 100
matrix=[[1,2,3],[4,5,6],[7,8,9]]
matrix[1][0]=100
print(matrix)



# array 2d
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
arr[1][0]=100
print(arr)


# list 
l=[1,2,3]
lm=l*2
print(lm)


# array
import numpy as np
arr=np.array(l)
arrm=arr*2
print(arrm)

# from the above we come to conclusion that array is more efficient than list 


# comparison
# list
import time
start=time.time()
l=[i*2 for i in range(100)]
print("list output",time.time() - start)

# array
import numpy as np
start=time.time()
arr=np.array(100)*2
print("array output",time.time() - start)


# zeros array 1d 
import numpy as np
arr=np.zeros(5)
print(arr)

# zeros array 2d 
import numpy as np
arr=np.zeros((3,4))
print(arr)


# ones array 1d
import numpy as np
arr=np.ones(5)
print(arr)


# ones array 2d
import numpy as np
arr=np.ones((3,4))
print(arr)


# question zeros  2d array increment every element by 10
import numpy as np
arr=np.zeros((3,4))
arr= arr + 10
print(arr)


# full for 1d
import numpy as np
arr=np.full((3),5)
print(arr)


# full for 2d 
import numpy as np
arr1=np.full((2,3),5)
print(arr1)


# question  with help of zeros make a 2d array having value 6
import numpy as np
arr=np.zeros((3,4))
arr= arr + 6
print(arr)


# question  with help of full make a 2d array having value 
import numpy as np
arr1=np.full((2,3),1)
print(arr1)


# random 1d 
import numpy as np
arr=np.random.random(5)
print(arr)


# random 2d 
arr1=np.random.random((2,3))
print(arr1)


# arange 1d
import numpy as np
arr=np.arange(10)
print(arr)


# arange 2d
import numpy as np
arr=np.arange(12).reshape(3,4)
print(arr) 


# vector,matrix,tensor

# vector 1d list 
l=[1,2,3,False,"vikram"]
print(l)

# vector 1d array
import numpy as np
arr=np.array(l)
print(arr)


# matrix 2d list 
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)


# matrix 2d array
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)


# tensor 3d list
tensor=[[[1,2],[3,4]],[[5,6],[7,8]]]
print(tensor)


# array
import numpy as np
arr=np.arange(12).reshape(3,4)
print("shape",np.shape(arr))
print("dimension",np.ndim(arr))
print("size",np.size(arr))
print("datatype",arr.dtype)
