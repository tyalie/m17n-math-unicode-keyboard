#!/usr/bin/env python3

import math_map as m
from string import Template

dic = {
        "title": "Math: Latex",
        "description": "Improved math latex input from unicodeit",
        "name": "math-latex-improved",
        "mapping": None
}

map_template = Template('    ("${src}"   "${to}")')


with open("template.mim", "r") as f:
    template = Template(f.read())

map_strings = []

equals = 0

for s, t in m.REPLACEMENTS:
    s = s.lstrip("\\")
    if s == t or t.strip() == "":
        equals += 1
        continue
    map_strings.append(map_template.substitute(src=s, to=t))

print(f"Mapped {len(map_strings)} symbols, skipped {equals}")

dic["mapping"] = "\n".join(map_strings)

result = template.substitute(dic)

with open(f"{dic['name']}.mim", "w") as f:
    f.write(result)
