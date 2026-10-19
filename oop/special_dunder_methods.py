"""
Special (Magic / Dunder) Methods
================================
Learn how to customize class behavior using special methods.

'Dunder' = Double UNDERscore (e.g. __repr__)

Topics covered:
    - __repr__: unambiguous string for debugging / developers
    - __str__: readable string for end users
    - __add__: operator overloading for +
    - __len__: support for len()
    - __eq__: equality comparison with ==
    - __lt__: less-than comparison with <
"""


class Employee:
    """Employee class demonstrating special/dunder methods."""

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

    # --- __repr__: for developers / debugging ---
    def __repr__(self) -> str:
        """
        Return an unambiguous representation of the object.

        Convention: should look like a valid constructor call when possible.
        This is what you see in the REPL or when using repr().
        """
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    # --- __str__: for end users ---
    def __str__(self) -> str:
        """
        Return a readable, user-friendly string.

        This is what print() and str() use.
        If __str__ is not defined, Python falls back to __repr__.
        """
        return f"{self.fullname()} - {self.email}"

    # --- __add__: operator overloading (+) ---
    def __add__(self, other: "Employee") -> int:
        """
        Define what + means for Employee objects.

        Here: adding two employees returns their combined salary.
        (Just like int.__add__ defines 1 + 2 = 3)
        """
        return self.pay + other.pay

    # --- __len__: support len() ---
    def __len__(self) -> int:
        """
        Define what len() returns for an Employee.

        Here: the length of the employee's full name.
        """
        return len(self.fullname())

    # --- __eq__: equality comparison (==) ---
    def __eq__(self, other: object) -> bool:
        """
        Define what == means for Employee objects.

        Two employees are 'equal' if they have the same email.
        """
        if not isinstance(other, Employee):
            return NotImplemented
        return self.email == other.email

    # --- __lt__: less-than comparison (<) ---
    def __lt__(self, other: "Employee") -> bool:
        """
        Define what < means — compare by pay.

        This also enables sorting: sorted([emp1, emp2, emp3])
        """
        return self.pay < other.pay


def demo() -> None:
    """Demonstrate special/dunder methods."""

    emp_1 = Employee("Aquib", "Ahmad", 50000)
    emp_2 = Employee("Test", "User", 60000)

    # --- __repr__ vs __str__ ---
    print("repr(emp_1):", repr(emp_1))
    print("str(emp_1) :", str(emp_1))
    print()

    # print() calls __str__ first, falls back to __repr__
    print("print(emp_1):", emp_1)
    print()

    # --- __add__: using the + operator ---
    combined_salary = emp_1 + emp_2
    print(f"{emp_1.fullname()} + {emp_2.fullname()} = {combined_salary} (combined pay)")
    print()

    # --- __len__: using len() ---
    print(f"len(emp_1) = {len(emp_1)} (length of '{emp_1.fullname()}')")
    print(f"len(emp_2) = {len(emp_2)} (length of '{emp_2.fullname()}')")
    print()

    # --- __eq__: using == ---
    emp_3 = Employee("Aquib", "Ahmad", 70000)  # Same name/email, different pay
    print(f"emp_1 == emp_2: {emp_1 == emp_2}   (different emails)")
    print(f"emp_1 == emp_3: {emp_1 == emp_3}  (same email)")
    print()

    # --- __lt__: using < and sorted() ---
    print(f"emp_1 < emp_2: {emp_1 < emp_2}  ({emp_1.pay} < {emp_2.pay})")
    employees = [emp_2, emp_3, emp_1]
    sorted_emps = sorted(employees)
    print(f"Sorted by pay: {[repr(e) for e in sorted_emps]}")


if __name__ == "__main__":
    demo()
