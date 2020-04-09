# Hromadný generátor pdfek z jednoho poznámkového souboru

Skript generuje pdfka ve formátu vhodném k vložení na server s poznámkami z jednoho textového souboru s poznámkami.

- Před použitím
	1. Zkontrolujte si, že máte Linux. Negarantuji funkčnost na Windowsech.
	2. Zkontrolujte, zda máte nainstalovaný Python 2, který můžete spustit v libovolné složce (napište `python` do terminálu). V něm budete potřebovat package `fpdf`, kterou naistalujete pomocí
	
			pip install fpdf

	3. Knihovna `fpdf` defaultně nepodporuje češtinu. Nejprve si ze stránky `http://ftp.gnu.org/gnu/freefont/` stáhněte archiv `freefont-ttf-20120503.zip`.
	4. Rozbalte archiv a zkopírujte soubor `FreeSans.ttf` do složky `...../python2.x/site-packages/fpdf/font`, přičemž složku `font` musíte vytvořit. Pokud byste cílovou složku nemohli najít, pak funkční řešení je spustit pythoní program
	
			import sys
			print(sys.path)
			
	5. V kódu skriptu upravte jméno na svoje.
			
	
- Použití
	1. Vytvořte složku na jednu úlohu, do ní stáhněte všechna řešení a zkopírujte skript `pdfgen.py` a obrázek PraSátka. Zkontrolujte, že v té složce nejsou žádné jiné `.pdf` soubory.
	2. Vytvořte textový soubor `pozn.txt`, setřiďte řešení vzestupně podle názvu, projděte je a takto postupně napište do `pozn.txt` jména všech řešitelů, oddělená znakem ***|*** v samostatném odstavci (jako v TeXu). Soubor `pozn.txt` pak ukončete opět znakem ***|*** ve svém vlastním odstavci.
	3. Napište poznámky k dříve napsaným jménům standardními TeXovými odstavci tak, aby byli různí řešitelé pořád odděleni **|** v samostatném odstavci.
	4. Když jste hotovi, vygenerujte pdf příkazem
	
			python pdfgen.py < pozn.txt
		
	Pak už stačí jen nahrát na gimliho.
