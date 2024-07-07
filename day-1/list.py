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

#reverse
stream = ['computer_science', 'civil', 'electronics', 'electrical', 'mechanical'] #here this is my list
stream.reverse()  #here i used reverse function to reverse the list.
print(stream)

#sorting with ascending order and desceding order
num = [1, 7, 9, 2, 4, 3]  #here this is my list of num
num.sort  #here i'm using sort function
print(num)

num = [1, 7, 9, 2, 4, 3] #here this my list num
num.sort(reverse=True) #here i'm calling list in reverse order
print(num)

stream = ['computer_science', 'civil', 'electronics', 'electrical', 'mechanical'] #here this is my list.
sorted = sorted(stream) #here we are sorting the elements without modifying the original elements.
print(stream)

#getting min and max number using python.
num =  [1, 7, 9, 2, 4, 3] #here is my list.
print(min(num)) #here i'm getting minmum number from the list.
print(max(num)) #here i'm getting maximum number from the list.
print(sum(num)) #here i'm getting sum of the given list.

#indexing the list.
stream = ['computer_science', 'civil', 'electronics', 'electrical', 'mechanical'] #here is my list.
print(stream.index('civil')) #here we are calling the index from given list.

stream = ['computer_science', 'civil', 'electronics', 'electrical', 'mechanical'] #here is my list.
print('bio_tech' in stream) #here i'm checking the wheather bio_tech is present or not from given list.


