# 1. Find maximum of three numbers
def max_of_three(a, b, c):
    return max(a, b, c)

print("1.", max_of_three(10, 25, 15))

# 2. Sum all numbers in a list
def sum_list(numbers):
    return sum(numbers)

sample_list = (8, 2, 3, 0, 7)
print("2.", sum_list(sample_list))

# 3. Multiply all numbers in a list
def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

sample_list = (8, 2, 3, -1, 7)
print("3.", multiply_list(sample_list))

# 4. Reverse a string
def reverse_string(s):
    return s[::-1]

print("4.", reverse_string("1234abcd"))

# 5. Check if number falls within a given range
def in_range(num, start, end):
    return start <= num <= end

print("5. 5 in range 1-10:", in_range(5, 1, 10))
print("5. 15 in range 1-10:", in_range(15, 1, 10))

# 6. Count upper and lower case letters
def count_case(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    return upper_count, lower_count

sample_string = 'The quick Brow Fox'
upper, lower = count_case(sample_string)
print("6.")
print(f"No. of Upper case characters : {upper}")
print(f"No. of Lower case Characters : {lower}")

# 7. Get distinct elements from list
def distinct_elements(lst):
    return list(set(lst))

sample_list = [1,2,3,3,3,3,4,5]
print("7.", distinct_elements(sample_list))

# 8. Check if string is palindrome
def is_palindrome(s):
    # Remove spaces and convert to lowercase for comparison
    cleaned = ''.join(s.lower().split())
    return cleaned == cleaned[::-1]

print("8. 'madam' is palindrome:", is_palindrome("madam"))
print("8. 'nurses run' is palindrome:", is_palindrome("nurses run"))
print("8. 'hello' is palindrome:", is_palindrome("hello"))

# 9. Sort hyphen-separated words
def sort_hyphenated_words(s):
    words = s.split('-')
    words.sort()
    return '-'.join(words)

print("9.", sort_hyphenated_words("green-red-yellow-black-white"))

# 10. Detect number of local variables in a function
def count_local_variables(func):
    return func.__code__.co_nlocals

def test_function():
    a = 1
    b = 2
    c = 3
    d = 4

print("10. Local variables in test_function:", count_local_variables(test_function))

# 11. Lambda functions
add_15 = lambda x: x + 15
multiply = lambda x, y: x * y

print("11.")
print(add_15(10))
print(multiply(6, 8))

# 12. Function that multiplies with unknown number
def multiply_with_unknown(num):
    return lambda x: x * num

double = multiply_with_unknown(2)
triple = multiply_with_unknown(3)
quadruple = multiply_with_unknown(4)
quintuple = multiply_with_unknown(5)

print("12.")
print(f"Double the number of 15 = {double(15)}")
print(f"Triple the number of 15 = {triple(15)}")
print(f"Quadruple the number of 15 = {quadruple(15)}")
print(f"Quintuple the number 15 = {quintuple(15)}")

# 13. Sort list of tuples using Lambda
def sort_tuples_by_score(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])

tuples_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("13.")
print("Original:", tuples_list)
print("Sorted:", sort_tuples_by_score(tuples_list))

# 14. Sort list of dictionaries using Lambda
def sort_dicts_by_model(dicts_list):
    return sorted(dicts_list, key=lambda x: str(x['model']))

dicts_list = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]
print("14.")
print("Original:", dicts_list)
print("Sorted:", sort_dicts_by_model(dicts_list))

# 15. Filter even and odd numbers using Lambda
def filter_even_odd(numbers):
    even = list(filter(lambda x: x % 2 == 0, numbers))
    odd = list(filter(lambda x: x % 2 != 0, numbers))
    return even, odd

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even, odd = filter_even_odd(numbers)
print("15.")
print("Even numbers:", even)
print("Odd numbers:", odd)

# 16. Square and cube every number using Lambda
def square_cube_list(numbers):
    squares = list(map(lambda x: x**2, numbers))
    cubes = list(map(lambda x: x**3, numbers))
    return squares, cubes

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares, cubes = square_cube_list(numbers)
print("16.")
print("Squares:", squares)
print("Cubes:", cubes)

# 18. Check if string starts with given character using Lambda
starts_with = lambda s, char: s.startswith(char) if s else False

print("18.")
print("'Hello' starts with 'H':", starts_with("Hello", "H"))
print("'Hello' starts with 'h':", starts_with("Hello", "h"))

# 19. Rearrange positive and negative numbers using Lambda
def rearrange_positive_negative(arr):
    positive = sorted(filter(lambda x: x >= 0, arr))
    negative = sorted(filter(lambda x: x < 0, arr))
    return positive + negative

arr = [-1, 2, -3, 5, 7, 8, 9, -10]
print("19.")
print("Original:", arr)
print("Rearranged:", rearrange_positive_negative(arr))

# 20. Count even and odd numbers using Lambda
def count_even_odd(arr):
    even_count = len(list(filter(lambda x: x % 2 == 0, arr)))
    odd_count = len(list(filter(lambda x: x % 2 != 0, arr)))
    return even_count, odd_count

arr = [1, 2, 3, 5, 7, 8, 9, 10]
even, odd = count_even_odd(arr)
print("20.")
print(f"Number of even numbers: {even}")
print(f"Number of odd numbers: {odd}")

# 21. Find numbers divisible by 19 or 13 using Lambda
def divisible_by_13_or_19(numbers):
    return list(filter(lambda x: x % 13 == 0 or x % 19 == 0, numbers))

numbers = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
print("21.")
print("Original:", numbers)
print("Divisible by 13 or 19:", divisible_by_13_or_19(numbers))

# 22. Check string requirements using lambda
def validate_string(s):
    checks = [
        lambda s: any(c.isupper() for c in s),  # has capital letter
        lambda s: any(c.islower() for c in s),  # has lower case letter
        lambda s: any(c.isdigit() for c in s),  # has number
        lambda s: len(s) >= 8                   # minimum length 8
    ]
    return all(check(s) for check in checks)

# Create a lambda version
validate_string_lambda = lambda s: (any(c.isupper() for c in s) and
                                     any(c.islower() for c in s) and
                                     any(c.isdigit() for c in s) and
                                     len(s) >= 8)

print("22.")
print("'Hello123' is valid:", validate_string_lambda("Hello123"))
print("'hello123' is valid:", validate_string_lambda("hello123"))
print("'HelloWorld' is valid:", validate_string_lambda("HelloWorld"))
print("'Hello1234' is valid:", validate_string_lambda("Hello1234"))