# song-lyrics-analyser

Retrieve songs lyrics from [Genius](https://genius.com/) and display the words frequency used in the lyrics as a WordCloud.

## Requirements

- Python3

You need the following packages:

- lyricsgenius
- google_trans_new
- nltk
- wordcloud

## Run

```
python3 main.py
```

## Usage

### properties.py

Available properties:

- `GENIUS_API_TOKEN`: The Genius API token. You can register for the token over [here](https://docs.genius.com/#/getting-started-h1).
- `ARTIST_NAME`: The primary artist name of the songs lyrics
- `SEARCH_MAX_SONGS`: Maximum number of songs to retrieved. Currently, songs tagged with "Version", "Remix" and "Live" are skipped. You can cater for your needs in get_lyrics.py.
- `SONGS_FILENAME`: The song lyrics are saved in this filename. By default, the filename is `ARTIST_NAME`.json.
