"""
Classes and Instances
=====================
Learn the basics of creating classes and instances in Python.

Topics covered:
    - Defining a class with `class` keyword
    - The `__init__` constructor method
    - Instance attributes vs class-level code
    - Instance methods and `self`
    - Creating instances (objects) from a class
    - Calling methods on instances vs on the class
"""


class Employee:
    """Represents an employee with first name, last name, and pay."""

    def __init__(self, first: str, last: str, pay: int) -> None:
        """
        Initialize an Employee instance.

        Args:
            first: Employee's first name.
            last: Employee's last name.
            pay: Employee's annual pay (integer).
        """
        # These are instance attributes — each object gets its own copy
        self.first = first
        self.last = last
        self.pay = pay
        # Derived attribute: generated from first and last
        self.email = f"{first}.{last}@company.com"

    def fullname(self) -> str:
        """Return the employee's full name."""
        return f"{self.first} {self.last}"


def demo() -> None:
    """Demonstrate classes and instances."""

    # --- Creating instances ---
    # Each call to Employee() creates a new, independent object
    emp_1 = Employee("Aquib", "Ahmad", 50000)
    emp_2 = Employee("Test", "User", 60000)

    # --- Accessing instance attributes ---
    print(f"emp_1 email : {emp_1.email}")
    print(f"emp_2 email : {emp_2.email}")

    # --- Calling instance methods ---
    # Both of these are equivalent:
    #   emp_1.fullname()     → Python passes emp_1 as 'self' automatically
    #   Employee.fullname(emp_1) → We pass the instance explicitly
    print(f"emp_1 fullname (via instance) : {emp_1.fullname()}")
    print(f"emp_1 fullname (via class)    : {Employee.fullname(emp_1)}")

    # --- Instance attributes are independent ---
    print(f"\nemp_1 pay: {emp_1.pay}")
    print(f"emp_2 pay: {emp_2.pay}")


# Allow running this file directly for quick testing
if __name__ == "__main__":
    demo()
