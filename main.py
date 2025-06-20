"""Main module that greets a user and performs a division."""

from utils import greet_user
from math_utils import divide

if __name__ == "__main__":
    name = "Gustavo Guzman"
    greet_user(name)

    result = divide(10, 6)
    print("Result:", result)
