# -*- coding: utf-8 -*-
"""Textbook naming. The content was written in a teaching voice; a reference
wants neutral section and entry names with no course framing in them."""

CATS = {
 "Your first lines":"Output and variables", "The data types":"Data types",
 "Taking input":"Input", "Making decisions":"Conditional statements",
 "Writing a function":"Defining functions", "The five kinds of argument":"Function arguments",
 "lambda, map, filter, reduce":"Lambda, map, filter and reduce",
 "List comprehension":"Comprehensions",
 "Strings and slicing":"String indexing and slicing",
 "Error handling":"Exception handling", "The four pillars":"The four pillars of OOP",
}

NAMES = {
 # basics
 "Several things in one print":"Printing multiple values", "Comments  #":"Comments",
 "int  —  whole numbers":"int", "float  —  numbers with a decimal":"float",
 "str  —  text":"str", "bool  —  True or False":"bool",
 "Why conversion matters":"Text and numbers behave differently",
 "When it cannot convert":"Invalid conversion",
 "int(input())  —  the one everybody forgets":"input() returns text",
 "The fix":"Converting input",
 "% — the even/odd test":"Modulo", "and  /  or  /  not":"Logical operators",
 "if  /  else":"if and else", "if  /  elif  /  else":"if, elif and else",
 "Order matters":"Condition order",
 # collections
 "for  —  over a list":"for", "for with an index":"for with range(len())",
 "Making one, and reaching in":"Creating and indexing", "Changing a list":"Modifying a list",
 "sum / max / min on a list":"sum, max and min",
 "A tuple is a list that cannot change":"Creating a tuple",
 "Trying to change one":"Tuples cannot be changed", "Why use one at all":"Tuple methods",
 "A set throws away duplicates":"Creating a set",
 "De-duplicating a list":"Removing duplicates from a list",
 "add / remove / discard":"add, remove and discard",
 "union / intersection / difference":"union, intersection and difference",
 "Key and value":"Creating a dictionary", "get()  —  the safe way to read":"get()",
 "Adding and changing":"Adding and changing entries",
 "keys / values / items":"keys, values and items",
 # functions
 "Passing something in":"Parameters and arguments", "print is not return":"print and return",
 "Returning more than one value":"Returning multiple values",
 "1. Positional":"Positional arguments", "2. Keyword":"Keyword arguments",
 "3. Default":"Default arguments", "4. Variable length  *args":"*args",
 "5. Variable length  **kwargs":"**kwargs", "The order they must go in":"Argument order",
 "The three side by side":"map, filter and reduce compared",
 "A function that calls itself":"Defining a recursive function",
 "Forgetting the base case":"A missing base case",
 "The short way to build a list":"Basic syntax",
 "if ... else inside one":"if and else inside a comprehension",
 "On a string, and nested":"On strings, and nested",
 # strings
 "Indexing a string":"Indexing", "Slicing  [start:stop]":"Slicing",
 "The third number  —  step":"Step", "A string cannot be changed":"Strings cannot be changed",
 "in  —  is it there?":"The in operator",
 "strip()  —  removing stray spaces":"strip()",
 "split()  and  join()":"split() and join()", "find()  and  count()":"find() and count()",
 "The is... checks":"The is-checks", "Rounding inside an f-string":"Rounding",
 "Lining things up":"Alignment", "format()  —  the older way":"format()",
 "What a meta character is":"Meta characters", "re.match()  —  only at the start":"re.match()",
 "re.sub()  —  find and replace":"re.sub()",
 "A real check  —  is this an email?":"Validating an email",
 # files / errors / oop
 "open() and the three modes":"open() and file modes",
 '"w" wipes the file':"Write mode overwrites", '"a" adds instead':"Append mode",
 "read / readline / readlines":"read, readline and readlines",
 "Looping over a file":"Reading line by line", "with open()  —  closes it for you":"with open()",
 "Why it exists":"An unhandled error", "try  /  except":"try and except",
 "Catching a SPECIFIC error":"Catching a specific error",
 "More than one except":"Multiple except blocks", "else  and  finally":"else and finally",
 "The error names worth knowing":"Common exceptions",
 "class and object":"Defining a class", "__init__  and  self":"__init__ and self",
 "Each object keeps its own data":"Each object has its own data",
 "super()  —  extending the parent":"super()",
 "Polymorphism  —  overriding":"Polymorphism",
 # numpy
 "np.zeros()  and  np.ones()":"np.zeros() and np.ones()",
 "np.sqrt()  and  np.round()":"np.sqrt() and np.round()",
 "sum, mean, min, max":"sum, mean, min and max", "std and var":"std and var",
 "argmin and argmax":"argmin and argmax",
 "Nothing is stored unless assigned":"Operations return a new array",
 "Two arrays together":"Two arrays",
 "A single value":"With a single value", "A row across a table":"With a row",
 "When the shapes do not fit":"Mismatched shapes",
 "A condition returns True and False":"A condition returns booleans",
 "Using the condition to select":"Selecting with a condition",
 "Counting matches":"Counting matches", "Two conditions":"Two conditions",
 "reshape must fit":"reshape must match the size",
 # pandas
 "A chosen index":"A custom index", "One column":"One column",
 "Several columns":"Several columns", "loc  —  by label":"loc",
 "iloc  —  by position":"iloc", "Rows and columns together":"Rows and columns",
 "at  —  a single cell":"at", "iat  —  a single cell by position":"iat",
 "A condition":"A condition", "Using the condition":"Filtering with a condition",
 "and does not work here":"and cannot be used", "Counting the matches":"Counting matches",
 "More than one column":"Several columns", "The original is unchanged":"Sorting returns a new table",
 "unique() and nunique()":"unique() and nunique()", "Column statistics":"Column statistics",
}

