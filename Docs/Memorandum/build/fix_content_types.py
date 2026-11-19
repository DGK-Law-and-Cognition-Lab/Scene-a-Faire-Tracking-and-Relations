#!/usr/bin/env python3
"""Declare PNG as a default content type in a .docx (pandoc declares each image separately, which Word accepts; some checkers want the default).
Usage: python3 fix_content_types.py file.docx"""
import sys, zipfile, shutil, tempfile, os
path = sys.argv[1]; tmp = tempfile.mktemp(suffix='.docx')
with zipfile.ZipFile(path) as zin, zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zout:
    for item in zin.infolist():
        if item.filename.endswith('/'):
            continue
        data = zin.read(item.filename)
        if item.filename == '[Content_Types].xml' and b'Extension="png"' not in data:
            data = data.replace(b'<Default Extension="xml"', b'<Default Extension="png" ContentType="image/png" /><Default Extension="xml"', 1)
        zout.writestr(item, data)
shutil.move(tmp, path); print('content types checked:', os.path.basename(path))
