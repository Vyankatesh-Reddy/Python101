import random
import datetime
from datetime import date
from abc import ABC, abstractmethod
from typing import Optional, Union


# 1. Circle class
class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * 3.14159 * self.radius


print("1. Circle:")
circle = Circle(5)
print(f"Area: {circle.area():.2f}, Perimeter: {circle.perimeter():.2f}")


# 2. Person class
class Person:
    def __init__(self, name: str, country: str, dob: str):
        self.name = name
        self.country = country
        self.dob = dob  # Format: YYYY-MM-DD

    def calculate_age(self) -> int:
        today = date.today()
        birth_date = datetime.datetime.strptime(self.dob, "%Y-%m-%d").date()
        age = today.year - birth_date.year
        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
            age -= 1
        return age


print("\n2. Person:")
person = Person("John Doe", "USA", "1990-05-15")
print(f"Age: {person.calculate_age()} years")


# 3. Calculator class with static methods
class Calculator:
    @staticmethod
    def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a + b

    @staticmethod
    def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a - b

    @staticmethod
    def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a * b

    @staticmethod
    def divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float, str]:
        if b != 0:
            return a / b
        return "Cannot divide by zero"


print("\n3. Calculator:")
print(f"10 + 5 = {Calculator.add(10, 5)}")
print(f"10 - 5 = {Calculator.subtract(10, 5)}")


# 4. Shape hierarchy
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass


class CircleShape(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * 3.14159 * self.radius


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        self.a, self.b, self.c = a, b, c

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def perimeter(self) -> float:
        return self.a + self.b + self.c


class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side ** 2

    def perimeter(self) -> float:
        return 4 * self.side


print("\n4. Shapes:")
circle_shape = CircleShape(5)
print(f"Circle area: {circle_shape.area():.2f}")
square = Square(4)
print(f"Square area: {square.area()}")


# 5. Binary Search Tree
class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class BinarySearchTree:
    def __init__(self):
        self.root: Optional[TreeNode] = None

    def insert(self, value: int) -> None:
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node: TreeNode, value: int) -> None:
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value: int) -> bool:
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node: Optional[TreeNode], value: int) -> bool:
        if node is None or node.value == value:
            return node is not None
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)


print("\n5. Binary Search Tree:")
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
print(f"Search 30: {bst.search(30)}")
print(f"Search 100: {bst.search(100)}")


# 6. Stack
class Stack:
    def __init__(self):
        self._stack = []

    def push(self, item: any) -> None:
        self._stack.append(item)

    def pop(self) -> any:
        if not self.is_empty():
            return self._stack.pop()
        return "Stack is empty"

    def is_empty(self) -> bool:
        return len(self._stack) == 0

    def peek(self) -> any:
        if not self.is_empty():
            return self._stack[-1]
        return "Stack is empty"


print("\n6. Stack:")
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(f"Popped: {stack.pop()}")
print(f"Peek: {stack.peek()}")


# 7. Linked List
class ListNode:
    def __init__(self, data: any):
        self.data = data
        self.next: Optional[ListNode] = None


class LinkedList:
    def __init__(self):
        self.head: Optional[ListNode] = None

    def display(self) -> None:
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert(self, data: any) -> None:
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key: any) -> None:
        current = self.head
        if current and current.data == key:
            self.head = current.next
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            return
        if prev:
            prev.next = current.next


print("\n7. Linked List:")
ll = LinkedList()
ll.insert(3)
ll.insert(2)
ll.insert(1)
ll.display()
ll.delete(2)
ll.display()


# 8. Shopping Cart
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name: str, price: float, quantity: int = 1) -> None:
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'price': price, 'quantity': quantity}

    def remove_item(self, item_name: str) -> None:
        if item_name in self.items:
            del self.items[item_name]

    def total_price(self) -> float:
        return sum(item['price'] * item['quantity'] for item in self.items.values())


print("\n8. Shopping Cart:")
cart = ShoppingCart()
cart.add_item("Apple", 0.5, 5)
cart.add_item("Banana", 0.3, 3)
print(f"Total: ${cart.total_price()}")


# 9. Stack with display
class StackWithDisplay:
    def __init__(self):
        self._stack = []

    def push(self, item: any) -> None:
        self._stack.append(item)

    def pop(self) -> any:
        if self._stack:
            return self._stack.pop()
        return "Empty"

    def display(self) -> None:
        print(self._stack)


