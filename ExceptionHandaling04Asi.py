"""
Exception Handling Programs in Python
All programs include proper error handling and user feedback
"""


# 1. Handle ZeroDivisionError exception
def handle_zero_division():
    print("\n1. ZeroDivisionError Handler")
    try:
        numerator = float(input("Enter numerator: "))
        denominator = float(input("Enter denominator: "))
        result = numerator / denominator
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero! Please enter a non-zero denominator.")
    except ValueError:
        print("Error: Please enter valid numbers.")
    except Exception as e:
        print(f"Unexpected error: {e}")


# 2. Raise ValueError for non-integer input
def validate_integer_input():
    print("\n2. ValueError Handler")
    try:
        user_input = input("Please enter an integer: ")
        number = int(user_input)
        print(f"Valid integer entered: {number}")
    except ValueError:
        print("Error: Invalid input! Please enter a valid integer.")
    except Exception as e:
        print(f"Unexpected error: {e}")


# 3. Handle FileNotFoundError
def handle_file_not_found():
    print("\n3. FileNotFoundError Handler")
    filename = input("Enter filename to open: ")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"File content:\n{content}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist. Please check the filename and try again.")
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'.")
    except Exception as e:
        print(f"Unexpected error: {e}")


# 4. Raise TypeError for non-numerical inputs
def validate_numerical_inputs():
    print("\n4. TypeError Handler")
    try:
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")

        # Check if inputs are numerical
        if not (num1.replace('.', '').replace('-', '').isdigit() and
                num2.replace('.', '').replace('-', '').isdigit()):
            raise TypeError("Both inputs must be numbers")

        num1 = float(num1)
        num2 = float(num2)
        result = num1 + num2
        print(f"Sum: {result}")
    except TypeError as e:
        print(f"TypeError: {e}")
    except ValueError:
        print("Error: Invalid number format.")
    except Exception as e:
        print(f"Unexpected error: {e}")


