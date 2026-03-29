#!/usr/bin/env python3
"""regex_test - Regex testing tool."""
import sys, argparse, json, re

def test_regex(pattern, text, flags=0):
    matches = []
    for m in re.finditer(pattern, text, flags):
        match = {"match": m.group(), "start": m.start(), "end": m.end(), "groups": list(m.groups())}
        if m.groupdict(): match["named"] = m.groupdict()
        matches.append(match)
    return matches

def main():
    p = argparse.ArgumentParser(description="Regex tester")
    p.add_argument("pattern")
    p.add_argument("text", help="Text or @filename")
    p.add_argument("-i", "--ignorecase", action="store_true")
    p.add_argument("-m", "--multiline", action="store_true")
    p.add_argument("--replace", help="Replacement string")
    args = p.parse_args()
    text = args.text
    if text.startswith("@"):
        with open(text[1:]) as f: text = f.read()
    flags = 0
    if args.ignorecase: flags |= re.IGNORECASE
    if args.multiline: flags |= re.MULTILINE
    if args.replace:
        result = re.sub(args.pattern, args.replace, text, flags=flags)
        print(json.dumps({"pattern": args.pattern, "replacement": args.replace, "result": result}))
    else:
        matches = test_regex(args.pattern, text, flags)
        print(json.dumps({"pattern": args.pattern, "total_matches": len(matches), "matches": matches}, indent=2))

if __name__ == "__main__": main()
