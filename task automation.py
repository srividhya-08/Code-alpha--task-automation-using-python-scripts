
import re
sample_text = """
Hello John,

Please contact us at support@gmail.com for help.
You can also mail admin@yahoo.com or sales@company.in

For business queries:
manager@office.org
hr.department@company.com

Thank you!
"""


with open("input.txt", "w") as file:
    file.write(sample_text)

print("Sample input.txt file created successfully")

# Opening input.txt in read mode
with open("input.txt", "r") as file:
    data = file.read()

print("Reading data from input.txt...\n")
# Regular Expression Pattern for Email Addresses
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Extracting all matching email addresses
emails = re.findall(pattern, data)

print("Email addresses found successfully.\n")
with open("emails.txt", "w") as output:
    for email in emails:
        output.write(email + "\n")

print("Extracted emails saved to emails.txt\n")

print("========== Extracted Email Addresses ==========")

for email in emails:
    print(email)

print("\nTask Completed Successfully!")


