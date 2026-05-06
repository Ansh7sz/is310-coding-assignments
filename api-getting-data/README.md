## Getting Culture Data from APIs

This project uses the following APIs:

- [RAWG](https://rawg.io/)
- [Europeana](https://www.europeana.eu/)

With a focus on a specifc game, which in this case was "Valorant", I used the APIs to gather data on the game and it's cultural significance.

At first I wasn't sure why most of the results appeared from spanish institutions, but upon further exploring I realized that this is normal because Europeana aggregates multilingual metadata from a wide range of institutions. Some of the institutions include:

- "Polytechnic University of Valencia"
- "Digital Memory of Catalonia"

## API Keys

This script requires two API keys stored locally as environment variables:

- `RAWG_API_KEY`
- `EUROPEANA_API_KEY`
