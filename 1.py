1a)
def find_numbers_with_square_divisible_by_8(numbers_list):
    for number in numbers_list:
        if (number ** 2) % 8 == 0:
            print(number)

input_string = input("Enter a list of numbers separated by commas: ")
numbers_list = [int(num.strip()) for num in input_string.split(",")]


print("Numbers whose square 222222222222is divisible by 8:")
find_numbers_with_square_divisible_by_8(numbers_list)
....................................................................................................................
1b)
def illustrate_errors():

    try:
       
        my_list = [1, 2, 3]
        print(my_list[5])
    except IndexError as e:
        print(f"IndexError: {e}")

    try:
       
        number = int("not_a_number")
    except ValueError as e:
        print(f"ValueError: {e}")

    try:
        result = "string" + 10
    except TypeError as e:
        print(f"TypeError: {e}")

illustrate_errors()
................................................................................
1b)
amount=10000
if(amount>2999):
     print("hello")
if(amount>2999)
# num_list=[2,3,4,5,6,7]
# num_list[7]

# int ('67.8')

# a=2
# b="datacamp"
# print(a+b)

# a='s'
# b='d'
# print(a+b)