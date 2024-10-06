""" import re

str1 = "menos de 10 pepinos"
str2 = "42 pepinos"

pattern_1 = re.compile(r"\b(?:menos|más)\sde\b\s(\d+) pepinos")
match_1 = pattern_1.match(str1)
print(match_1.groups())
print("grupo(1): " + match_1.group(1))

pattern_2 = re.compile(r'(\d+)\spepinos\b')
match_2 = pattern_2.match(str2)
print(match_2.groups()) """