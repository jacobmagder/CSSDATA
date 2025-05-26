import json
import os
from datetime import date

# Paths to individual data files
data_dir = os.path.join(os.path.dirname(__file__), 'data', 'individual_files')
files = [
    ('atRules', 'at-rules.json'),
    ('functions', 'functions.json'),
    ('properties', 'properties.json'),
    ('selectors', 'selectors.json'),
    ('syntaxes', 'syntaxes.json'),
    ('types', 'types.json'),
    ('units', 'units.json'),
]

merged = {
    "meta": {
        "version": "1.0.0",
        "generated": str(date.today()),
        "description": "Merged CSS data including at-rules, functions, properties, selectors, syntaxes, types, and units."
    }
}

for key, filename in files:
    path = os.path.join(data_dir, filename)
    with open(path, 'r', encoding='utf-8') as f:
        merged[key] = json.load(f)

with open('cssdata-merged.json', 'w', encoding='utf-8') as f:
    json.dump(merged, f, indent=2, ensure_ascii=False)
