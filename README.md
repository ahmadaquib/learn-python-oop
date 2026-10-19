# Object-Oriented Programming in Python

Complete OOP concepts in Python — classes, inheritance, decorators, and more.

## Topics Covered

| # | Topic | File |
|---|-------|------|
| 1 | Classes and Instances | `oop/classes_and_instances.py` |
| 2 | Class Variables | `oop/class_variables.py` |
| 3 | Classmethods and Staticmethods | `oop/classmethods_and_staticmethods.py` |
| 4 | Inheritance — Creating Subclasses | `oop/inheritance.py` |
| 5 | Special (Magic/Dunder) Methods | `oop/special_dunder_methods.py` |
| 6 | Property Decorators | `oop/property_decorators.py` |

> **Note:** Each module intentionally defines its own self-contained `Employee` class tailored to the specific concept demonstrated. This keeps each topic independent, readable, and runnable on its own without cross-file dependencies.

## Requirements

- Python 3.14+
- [uv](https://docs.astral.sh/uv/) (recommended package manager)

## Setup

```bash
# Clone the repo
git clone https://github.com/ahmadaquib/learn-python-oop.git
cd learn-python-oop

# Create virtual environment and install
uv sync
```

## Run

```bash
# Run all demos
uv run python main.py

# Or run individual modules
uv run python -m oop.classes_and_instances
uv run python -m oop.inheritance
```

## Project Structure

```
├── main.py                              # Entry point — runs all demos
├── oop/                                 # OOP package
│   ├── __init__.py
│   ├── classes_and_instances.py         # Classes, __init__, self
│   ├── class_variables.py              # Class vs instance variables
│   ├── classmethods_and_staticmethods.py  # @classmethod, @staticmethod
│   ├── inheritance.py                  # Subclasses, super(), MRO
│   ├── special_dunder_methods.py       # __repr__, __str__, __add__, etc.
│   └── property_decorators.py          # @property, setters, deleters
├── pyproject.toml
├── .python-version
└── README.md
```

## Built With

- **Python 3.14** - Latest stable release
- **uv** - Fast Python package manager by Astral
- **AI-Assisted** - This repository was structured, improved, and documented with the help of AI (Google Antigravity / Gemini). All code was reviewed and verified to run correctly.

## License

This project is for educational purposes.