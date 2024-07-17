#importing libraries
import numpy as np
import pandas as pd
from skimage import io
from numpy import array
from sys import getsizeof

#Fetching the url and showing the image using cv2_imshow
urls=["the_last_of_us.jpg"]
for url in urls:
  image = io.imread(url)
  print('\n')

#Getting the multi-dimensional array from the image
array1 = array(image)
#Memory occupied by the multi-dimensional array
size1 = getsizeof(array1)
print(array1)

#Using Flatten function on array 1 to convert the multi-dimensional 
# array to 1-D array
array2 = array1.flatten()
#Memory occupied by array 2
size2 = getsizeof(array2)
#displaying the 1-D array
print(array2)

#Print's the two different size's of the array
print(f"Size of Multidimensional Image : {size1}")
print(f"Size of Flattened Image : {size2}")
difference = size1 - size2
#Print's the difference of memory between the size of Multidimensional & 1-D array
print(difference)