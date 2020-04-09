from fpdf import FPDF
import os
import sys

pdffiles = [];

for filename in os.listdir(os.getcwd()):
	if filename.endswith('.pdf') & (not (filename.endswith('opraveno.pdf'))):
		s = '';
		for c in filename:
			if c == '.':
				break;
			
			s += c
		
		pdffiles.append(s)
		
		
pdffiles.sort()

for filename in pdffiles:
	pdf = FPDF()
	
	pdf.add_page()
	pdf.add_font('FreeSans', '', 'FreeSans.ttf', True)
	pdf.set_font('FreeSans', size = 12)
	
	pdf.cell(195, 6, border = 0, txt = 'Opravoval: Pavel Hudec', ln = 1, align = 'L')
	pdf.image('prasatko.png', 175 , 5, 80, 0)
	pdf.cell(195, 15, border = 'B', txt = '', ln = 1, align = 'L')
	while True:
		t = unicode(raw_input(), 'utf8')
		if t == '|':
			break
		
		pdf.multi_cell(0, 6, txt = t, align = 'L')
		
		
	pdf.output(filename + '_opraveno.pdf')
