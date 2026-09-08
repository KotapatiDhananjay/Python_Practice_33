import re

phones = "John-8956237845, Carol-7845128956, mark-0123456578"

pattern = r"\d{10}"
pattern_compiled = re.compile(pattern)

print(pattern_compiled)
print(type(pattern_compiled))

match_obj = re.findall(pattern_compiled, phones)
print(match_obj)

with open("student_details", "r") as fh:
    data = fh.read()
print(data)

phone_matches = re.finditer(pattern_compiled, data)
print(phone_matches)

for match in phone_matches:
    print(match)