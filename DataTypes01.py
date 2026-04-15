# 1. Add two lists index-wise
def add_lists_index_wise(list1, list2):
    result = [[list1[i], list2[i]] if i < len(list1) and i < len(list2)
              else (list1[i] if i < len(list1) else list2[i])
              for i in range(max(len(list1), len(list2)))]
    return result


list1 = ["M", "na", "i", "Ra"]
list2 = ["y", "me", "s", "hul"]
print("1.", add_lists_index_wise(list1, list2))


# 2. Add item 7000 after 6000
def add_after_6000(lst):
    for sublist in lst:
        if isinstance(sublist, list):
            for sub_sublist in sublist:
                if isinstance(sub_sublist, list) and 6000 in sub_sublist:
                    idx = sub_sublist.index(6000)
                    sub_sublist.insert(idx + 1, 7000)
    return lst


list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
print("2.", add_after_6000(list1))


# 3. Display candy and their counts
def display_candy_counts(candy_list, no_of_items):
    for candy, count in zip(candy_list, no_of_items):
        print(f"{candy}-{count}")


candy_list = ['Jelly Belly', 'Kit Kat', 'Double Bubble', 'Milky Way', 'Three Musketeers']
no_of_items = [10, 20, 34, 74, 32]
print("3.")
display_candy_counts(candy_list, no_of_items)


# 4. Running sum on list
def running_sum(lst):
    result = []
    total = 0
    for num in lst:
        total += num
        result.append(total)
    return result


list1 = [1, 2, 3, 4, 5, 6]
print("4.", running_sum(list1))


# 5. Sum of all elements greater than or equal to current element
def sum_greater_equal(lst):
    result = []
    n = len(lst)
    for i in range(n):
        total = sum(x for x in lst if x >= lst[i])
        result.append(total)
    return result


print("5.", sum_greater_equal([2, 4, 6, 10, 1]))


# 6. Common unique items from two lists in increasing order
def common_unique_items(list1, list2):
    return sorted(set(list1) & set(list2))


num1 = [23, 45, 67, 78, 89, 34]
num2 = [34, 89, 55, 56, 39, 67]
print("6.", common_unique_items(num1, num2))


# 7. Sort alphanumeric strings based on product of numeric characters
def product_of_numerics(s):
    product = 1
    has_digit = False
    for char in s:
        if char.isdigit():
            product *= int(char)
            has_digit = True
    return product if has_digit else 1


def sort_by_numeric_product(lst):
    return sorted(lst, key=product_of_numerics)


print("7.", sort_by_numeric_product(['1ac21', '23fg', '456', '098d', '1', 'kls']))


# 8. Max number of each row in matrix
def max_of_rows(matrix):
    return [max(row) for row in matrix]


print("8.", max_of_rows([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


# 9. Shortlist Students for a Job role
def shortlist_students():
    n = int(input("Enter No of records: "))
    students = []

    for i in range(n):
        print(f"Enter Details of student-{i + 1}")
        name = input("Enter Student name: ")
        education = input("Enter Higher Education: ")
        skill = input("Enter Primary Skill: ")
        graduation_year = input("Enter Year of Graduation: ")
        students.append((name, education, skill, graduation_year))

    print("\nEnter Job Role Requirement")
    req_skill = input("Enter Skill: ")
    req_education = input("Enter Higher Education: ")
    req_year = input("Enter Year of Graduation: ")

    matches = [student for student in students
               if student[1] == req_education and
               student[2] == req_skill and
               student[3] == req_year]

    if matches:
        for match in matches:
            print(match)
    else:
        print("No such candidate")


# Uncomment to test:
# shortlist_students()

# 10. Common elements in three lists using sets
def common_in_three(list1, list2, list3):
    return list(set(list1) & set(list2) & set(list3))


ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
print("10.", common_in_three(ar1, ar2, ar3))


# 11. Count unique vowels in string (case-sensitive)
def count_unique_vowels(s):
    vowels = set('aeiouAEIOU')
    found_vowels = set(char for char in s if char in vowels)
    return len(found_vowels)


Str1 = "hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX"
print("11.", count_unique_vowels(Str1))


# 12. Intersection of two lists using list comprehension
def intersection_list_comprehension(lst1, lst2):
    return [x for x in lst1 if x in lst2]


lst1 = {15, 9, 10, 56, 23, 78, 5, 4, 9}
lst2 = {9, 4, 5, 36, 47, 26, 10, 45, 87}
print("12.", intersection_list_comprehension(lst1, lst2))


# 13. Convert list of tuples to dictionary
def tuples_to_dict(tuple_list):
    return {t[0]: [t[1]] for t in tuple_list}


print("13.", tuples_to_dict([("akash", 10), ("gaurav", 12), ("anand", 14),
                             ("suraj", 20), ("akhil", 25), ("ashish", 30)]))


# 14. Get unique elements from list
def unique_elements(lst):
    return list(set(lst))


print("14.", unique_elements([1, 2, 3, 3, 3, 3, 4, 5]))


# 15. Print even numbers from list
def even_numbers(lst):
    return [x for x in lst if x % 2 == 0]


print("15.", even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))


# 16. Check if number is perfect
def is_perfect(n):
    if n <= 1:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n


print("16. 6 is perfect:", is_perfect(6))
print("16. 28 is perfect:", is_perfect(28))
print("16. 10 is perfect:", is_perfect(10))


# 17. Concatenate any number of dictionaries
def concatenate_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result


dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
print("17.", concatenate_dicts(dic1, dic2, dic3))


# 18. Histogram of bin size 10
def histogram_bin10(lst):
    bins = {}
    for num in lst:
        lower_bound = ((num - 1) // 10) * 10 + 1
        upper_bound = lower_bound + 9
        bin_key = f"{lower_bound}-{upper_bound}"
        bins[bin_key] = bins.get(bin_key, 0) + 1
    return bins


print("18.", histogram_bin10([13, 42, 15, 37, 22, 39, 41, 50]))