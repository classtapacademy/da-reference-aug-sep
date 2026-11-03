# -*- coding: utf-8 -*-
from runner import build
I = "import pandas as pd\n"
DF = (I + 'df = pd.DataFrame({\n'
          '    "name":   ["Rahul", "Priya", "Amit", "Kavya", "Arjun"],\n'
          '    "dept":   ["HR", "Tech", "Sales", "Tech", "HR"],\n'
          '    "salary": [47764, 62990, 51200, 58300, 45100],\n'
          '    "exp":    [4, 7, 3, 6, 2]\n'
          '})\n\n')

ROWS = [
# ---------------- Series and DataFrame ----------------
dict(cat="Series and DataFrame", name="pd.Series()",
 desc="A single column of values. Pandas adds a numbered index on the left.",
 code=I+'s = pd.Series([10, 20, 30])\nprint(s)'),
dict(cat="Series and DataFrame", name="A chosen index",
 desc="The index can be any set of labels instead of 0, 1, 2.",
 code=I+'s = pd.Series([10, 20, 30], index=["a", "b", "c"])\nprint(s)\nprint(s["b"])'),
dict(cat="Series and DataFrame", name="pd.DataFrame()",
 desc="A table. Built from a dictionary, each key becomes a column name.",
 code=I+'df = pd.DataFrame({\n    "name": ["Rahul", "Priya"],\n    "dept": ["HR", "Tech"]\n})\nprint(df)'),
dict(cat="Series and DataFrame", name="read_csv()",
 desc="Loads a comma-separated file into a DataFrame.",
 code=I+'open("staff.csv", "w").write("name,dept\\nRahul,HR\\nPriya,Tech\\n")\n\ndf = pd.read_csv("staff.csv")\nprint(df)'),

# ---------------- Inspecting ----------------
dict(cat="Inspecting a DataFrame", name="head() and tail()",
 desc="The first or last rows. The default is five; pass a number for more or fewer.",
 code=DF+'print(df.head(3))\nprint()\nprint(df.tail(2))'),
dict(cat="Inspecting a DataFrame", name="shape, columns, dtypes",
 desc="The number of rows and columns, the column names, and the type held in each.",
 code=DF+'print(df.shape)\nprint(list(df.columns))\nprint(df.dtypes)'),
dict(cat="Inspecting a DataFrame", name="info()",
 desc="Column names, their types and how many non-empty values each one holds.",
 code=DF+'df.info()'),
dict(cat="Inspecting a DataFrame", name="describe()",
 desc="Count, mean, standard deviation, minimum, quartiles and maximum for the numeric columns.",
 code=DF+'print(df.describe())'),

# ---------------- Selecting ----------------
dict(cat="Selecting columns", name="One column",
 desc="Square brackets with the column name return that column as a Series.",
 code=DF+'print(df["name"])'),
dict(cat="Selecting columns", name="Several columns",
 desc="Two or more column names must be passed as a list, so there are two sets of brackets.",
 code=DF+'print(df[["name", "salary"]])'),

# ---------------- loc and iloc ----------------
dict(cat="loc and iloc", name="loc  —  by label",
 desc="Selects rows by their index label.",
 code=DF+'print(df.loc[0])\nprint()\nprint(df.loc[0:2])'),
dict(cat="loc and iloc", name="iloc  —  by position",
 desc="Selects rows by their position. Unlike loc, the stop position is not included.",
 code=DF+'print(df.iloc[0:2])\nprint()\nprint(df.iloc[-1])'),
dict(cat="loc and iloc", name="Rows and columns together",
 desc="Give the rows first, then the columns.",
 code=DF+'print(df.loc[0:2, ["name", "salary"]])\nprint()\nprint(df.iloc[0:2, 0:2])'),
dict(cat="loc and iloc", name="at  —  a single cell",
 desc="Reads one value, given the row label and the column name.",
 code=DF+'print(df.at[0, "name"])\nprint(df.at[3, "salary"])'),
dict(cat="loc and iloc", name="iat  —  a single cell by position",
 desc="The same as at, but both the row and the column are given as numbers.",
 code=DF+'print(df.iat[0, 0])\nprint(df.iat[3, 2])'),

# ---------------- Filtering ----------------
dict(cat="Filtering rows", name="A condition",
 desc="Comparing a column to a value returns True or False for every row.",
 code=DF+'print(df["salary"] > 50000)'),
dict(cat="Filtering rows", name="Using the condition",
 desc="Putting the condition inside the brackets keeps only the rows where it was True.",
 code=DF+'print(df[df["salary"] > 50000])'),
dict(cat="Filtering rows", name="Two conditions",
 desc="Use & for and, | for or. Each condition must be inside its own brackets.",
 code=DF+'print(df[(df["dept"] == "Tech") & (df["salary"] > 55000)])\nprint()\nprint(df[(df["dept"] == "HR") | (df["exp"] > 5)])'),
dict(cat="Filtering rows", name="and does not work here",
 desc="The word and expects one True or False, not a whole column of them.",
 code=DF+'print(df[(df["dept"] == "Tech") and (df["salary"] > 55000)])', raises=True),
dict(cat="Filtering rows", name="Counting the matches",
 desc="A condition can be summed, because True counts as 1.",
 code=DF+'print((df["salary"] > 50000).sum())\nprint(len(df[df["salary"] > 50000]))'),

# ---------------- Sorting ----------------
dict(cat="Sorting", name="sort_values()",
 desc="Orders the rows by a column. Smallest first unless told otherwise.",
 code=DF+'print(df.sort_values("salary"))'),
dict(cat="Sorting", name="ascending=False",
 desc="Reverses the order, largest first.",
 code=DF+'print(df.sort_values("salary", ascending=False))'),
dict(cat="Sorting", name="More than one column",
 desc="Pass a list. The second column breaks ties in the first.",
 code=DF+'print(df.sort_values(["dept", "salary"]))'),
dict(cat="Sorting", name="The original is unchanged",
 desc="Sorting returns a new table. Assign it if the order is to be kept.",
 code=DF+'df.sort_values("salary")\nprint(df["salary"].tolist())\n\ndf = df.sort_values("salary")\nprint(df["salary"].tolist())'),

# ---------------- Counting ----------------
dict(cat="Counting values", name="value_counts()",
 desc="How many times each value appears in a column, most frequent first.",
 code=DF+'print(df["dept"].value_counts())'),
dict(cat="Counting values", name="unique() and nunique()",
 desc="The distinct values in a column, and how many there are.",
 code=DF+'print(df["dept"].unique())\nprint(df["dept"].nunique())'),
dict(cat="Counting values", name="Column statistics",
 desc="The same summaries as NumPy, applied to one column.",
 code=DF+'print(df["salary"].sum())\nprint(round(df["salary"].mean(), 2))\nprint(df["salary"].min(), df["salary"].max())\nprint(df["salary"].median())'),
]

