# Exercise level 1

import random
import string
# Question 1: Writ a function which generates a six digit/character random_user_id
def random_user_id():
    result = ''
    char = string.ascii_letters + string.digits
    for _ in range(6):
        result += random.choice(char)
    return result
print(f"Generate six random digit/character: {random_user_id()}")
print()
# Question 2: Modify the previous task. Declare a function named user_id_gen_by_user. 
# It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number
# of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    number_of_characters = int(input('Enter number of character: '))
    number_of_ID = int(input('Enter number of ID: '))
   
    char = string.ascii_letters + string.digits
    out_loop = ''
    for _ in range(number_of_ID):
        inner_loop = ''
        for _ in range(number_of_characters):
            inner_loop += random.choice(char)
        out_loop += inner_loop + "\n"
    return out_loop
print(user_id_gen_by_user())
print()
# Question 3: Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    rgb_color = []
    for _ in range(3):
        rgb = random.randint(0, 255)
        rgb_color.append(rgb)
    return  'rgb' + str(tuple(rgb_color))
print(rgb_color_gen())
print('')

Exercise Level 2

# Question 1: Write a function list_of_hexa_colors which returns any number 
# of hexadecimal colors in an array (six hexadecimal numbers written after #. 
# Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. 
# Check the task 6 for output examples).
def list_of_hex_colors(number_of_time):
    
    hex = string.digits + string.ascii_letters[:6]
    
    result = []
    for _ in range(number_of_time):
        store = '#'
        for _ in range(6):
            store += random.choice(hex)
        result.append(store)
    return result
print(list_of_hex_colors(5))
print()
# Question 2: Write a function list_of_rgb_colors 
# which returns any number of RGB colors in an array.
def list_of_rgb_colors(number_of_time):
    result = []
    for _ in range(number_of_time):
        result.append(rgb_color_gen())
    return result
print(list_of_rgb_colors(5))
print()
# Question 3: Write a function generate_colors which 
# can generate any number of hexa or rgb colors.
def generate_colors(color_type, number_of_color):
    if color_type == 'hexa':
        result = list_of_hex_colors(number_of_color)  
    elif color_type == 'rgb':
        result = list_of_rgb_colors(number_of_color)
    else:
        result = 'invalid input'
        
    return result

print(generate_colors('rgb', 3))
print(generate_colors('hexa', 3))
print(generate_colors('color', 3))
#print(generate_colors('color', 3))
print()


#Exercises Level 3

# Question 1: Call your function shuffle_list, it takes a list as a parameter 
# and it returns a shuffled list

def shuffle_list(list):
    return random.shuffle(list)
def shuffle_list(lst):
    random.shuffle(lst)
    return lst

print(shuffle_list([1,2,3,4,5,6,7,8]))
print(shuffle_list([1, 2, 3,4, 5,6,7,8,9]))
print()

# Question 2: Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def seven_random_number():
    count = 0
    result = []
    while count < 7:
        num = random.randrange(0, 9)
        if num in result:
            continue
        else:
            result.append(num)
            count += 1 
    return result