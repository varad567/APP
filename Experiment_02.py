"""
Experiment 02 - Dynamic Report Generator (CO-1)
Uses decorators, class methods and magic methods to define report templates
and apply formatting options dynamically.
"""


# ---------- Decorators for formatting ----------
def uppercase(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper


def add_border(func):
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        width = max(len(line) for line in text.split("\n")) + 4
        border = "*" * width
        lines = [f"* {line.ljust(width - 4)} *" for line in text.split("\n")]
        return border + "\n" + "\n".join(lines) + "\n" + border
    return wrapper


class Report:
    report_count = 0          # class variable

    def __init__(self, title, data):
        self.title = title
        self.data = data      # dictionary of field -> value
        Report.report_count += 1

    # ----- Class methods -----
    @classmethod
    def from_template(cls, template_name, data):
        templates = {
            "sales": "Monthly Sales Report",
            "student": "Student Performance Report",
        }
        return cls(templates.get(template_name, "General Report"), data)

    @classmethod
    def total_reports(cls):
        return cls.report_count

    # ----- Magic methods -----
    def __str__(self):
        lines = [self.title, "-" * len(self.title)]
        for key, value in self.data.items():
            lines.append(f"{key:<12}: {value}")
        return "\n".join(lines)

    def __len__(self):
        return len(self.data)

    def __add__(self, other):
        merged = {**self.data, **other.data}
        return Report(f"{self.title} + {other.title}", merged)

    def __getitem__(self, key):
        return self.data[key]

    # ----- Formatted outputs using decorators -----
    def plain(self):
        return str(self)

    @uppercase
    def shout(self):
        return str(self)

    @add_border
    def boxed(self):
        return str(self)


if __name__ == "__main__":
    sales = Report.from_template("sales", {"Month": "October", "Revenue": 50000, "Units": 320})
    student = Report.from_template("student", {"Name": "Varad", "Marks": 92})

    print("Plain format:\n" + sales.plain())
    print("\nUppercase format:\n" + sales.shout())
    print("\nBordered format:\n" + student.boxed())

    print("\nNumber of fields in sales report (len):", len(sales))
    print("Revenue (getitem):", sales["Revenue"])

    combined = sales + student
    print("\nCombined report (add):\n" + combined.boxed())

    print("\nTotal reports created:", Report.total_reports())
