# -*- coding: utf-8 -*-
from runner import build

ROWS = [
# ---------------- Your first lines ----------------
dict(cat="Your first lines", name="print()",
 desc="Shows something on the screen. Anything in quotes is text; anything without is worked out first.",
 code='print("Hello, Data Analytics")\nprint(2026)\nprint(60 * 7)'),
dict(cat="Your first lines", name="Several things in one print",
 desc="Separate the parts with commas. Python puts a single space between them for you.",
 code='name = "Rahul"\ndept = "HR"\nprint("Employee", name, "works in", dept)'),
dict(cat="Your first lines", name="Comments  #",
 desc="Anything after a # is ignored by Python. It is a note for the human reading the code.",
 code='# this line does nothing at all\nsalary = 47764      # monthly, in rupees\nprint(salary)'),
dict(cat="Your first lines", name="Variables",
 desc="A name that holds a value. Assign with a single =, and you can change it later.",
 code='emp_id = 1001\nname   = "Rahul Sharma"\nsalary = 47764\n\nprint(emp_id, name, salary)\n\nsalary = 52000          # changed\nprint("after the hike:", salary)'),

# ---------------- The five data types ----------------
dict(cat="The data types", name="int  —  whole numbers",
 desc="Counting numbers, positive or negative, with no decimal point.",
 code='experience = 4\nprint(experience)\nprint(type(experience))'),
dict(cat="The data types", name="float  —  numbers with a decimal",
 desc="Any number with a dot in it. Division always produces one, even when it divides evenly.",
 code='height = 169.5\nprint(height, type(height))\nprint(10 / 2, type(10 / 2))'),
dict(cat="The data types", name="str  —  text",
 desc="Anything inside quotes. Single or double quotes both work, as long as you match them.",
 code="dept = 'HR'\ncity = \"Hyderabad\"\nprint(dept, city)\nprint(type(dept))"),
dict(cat="The data types", name="bool  —  True or False",
 desc="Only two possible values, and both start with a capital letter.",
 code='is_active = True\nprint(is_active, type(is_active))\nprint(5 > 3)\nprint(5 == 3)'),
dict(cat="The data types", name="type()",
 desc="Asks Python what something is. Useful the moment a value does not behave the way you expected.",
 code='print(type(10))\nprint(type(10.0))\nprint(type("10"))\nprint(type(True))'),

# ---------------- Type conversion ----------------
dict(cat="Type conversion", name="int()",
 desc="Turns something into a whole number. On a float it CUTS the decimal off — it does not round.",
 code='print(int("25"))\nprint(int(9.99))        # 9, not 10\nprint(int(True))'),
dict(cat="Type conversion", name="float()  and  str()",
 desc="float() adds a decimal point, str() turns a number into text so it can be joined to other text.",
 code='print(float(25), type(float(25)))\nprint(str(25) + " employees")'),
dict(cat="Type conversion", name="Why conversion matters",
 desc='"25" and 25 look the same on screen and behave completely differently. Text repeats; numbers add.',
 code='print("25" + "25")      # text joins\nprint(25 + 25)          # numbers add\nprint(int("25") + 25)   # convert first'),
dict(cat="Type conversion", name="When it cannot convert",
 desc="int() only works on something that really is a number. Anything else stops the program.",
 code='print(int("50"))\nprint(int("fifty"))', raises=True),

# ---------------- Taking input ----------------
dict(cat="Taking input", name="input()",
 desc="Stops and waits for the user to type. Whatever they type arrives as TEXT, always.",
 code='name = input("Enter your name: ")\nprint("Welcome,", name)\nprint(type(name))',
 stdin=["Priya"]),
dict(cat="Taking input", name="int(input())  —  the one everybody forgets",
 desc="input() hands back text, so you must convert before doing any maths with it.",
 code='age = input("Enter your age: ")\nprint("next year you are", age + 1)',
 stdin=["23"], raises=True),
dict(cat="Taking input", name="The fix",
 desc="Wrap input() in int() — or float() if decimals are possible.",
 code='age = int(input("Enter your age: "))\nprint("next year you are", age + 1)',
 stdin=["23"]),

# ---------------- Operators ----------------
dict(cat="Operators", name="Arithmetic",
 desc="The usual five, plus // for whole-number division and % for the remainder.",
 code='a, b = 17, 5\nprint("add      ", a + b)\nprint("subtract ", a - b)\nprint("multiply ", a * b)\nprint("divide   ", a / b)      # always a float\nprint("floor    ", a // b)     # whole part only\nprint("remainder", a % b)\nprint("power    ", a ** 2)'),
dict(cat="Operators", name="% — the even/odd test",
 desc="The remainder operator is how you check whether a number divides evenly. Remainder 0 means it does.",
 code='for n in [10, 7, 24]:\n    if n % 2 == 0:\n        print(n, "is even")\n    else:\n        print(n, "is odd")'),
dict(cat="Operators", name="Comparison",
 desc="Six of them, and every one hands back True or False. Note == is a question, = is an instruction.",
 code='salary = 47764\nprint(salary > 50000)\nprint(salary < 50000)\nprint(salary == 47764)\nprint(salary != 47764)\nprint(salary >= 47764)'),
dict(cat="Operators", name="and  /  or  /  not",
 desc="Join two conditions. and needs both true; or needs one; not flips it.",
 code='dept, salary = "Tech", 62990\n\nprint(dept == "Tech" and salary > 50000)\nprint(dept == "HR"   or  salary > 50000)\nprint(not dept == "Tech")'),

# ---------------- Decisions ----------------
dict(cat="Making decisions", name="if",
 desc="Runs the indented block only when the condition is True. The colon and the indent are both required.",
 code='salary = 62990\n\nif salary > 50000:\n    print("above fifty thousand")\n\nprint("this line always runs")'),
dict(cat="Making decisions", name="if  /  else",
 desc="Two paths, and exactly one of them runs.",
 code='age = 17\n\nif age >= 18:\n    print("can vote")\nelse:\n    print("cannot vote yet")'),
dict(cat="Making decisions", name="if  /  elif  /  else",
 desc="More than two paths. Python checks top to bottom and stops at the FIRST one that is true.",
 code='marks = 72\n\nif marks >= 90:\n    print("A")\nelif marks >= 75:\n    print("B")\nelif marks >= 60:\n    print("C")\nelse:\n    print("D")'),
dict(cat="Making decisions", name="Order matters",
 desc="Because it stops at the first match, a loose condition placed first swallows all the rest.",
 code='marks = 95\n\n# WRONG - 95 is >= 60, so it stops here\nif marks >= 60:\n    print("C")\nelif marks >= 90:\n    print("A")      # never reached'),
dict(cat="Making decisions", name="Nested if",
 desc="An if inside another if. The inner one is only reached when the outer one passed.",
 code='dept, salary = "Tech", 62990\n\nif dept == "Tech":\n    if salary > 50000:\n        print("senior tech")\n    else:\n        print("junior tech")\nelse:\n    print("not tech")'),
]

