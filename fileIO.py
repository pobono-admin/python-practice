# my_list = [i**2 for i in range(1,11)]

# with open('text.txt', 'w') as text_test:
# 	for item in my_list:
# 		text_test.write( str(item) + '\n' )

import numpy as np
import math 

for x in range(1, 11):
	my_list = repr(x).rjust(1), repr(x*x).rjust(3), repr(x*x*x).rjust(4)
	print (my_list)


for x in range(1, 11):
	list2D = '{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x)
	# Note use of 'end' on previous line
	print (list2D)


# with open('text.txt', 'w') as text_test:
# 	text_test.write(str(list2D))


# NumPY

c = np.array([[1, 2, 3, 4],[4, 5, 6, 7], [7, 8, 9, 10]])
print c.shape # size of the array

new_list = c[:] # copy

print c
print new_list


with open('empy_array.txt', 'w') as text_test:
 	text_test.write(str(np.ones((5,5))))
# text_test.closed



with open('empy_array.txt', 'r') as text_test:
	print text_test.read()





# .format
print '{0} and {1}'.format('spam', 'eggs')
print '{1} and {0}'.format('spam', 'eggs')
print 'The value of PI is approximately {0}.'.format(math.pi)  # impoart math
print 'The value of PI is approximately {0:.3f}.'.format(math.pi)  # impoart math

constant = 123456.78998765
print 'The constant is {0}'.format(constant)
print 'The constant is {0:20}'.format(constant) # int space size
print 'The constant is {0:.3f}'.format(constant) # float space size



table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}

for name, phone in table.items():
	table_list = '{0} ==> {1}'.format(name, phone)
	print table_list





# Generate some test data
data = np.arange(200).reshape((1, 1,200))

# Write the array to disk
with file('test3D.txt', 'w') as outfile:
    # I'm writing a header here just for the sake of readability
    # Any line starting with "#" will be ignored by numpy.loadtxt
    # outfile.write('# Array shape: {0}\n'.format(data.shape))

    # Iterating through a ndimensional array produces slices along
    # the last axis. This is equivalent to data[i,:,:] in this case
    for data_slice in data:

        # The formatting string indicates that I'm writing out
        # the values in left-justified columns 7 characters in width
        # with 2 decimal places.  
        np.savetxt(outfile, data_slice, fmt='%-7.2f')

        # Writing out a break to indicate different slices...
        outfile.write('# New slice\n')


# new_data = np.loadtxt('test1.txt')
# print new_data


x = np.arange(20).reshape((4,5))
np.savetxt('test2D.txt', x, fmt = '%-7.0f')  # %s ==> string




a = np.array([[1,2,3], [4,5,6], [7,8,9]])
print np.reshape(a, (9,1))



