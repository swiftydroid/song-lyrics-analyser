import lyricsgenius
from properties import GENIUS_API_TOKEN, ARTIST_NAME, SEARCH_MAX_SONGS, SONGS_FILENAME


def get_lyrics():
    genius = lyricsgenius.Genius(GENIUS_API_TOKEN, remove_section_headers=True)

    artist = genius.search_artist(ARTIST_NAME, max_songs=SEARCH_MAX_SONGS)
    artist.save_lyrics(filename=SONGS_FILENAME, overwrite=True)
