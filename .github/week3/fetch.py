# /// script
# requires-python = ">=3.10"
# dependencies = ["requests"]
# ///

from pathlib import Path
import requests


URL = "https://raw.githubusercontent.com/meesvandongen/anime-dataset/main/data/anime.csv"

HERE = Path(__file__).parent
FILE = HERE / "data" / "anime.csv"


if FILE.exists():
    print("Data already exists:", FILE)
else:
    print("Downloading data...")

    response = requests.get(
        URL,
        headers={"User-Agent": "student-data-visualisation-project"},
        timeout=30,
    )

    response.raise_for_status()

    FILE.parent.mkdir(exist_ok=True)
    FILE.write_bytes(response.content)

    print("Saved:", FILE)