print("\n9. Stack with Display:")
stack_disp = StackWithDisplay()
stack_disp.push(10)
stack_disp.push(20)
stack_disp.display()


# 10. Queue
class Queue:
    def __init__(self):
        self._queue = []

    def enqueue(self, item: any) -> None:
        self._queue.append(item)

    def dequeue(self) -> any:
        if self._queue:
            return self._queue.pop(0)
        return "Empty"


print("\n10. Queue:")
q = Queue()
q.enqueue(1)
q.enqueue(2)
print(f"Dequeued: {q.dequeue()}")


# 11. Bank Account
class BankAccount:
    def __init__(self, account_number: int, name: str, balance: float):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount: float) -> None:
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdrawal(self, amount: float) -> None:
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds")

    def bank_fees(self) -> None:
        fee = self.balance * 0.05
        self.balance -= fee
        print(f"Bank fee of ${fee} applied")

    def display(self) -> None:
        print(f"Account: {self.account_number}, Name: {self.name}, Balance: ${self.balance}")


print("\n11. Bank Account:")
account = BankAccount(12345, "John Smith", 1000)
account.display()
account.deposit(500)
account.withdrawal(200)
account.bank_fees()
account.display()


# 12. Flashcard Game
class FlashCard:
    def __init__(self):
        self.fruits = {"Banana": "yellow", "Strawberries": "pink", "Apple": "red",
                       "Watermelon": "green", "Orange": "orange"}

    def play(self) -> None:
        print("Welcome to fruit quiz!")
        while True:
            fruit, color = random.choice(list(self.fruits.items()))
            answer = input(f"What is the color of {fruit}\n").lower()
            if answer == color:
                print("Correct answer")
            else:
                print(f"Wrong answer! The correct color is {color}")

            play_again = input("Enter 0 if you want to play again: ")
            if play_again != '0':
                break


print("\n12. Flashcard Game (commented to avoid input loop):")


# flash = FlashCard()
# flash.play()

# 13. Instructor Allocation
class Instructor:
    def __init__(self, name: str, technology_skills: list, experience: float, avg_feedback: float):
        self.__name = name
        self.__technology_skills = technology_skills
        self.__experience = experience
        self.__avg_feedback = avg_feedback

    def get_name(self) -> str:
        return self.__name

    def get_technology_skills(self) -> list:
        return self.__technology_skills

    def check_eligibility(self) -> bool:
        if self.__experience > 3:
            return self.__avg_feedback >= 4.5
        else:
            return self.__avg_feedback >= 4

    def allocate_course(self, technology: str) -> bool:
        return technology in self.__technology_skills and self.check_eligibility()


print("\n13. Instructor:")
instructor = Instructor("John", ["Python", "Java"], 5, 4.7)
print(f"Eligible: {instructor.check_eligibility()}")
print(f"Can teach Python: {instructor.allocate_course('Python')}")


# 14. Product Expiry
class Product:
    def __init__(self, mfg_date: str, exp_date: str):
        self.mfg_date = datetime.datetime.strptime(mfg_date, "%Y-%m-%d")
        self.exp_date = datetime.datetime.strptime(exp_date, "%Y-%m-%d")

    def time_left(self) -> str:
        today = datetime.datetime.now()
        if today > self.exp_date:
            return "Expired"
        remaining = self.exp_date - today
        years = remaining.days // 365
        months = (remaining.days % 365) // 30
        days = (remaining.days % 365) % 30
        return f"{years} years, {months} months, {days} days left for expiry"


print("\n14. Product Expiry:")
product = Product("2023-01-01", "2025-12-31")
print(product.time_left())


# 15. University Admission
class Student:
    def __init__(self, student_id: str, age: int, marks: float):
        self.student_id = student_id
        self.age = age
        self.marks = marks

    def is_valid(self) -> bool:
        return self.age > 20 and 0 <= self.marks <= 100

    def qualifies(self) -> bool:
        return self.is_valid() and self.marks >= 65


print("\n15. University Admission:")
student = Student("S001", 22, 75)
print(f"Valid: {student.is_valid()}, Qualifies: {student.qualifies()}")


# 16. Ice-Cream Shop
class Scoop:
    quantity_sold = 0

    def __init__(self, flavor: str, price: float):
        self.flavor = flavor
        self.__price = price

    def get_price(self) -> float:
        return self.__price

    def set_price(self, price: float) -> None:
        self.__price = price

    @staticmethod
    def sold() -> None:
        Scoop.quantity_sold += 1


