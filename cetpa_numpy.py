# Questions --- 

#1 Create and Access an Array 

# import numpy as np 

# a = np.array([10, 20, 30, 40, 50]) 
# print(a)       # Complete Array 
# print(a[0])     # first element 
# print(a[-1])    # Last element 

# a[2] = 100     # update Value 
# print(a)    

#2... Array Slicing 

# import numpy as np 

# a = np.array([10, 20, 30, 40, 50, 60, 70]) 

# print(a)  
# print(a[:3])    # First 3 element
# print(a[2:6])   # index 2 to 5   
# print(a[-3:])   # Last 3 element
# print(a[::2])   # step of 2 element
# print(a[:-1])   # Reverse 



#3... 2 D Array Indexing 

# import numpy as np 

# a = np.array([
#     [1, 2, 3], 
#     [4, 5, 6], 
#     [7, 8, 9]
# ]) 

# print(a[1, 1])     # 5 
# print(a[0])        # First Row 
# print(a[-1])       # Last Row 
# print(a[:, 0])     # first Column 
# print(a[2, 1])   

# a[1, 1] = 50       # change 5 to 50 
# print(a)   


#4... Array Attributes 

# import numpy as np 

# a = np.array([
#     [1, 2, 3, 4], 
#     [5, 6, 7, 8], 
#     [9, 10, 11, 12]  
# ])   

# print(a.ndim)    # Dimensions 
# print(a.shape)   # Shape 
# print(a.size)     # Size 
# print(a.dtype)    # data type 


#5... Zeros(), ones() and empty() 

# import numpy as np 

# a = np.zeros(5)   # Contain 5 Zero
# print(a)    

# b = np.ones(5)     # Contain 5 ones 
# print(b)  

# c = np.zeros((3, 3))  # 3x3 matrix of zeros 
# print(c)  

# d = np.ones((2, 4))    # 2x4 matrix of ones 
# print(d)   

# e = np.array([3, 3])   # 3x3 empty array
# print(a)   


#6.. Arange() 

# import numpy as np 

# print(np.arange(1, 11)) # number from 1 to 100 
# print(np.arange(2, 21, 2)) # Even number from 2 to 20 
# print(np.arange(1, 20, 2)) # odd number from 1 to 19 
# print(np.arange(10, 0, -1)) # number from 10 to 1   


#7.. linspace 

# import numpy as np

# print(np.linspace(0, 10, 5)) # 5 equally spaced numbers from 0 to 10

# print(np.linspace(1, 100, 10)) # 10 numbers from 1 to 100

# print(np.linspace(10, 20, 6)) # 6 numbers from 10 to 20     


#8.. Sorting an Array 

# import numpy as np 

# a = np.array([45, 23, 56, 67, 23, 46, 12]) 
# b = np.sort(a)

# print(a)   # original array 
# print(b)   # Sorted array 



#9.. Concatenation Two 1D arrays 

# import numpy as np 

# a = np.array([1, 2, 3]) 
# b = np.array([4, 5, 6])  

# c = np.concatenate((a, b))    # Join Two array 
# print(c)     

# d = np.array([7, 8, 9]) 
# result = np.concatenate((a, b, d))  # Join three array 

# print(result)   



#10. Concatenate 2D arrays 

# import numpy as np 

# a = np.array([ 
#     [1, 2], 
#     [3, 4]
# ])  

# b = np.array([
#     [5, 6]
# ])   

# result = np.concatenate((a, b), axis=0)  # Join Rows 

# print(result)   


#11.. Analyze a 3D array 

# import numpy as np 

# a = np.arange(24).reshape(3, 2, 4) 
# # 3 means no of blocks 
# # 2 means rows in each 
# # 4 measn column in each 

# print(a)   

# print(a.ndim)     # dimensions 
# print(a.shape)   # Shape 
# print(a.size)    # Size 



#12... Reshape an array 

# import numpy as np 

# a = np.arange(12) 
# print(a)  

# print(a.reshape(2, 6))   
# print(a.reshape(3, 4))  
# print(a.reshape(4, 3))  
# print(a.reshape(1, 12))
# print(a.reshape(12, 1))   



#13..1D Rows and Column 
# 
# import numpy as np 

# a = np.array([10, 20, 30, 40, 50]) 
# row = a[np.newaxis, :]
# column = a[:, np.newaxis]  

# print(row) 
# print(row.shape)  

