# Data Analytics — Student Reference

**August B3 + September B2**

Student-facing reference for the **August B3 + September B2** Data Analytics batch.

**Live:** https://classtapacademy.github.io/da-reference-aug-sep/

Seven tabs: Basics · Collections · Functions · Strings · Files & Classes · NumPy · pandas.

188 entries and 76 practice questions. Each section ends with practice questions and a
collapsible worked answer.

The page itself carries no course framing — no batch names, no session numbers, no
commentary. It reads as a reference.

## Every example is executed

Nothing on the page is hand-copied output. `build/runner.py` executes each snippet,
captures its real stdout and writes it into the JSON. It also:

- runs each snippet a **second time in a fresh interpreter** and refuses to build if the
  output differs — Python randomises string hashing per process, so printing a set gives a
  different order each run and that must never reach a student;
- runs snippets in a **temp working directory**, so file-handling examples work and leave
  nothing behind;
- feeds scripted `stdin` to `input()` examples so they produce a real terminal transcript.

## Rebuilding

```bash
cd build
python3 c1_basics.py        # each one re-executes its snippets and rewrites its JSON
python3 c2_collections.py
python3 c3_functions.py
python3 c4_strings.py
python3 c5_oop.py
python3 c6_numpy.py
python3 c7_pandas.py
python3 build_page.py       # -> ../public/index.html
cp ../public/index.html ../index.html
```

`build_page.py` fails the build on unbalanced tags.

## Scope

Python, NumPy, and pandas as far as it has been delivered to this batch. pandas covers
two sessions so far, so that tab is the smallest; it grows as more are recorded.

`rename.py` holds the textbook naming — the content is authored in a teaching voice and
renamed to neutral reference headings at build time.
