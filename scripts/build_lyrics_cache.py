"""Build a unique, verified song cache from Genius via LyricsGenius.

Usage:
  GENIUS_ACCESS_TOKEN=... python3 scripts/build_lyrics_cache.py

The token is read from the environment and is never written to the project.
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

try:
    import lyricsgenius
except ImportError:
    raise SystemExit("Install the dependency first: python3 -m pip install lyricsgenius")

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "songs-cache.json"
ARTISTS = [
    ("Taylor Swift", 70),
    ("Olivia Rodrigo", 30),
    ("Gracie Abrams", 30),
    ("Noah Kahan", 30),
    ("Sabrina Carpenter", 30),
    ("Chappell Roan", 20),
]

def clean_lyrics(text: str) -> str:
    text = re.sub(r"\[.*?\]", "", text or "")
    return re.sub(r"\s+", " ", text).strip()

def main() -> None:
    token = os.environ.get("GENIUS_ACCESS_TOKEN")
    if not token:
        raise SystemExit("Missing GENIUS_ACCESS_TOKEN")
    genius = lyricsgenius.Genius(token, skip_non_songs=True, remove_section_headers=True, verbose=False)
    genius.timeout = 15
    seen: set[tuple[str, str]] = set()
    songs: list[dict] = []
    for artist_name, limit in ARTISTS:
        artist = genius.search_artist(artist_name, max_songs=limit, sort="popularity")
        if not artist:
            continue
        for song in artist.songs:
            key = (artist_name.casefold(), song.title.casefold())
            if key in seen:
                continue
            lyric_text = clean_lyrics(song.lyrics)
            if not lyric_text:
                continue
            seen.add(key)
            songs.append({
                "artist": artist_name,
                "song": song.title,
                "album": song.album or "",
                "lyrics": lyric_text,
                "geniusUrl": song.url,
                "source": "LyricsGenius / Genius",
            })
    if len(songs) < 365:
        raise SystemExit(f"Only collected {len(songs)} unique songs; add more artists or raise limits.")
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(songs, ensure_ascii=False, indent=2) + "\n")
    print(f"Wrote {len(songs)} unique songs to {OUT}")

if __name__ == "__main__":
    main()
