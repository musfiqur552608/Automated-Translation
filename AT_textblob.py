#pip install textblob

from textblob import TextBlob
text = TextBlob('Easy way to translate a text in python')
text.translate(to = 'fr')