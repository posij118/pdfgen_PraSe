from fpdf import FPDF
import os
import sys

pdffiles = [];

for filename in os.listdir(os.getcwd()):
	if filename.endswith(".pdf") & (not (filename.endswith("opraveno.pdf"))):
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
	pdf.set_font("Arial", size = 12)
	cnt = 1
	
	while True:
		t = raw_input()
		if t == '|':
			break
		
		pdf.cell(200, 5, txt = t, ln = cnt, align = 'L')
		cnt = cnt + 1
		
	pdf.output(filename + "_opraveno.pdf")
	

		
