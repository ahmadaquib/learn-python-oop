"""
Inheritance — Creating Subclasses
=================================
Learn how to create subclasses that inherit from a parent class.

Topics covered:
    - Inheriting attributes and methods from a parent class
    - Using super().__init__() to call the parent constructor
    - Adding new attributes to subclasses
    - Method overriding
    - isinstance() and issubclass() built-in functions
    - Method Resolution Order (MRO)
"""


class Employee:
    """Base class for all employees."""

    raise_amount = 1.04

    def __init__(self, first: str, last: str, pay: int) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

    def fullname(self) -> str:
        return f"{self.first} {self.last}"

    def apply_raise(self) -> None:
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    """
    Developer subclass — inherits everything from Employee.

    Adds:
        - Higher default raise (10%)
        - A programming language attribute
    """

    raise_amount = 1.10  # Override the class variable (10% raise)

    def __init__(self, first: str, last: str, pay: int, prog_lang: str) -> None:
        """
        Initialize a Developer.

        We call super().__init__() to let Employee handle the common attributes
        (first, last, pay, email). Then we add the developer-specific attribute.
        """
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    """
    Manager subclass — inherits from Employee.

    Adds:
        - A list of employees they supervise
        - Methods to add/remove employees
        - Override fullname to include title
    """

    def __init__(
        self,
        first: str,
        last: str,
        pay: int,
        employees: list[Employee] | None = None,
    ) -> None:
        """
        Initialize a Manager.

        Note: We use None as default instead of [] to avoid the
        mutable default argument pitfall.
        """
        super().__init__(first, last, pay)
        self.employees = employees if employees is not None else []

    def add_employee(self, emp: Employee) -> None:
        """Add an employee to this manager's team."""
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp: Employee) -> None:
        """Remove an employee from this manager's team."""
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self) -> None:
        """Print all employees managed by this manager."""
        print(f"  Employees managed by {self.fullname()}:")
        for emp in self.employees:
            print(f"    -> {emp.fullname()}")

    def fullname(self) -> str:
        """Override: include 'Mgr.' title."""
        return f"Mgr. {self.first} {self.last}"


def demo() -> None:
    """Demonstrate inheritance and subclasses."""

    dev_1 = Developer("Aquib", "Ahmad", 50000, "Python")
    dev_2 = Developer("Test", "User", 60000, "Java")
    mgr_1 = Manager("Sarah", "Connor", 90000, [dev_1])

    # --- Inherited attributes work ---
    print(f"Developer: {dev_1.fullname()} - {dev_1.email}")
    print(f"  Programming language: {dev_1.prog_lang}")

    # --- Overridden class variable ---
    print(f"\nDeveloper raise_amount: {Developer.raise_amount} (10%)")
    print(f"Employee raise_amount : {Employee.raise_amount} (4%)")

    print(f"\ndev_1 pay before raise: {dev_1.pay}")
    dev_1.apply_raise()  # Uses Developer.raise_amount = 1.10
    print(f"dev_1 pay after raise : {dev_1.pay}")

    # --- Manager with employees ---
    print(f"\nManager: {mgr_1.fullname()} - {mgr_1.email}")
    mgr_1.add_employee(dev_2)
    mgr_1.print_employees()

    mgr_1.remove_employee(dev_1)
    print("\nAfter removing dev_1:")
    mgr_1.print_employees()

    # --- isinstance() and issubclass() ---
    print(f"\nisinstance(dev_1, Developer) : {isinstance(dev_1, Developer)}")
    print(f"isinstance(dev_1, Employee)  : {isinstance(dev_1, Employee)}")
    print(f"isinstance(mgr_1, Developer) : {isinstance(mgr_1, Developer)}")

    print(f"\nissubclass(Developer, Employee) : {issubclass(Developer, Employee)}")
    print(f"issubclass(Manager, Employee)   : {issubclass(Manager, Employee)}")
    print(f"issubclass(Manager, Developer)  : {issubclass(Manager, Developer)}")

    # --- Method Resolution Order ---
    print(f"\nDeveloper MRO: {[cls.__name__ for cls in Developer.__mro__]}")
    print(f"Manager MRO  : {[cls.__name__ for cls in Manager.__mro__]}")


if __name__ == "__main__":
    demo()