class Bowl:
    def __init__(self):
        self.__scoop_list = []

    def add_scoops(self, *scoops: Scoop) -> None:
        for scoop in scoops:
            self.__scoop_list.append(scoop)

    def display(self) -> None:
        total = 0
        for scoop in self.__scoop_list:
            print(f"Flavor: {scoop.flavor}, Price: ${scoop.get_price()}")
            total += scoop.get_price()
        print(f"Total price: ${total}")

    def sold(self) -> None:
        for _ in self.__scoop_list:
            Scoop.sold()


print("\n16. Ice-Cream Shop:")
s1 = Scoop("Vanilla", 2.5)
s2 = Scoop("Chocolate", 3.0)
bowl = Bowl()
bowl.add_scoops(s1, s2)
bowl.display()


# 17. Bus Fare
class Vehicle:
    def __init__(self, seating_capacity: int):
        self.seating_capacity = seating_capacity

    def fare(self) -> float:
        return self.seating_capacity * 100


class Bus(Vehicle):
    def fare(self) -> float:
        total_fare = super().fare()
        return total_fare + (total_fare * 0.10)


print("\n17. Bus Fare:")
bus = Bus(50)
print(f"Bus fare: ${bus.fare()}")


# 18. Employee Management
class Employee:
    def __init__(self, emp_name: str, emp_id: str, emp_salary: float, emp_department: str):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def calculate_emp_salary(self, hours_worked: int) -> float:
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = overtime * (self.emp_salary / 50)
            self.emp_salary += overtime_amount
        return self.emp_salary

    def emp_assign_department(self, new_department: str) -> None:
        self.emp_department = new_department

    def print_employee_details(self) -> None:
        print(f"Name: {self.emp_name}, ID: {self.emp_id}, Salary: ${self.emp_salary}, Dept: {self.emp_department}")


print("\n18. Employee:")
emp = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
emp.calculate_emp_salary(55)
emp.print_employee_details()


# 19. Restaurant
class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.book_table = set()
        self.customer_orders = {}

    def add_item_to_menu(self, item: str, price: float) -> None:
        self.menu_items[item] = price

    def book_tables(self, table_number: int) -> None:
        self.book_table.add(table_number)

    def customer_order(self, table_number: int, order: list) -> None:
        if table_number in self.book_table:
            self.customer_orders[table_number] = order
        else:
            print("Table not booked")

    def print_menu(self) -> None:
        print("Menu:", self.menu_items)

    def print_table_reservations(self) -> None:
        print("Reserved tables:", self.book_table)

    def print_customer_orders(self) -> None:
        print("Customer orders:", self.customer_orders)


print("\n19. Restaurant:")
restaurant = Restaurant()
restaurant.add_item_to_menu("Pizza", 10)
restaurant.book_tables(5)
restaurant.print_menu()


# 20. Bank Account (simpler version)
class BankAccountSimple:
    def __init__(self, account_number: str, customer_name: str, balance: float, date_of_opening: str):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance
        self.date_of_opening = date_of_opening

    def deposit(self, amount: float) -> float:
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> Union[float, str]:
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        return "Insufficient balance"

    def check_balance(self) -> float:
        return self.balance


print("\n20. Bank Account Simple:")
bank_acc = BankAccountSimple("ACC001", "John", 1000, "2024-01-01")
print(f"Balance: ${bank_acc.check_balance()}")
bank_acc.deposit(500)
print(f"After deposit: ${bank_acc.check_balance()}")


# 21. Inventory Management
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id: str, item_name: str, stock_count: int, price: float) -> None:
        self.items[item_id] = {
            'name': item_name,
            'stock': stock_count,
            'price': price
        }

    def update_item(self, item_id: str, stock_count: Optional[int] = None, price: Optional[float] = None) -> None:
        if item_id in self.items:
            if stock_count:
                self.items[item_id]['stock'] = stock_count
            if price:
                self.items[item_id]['price'] = price

    def check_item_details(self, item_id: str) -> Union[dict, str]:
        if item_id in self.items:
            return self.items[item_id]
        return "Item not found"


print("\n21. Inventory:")
inventory = Inventory()
inventory.add_item("I001", "Laptop", 10, 1000)
inventory.update_item("I001", stock_count=8)
print(inventory.check_item_details("I001"))