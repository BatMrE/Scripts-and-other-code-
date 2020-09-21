import nltk
from textblob import TextBlob

#The text from the feedback
text = "Testing feedback review classification on some text"

def sentiment(text):
    obj = TextBlob(text)
    
    #returns the sentiment of text
    #by returning a value between -1.0 and 1.0
    sentiment = obj.sentiment.polarity
    print(sentiment)
    
    if sentiment == 0:
        #Add to neutral count
        print('The text is neutral')
    elif sentiment > 0:
        #Add to positive count
        print('The text is positive')
    else:
        #Add to negative count
        print('The text is negative')
        
sentiment(text)        