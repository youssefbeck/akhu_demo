def run_calculator():
    """Runs an interactive calculator loop with exception handling and history."""
    history = [] # Initialize history list
    print("===== Safe Calculator =====")
    while True:
        a_str = input("Enter first number (or 'q' to quit): ")
        if a_str.lower() == 'q': # Check quit condition
            print("Goodbye!")
            break
        op, b_str, result = "?", "?", None # Reset iteration variables
        try:
            num1 = float(a_str) # Convert first input
            b_str = input("Enter second number: ")
            num2 = float(b_str) # Convert second input
            op = input("Enter operator (+, -, *, /, %): ")
            if op not in ('+', '-', '*', '/', '%'): # Validate operator
                raise ValueError(f"Unknown operator '{op}'")
            if op in ('/', '%') and num2 == 0.0: # Check division by zero
                raise ZeroDivisionError("Cannot divide or take modulo by zero")
            if op == '+': result = num1 + num2 
            elif op == '-': result = num1 - num2 
            elif op == '*': result = num1 * num2 
            elif op == '/': result = num1 / num2 
            elif op == '%': result = num1 % num2 
            print(f"ValueError: {e}")
            history.append((f"{a_str} {op} {b_str}", None, "ValueError")) # value error
        except ZeroDivisionError as e:
            print(f"ZeroDivisionError: {e}")
            history.append((f"{float(a_str)} {op} {float(b_str)}", None, "ZeroDivisionError")) # zero error
        else:
            print(f"Result: {num1} {op} {num2} = {result:.4f}") # Output result
            history.append((f"{num1} {op} {num2}", result, "OK")) #  success
        finally:
            print("---") 
    return history # Return full session history
if __name__ == "__main__":
    session_history = run_calculator()
    print("\nFinal History List:")
    for entry in session_history:
        print(entry)