PRACTICE = [
dict(cat="Series and DataFrame", q="Build a DataFrame of three students with a name, a city and a mark, and print it.",
 code=I+'df = pd.DataFrame({\n    "name": ["Anita", "Rohit", "Meena"],\n    "city": ["Chennai", "Pune", "Delhi"],\n    "mark": [72, 85, 64]\n})\nprint(df)'),
dict(cat="Inspecting a DataFrame", q="Print the shape, the column names and the summary statistics of a table.",
 code=DF+'print(df.shape)\nprint(list(df.columns))\nprint(df.describe())'),
dict(cat="Selecting columns", q="Print only the name and department columns.",
 code=DF+'print(df[["name", "dept"]])'),
dict(cat="loc and iloc", q="Print the first two rows using iloc, and the salary of the row labelled 2 using at.",
 code=DF+'print(df.iloc[0:2])\nprint(df.at[2, "salary"])'),
dict(cat="Filtering rows", q="Print everyone earning more than 50,000, and count how many that is.",
 code=DF+'print(df[df["salary"] > 50000])\nprint((df["salary"] > 50000).sum())'),
dict(cat="Filtering rows", q="Print everyone in Tech with more than five years of experience.",
 code=DF+'print(df[(df["dept"] == "Tech") & (df["exp"] > 5)])'),
dict(cat="Sorting", q="Sort the table by salary, highest first, and print the top two names.",
 code=DF+'print(df.sort_values("salary", ascending=False)["name"].head(2).tolist())'),
dict(cat="Sorting", q="Sort by department, and within each department by salary.",
 code=DF+'print(df.sort_values(["dept", "salary"]))'),
dict(cat="Counting values", q="Print how many people are in each department, and the average salary of the table.",
 code=DF+'print(df["dept"].value_counts())\nprint(round(df["salary"].mean(), 2))'),
dict(cat="Series and DataFrame", q="Make a Series of five marks with the student names as the index, and read one out by name.",
 code='import pandas as pd\nmarks = pd.Series([72, 85, 64, 91, 55],\n                  index=["Rahul", "Priya", "Amit", "Kavya", "Arjun"])\nprint(marks)\nprint()\nprint("Kavya scored", marks["Kavya"])'),
dict(cat="Series and DataFrame", q="Build a DataFrame from a list of dictionaries, one dictionary per row.",
 code='import pandas as pd\nrows = [{"name": "Rahul", "dept": "HR",    "salary": 47764},\n        {"name": "Priya", "dept": "Tech",  "salary": 62990},\n        {"name": "Amit",  "dept": "Sales", "salary": 51200}]\nprint(pd.DataFrame(rows))'),
dict(cat="Series and DataFrame", q="Add a new column worked out from an existing one.",
 code='import pandas as pd\ndf = pd.DataFrame({"name": ["Rahul", "Priya", "Amit"],\n                   "salary": [47764, 62990, 51200]})\ndf["monthly"] = (df["salary"] / 12).round(0)\nprint(df)'),
dict(cat="Inspecting a DataFrame", q="Print the first two rows, the last two rows, and the data type of each column.",
 code='import pandas as pd\ndf = pd.DataFrame({"name":   ["Rahul", "Priya", "Amit", "Kavya", "Arjun"],\n                   "dept":   ["HR", "Tech", "Sales", "Tech", "HR"],\n                   "salary": [47764, 62990, 51200, 58300, 45100]})\nprint(df.head(2))\nprint()\nprint(df.tail(2))\nprint()\nprint(df.dtypes)'),
dict(cat="Inspecting a DataFrame", q="Find out how many values are missing in each column.",
 code='import pandas as pd\nimport numpy as np\ndf = pd.DataFrame({"name":   ["Rahul", "Priya", "Amit", "Kavya"],\n                   "salary": [47764, np.nan, 51200, np.nan],\n                   "city":   ["Chennai", "Pune", None, "Delhi"]})\nprint(df)\nprint()\nprint(df.isna().sum())'),
dict(cat="Selecting columns", q="Select one column as a Series and the same column as a DataFrame, and show the difference.",
 code='import pandas as pd\ndf = pd.DataFrame({"name": ["Rahul", "Priya"], "salary": [47764, 62990]})\nprint(type(df["salary"]).__name__)\nprint(type(df[["salary"]]).__name__)\nprint()\nprint(df[["name", "salary"]])'),
dict(cat="Selecting columns", q="Drop a column and show that the original table is unchanged unless you reassign it.",
 code='import pandas as pd\ndf = pd.DataFrame({"name": ["Rahul", "Priya"], "dept": ["HR", "Tech"], "salary": [47764, 62990]})\nsmaller = df.drop(columns=["dept"])\nprint(smaller)\nprint()\nprint("original still has:", list(df.columns))'),
dict(cat="loc and iloc", q="Use loc to pick rows 1 to 3 and two columns by name, then iloc to pick the same rows by position.",
 code='import pandas as pd\ndf = pd.DataFrame({"name":   ["Rahul", "Priya", "Amit", "Kavya", "Arjun"],\n                   "dept":   ["HR", "Tech", "Sales", "Tech", "HR"],\n                   "salary": [47764, 62990, 51200, 58300, 45100]})\nprint(df.loc[1:3, ["name", "salary"]])\nprint()\nprint(df.iloc[1:3, [0, 2]])'),
dict(cat="loc and iloc", q="Show that loc includes the last row of the range but iloc does not.",
 code='import pandas as pd\ndf = pd.DataFrame({"name": ["Rahul", "Priya", "Amit", "Kavya"]})\nprint("loc[1:3]  ->", len(df.loc[1:3]), "rows")\nprint("iloc[1:3] ->", len(df.iloc[1:3]), "rows")'),
dict(cat="loc and iloc", q="Use loc to change a value, picking the row by a condition rather than by number.",
 code='import pandas as pd\ndf = pd.DataFrame({"name": ["Rahul", "Priya", "Amit"],\n                   "salary": [47764, 62990, 51200]})\ndf.loc[df["name"] == "Amit", "salary"] = 55000\nprint(df)'),
dict(cat="Filtering rows", q="Show everyone in Tech who earns more than 55,000.",
 code='import pandas as pd\ndf = pd.DataFrame({"name":   ["Rahul", "Priya", "Amit", "Kavya", "Arjun"],\n                   "dept":   ["HR", "Tech", "Sales", "Tech", "HR"],\n                   "salary": [47764, 62990, 51200, 58300, 45100]})\nprint(df[(df["dept"] == "Tech") & (df["salary"] > 55000)])'),
dict(cat="Filtering rows", q="Show everyone who works in either HR or Sales, using isin.",
 code='import pandas as pd\ndf = pd.DataFrame({"name":   ["Rahul", "Priya", "Amit", "Kavya", "Arjun"],\n                   "dept":   ["HR", "Tech", "Sales", "Tech", "HR"],\n                   "salary": [47764, 62990, 51200, 58300, 45100]})\nprint(df[df["dept"].isin(["HR", "Sales"])])'),
dict(cat="Sorting", q="Sort by department, and within each department by salary from high to low.",
 code='import pandas as pd\ndf = pd.DataFrame({"name":   ["Rahul", "Priya", "Amit", "Kavya", "Arjun"],\n                   "dept":   ["HR", "Tech", "Sales", "Tech", "HR"],\n                   "salary": [47764, 62990, 51200, 58300, 45100]})\nprint(df.sort_values(["dept", "salary"], ascending=[True, False]))'),
dict(cat="Sorting", q="Print the two highest paid people without sorting the whole table.",
 code='import pandas as pd\ndf = pd.DataFrame({"name":   ["Rahul", "Priya", "Amit", "Kavya", "Arjun"],\n                   "salary": [47764, 62990, 51200, 58300, 45100]})\nprint(df.nlargest(2, "salary"))'),
dict(cat="Counting values", q="Count how many people are in each department, as a count and as a percentage.",
 code='import pandas as pd\ndf = pd.DataFrame({"dept": ["HR", "Tech", "Sales", "Tech", "HR", "Tech"]})\nprint(df["dept"].value_counts())\nprint()\nprint((df["dept"].value_counts(normalize=True) * 100).round(1))'),
dict(cat="Counting values", q="Print the average salary for each department.",
 code='import pandas as pd\ndf = pd.DataFrame({"dept":   ["HR", "Tech", "Sales", "Tech", "HR"],\n                   "salary": [47764, 62990, 51200, 58300, 45100]})\nprint(df.groupby("dept")["salary"].mean().round(0))'),
]

if __name__ == "__main__":
    import sys
    bad  = build(ROWS, "t7_pandas.json")
    bad += build(PRACTICE, "t7_pandas_practice.json")
    sys.exit(1 if bad else 0)