# entries that are pure lesson-summary and have no place in a reference
DROP = {"The four, in one line each"}

# conversational phrasing -> neutral
PHRASES = [
 ("The one you will use most on real data. ", ""),
 ("The one you will use most. ", ""),
 ("The single most common confusion. ", ""),
 ("The mistake that loses work. ", ""),
 ("The one to actually use. ", ""),
 ("The three you will use constantly once real data arrives.", "Totals and extremes."),
 ("The four you will use every day of your working life.", "The four basic summaries."),
 ("The version to actually use. ", ""),
 ("The classic. ", ""),
 ("That trips people up.", ""),
 ("You will still meet this in older code. ", ""),
 ("Good for something tiny you use once.", "Useful for a short, single-use function."),
 ("The one you will use most, and ", ""),
 ("Handy for filenames and codes.", "Commonly used for filenames and codes."),
 ("Python stops you rather than freezing — but the error is the only warning you get.",
  "Python raises RecursionError rather than running forever."),
 ("This is the whole difference, and the error names it: tuples do not support assignment.",
  "A tuple does not support item assignment."),
 ("The most common real use: wrap a list in set() to see the distinct values.",
  "Wrapping a list in set() gives its distinct values."),
 ("The pattern worth memorising: a dictionary of counts, built in one pass over the data.",
  "A dictionary of counts, built in one pass over the data."),
 ("The three views, and items() is the one you loop over when you want both halves.",
  "items() is used when both the key and the value are needed."),
 ("Four of them, and none of them change the original — they all hand back a new string.",
  "None of these change the original string; each returns a new one."),
 ("Put an f before the quote and anything in curly brackets is worked out and dropped in.",
  "An f before the quote allows an expression inside curly brackets."),
 (":.2f means two decimal places. This is how you stop a salary printing as 52540.400000000001.",
  ":.2f sets the number of decimal places."),
 ("A number after < > or ^ sets the width, which is how you get columns that line up.",
  "A number after <, > or ^ sets the field width."),
 ("A character that means something other than itself. These are the ones that matter.",
  "A character that stands for a class of characters rather than itself."),
 ("Finds EVERY match and hands them back as a list. The one you will use most.",
  "Returns every match as a list."),
 ("Putting the pieces together. ^ and $ mean the WHOLE string has to match, not just part of it.",
  "^ and $ anchor the pattern so the whole string must match."),
 ("Without it, one bad value stops the whole program and nothing after it runs.",
  "An uncaught error stops the program; nothing after it runs."),
 ("A bare except hides every problem, including the ones you wanted to know about. Name the error.",
  "Naming the error avoids hiding problems you did not expect."),
 ("Each one tells you something different. Read the name before you read anything else.",
  "The exception name identifies what went wrong."),
 ("A class is the blueprint. An object is one real thing built from it. One class, many objects.",
  "A class is a blueprint; an object is one instance built from it."),
 ("__init__ runs automatically when an object is made. self is that object — it is how each one keeps its own values.",
  "__init__ runs when an object is created. self refers to that object."),
 ("A function inside a class. It always takes self first, so it can reach the object's own values.",
  "A function defined inside a class. It takes self as its first parameter."),
 ("This is the point of self. Two objects from one class do not share anything.",
  "Two objects created from the same class do not share their data."),
 ("Once objects are in a list you can loop over them like any other data. This is where it becomes useful.",
  "Objects in a list can be looped over like any other data."),
 ("Everything you learned about lists still applies — the items just happen to be objects.",
  "List operations apply the same way when the items are objects."),
 ("Introduced together in the last session. Each one is a way of organising code, not a new syntax.", ""),
 ("The data and the methods that work on it live in the same class. Two underscores marks something as internal.",
  "The data and the methods that use it live in the same class. Two leading underscores mark an attribute as internal."),
 ("Put the parent class in the brackets and the child gets everything it has, for free.",
  "Naming a parent class in the brackets gives the child all of its attributes and methods."),
 ("Call the parent's version first, then add to it, instead of rewriting what already works.",
  "Calls the parent's version, so it does not have to be rewritten."),
 ("The caller uses hike() without knowing how it works. A base class can name a method and leave the detail to the children.",
  "A base class names a method and leaves the detail to each child class."),
]

def apply(rows):
    out=[]
    for r in rows:
        if r.get("name") in DROP: continue
        r=dict(r)
        r["cat"]=CATS.get(r["cat"], r["cat"])
        if "name" in r: r["name"]=NAMES.get(r["name"], r["name"])
        if "desc" in r:
            d=r["desc"]
            for a,b in PHRASES: d=d.replace(a,b)
            r["desc"]=d.strip()
        return_rows=None
        out.append(r)
    return out