PRACTICE = [
dict(cat="Your first lines", q="Store your own name, your city and your age in three variables, then print them in one sentence.",
 code='name = "Anita"\ncity = "Chennai"\nage  = 22\nprint(name, "is", age, "and lives in", city)'),
dict(cat="The data types", q="Print the type of each of these: 7, 7.0, \"7\", True. Say out loud why 7 and \"7\" are different.",
 code='for v in [7, 7.0, "7", True]:\n    print(v, "->", type(v))'),
dict(cat="Type conversion", q="A salary arrives as the text \"47764\". Add a 10% bonus to it and print the total.",
 code='salary = "47764"\ntotal = int(salary) + int(salary) * 10 / 100\nprint(total)'),
dict(cat="Taking input", q="Ask for two numbers and print their sum. Make sure it adds rather than joins.",
 code='a = int(input("first number: "))\nb = int(input("second number: "))\nprint("sum is", a + b)', stdin=["12","30"]),
dict(cat="Operators", q="Ask for a number and say whether it is even or odd.",
 code='n = int(input("number: "))\nif n % 2 == 0:\n    print(n, "is even")\nelse:\n    print(n, "is odd")', stdin=["18"]),
dict(cat="Operators", q="An employee is in Tech AND earns over 50,000. Print True or False for salary 48,000.",
 code='dept, salary = "Tech", 48000\nprint(dept == "Tech" and salary > 50000)'),
dict(cat="Making decisions", q="Grade a mark out of 100: 90+ A, 75+ B, 60+ C, 40+ D, below that Fail. Test it with 61.",
 code='marks = 61\nif marks >= 90:\n    print("A")\nelif marks >= 75:\n    print("B")\nelif marks >= 60:\n    print("C")\nelif marks >= 40:\n    print("D")\nelse:\n    print("Fail")'),
dict(cat="Making decisions", q="Ask for a year and print whether it is a leap year. (Divisible by 4, but not by 100, unless also by 400.)",
 code='y = int(input("year: "))\nif y % 400 == 0:\n    print(y, "is a leap year")\nelif y % 100 == 0:\n    print(y, "is not a leap year")\nelif y % 4 == 0:\n    print(y, "is a leap year")\nelse:\n    print(y, "is not a leap year")', stdin=["2024"]),
]

if __name__ == "__main__":
    import sys
    bad  = build(ROWS, "t1_basics.json")
    bad += build(PRACTICE, "t1_basics_practice.json")
    sys.exit(1 if bad else 0)
