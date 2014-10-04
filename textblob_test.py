from textblob import TextBlob


text = "I hate everyone. I love pie."

blob = TextBlob(text)


for sentence in blob.sentences:
    print(sentence.sentiment.polarity)
