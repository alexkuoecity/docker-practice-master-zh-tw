#!/usr/bin/env python3
"""Translate docker_practice from Simplified Chinese to Taiwan Traditional Chinese."""

import os
import re
from opencc import OpenCC

cc = OpenCC('s2twp')

# Post-conversion fixes for Docker/IT terminology
POST_FIXES = [
    ('映象', '映像檔'),
    ('從入門到實踐', '從入門到實戰'),
]

def translate_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by code blocks to preserve code formatting
    parts = re.split(r'(```[\s\S]*?```)', content)
    
    translated_parts = []
    for part in parts:
        if part.startswith('```'):
            # Code block - translate comments but preserve commands
            translated_parts.append(cc.convert(part))
        else:
            # Regular text - full conversion
            converted = cc.convert(part)
            for old, new in POST_FIXES:
                converted = converted.replace(old, new)
            translated_parts.append(converted)
    
    result = ''.join(translated_parts)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(result)


def main():
    count = 0
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', '.vuepress']]
        for fname in files:
            if fname.endswith('.md'):
                fpath = os.path.join(root, fname)
                translate_file(fpath)
                count += 1
                if count % 20 == 0:
                    print(f'  Processed {count} files...')
    
    print(f'Translated {count} Markdown files')


if __name__ == '__main__':
    main()
