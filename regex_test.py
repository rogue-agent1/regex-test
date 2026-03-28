#!/usr/bin/env python3
"""regex_test - Test and explain regex patterns."""
import sys,re
COMMON={"email":r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "ipv4":r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b",
    "url":r"https?://[\w.-]+(?:/[\w./-]*)?",
    "phone":r"[\+]?[\d\s()-]{7,15}",
    "date":r"\d{4}-\d{2}-\d{2}"}
def test_pattern(pattern,text,flags=0):
    matches=list(re.finditer(pattern,text,flags))
    return[{"match":m.group(),"start":m.start(),"end":m.end(),"groups":m.groups()} for m in matches]
def highlight(pattern,text):
    result="";last=0
    for m in re.finditer(pattern,text):
        result+=text[last:m.start()]+f"\033[31m{m.group()}\033[0m";last=m.end()
    return result+text[last:]
if __name__=="__main__":
    if len(sys.argv)<2:print("Patterns: "+", ".join(COMMON.keys()));sys.exit(1)
    pattern=COMMON.get(sys.argv[1],sys.argv[1])
    if len(sys.argv)>2:
        text=" ".join(sys.argv[2:]);matches=test_pattern(pattern,text)
        print(highlight(pattern,text));print(f"\n{len(matches)} matches:")
        for m in matches:print(f"  '{m['match']}' at [{m['start']}:{m['end']}]")
    else:print(f"Pattern: {pattern}")
