"""
Class Variables
===============
Learn the difference between class variables and instance variables.

Topics covered:
    - Class variables: shared across all instances
    - Instance variables: unique to each object
    - Namespace lookups: instance → class → parent class
    - Using `__dict__` to inspect namespaces
    - Class variable for counting instances
"""


class Employee:
    """Employee class demonstrating class variables."""

    # --- Class variables ---
    # Shared by ALL instances. Accessed via self.<name> or Employee.<name>
    raise_amount = 1.04  # 4% annual raise
    num_of_emps = 0      # Track total employees created

    def __init__(self, first: str, last: str, pay: int) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

        # Increment the class variable — use the CLASS name here,
        # not self, because we always want to modify the shared counter
        Employee.num_of_emps += 1

    def fullname(self) -> str:
        """Return the employee's full name."""
        return f"{self.first} {self.last}"

    def apply_raise(self) -> None:
        """
        Apply the raise_amount to this employee's pay.

        Uses self.raise_amount (not Employee.raise_amount) so that
        individual instances can override their own raise percentage.
        """
        self.pay = int(self.pay * self.raise_amount)


def demo() -> None:
    """Demonstrate class variables vs instance variables."""

    emp_1 = Employee("Aquib", "Ahmad", 50000)
    emp_2 = Employee("Test", "User", 60000)

    # --- Class variable is shared ---
    print(f"Employee.raise_amount : {Employee.raise_amount}")
    print(f"emp_1.raise_amount    : {emp_1.raise_amount}")
    print(f"emp_2.raise_amount    : {emp_2.raise_amount}")

    # --- Overriding on an instance creates an INSTANCE variable ---
    emp_1.raise_amount = 1.05  # Only emp_1 gets 5%; class stays at 4%
    print(f"\nAfter setting emp_1.raise_amount = 1.05:")
    print(f"Employee.raise_amount : {Employee.raise_amount}")
    print(f"emp_1.raise_amount    : {emp_1.raise_amount}  (overridden)")
    print(f"emp_2.raise_amount    : {emp_2.raise_amount}  (still from class)")

    # --- __dict__ shows namespace contents ---
    print(f"\nemp_1.__dict__ : {emp_1.__dict__}")
    print(f"emp_2.__dict__ : {emp_2.__dict__}")

    # --- apply_raise uses the instance's raise_amount ---
    print(f"\nemp_1 pay before raise: {emp_1.pay}")
    emp_1.apply_raise()
    print(f"emp_1 pay after raise : {emp_1.pay}  (5% raise)")

    print(f"\nemp_2 pay before raise: {emp_2.pay}")
    emp_2.apply_raise()
    print(f"emp_2 pay after raise : {emp_2.pay}  (4% raise)")

    # --- Tracking instances ---
    print(f"\nTotal employees created: {Employee.num_of_emps}")


if __name__ == "__main__":
    demo()
