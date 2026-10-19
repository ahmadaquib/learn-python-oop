"""
Object-Oriented Programming in Python - Complete Demo
=====================================================
Run this file to see output from all OOP modules.

Usage:
    uv run python main.py
"""

from oop import classes_and_instances
from oop import class_variables
from oop import classmethods_and_staticmethods
from oop import inheritance
from oop import special_dunder_methods
from oop import property_decorators


def separator(title: str) -> None:
    """Print a visual separator with a title."""
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print(f"{'=' * 60}\n")


def main() -> None:
    """Run all OOP module demos sequentially."""
    print("Object-Oriented Programming in Python")
    print("Complete Revision & Demo")

    separator("1. Classes and Instances")
    classes_and_instances.demo()

    separator("2. Class Variables")
    class_variables.demo()

    separator("3. Classmethods and Staticmethods")
    classmethods_and_staticmethods.demo()

    separator("4. Inheritance - Creating Subclasses")
    inheritance.demo()

    separator("5. Special (Magic/Dunder) Methods")
    special_dunder_methods.demo()

    separator("6. Property Decorators - Getters, Setters, Deleters")
    property_decorators.demo()

    print(f"\n{'=' * 60}")
    print("  All OOP topics covered!")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
