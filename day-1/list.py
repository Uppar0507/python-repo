#list in python
stream = ['computer_science', 'civil', 'electronics', 'electrical', 'mechanical']  ## this is my list
print(stream) #here i'm calling my list

stream = ['computer_science', 'civil', 'electronics', 'electrical', 'mechanical']
print(len(stream)) #here i'm using length function for my list.

strame = ['computer_science', 'civil', 'electronics', 'electrical', 'mechanical'] ##inexing the list
print(stream[3]) #here i'm indexing the 3rd element of my list that is "electrical"

stream = ['computer_science', 'civil', 'electronics', 'electrical', 'mechanical']
print(stream[-1]) #here i'm indexing the negative element of my list is 'mechanical'

stream = ['computer_science', 'civil', 'electronics', 'electrical', 'mechanical']
print(stream[0:2])  #access the range of value. Here i will get "computer_science & civil" it will index 0 & 1 and stops at 2
print(stream[:3])   #access the range of value. Here i will get "same values with one extra electronics"
print(stream[2:])   #access the last two elements of my list 


#appending in python
stream = ['computer_science', 'civil', 'electronics', 'electrical', 'mechanical']
stream.append('data_scinece')  #appending the element to the list 
print(stream)

stream = ['computer_science', 'civil', 'electronics', 'electrical', 'mechanical', 'data_science']
stream.insert(2, 'data_science') #here i'm using insert method for add element to specific location of my list.
print(stream)

stream = ['computer_science', 'civil', 'electronics', 'electrical', 'mechanical'] #here this is my list.
stream_1 = ['bio_tech', 'vsli'] #here this is my extended list using function called "extended"
stream.extend(stream_1)
print(stream)

stream = ['computer_science', 'civil', 'electronics', 'electrical', 'mechanical'] #here this is my list
stream.remove('electrical') #here i used remove function to remove the element called "electrical"
stream.pop('civil')   #here i used pop function to remove the element called "civil" both remove and pop do the same work.
print(stream)




