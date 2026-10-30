# -*- coding: utf-8 -*-
"""Takes the content tables, RUNS every snippet, captures the real stdout,
and writes <tab>.json. Nothing on the page is hand-copied output."""
import io, json, sys, contextlib, traceback, os, subprocess, tempfile

_HARNESS = (
 "import sys,json,io,contextlib\n"
 "import os,tempfile\n"
 "d=json.load(sys.stdin); buf=io.StringIO(); g={'__name__':'__main__'}\n"
 "os.chdir(tempfile.mkdtemp(prefix='sref-'))\n"
 "if d.get('stdin') is not None:\n"
 "    f=list(d['stdin'])\n"
 "    def _i(p=''):\n"
 "        v=f.pop(0); buf.write(str(p)+v+chr(10)); return v\n"
 "    g['input']=_i\n"
 "try:\n"
 "    with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):\n"
 "        exec(compile(d['code'],'<s>','exec'),g)\n"
 "except Exception as e:\n"
 "    buf.write(type(e).__name__+': '+str(e))\n"
 "sys.__stdout__.write(buf.getvalue())\n")

def run(code, stdin=None):
    """Execute a snippet in a fresh namespace and return its printed output.
    `stdin` is a list of lines fed to input(), which echoes them like a real
    terminal does, so the output looks exactly like the student's screen."""
    buf = io.StringIO()
    g = {"__name__": "__main__"}
    if stdin is not None:
        feed = list(stdin)
        def _input(prompt=""):
            val = feed.pop(0)
            buf.write(str(prompt) + val + "\n")
            return val
        g["input"] = _input
    here = os.getcwd()
    tmp = tempfile.mkdtemp(prefix="sref-")
    try:
        os.chdir(tmp)          # snippets that write files leave nothing behind
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
            exec(compile(code, "<snippet>", "exec"), g)
    except Exception as e:
        return buf.getvalue() + type(e).__name__ + ": " + str(e), True
    finally:
        os.chdir(here)
    return buf.getvalue(), False

def build(rows, outfile):
    done, failed, unstable = [], [], []
    for r in rows:
        out, err = run(r["code"], r.get("stdin"))
        out = out.rstrip("\n")
        # Run it a second time in a FRESH interpreter. Python randomises string
        # hashing per process, so printing a set or a set-derived dict gives a
        # different order each run - that output must never reach the page.
        chk = subprocess.run([sys.executable, "-c", _HARNESS],
                             input=json.dumps({"code": r["code"], "stdin": r.get("stdin")}),
                             capture_output=True, text=True)
        if chk.returncode == 0 and chk.stdout.rstrip("\n") != out:
            unstable.append(r["name"])
        # a row may declare that it is SUPPOSED to raise
        if err and not r.get("raises"):
            failed.append((r["name"], out.splitlines()[-1] if out else "?"))
        r = dict(r); r["out"] = out
        r.pop("raises", None); r.pop("stdin", None)
        done.append(r)
    if unstable:
        print("%-28s %d NON-DETERMINISTIC rows:" % (outfile, len(unstable)))
        for n in unstable: print("     -", n)
        return len(failed) + len(unstable)
    json.dump(done, io.open(outfile, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print("%-16s %3d rows" % (outfile, len(done)), end="")
    if failed:
        print("   %d UNEXPECTED FAILURES:" % len(failed))
        for n, m in failed: print("     -", n, "->", m)
    else:
        print("   all executed clean")
    return len(failed)
