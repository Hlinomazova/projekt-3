import sys
import csv
import requests
from bs4 import BeautifulSoup

def get_soup(url: str):
    """Stáhne obsah stránky a vytvoří BeautifulSoup objekt."""
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=header)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except Exception as e:
        print(f"Chyba při stahování dat: {e}")
        return None

def get_town_data(town_url: str) -> list:
    """Extrahuje statisti stran z detailu konkrétní obce."""
    soup = get_soup(town_url)
    if not soup:
        return []

    # Atributy 'headers' odpovídají ID buněk v tabulce na webu volby.cz
    registered = soup.find("td", {"headers": "sa2"}).text.replace('\xa0', '')
    envelopes = soup.find("td", {"headers": "sa3"}).text.replace('\xa0', '')
    valid = soup.find("td", {"headers": "sa6"}).text.replace('\xa0', '')
    
    results = [registered, envelopes, valid]
    
    # Extrahuje data z buněk, které obsahují počty hlasů pro jednotlivé strany.
    party_votes = soup.find_all("td", {"class": "cislo", "headers": ["t1sa2", "t1sb3", "t2sa2", "t2sb3"]})
    
    for vote in party_votes:
        results.append(vote.text.replace('\xa0', ''))
        
    return results

def get_party_names(town_url: str) -> list:
    """Vytáhne názvy politických stran z detailu obce pro hlavičku CSV."""
    soup = get_soup(town_url)
    if not soup:
        return []
    
    party_names = soup.find_all("td", {"class": "overflow_name"})
    return [name.text for name in party_names]

def main():
    # Kontrola vstupních argumentů
    if len(sys.argv) != 3:
        print("Chyba: špatný počet argumentů!")
        print("Použití: python main.py <URL_adresa> <název_souboru>")
        sys.exit(1)

    url = sys.argv[1]
    output_file = sys.argv[2]
    
    # Dynamické určení základní URL pro spojování odkazů
    base_url = url[:url.rfind('/') + 1]

    print(f"Stahuji data z adresy: {url}")
    soup = get_soup(url)
    
    if not soup:
        return

    # Najde všechny řádky v hlavní tabulce okresu
    rows = soup.find_all("tr")
    
    with open(output_file, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        header_written = False

        for row in rows:
            cells = row.find_all("td")
            
            # Identifikuje obce podle toho, zda první buňka obsahuje kód (číslo)
            if len(cells) > 2 and cells[0].text.strip().isdigit():
                town_code = cells[0].text.strip()
                town_name = cells[1].text.strip()
                
                link = cells[0].find("a")
                if not link:
                    continue
                
                full_town_url = base_url + link.get("href")
                town_data = get_town_data(full_town_url)

                #  Generuje hlavičku CSV souboru při zpracování první nalezené obce
                if not header_written:
                    parties = get_party_names(full_town_url)
                    header = ["code", "location", "registered", "envelopes", "valid"] + parties
                    writer.writerow(header)
                    header_written = True
                
                writer.writerow([town_code, town_name] + town_data)
                print(f"Zpracovávám obec: {town_name}")

    print("-" * 30)
    print(f"Hotovo! Data uložena do: {output_file}")

if __name__ == "__main__":
    main()
