# Projekt 3: Election Scraper

Tento projekt vznikl jako **třetí projekt** v rámci kurzu **Datový analytik s Pythonem**. Skript slouží ke sběru dat (scrapingu) výsledků voleb do Poslanecké sněmovny z roku 2017 z oficiálního webu [volby.cz](https://www.volby.cz/).

---

## 📝 Popis projektu
Cílem projektu je vytvořit nástroj, který pro zvolený územní celek (okres) extrahuje výsledky voleb a uloží je do formátu `.csv`. Program automaticky prochází odkazy pro jednotlivé obce, sbírá údaje o volební účasti a počty hlasů pro všechny kandidující politické strany.

**Výstupní soubor obsahuje:**
* **Kód obce** a **Název obce**.
* **Počet voličů** v seznamu (registered).
* **Vydané obálky** (envelopes) a **Platné hlasy** (valid).
* **Počty hlasů** pro každou politickou stranu.

---

## ⚙️ Instalace a požadavky
Ke spuštění projektu je vyžadován **Python 3**. Před prvním spuštěním je nutné nainstalovat externí knihovny definované v souboru `requirements.txt`.

**Postup instalace:**

1. **Stažení projektu:**
   Uložte soubory `main.py` a `requirements.txt` do své pracovní složky.

2. **Instalace knihoven:**
   Otevřete terminál v dané složce a nainstalujte requirements pomocí správce balíčků `pip`:
   ```bash
   pip install -r requirements.txt
````

-----

## 🚀 Spuštění projektu

Skript vyžaduje dva povinné argumenty zadané při spuštění v příkazové řádce:

1.  **URL** – odkaz na vybraný územní celek (výběr obce).
2.  **Název souboru** – jméno výstupního souboru s příponou `.csv`.

### Příklad spuštění (pro okres Benešov):

```bash
python main.py "[https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101](https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101)" vysledky_benesov.csv
```

-----

## 📊 Ukázka průběhu a výsledků

### Průběh v terminálu:

Během stahování program informuje o aktuálně zpracovávané obci:

> **Stahuji data z adresy:** https://www.google.com/search?q=https://www.volby.cz/pls/ps2017nss/ps32...  
> **Zpracovávám obec:** Benešov  
> **Zpracovávám obec:** Bystřice  
> ...  
> **Hotovo\! Data uložena do:** vysledky\_benesov.csv

### Ukázka výsledných dat v CSV:

Výstupní soubor je strukturován tak, aby byl snadno analyzovatelný v Excelu nebo v knihovně Pandas:

| code | location | registered | envelopes | valid | ODS | ANO | ... |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 529303 | Benešov | 13180 | 8345 | 8272 | 1083 | 2150 | ... |
| 529451 | Bystřice | 3445 | 2276 | 2261 | 240 | 680 | ... |
