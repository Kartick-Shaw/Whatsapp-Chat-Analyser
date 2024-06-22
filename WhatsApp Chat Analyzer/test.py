from deep_translator import GoogleTranslator
# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# sentence = "Tum kahe nahi dekh rahi hai re"
# sentence1 = "Ma'am 12.30 theke class korabe bolchhen to!"


# translated_text = GoogleTranslator(source='auto', target='en').translate(sentence)
# translated_text1 = GoogleTranslator(source='auto', target='en').translate(sentence1)
# # translated = MyMemoryTranslator(source='auto', target='en').translate(sentence)
# print(translated_text)
# print(translated_text1)
# # print(translated)

# # translated_text = GoogleTranslator(source='auto', target='en').translate(sentence)
#     #print(translated_text)
# analyzer = SentimentIntensityAnalyzer()
# sentiment_dict = analyzer.polarity_scores(translated_text)
# sentiment_dict1 = analyzer.polarity_scores(translated_text1)

# # print("\nTranslated Sentence=",translated_text, "\nDictionary=",sentiment_dict)
# if sentiment_dict1['compound'] >= 0.05 :
#         print("It is a Positive Sentence")
        
# elif sentiment_dict1['compound'] <= - 0.05 :
#         print("It is a Negative Sentence")      
# else :    
#     print("It is a Neutral Sentence")

# from translate import Translator

# def translate_hinglish_to_english(text):
#     translator = Translator(to_lang="en")
#     translation = translator.translate(text)
#     return translation

# hinglish_text = "mai khush hu"
# translated_text = translate_hinglish_to_english(hinglish_text)
# print("Translated Text:", translated_text)

# from googletrans import Translator

# def translate_hinglish_to_english(text):
#     translator = Translator()
#     translation = translator.translate(text, src='auto', dest='en')
#     return translation.text

# hinglish_text = " <Media omitted>"
# translated_text = translate_hinglish_to_english(hinglish_text)
# print("Translated Text:", translated_text)

from textblob import TextBlob

def translate_hinglish_to_english(text):
    blob = TextBlob(text)
    translated_text = blob(from_lang='hi', to='en')
    return str(translated_text)

# Example usage
hinglish_text = "मैं खुश हूँ"
translated_text = translate_hinglish_to_english(hinglish_text)
print("Translated Text:", translated_text)

