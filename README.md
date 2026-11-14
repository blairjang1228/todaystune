# today's tune

A small static music-fan site for a daily lyric moment from Taylor Swift, Olivia Rodrigo, Gracie Abrams, Noah Kahan, Sabrina Carpenter, and Sienna Spiro.

## Run locally

Open `index.html` in a browser, or serve this folder with any static server. There are no build steps or package dependencies, so it can be published directly with GitHub Pages.

## Project notes

- `index.html` contains the semantic page structure and accessibility labels.
- `styles.css` contains the responsive layout and requested palette: `#7b435b`, `#90c3c8`, `#3d5a6c`, `#cab6cd`, `#2b4162`, and `#ffcad4`.
- `script.js` contains cached lyric data and the tune shuffle/save interactions.
- The display uses Special Elite for the typewriter-style heading and lyric treatment, with DM Sans for supporting text. The supplied Olivia Rodrigo font can be added later as a local `@font-face` asset if licensing permits.

## Lyrics repository

The production cache is generated with `scripts/build_lyrics_cache.py` using the LyricsGenius API. Set `GENIUS_ACCESS_TOKEN` in your local shell, run the script, and it writes unique entries to `data/songs-cache.json`. Never commit the token. A static GitHub Pages site should expose only permitted short excerpts, not full lyric text.

## Prompt log

Created from Blair's workspace brief: build a static “song lyrics of the day” site for the six listed artists, use the specified Coolors palette, use a display font plus a readable text font, include artist information, song links, and a tour-information-ready layout, and maintain a README for GitHub Pages.
