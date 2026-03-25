# Web Scraping – Fandom Wiki (Teamfight Tactics)

## Fandom wiki choice

For this assignment I chose the Teamfight Tactics (TFT) content on the League of Legends Fandom Wiki. Since TFT differs a lot depending on the set, I chose to scrape the [Set 11 base statistics page] so i can focus on a single set. I also wanted to keep the data as simple and clean as possible.


- TFT Set 11 base stats page: https://leagueoflegends.fandom.com/wiki/List_of_champions_(Teamfight_Tactics)/Base_statistics/Set_11

This page contains a structured table of TFT champions in Set 11 along with their numeric base statistics (such as health, attack damage, attack speed, range, armor, and magic resist).

## Why this data is interesting for research

Champion base statistics are useful for studying how game designers balance units in an auto‑battler like TFT. Because each champion has a cost and a set of base stats, researchers can:

- Analyze how stats scale with cost (for example, if higher‑cost units always have strictly better stats or if there are trade‑offs).
- Look for outliers where a champion seems over‑ or under‑tuned relative to others at the same cost.
- Compare distributions of stats across roles or archetypes (frontline vs. backline, melee vs. ranged).

More broadly, this kind of dataset can support questions about **game balance, complexity, and design trends** within one TFT set and across sets if combined with other pages.

## Robots.txt / bot and scraping policy

Before scraping, I checked the relevant robots and bot policy information:

- League of Legends Wiki robots / bot info :  
  https://leagueoflegends.fandom.com/robots.txt


## Script description


1. Uses the `cloudscraper` library to fetch the HTML of the TFT Set 11 base statistics page.[web:30][web:54]  
2. Uses `BeautifulSoup` (from `bs4`) to parse the page and locate the first main table that contains the champion base stats.[web:30][web:54]  
3. Iterates over each row of the table to extract:

   - Champion name  
   - Cost  
   - Health (HP)  
   - Attack damage (AD)  
   - Attack speed  
   - Range  
   - Armor  
   - Magic resist  

4. Stores each champion as a Python dictionary and collects all of them in a list.  
5. Saves the resulting data to a JSON file called `tft_set11_base_stats.json` in the **same folder** as the script using a path based on `__file__` so the output is colocated with the code.

## Output data

The script produces the following interoperable data file in the `web-scraping` directory:

- `tft_set11_base_stats.json`  
  - Format: JSON array of objects.  
  - Each object represents one TFT champion in Set 11 with fields for name, cost, and base stats (HP, AD, attack speed, range, armor, magic resist).

This format can be easily loaded into Python, R, or other tools for further analysis of TFT balance and champion design.
