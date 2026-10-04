# Process

## Initial Idea

I wanted to explore a topic related to anime because it is an area I am familiar with.

My original question was:

> Do longer anime series receive higher audience ratings?

I decided to compare two numerical variables:

- number of episodes
- audience score

A scatter plot seemed suitable because it allows each anime to appear as one observation and makes it possible to examine whether the two variables have a visible relationship.

## Finding the Data

I used a public anime dataset based on MyAnimeList information.

The dataset includes the fields I needed:

- title
- media type
- airing status
- number of episodes
- audience score

I saved the raw CSV file in the `data/` folder so the project can be run again without downloading the data every time.

## First Version

In my first version, I included all completed TV anime with valid episode counts and scores.

The code successfully produced a scatter plot, but the result was difficult to read.

A small number of extremely long-running anime had several hundred or even more than two thousand episodes. These values stretched the x-axis.

As a result, most anime were compressed into a narrow area on the left side of the graph.

## What I Rejected

I rejected the first version of the visualisation because the full episode range made the main distribution difficult to see.

I also considered keeping every anime and using the original x-axis, but this made the picture less useful for comparing most TV anime.

## What I Kept

I kept the scatter plot because it clearly represents the relationship between two numerical variables.

I also kept the filters for:

- TV anime
- completed series
- valid episode counts
- valid audience scores

These filters make the dataset more consistent.

## Final Design Decision

For the final version, I limited the dataset to anime with 100 episodes or fewer.

This made the main distribution much easier to see.

The final research question became:

> Is there a relationship between episode count and audience score among completed TV anime with 100 episodes or fewer?

The x-axis represents episode count and the y-axis represents audience score.

Each point represents one anime.

## Result

The final visualisation does not show a simple relationship where more episodes lead to a higher audience score.

Anime with similar episode counts can have very different scores.

The picture suggests that episode count alone is not a strong explanation for audience rating.

## Limitations

The visualisation only compares episode count and score.

It does not include other factors that may influence audience ratings, such as:

- genre
- release year
- popularity
- studio
- review count
- source material

The decision to exclude anime with more than 100 episodes also means that very long-running anime are not represented in the final visualisation.

This was a trade-off between completeness and readability.