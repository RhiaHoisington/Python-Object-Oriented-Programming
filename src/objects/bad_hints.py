"""
Python 3 Object-Oriented Programming 4th ed.
Chapter 2, Objects in Python.
NOTE. Remove the ``# type: ignore`` comments to reproduce examples in the text.
"""
#from __future__ import annotations
# annotations is required for Python 3.7 and earlier for generic types

def odd(n: int) -> bool:
    return n % 2 != 0


def main():  # type: ignore
    print(odd("Hello, world!"))  # type: ignore


if __name__ == "__main__":
    main()  # type: ignore