import sys
import datetime

from sentiment_analysis_spanish import sentiment_analysis




def sent(texto):
    sentiment = sentiment_analysis.SentimentAnalysisSpanish()
    sentimiento = sentiment.sentiment(texto) 

    return sentimiento

   

time=datetime.datetime.now()

output="Hi %s current time is %s" % (sys.argv[1],time)

print(output)