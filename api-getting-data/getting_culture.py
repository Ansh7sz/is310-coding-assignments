import json
import requests
import os


# Requires RAWG_KEY and EUROPEANA_KEY in your environment


EUROPEANA_API_KEY = os.getenv("EUROPEANA_API_KEY")
RAWG_API_KEY = os.getenv("RAWG_API_KEY")

if not EUROPEANA_API_KEY or not RAWG_API_KEY:
    raise ValueError("Missing API keys. Set EUROPEANA_API_KEY and RAWG_API_KEY first.")

search_term = "Valorant"

rawg_search_url = "https://api.rawg.io/api/games"
rawg_search_params = {
    "key": RAWG_API_KEY,
    "search": search_term,
    "search_precise": True,
    "page_size": 1
}

rawg_response = requests.get(rawg_search_url, params=rawg_search_params)
print("RAWG search status:", rawg_response.status_code)

rawg_data = rawg_response.json()
print("RAWG SEARCH RESPONSE:")
print(json.dumps(rawg_data, indent=2))

chosen_game = rawg_data["results"][0]
game_name = chosen_game["name"]
game_id = chosen_game["id"]

print("Chosen game:", game_name)

detail_url = f"https://api.rawg.io/api/games/{game_id}"
detail_params = {
    "key": RAWG_API_KEY
}

detail_response = requests.get(detail_url, params=detail_params)
print("RAWG detail status:", detail_response.status_code)

detail_data = detail_response.json()
print("RAWG DETAIL RESPONSE:")
print(json.dumps(detail_data, indent=2))

euro_url = "https://api.europeana.eu/record/v2/search.json"
euro_params = {
    "wskey": EUROPEANA_API_KEY,
    "query": game_name,
    "rows": 5
}

euro_response = requests.get(euro_url, params=euro_params)
print("Europeana status:", euro_response.status_code)

euro_data = euro_response.json()
print("EUROPEANA RESPONSE:")
print(json.dumps(euro_data, indent=2))

items = euro_data.get("items", [])

clean_items = []
for item in items:
    clean_item = {
        "id": item.get("id"),
        "title": item.get("title"),
        "type": item.get("type"),
        "dataProvider": item.get("dataProvider"),
        "country": item.get("country"),
        "rights": item.get("rights"),
        "edmPreview": item.get("edmPreview")
    }
    clean_items.append(clean_item)

output_data = {
    "selected_api": "rawg",
    "search_term": search_term,
    "rawg_item": {
        "id": detail_data.get("id"),
        "name": detail_data.get("name"),
        "released": detail_data.get("released"),
        "rating": detail_data.get("rating"),
        "metacritic": detail_data.get("metacritic"),
        "genres": [genre["name"] for genre in detail_data.get("genres", [])],
        "platforms": [
            platform["platform"]["name"]
            for platform in detail_data.get("platforms", [])
        ]
    },
    "europeana_items": clean_items
}

with open("rawg_valorant_culture.json", "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=4, ensure_ascii=False)

print("Saved to rawg_valorant_culture.json")