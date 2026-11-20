"""
Experiment 07 - Find email patterns using Regular Expressions (CO-3)
"""
import re

text = """
Contact us at support@example.com or sales.team@company.co.in.
Varad's mail: varad.bidwai_5607@gmail.com
Invalid ones: user@.com, @gmail.com, name@domain
HR: hr-dept@mitadt.edu.in
"""

pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}"

# findall -> all matching emails
emails = re.findall(pattern, text)
print("Emails found:")
for email in emails:
    print(" ", email)
print("Total:", len(emails))

# finditer -> match position and split into username / domain
print("\nDetails:")
for match in re.finditer(r"([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})", text):
    print(f"  {match.group():<32} user = {match.group(1):<20} domain = {match.group(2)}")

# fullmatch -> validate single email addresses
print("\nValidation:")
for e in ["varad@gmail.com", "wrong@com", "test.user@mit.edu"]:
    status = "Valid" if re.fullmatch(pattern, e) else "Invalid"
    print(f"  {e:<20} -> {status}")
