"""Mathematical utility functions."""

def divide(a, b):
    """Safely divide two numbers, avoiding division by zero."""
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b  
