#!/usr/bin/env python3

import math_map as m
import additional_math_map as am
from string import Template
import json

dic = {
        "title": "Math: Latex",
        "description": "Improved math latex input from unicodeit",
        "name": "math-latex-improved",
        "mapping": None
}

map_template = Template('    ("${src}"   "${to}")')


def escape(s: str):
    return json.dumps(s, ensure_ascii=False).strip('"')


with open("template.mim", "r") as f:
    template = Template(f.read())

map_strings = []

equals = 0

for os, t in (m.REPLACEMENTS + m.COMBININGMARKS + m.SUBSUPERSCRIPTS + am.CUSTOM_SYMBOLS):
    s = os.lstrip("\\")

    # commands with same output and with empty target
    if s == t or t.strip() == "":
        equals += 1
        continue

    s = escape(s)
    t = escape(t)

    map_strings.append(map_template.substitute(src=s, to=t))


print(f"Mapped {len(map_strings)} symbols, skipped {equals}")

dic["mapping"] = "\n".join(map_strings)

result = template.substitute(dic)

with open(f"{dic['name']}.mim", "w") as f:
    f.write(result)
