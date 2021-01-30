import json
import matplotlib.pyplot as wc_plt
from properties import SONGS_FILENAME
from google_trans_new import google_translator
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from additional_stopwords import additional_stopwords
from wordcloud import WordCloud


def generate_wordcloud():
    lyrics_org = []
    lyrics_translated = []

    all_stopwords = stopwords.words('english')
    all_stopwords.extend(additional_stopwords)

    with open(SONGS_FILENAME) as fp:
        data = json.load(fp)

        for song in data['songs']:
            lyrics_org.append(song['lyrics'])

    translator = google_translator()
    for lyrics in lyrics_org:
        translated_lyrics = translator.translate(lyrics, lang_tgt='en')
        lyrics_translated.append(translated_lyrics)

    lyrics_translated = ' '.join(lyrics_translated).lower().replace('—', ' ').replace('-', ' ')

    # remove all stop words
    lyrics_translated = word_tokenize(lyrics_translated)
    lyrics_tokens_without_sw = [word for word in lyrics_translated if word not in all_stopwords]

    # join the tokens into a long string before passing to WordCloud
    lyrics_translated = ' '.join(lyrics_tokens_without_sw)

    wc = WordCloud(max_words=1000000, max_font_size=50, collocations=False).generate(lyrics_translated)
    wc_plt.figure()
    wc_plt.imshow(wc, interpolation='bilinear')
    wc_plt.axis('off')
    wc_plt.show()
