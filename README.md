# Hromadný generátor pdfek z jednoho poznámkového souboru

Skript generuje pdfka ve formátu vhodném k vložení na server s poznámkami z jednoho textového souboru s poznámkami.

- Před použitím
	1. Zkontrolujte si, že máte Linux. Negarantuji funkčnost na Windowsech.
	2. Zkontrolujte, zda máte nainstalovaný Python 2, který můžete spustit v libovolné složce (napište python do terminálu). V něm budete potřebovat package fpdf, kterou naistalujete pomocí
	
			pip install fpdf

- Použití
	1. Vytvořte složku na jednu úlohu, do ní stáhněte všechna řešení a zkopírujte skript pdfgen.py.
	2. Vytvořte textový soubor pozn.txt, setřiďte řešení vzestupně podle názvu, projděte je a takto postupně napište do pozn.txt jména všech řešitelů, oddělená znakem ***|*** v samostatném odstavci (jako v TeXu).
	3. Napište poznámky standardními TeXovými odstavci tak, aby byli řešitelé pořád odděleni **|** v samostatném odstavci.
	4. Když jste hotovi, vygenerujte pdf příkazem
	
			python pdfgen.py < pozn.txt
		
	Pak už stačí jen nahrát na gimliho.
