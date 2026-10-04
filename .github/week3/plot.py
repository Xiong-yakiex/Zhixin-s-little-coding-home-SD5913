# /// script
# requires-python = ">=3.10"
# dependencies = ["pandas", "matplotlib"]
# ///

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


HERE = Path(__file__).parent
DATA = HERE / "data" / "anime.csv"
OUT = HERE / "out" / "anime-rating.png"


# Read data
df = pd.read_csv(DATA)

# Keep completed TV anime with valid episode counts and scores
df = df[
    (df["media_type"] == "tv")
    & (df["status"] == "finished_airing")
    & (df["num_episodes"].notna())
    & (df["mean"].notna())
]
plt.show()

# Remove invalid values and very long-running series
df = df[
    (df["num_episodes"] > 0)
    & (df["num_episodes"] <= 100)
    & (df["mean"] > 0)
]
# Remove impossible / unhelpful values
df = df[
    (df["num_episodes"] > 0)
    & (df["mean"] > 0)
]

print(df[["title", "num_episodes", "mean"]].head())
print("Anime used:", len(df))

# Draw
plt.figure(figsize=(9, 6))

plt.scatter(
    df["num_episodes"],
    df["mean"],
    alpha=0.35
)

plt.xlabel("Number of Episodes")
plt.ylabel("Audience Score")
plt.title("Episode Count vs Audience Score for Completed TV Anime")

plt.tight_layout()

# Save
OUT.parent.mkdir(exist_ok=True)
plt.savefig(OUT, dpi=150)

