from cgitb import text
import sys
import json
import os

from sentiment_analysis_spanish import sentiment_analysis

output=sys.argv[1]

#def emocional(texto):
#    sentiment = sentiment_analysis.SentimentAnalysisSpanish()
#    sentimiento = sentiment.sentiment(texto) #[0,1]
#    return sentimiento


def sent(texto):
    sentiment = sentiment_analysis.SentimentAnalysisSpanish()
    sentimiento = sentiment.sentiment(texto) 
        
    carita = ":|"
    if sentimiento > 0.6:
        carita = ":)"
    elif sentimiento < 0.4:
        carita = ":("
    
    return sentimiento, carita



def hola():
    output2=output.replace('"',"'")
    response_data = {}
    response_data['result'] = output

    text_file = open("./sample.txt", "w")
    result = json.dumps(response_data)
    n = text_file.write(result)

    

    return response_data
    #return output






hola()