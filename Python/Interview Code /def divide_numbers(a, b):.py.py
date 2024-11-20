

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Both arguments must be numbers.")
    else:
        print(f"The result is {result}")
    finally:
        print("Execution complete.")

# Example usage
divide_numbers(10, 2)   # Normal operation
divide_numbers(10, 0)   # Division by zero
divide_numbers(10, "a") # Invalid type
