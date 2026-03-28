#!/usr/bin/env python3
"""regex_test - Test and explain regex patterns."""
import sys, re, json

def test(pattern, text, flags=0):
    try:
        matches = list(re.finditer(pattern, text, flags))
    except re.error as e:
        return {'error': str(e)}
    results = []
    for m in matches:
        r = {'match': m.group(), 'start': m.start(), 'end': m.end(), 'groups': {}}
        for i, g in enumerate(m.groups(), 1):
            r['groups'][i] = g
        for name, val in m.groupdict().items():
            r['groups'][name] = val
        results.append(r)
    return {'pattern': pattern, 'matches': len(results), 'results': results}

def highlight(pattern, text, flags=0):
    last = 0; out = ''
    for m in re.finditer(pattern, text, flags):
        out += text[last:m.start()] + f'\033[31;1m{m.group()}\033[0m'
        last = m.end()
    out += text[last:]
    return out

def main():
    args = sys.argv[1:]
    if len(args) < 2 or '-h' in args:
        print("Usage: regex_test.py PATTERN TEXT [--json] [--file]\n  regex_test.py '\\d+' 'abc 123 def 456'"); return
    pattern = args[0]
    if '--file' in args:
        text = open(args[1]).read()
    else:
        text = args[1]
    flags = re.IGNORECASE if '-i' in args else 0
    if '--json' in args:
        print(json.dumps(test(pattern, text, flags), indent=2))
    else:
        result = test(pattern, text, flags)
        if 'error' in result: print(f"  ❌ {result['error']}"); return
        print(f"  Pattern: {pattern}")
        print(f"  Matches: {result['matches']}")
        print(f"  Highlighted: {highlight(pattern, text, flags)}")
        for r in result['results']:
            print(f"  [{r['start']}:{r['end']}] '{r['match']}'", end='')
            if r['groups']: print(f" groups={r['groups']}", end='')
            print()

if __name__ == '__main__': main()
