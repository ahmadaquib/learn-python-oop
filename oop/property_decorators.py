"""
Property Decorators — Getters, Setters, and Deleters
=====================================================
Learn how to use @property to control attribute access.

Topics covered:
    - The problem: computed attributes go stale
    - @property: define a method that acts like an attribute
    - @<name>.setter: validate or transform on assignment
    - @<name>.deleter: clean up on deletion
    - Why properties are Pythonic (no need for Java-style getters/setters)
"""


class Employee:
    """Employee class demonstrating property decorators."""

    def __init__(self, first: str, last: str) -> None:
        self.first = first
        self.last = last

    # --- @property: getter ---
    @property
    def email(self) -> str:
        """
        Computed property — dynamically generates the email.

        WITHOUT @property, if we stored self.email in __init__,
        changing self.first later would NOT update the email.
        With @property, it's always computed fresh.

        Usage: emp.email  (no parentheses — looks like an attribute!)
        """
        return f"{self.first}.{self.last}@company.com"

    @property
    def fullname(self) -> str:
        """Computed property for full name."""
        return f"{self.first} {self.last}"

    # --- @<name>.setter ---
    @fullname.setter
    def fullname(self, name: str) -> None:
        """
        Setter — allows `emp.fullname = "New Name"` to work.

        This splits the full name and updates first + last accordingly.
        Without a setter, assigning to a @property raises AttributeError.
        """
        parts = name.strip().split(" ", 1)
        if len(parts) != 2:
            raise ValueError("fullname must contain a first and a last name")
        self.first, self.last = parts

    # --- @<name>.deleter ---
    @fullname.deleter
    def fullname(self) -> None:
        """
        Deleter — runs when `del emp.fullname` is called.

        Useful for cleanup. Here we reset first and last to empty strings.
        """
        print(f"  Deleting fullname for {self.first} {self.last}!")
        self.first = ""
        self.last = ""


def demo() -> None:
    """Demonstrate property decorators."""

    emp = Employee("Aquib", "Ahmad")

    # --- @property as getter ---
    # Access like attributes (no parentheses), but they compute dynamically
    print(f"First : {emp.first}")
    print(f"Last  : {emp.last}")
    print(f"Email : {emp.email}")
    print(f"Name  : {emp.fullname}")

    # --- The problem @property solves ---
    # If email were a regular attribute set in __init__, this would break:
    print("\n--- Changing first name to 'John' ---")
    emp.first = "John"
    print(f"First : {emp.first}")
    print(f"Email : {emp.email}    <- auto-updated! (because it's a @property)")
    print(f"Name  : {emp.fullname}  <- auto-updated!")

    # --- @fullname.setter ---
    print("\n--- Using setter: emp.fullname = 'Jane Doe' ---")
    emp.fullname = "Jane Doe"
    print(f"First : {emp.first}")
    print(f"Last  : {emp.last}")
    print(f"Email : {emp.email}")
    print(f"Name  : {emp.fullname}")

    # --- @fullname.deleter ---
    print("\n--- Using deleter: del emp.fullname ---")
    del emp.fullname
    print(f"First : '{emp.first}'")
    print(f"Last  : '{emp.last}'")
    print(f"Email : {emp.email}")


if __name__ == "__main__":
    demo()
