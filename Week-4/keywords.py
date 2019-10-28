'''
keywords.py

Create functions that use keyword arguments
with default values.
'''

# Create a function called welcome_message():
# if no input argument is provided
# it returns the string 'Hello and welcome'
# if a keyword argument called user_name is provided
# it returns 'Hello, <user_name>, and welcome'
# if a keyword argument called place is provided
# it returns 'Hello and welcome to <place>'
# if both user_name and place are provided
# it returns 'Hello, <user_name>, and welcome to <place>
def welcome_message(user_name, place):
    if (user_name == None) and (place == None):
        print("Hello and welcome")
    else if (user_name !== None) and (place == None):
        print("Hello, " & user_name & ", and welcome")
    else if (user_name == None) and (place !== None):
        print("Hello and welcome to " & place)
    else:
        print("Hello, " & user_name & ", and welcome to " & place)
        


# Create a function called list_average()
# without using any libraries to do the maths for you 
# (the point of this exercise is to practice interacting 
# with lists)
# the first argument is a list of numbers
# the second optional keyword arguemt is called avg_type
# if nothing for avg_type provided, return the mean of the list
# if avg_type='mode', return the mode of the list 
# (return list of all modes if there is a tie between multiple values)
# if avg_type='mean', return the mean of the list
# if avg_type='median', return the median of this list
def list_average(list_of_num, avg_type):
    if (avg_type == None) or avg_type = "mean":
        count = 0
        sum = 0
        for nums in list_of_num:
            count += 1
            sum += nums
        mean = sum / count
    else if avg_type == "mode":
        count_dictionary = {}
        for nums in list_of_num:
            current_count = 0
            if nums in count_dictionary:
                current_count = count_dictionary[nums]
            count_dictionary[nums] = current_count += 1

    