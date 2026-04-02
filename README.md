# Election Scraper

Tento skript slouží k automatizovanému stahování výsledků voleb do Poslanecké sněmovny z roku 2017 z webu [volby.cz](https://www.volby.cz/). Projekt byl vytvořen jako závěrečná práce pro **Python Akademii od Engeta**.

---

## Popis projektu
Program umožňuje uživateli zvolit si konkrétní územní celek (okres) a pro něj vygenerovat ucelený přehled výsledků ve formátu `.csv`. Data jsou sbírána přímo z HTML kódu stránek pomocí knihovny `BeautifulSoup`.

**Výstupní soubor obsahuje:**
* **Identifikaci:** Kód a název obce.
* **Statistiku:** Počet registrovaných voličů, vydané obálky a platné hlasy.
* **Výsledky:** Počty hlasů pro každou kandidující politickou stranu.

---

## Požadavky a instalace
Pro spuštění projektu je vyžadován **Python 3**. Před prvním spuštěním je nutné nainstalovat externí knihovny definované v souboru `requirements.txt`.

**Postup instalace:**
1. Stáhni si tento repozitář nebo zkopíruj soubory do své lokální složky.
2. Otevři terminál (příkazový řádek) v dané složce.
3. Nainstaluj potřebné balíčky příkazem:
   ```bash
   pip install -r requirements.txt