# 5. Handle PermissionError
def handle_permission_error():
    print("\n5. PermissionError Handler")
    filename = input("Enter filename to write to: ")
    try:
        with open(filename, 'w') as file:
            file.write("This is a test content.")
        print(f"Successfully wrote to '{filename}'")
    except PermissionError:
        print(f"Error: Permission denied! You don't have write access to '{filename}'.")
    except IOError as e:
        print(f"IO Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


# 6. Handle IndexError for list operations
def handle_index_error():
    print("\n6. IndexError Handler")
    sample_list = [10, 20, 30, 40, 50]
    print(f"Sample list: {sample_list}")

    try:
        index = int(input(f"Enter index (0 to {len(sample_list) - 1}): "))
        value = sample_list[index]
        print(f"Value at index {index}: {value}")
    except IndexError:
        print(f"Error: Index out of range! Please enter an index between 0 and {len(sample_list) - 1}.")
    except ValueError:
        print("Error: Please enter a valid integer index.")
    except Exception as e:
        print(f"Unexpected error: {e}")


# 7. Handle ArithmeticError for division
def handle_arithmetic_error():
    print("\n7. ArithmeticError Handler")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # This can cause various arithmetic errors
        result = num1 / num2
        print(f"Division result: {result}")

        # Additional arithmetic operation that might cause overflow
        power_result = num1 ** 1000000  # This might cause overflow
        print(f"Power result: {power_result}")

    except ArithmeticError as e:
        print(f"ArithmeticError: {e}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except OverflowError:
        print("Error: Arithmetic operation resulted in overflow!")
    except ValueError:
        print("Error: Please enter valid numbers.")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Advanced example: Combining multiple exception handlers
def demonstrate_exception_hierarchy():
    print("\n--- Advanced: Exception Hierarchy Demonstration ---")

    def safe_division(a, b):
        """Demonstrates proper exception handling hierarchy"""
        try:
            result = a / b
            return result
        except ZeroDivisionError:
            print("Specific: Cannot divide by zero")
            return None
        except ArithmeticError:
            print("General: Arithmetic error occurred")
            return None
        except Exception:
            print("Catch-all: Unexpected error")
            return None

    print(f"10 / 2 = {safe_division(10, 2)}")
    print(f"10 / 0 = {safe_division(10, 0)}")


# Main menu to test all programs
def main_menu():
    """Interactive menu to test all exception handling programs"""
    while True:
        print("\n" + "=" * 50)
        print("EXCEPTION HANDLING DEMONSTRATION")
        print("=" * 50)
        print("1. ZeroDivisionError - Division by zero")
        print("2. ValueError - Invalid integer input")
        print("3. FileNotFoundError - Missing file")
        print("4. TypeError - Non-numerical inputs")
        print("5. PermissionError - File permission issues")
        print("6. IndexError - List index out of range")
        print("7. ArithmeticError - Arithmetic operations")
        print("8. Run all demonstrations sequentially")
        print("9. Advanced exception hierarchy")
        print("0. Exit")

        choice = input("\nEnter your choice (0-9): ")

        if choice == '1':
            handle_zero_division()
        elif choice == '2':
            validate_integer_input()
        elif choice == '3':
            handle_file_not_found()
        elif choice == '4':
            validate_numerical_inputs()
        elif choice == '5':
            handle_permission_error()
        elif choice == '6':
            handle_index_error()
        elif choice == '7':
            handle_arithmetic_error()
        elif choice == '8':
            print("\n" + "=" * 50)
            print("RUNNING ALL DEMONSTRATIONS")
            print("=" * 50)
            handle_zero_division()
            validate_integer_input()
            handle_file_not_found()
            validate_numerical_inputs()
            handle_permission_error()
            handle_index_error()
            handle_arithmetic_error()
        elif choice == '9':
            demonstrate_exception_hierarchy()
        elif choice == '0':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 9.")


# Example of custom exception class
class CustomArithmeticError(Exception):
    """Custom exception for specific arithmetic conditions"""
    pass


def demonstrate_custom_exception():
    print("\n--- Custom Exception Demonstration ---")
    try:
        number = float(input("Enter a positive number: "))
        if number < 0:
            raise CustomArithmeticError("Negative numbers are not allowed in this operation")
        result = number ** 0.5  # Square root
        print(f"Square root: {result}")
    except CustomArithmeticError as e:
        print(f"Custom Error: {e}")
    except ValueError:
        print("Error: Please enter a valid number")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Standalone function to test all programs without menu
def run_all_tests():
    """Run all exception handling tests with sample inputs"""
    print("\n" + "=" * 60)
    print("RUNNING ALL EXCEPTION HANDLING TESTS (WITH DEMO INPUTS)")
    print("=" * 60)

    # Test 1: ZeroDivisionError
    print("\n[Test 1] ZeroDivisionError with demo input 10/0")
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("✓ Caught ZeroDivisionError: Cannot divide by zero")

    # Test 2: ValueError
    print("\n[Test 2] ValueError with invalid integer 'abc'")
    try:
        number = int("abc")
    except ValueError:
        print("✓ Caught ValueError: Invalid integer conversion")

    # Test 3: FileNotFoundError
    print("\n[Test 3] FileNotFoundError with non-existent file")
    try:
        with open("non_existent_file_12345.txt", 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print("✓ Caught FileNotFoundError: File does not exist")

    # Test 4: TypeError
    print("\n[Test 4] TypeError with non-numerical addition")
    try:
        result = "string" + 5
    except TypeError:
        print("✓ Caught TypeError: Cannot concatenate str and int")

    # Test 5: PermissionError (simulated)
    print("\n[Test 5] PermissionError simulation")
    try:
        # This might not trigger on all systems, so we'll simulate
        raise PermissionError("Permission denied")
    except PermissionError as e:
        print(f"✓ Caught PermissionError: {e}")

    # Test 6: IndexError
    print("\n[Test 6] IndexError with list index out of range")
    test_list = [1, 2, 3]
    try:
        value = test_list[10]
    except IndexError:
        print("✓ Caught IndexError: List index out of range")

    # Test 7: ArithmeticError
    print("\n[Test 7] ArithmeticError with division by zero")
    try:
        result = 10 / 0
    except ArithmeticError:
        print("✓ Caught ArithmeticError")
    except ZeroDivisionError:
        print("✓ Caught ZeroDivisionError (subclass of ArithmeticError)")


# Alternative: Simple standalone versions of each program
def program1():
    """Program 1: Simple ZeroDivisionError handler"""
    print("\n--- Program 1: ZeroDivisionError Handler ---")
    try:
        x = 10
        y = 0
        result = x / y
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")


def program2():
    """Program 2: Simple ValueError handler"""
    print("\n--- Program 2: ValueError Handler ---")
    try:
        user_input = input("Enter an integer: ")
        number = int(user_input)
        print(f"You entered: {number}")
    except ValueError:
        print("Error: That's not a valid integer!")


def program3():
    """Program 3: Simple FileNotFoundError handler"""
    print("\n--- Program 3: FileNotFoundError Handler ---")
    filename = "nonexistent_file.txt"
    try:
        with open(filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found!")


def program4():
    """Program 4: Simple TypeError handler"""
    print("\n--- Program 4: TypeError Handler ---")
    try:
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        result = float(num1) + float(num2)
        print(f"Sum: {result}")
    except (TypeError, ValueError):
        print("Error: Please enter numerical values!")


def program5():
    """Program 5: Simple PermissionError handler"""
    print("\n--- Program 5: PermissionError Handler ---")
    filename = "/root/test.txt"  # Typically requires root privileges
    try:
        with open(filename, 'w') as file:
            file.write("test")
    except PermissionError:
        print(f"Error: Permission denied to write to '{filename}'!")


def program6():
    """Program 6: Simple IndexError handler"""
    print("\n--- Program 6: IndexError Handler ---")
    my_list = [1, 2, 3, 4, 5]
    try:
        index = 10
        print(f"Value at index {index}: {my_list[index]}")
    except IndexError:
        print(f"Error: Index {index} is out of range for list of length {len(my_list)}!")


def program7():
    """Program 7: Simple ArithmeticError handler"""
    print("\n--- Program 7: ArithmeticError Handler ---")
    try:
        import math
        result = math.sqrt(-1)  # This causes ValueError, not ArithmeticError
        # Alternative arithmetic error:
        result = 10 / 0  # This causes ZeroDivisionError (subclass of ArithmeticError)
    except ArithmeticError:
        print("Error: Arithmetic error occurred!")
    except ZeroDivisionError:
        print("Error: Division by zero (ArithmeticError)!")


if __name__ == "__main__":
    # Option 1: Run interactive menu
    main_menu()

    # Option 2: Uncomment below to run simple standalone versions
    # program1()
    # program2()
    # program3()
    # program4()
    # program5()
    # program6()
    # program7()

    # Option 3: Uncomment below to run automated tests
    # run_all_tests()

    # Option 4: Uncomment below to test custom exception
    # demonstrate_custom_exception()