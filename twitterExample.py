# 1 - Criar um twitter app
# 2 - Pegar key e access token
# 3 - Instalar pelo pip, tweepy e textblob
# 4 - Ótimo exemplo https://github.com/rhnvrm/labeled-tweet-generator

import tweepy
from textblob import TextBlob

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

autenticacao = tweepy.OAuthHandler(consumer_key, consumer_secret)

autenticacao.set_access_token(access_token, access_token_secret)

api = tweepy.API(autenticacao)

public_tweets = api.search('Sua pesquisa aqui ...')

for tweet in public_tweets:
    print(tweet.text.encode("utf-8"))
    analise = TextBlob(tweet.text)
    print(analise.sentiment)
