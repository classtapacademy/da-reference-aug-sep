# Data Analytics — Student Reference

**August B3 + September B2**

Student-facing reference for the **August B3 + September B2** Data Analytics batch.

**Live:** https://classtapacademy.github.io/da-reference-aug-sep/

Covers every Python topic taught in sessions D01–D29, in teaching order, across five tabs:
Basics · Loops & Collections · Functions · Strings & Regex · Files, Errors & OOP.

124 entries and 55 practice questions. Each section ends with practice questions and a
collapsible worked answer.

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
python3 build_page.py       # -> ../public/index.html
cp ../public/index.html ../index.html
```

`build_page.py` fails the build on unbalanced tags.

## Scope

**Python only so far**, as delivered to this batch up to D29 (15-10-2026).

NumPy and pandas tabs will be added once the recordings for *this* batch exist — the
August and September playlists both end at D29 Pillars of OOPs, so there is nothing to
build them from yet. The July B2 NumPy/pandas recordings are a different batch with
different examples and are deliberately not used here.
