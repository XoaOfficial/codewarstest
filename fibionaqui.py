pip install sentiment-analysis-spanish
pip install keras tensorflow
from sentiment_analysis_spanish import sentiment_analysis
sentiment = sentiment_analysis.SentimentAnalysisSpanish()
print(sentiment.sentiment("menuda mierda que es el codewars"))