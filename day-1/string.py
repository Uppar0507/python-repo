#sample print function for python without passing varibales.
print('Hello we love python')

#passing variable using variable name "message" and values is "hello we love python".
message= 'Hello we love python'
print(message)

#how to calculate the length of the character in python.
message='hello we love python'
print(len(message))   #here i'm calling length function.

#how to access the elements in from given string characters in python it calculate space also.
message='hello we love python'
print(message[0]) #"0" is the index of H.

message='hello we love python'
print(message[3])  #"3" is the index of l.

#how get range of character using python.
message='hello we love python'
print=(message[0:5]) #here i'm calling range of character.

message='hello we love python'
print=(message[6:]) #here it is start from 6th index of my values.

#how to get lower_case and upper_case using python
message='hello we love python'
print=(message.lower())  #here we get lower_case for "hello we love python"

message='hello we love python'
print=(message.upper())  #here we get upper_case for the "hello we love python"

#count methon in  python
message='hello we love python'
print= (message.count('python')) #here is couting that how many time the word "python" is repated it's only 1 times.

message='hello we love python'
print=(message.count('e'))  #here it is counting that how may time the word "e" is reapted its only 3t times.

message='hello we love python'
print=(message.find('l'))  #here is used find function for same count function.

#replacing the string in python
message='hello we love python'
my_message=message.replace('python', 'python3')  #here function i used called replace, it is replacing the python to python3 
print=(my_message)


#add to two string using python called "concatenate"
message_1='welcome to'
message_2='hello we love python'
my_message=message_1 + '' + message_2 #here is used + operator to add the variables. those single '' I used for having proper space btween the varibles
print=(my_message)

message_1='welcome to'
message_2='hello we love python'
my_message=message_1 + '' + message_2 + '. have fun while learning python' #here i added extra word callded " have fun while learning python!" it is going to add existing string
print=(my_message)

message_1='welcome to'
message_2='hello we love python'
my_message='{}, {}. have fun while learning python'.format(message_1, message_2)  #used format function here. Else can you use f string
my_message=f'{message_1}, {message_2}. have fun while learning python'  #here is used f string
print=(my_message)

message_1='welcome to'
message_2='hello we love python'
my_message=f'{message_1.upper()}, {message_2}. have fun while learning python'  #here i'm making upper_case for message_1
print=(my_message)