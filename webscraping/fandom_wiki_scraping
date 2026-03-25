import cloudscraper
from bs4 import BeautifulSoup
import json
import os

url = "https://leagueoflegends.fandom.com/wiki/List_of_champions_(Teamfight_Tactics)/Base_statistics/Set_11"

scraper = cloudscraper.create_scraper()
response = scraper.get(url)

print("Status code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
print("Page title:", soup.title.get_text(strip=True))

tables = soup.find_all("table")
if not tables:
    raise RuntimeError("No tables found on the page")
stats_table = tables[0]
rows = stats_table.find_all("tr")

tft_stats = []

for row in rows[1:]:
    cells = row.find_all(["td", "th"])
    if len(cells) >= 8:
        champion = cells[0].get_text(strip=True)
        cost = cells[1].get_text(strip=True)
        hp = cells[4].get_text(strip=True)
        ad = cells[6].get_text(strip=True)
        attack_speed = cells[7].get_text(strip=True)
        range_ = cells[12].get_text(strip=True)
        armor = cells[8].get_text(strip=True)
        magic_resist = cells[9].get_text(strip=True)

        entry = {
            "champion": champion,
            "cost": cost,
            "hp": hp,
            "ad": ad,
            "attack_speed": attack_speed,
            "range": range_,
            "armor": armor,
            "magic_resist": magic_resist
        }
        tft_stats.append(entry)

print(f"Scraped {len(tft_stats)} TFT champions with base stats.\n")

for champ in tft_stats[:10]:
    print(champ)


script_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(script_dir, "tft_set11_base_stats.json")

with open(out_path, "w", encoding="utf-8") as f:
    json.dump(tft_stats, f, ensure_ascii=False, indent=4)

print("\nSaved data to", out_path)
