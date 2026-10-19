"""
Classmethods and Staticmethods
==============================
Learn the difference between regular methods, class methods, and static methods.

Topics covered:
    - Regular methods: take `self` (the instance) as first argument
    - @classmethod: take `cls` (the class) as first argument
    - @staticmethod: don't take `self` or `cls` — just a regular function
      that logically belongs to the class
    - Using @classmethod as alternative constructors
"""

import datetime


class Employee:
    """Employee class demonstrating classmethods and staticmethods."""

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first: str, last: str, pay: int) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"
        Employee.num_of_emps += 1

    def fullname(self) -> str:
        """Regular method — receives the instance as 'self'."""
        return f"{self.first} {self.last}"

    def apply_raise(self) -> None:
        """Regular method — operates on the instance."""
        self.pay = int(self.pay * self.raise_amount)

    # --- CLASS METHOD ---
    @classmethod
    def set_raise_amt(cls, amount: float) -> None:
        """
        Class method — receives the CLASS as 'cls' instead of an instance.

        This modifies the class variable for ALL instances (unless overridden).
        """
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str: str) -> "Employee":
        """
        Alternative constructor — creates an Employee from a dash-separated string.

        This is a common pattern: use @classmethod to provide multiple
        ways to create instances (like datetime.fromtimestamp, dict.fromkeys, etc.)

        Args:
            emp_str: Format "first-last-pay" (e.g. "John-Doe-70000")
        """
        first, last, pay = emp_str.split("-")
        return cls(first, last, int(pay))

    # --- STATIC METHOD ---
    @staticmethod
    def is_workday(day: datetime.date) -> bool:
        """
        Static method — doesn't access instance (self) or class (cls).

        It's just a utility function that logically belongs to Employee.
        If you don't need self or cls, it should probably be a staticmethod.

        Args:
            day: A date to check.

        Returns:
            True if the day is a weekday (Mon-Fri), False otherwise.
        """
        # Monday = 0, Sunday = 6
        return day.weekday() < 5


def demo() -> None:
    """Demonstrate classmethods and staticmethods."""

    # --- Regular constructor ---
    emp_1 = Employee("Aquib", "Ahmad", 50000)

    # --- @classmethod to modify class state ---
    print(f"Default raise_amount: {Employee.raise_amount}")
    Employee.set_raise_amt(1.06)  # Set 6% raise for everyone
    print(f"After set_raise_amt(1.06): {Employee.raise_amount}")

    # --- @classmethod as alternative constructor ---
    emp_str_1 = "John-Doe-70000"
    emp_str_2 = "Jane-Smith-80000"

    emp_2 = Employee.from_string(emp_str_1)
    emp_3 = Employee.from_string(emp_str_2)

    print(f"\nCreated from string: {emp_2.fullname()} - {emp_2.email}")
    print(f"Created from string: {emp_3.fullname()} - {emp_3.email}")

    # --- @staticmethod ---
    today = datetime.date.today()
    print(f"\nIs {today} a workday? {Employee.is_workday(today)}")

    # Check a specific Saturday
    saturday = datetime.date(2026, 10, 24)  # A Saturday
    print(f"Is {saturday} a workday? {Employee.is_workday(saturday)}")

    print(f"\nTotal employees created: {Employee.num_of_emps}")


if __name__ == "__main__":
    demo()
