import json
import matplotlib.pyplot as wc_plt
import re
from properties import SONGS_FILENAME
from google_trans_new import google_translator
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from additional_stopwords import additional_stopwords
from wordcloud import WordCloud


def clean_text(text):
    all_stopwords = stopwords.words('english')
    all_stopwords.extend(additional_stopwords)

    text = ' '.join(text).lower().replace('—', ' ').replace('-', ' ')

    # remove all punctuation except for apostrophe since we can have words like 'cause, fallin' etc
    text = re.sub(r"[^\w\d'\s]+", '', text)

    # remove all numbers
    text = re.sub(r'[0-9]', '', text)

    # remove all stop words
    text = word_tokenize(text)
    text_tokens_without_sw = [word for word in text if word not in all_stopwords]

    # join the tokens into a long string before passing to WordCloud
    text = ' '.join(text_tokens_without_sw)

    return text


def generate_wordcloud():
    lyrics_org = []
    lyrics_translated = []

    with open(SONGS_FILENAME) as fp:
        data = json.load(fp)

        for song in data['songs']:
            lyrics_org.append(song['lyrics'])

    translator = google_translator()
    for lyrics in lyrics_org:
        translated_lyrics = translator.translate(lyrics, lang_tgt='en')
        lyrics_translated.append(translated_lyrics)

    lyrics_translated = clean_text(lyrics_translated)

    wc = WordCloud(max_words=1000000, max_font_size=50, collocations=False).generate(lyrics_translated)
    wc_plt.figure()
    wc_plt.imshow(wc, interpolation='bilinear')
    wc_plt.axis('off')
    wc_plt.show()
