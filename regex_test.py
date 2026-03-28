#!/usr/bin/env python3
"""Regex tester — match, search, findall with group display."""
import sys, re
def cli():
    if len(sys.argv) < 3: print("Usage: regex_test <pattern> <text> [findall|match|sub REPL]"); sys.exit(1)
    pat, text = sys.argv[1], sys.argv[2]; cmd = sys.argv[3] if len(sys.argv)>3 else "findall"
    try:
        if cmd == "findall":
            for i, m in enumerate(re.finditer(pat, text)):
                print(f"  [{i}] '{m.group()}' at {m.start()}-{m.end()}")
                for j, g in enumerate(m.groups(), 1): print(f"      group {j}: '{g}'")
        elif cmd == "match":
            m = re.match(pat, text)
            print(f"  Match: {'Yes' if m else 'No'}")
            if m: print(f"  Matched: '{m.group()}'"); [print(f"  Group {i}: '{g}'") for i, g in enumerate(m.groups(), 1)]
        elif cmd == "sub": print(re.sub(pat, sys.argv[4], text))
    except re.error as e: print(f"  Error: {e}")
if __name__ == "__main__": cli()
