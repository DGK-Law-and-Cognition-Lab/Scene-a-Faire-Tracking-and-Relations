#!/usr/bin/env python3
"""Make the Word reference document for the Study 3 design memo: Times New Roman 12, 1.5 line spacing, justified body,
US Letter with one-inch margins. Usage: python3 make_reference.py reference_default.docx reference.docx"""
import sys
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
src, dst = sys.argv[1:3]
doc = Document(src)
def font(style, size, bold=None, italic=None):
    f = style.font; f.name = 'Times New Roman'; f.size = Pt(size); f.color.rgb = RGBColor(0, 0, 0)
    if bold is not None: f.bold = bold
    if italic is not None: f.italic = italic
    rpr = style.element.get_or_add_rPr(); rf = rpr.find(qn('w:rFonts'))
    if rf is None:
        rf = rpr.makeelement(qn('w:rFonts'), {}); rpr.append(rf)
    for a in ('w:ascii', 'w:hAnsi', 'w:eastAsia', 'w:cs'):
        rf.set(qn(a), 'Times New Roman')
    for a in ('w:asciiTheme', 'w:hAnsiTheme', 'w:eastAsiaTheme', 'w:cstheme'):
        if rf.get(qn(a)) is not None: del rf.attrib[qn(a)]
names = {s.name: s for s in doc.styles}
for n in ('Normal', 'Body Text', 'First Paragraph'):
    s = names[n]; font(s, 12); pf = s.paragraph_format
    pf.line_spacing = 1.5; pf.space_before = Pt(0); pf.space_after = Pt(8)
    if n != 'Normal': pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
for n in ('Compact',):
    s = names[n]; font(s, 10); s.paragraph_format.line_spacing = 1.0; s.paragraph_format.space_after = Pt(0); s.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
for n, size, before in (('Heading 1', 14, 18), ('Heading 2', 12, 12), ('Heading 3', 12, 10)):
    s = names[n]; font(s, size, bold=True, italic=(n == 'Heading 3')); pf = s.paragraph_format
    pf.space_before = Pt(before); pf.space_after = Pt(6); pf.keep_with_next = True; pf.line_spacing = 1.0; pf.alignment = WD_ALIGN_PARAGRAPH.LEFT
for n, size in (('Title', 16), ('Subtitle', 13), ('Author', 12), ('Date', 12)):
    if n in names:
        s = names[n]; font(s, size, bold=(n == 'Title')); s.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER; s.paragraph_format.line_spacing = 1.15
for n in ('Table Caption', 'Image Caption', 'Caption', 'Captioned Figure', 'Block Text', 'Footnote Text'):
    if n in names:
        s = names[n]; font(s, 10, italic=False); s.paragraph_format.line_spacing = 1.0; s.paragraph_format.space_after = Pt(8); s.paragraph_format.keep_with_next = (n == 'Table Caption')
sec = doc.sections[0]
sec.page_width = Inches(8.5); sec.page_height = Inches(11)
sec.left_margin = sec.right_margin = sec.top_margin = sec.bottom_margin = Inches(1)
sec.header_distance = sec.footer_distance = Inches(0.5); sec.gutter = Inches(0)
doc.save(dst)
print('wrote', dst)
