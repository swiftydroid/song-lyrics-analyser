# song-lyrics-analyser

Retrieve songs lyrics from [Genius](https://genius.com/) and display the words frequency used in the lyrics as a WordCloud.

## Requirements

You need to register for a Genius API token over [here](https://docs.genius.com/#/getting-started-h1).

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

- `GENIUS_API_TOKEN`: The Genius API token
- `ARTIST_NAME`: The primary artist name of the songs lyrics
- `SEARCH_MAX_SONGS`: Maximum number of songs to retrieved. Currently, songs tagged with "Version", "Remix" and "Live"
  are skipped. You can cater for your needs in get_lyrics.py.
- `SONGS_FILENAME`: The song lyrics are saved in this filename. By default, the filename is `ARTIST_NAME`.json.

### additional_stopwords.py

You can use stopwords from `nltk` to prevent useless words from displaying in the Wordcloud. Depending on your case,
sometimes you need to add more words to the stopwords. In this case, you can add them to `additional_stopwords.py`.