# print(column) 
# print(column.shape)    


# 14. Expand_dims()  

# import numpy as np 

# a = np.array([1, 2, 3, 4]) 

# row = np.expand_dims(a, axis=0)  # Add dimension at axis 0 -> row 

# column = np.expand_dims(a, axis=1) # Add dimension at axis 1 -> column 

# print(row) 
# print(row.shape) 

# print(column) 
# print(column.shape)


#15.. Advanced Slicing 

# import numpy as np 

# a = np.arange(1, 21) 

# print(a[:5])    # First 5 
# print(a[-5:])   # Last 5 
# print(a[5:15])  # Index 5 to 14 
# print(a[::2])   # Even Indexes
# print(a[1::2])  # Odd Indexes
# print(a[::-1])   # Reverse 


#16..Boolean Indexing 

# import numpy as np 

# a = np.array([10, 25, 30, 45, 50, 65, 70]) 

# print(a[a > 40])   # greater than 40 
# print(a[a < 40])   # less than 40 
# print(a[a % 2 == 0])  # Even Values
# print(a[a % 2 != 0])   # Odd values 
# print(a[(a >= 30) & (a <= 60)])   # between 30 and 60   



#17..Boolean Indexing in 2D 

# import numpy as np 

# a = np.array([
#     [1, 2, 3, 4], 
#     [5, 6, 7, 8], 
#     [9, 10, 11, 12]
# ])   

# print(a[a > 5]) 
# print(a[a % 2 == 0]) 
# print(a[(a >= 3) & (a <= 10)]) 
# print(a[a <= 5]) 


#18.. np.nonzero() 

# import numpy as np 

# a = np.array([
#     [10, 20, 30], 
#     [40, 50, 60], 
#     [70, 80, 90]
# ])  

# row, col = np.nonzero(a > 50)  # postions Greater than 50 

# print(row) 
# print(col)    

# row, col = np.nonzero(a == 20) 

# print(row) 
# print(col) 

# row, col = np.nonzero(a % 2 == 0)  # postions of 20 

# print(row) 
# print(col) 

# row, col = np.nonzero(a % 2 == 0) 

# print(row) 
# print(col)  


#19.. Practical np.nonzero() 

# import numpy as np 

# marks = np.array([
#     [47, 78, 32], 
#     [90, 56, 40], 
#     [67, 88, 29]
# ])   

# row, col = np.nonzero(marks > 60) 

# print(row) 
# print(col) 

# print("Marks:", marks[row, col])
  

#20.. vstack() and hstack() 

# import numpy as np 

# a = np.array([
#     [1, 2], 
#     [3, 4]
# ])

# b = np.array([
#     [5, 6], 
#     [7, 8]
# ])   

# vertical = np.vstack((a, b))   # Vertical Stacking -> add rows 

# horizontal = np.hstack((a, b))  # Horizontal Stacking -> add columns 

# print(vertical) 
# print(vertical.shape) 

# print(horizontal) 
# print(horizontal.shape)


#21... hspilt() 

# import numpy as np 

# a = np.arange(1, 25).reshape(2, 12) 

# print(a) 

# parts3 = np.hsplit(a, 3)  # Split into 3 equal Parts 

# print("3 parts:")
# for x in parts3:
#     print(x)
#     print(x.shape)  

# parts4 = np.hsplit(a, 4) # Split into 4 equal parts 

# print("4 Parts:") 
# for x in parts4: 
#     print(x) 
#     print(x.shape) 


# parts = np.hsplit(a, [3, 8])  # Split after column 3 and column 8 

# parts = np.hsplit(a, [3, 8]) 

# print("Split after Columns 3 and 8") 
# for x in parts: 
#     print(x) 
#     print(x.shape)  



#22.. View vs Copy 

# import numpy as np 

# a = np.array([10, 20, 30, 40, 50])

# b = a[1:4]  # Create a Slice 

# print("Before Change:")
# print(a) 
# print(b)   

# b[0] = 100  # change b 

# print("AFter Change:")
# print(a) 
# print(b)   


#23.. Independent Copy 

# import numpy as np 

# a = np.array([10, 20, 30, 40, 50]) 

# b = a.copy() # Create a Completely separate Copy 

# print("Before Change:")
# print(a) 
# print(b)

# b[0] = 100 

# print("After Change:") 
# print(a) 
# print(b)



















 








