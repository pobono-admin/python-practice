# LIST PRACTICE

test_list = ["a", 'b', 'c', 'd', 1, 2, 3, 5]
print (test_list)
print len(test_list) # length of the array


list_slicing = test_list[0:2] #Slicing Lists 
a_index = list_slicing.index('a') #Find element
print (list_slicing, a_index)

test_list1 = [1,2,3,4,5]
test_list2 = ['a','b','c','d']
# test_insert = test_list1.insert(3, 'insert')
# test_append = test_list1.append('append')


def test_insert(ss): 
	ss.insert(3, 'insert')
	return ss

def test_append(ss): 
	ss.append(3, 'insert')
	return ss

def test_pop(ss): 
	ss.pop(2)
	return ss

def test_join(ss):
	S1= []
	S1 = 'LL'.join(ss)
	return S1

def list_comprehension(num):
	S1 = [i for i in range(num)]
	return S1

print list_comprehension(20) 




def add(x,y): 
	return x+y
s1 = reduce(add, range(1, 11)) #1+2+3+...+10 = 55


def cube(x): 
	return x*x*x
map(cube, range(1, 11))



