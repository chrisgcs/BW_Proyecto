import pandas as pd

# =========================== DATAFRAMES ============================= #
df = pd.read_csv("twits_cop25_results_en_es.csv")
df_chile = pd.read_csv("twits_cop25chile_results_en_es.csv")

# =========================== REMOVE COLUMNS ============================= #

tweets_global = df['tweet']
tweets_chile = df_chile['tweet']

# =========================== CREATE FILES ============================= #

with open("tweets_mundo.txt", "w") as file:
  i = 0
  for tweet in tweets_global:
    if(i < (len(tweets_global) - 1)):
      file.write(tweet.replace('\n', ' ') + "\n")
    else:
      file.write(tweet.replace('\n', ' '))
    i += 1

with open("tweets_chile.txt", "w") as file:
  i = 0
  for tweet in tweets_chile:
    if(i < (len(tweets_chile) - 1)):
      file.write(tweet.replace('\n', ' ') + "\n")
    else:
      file.write(tweet.replace('\n', ' '))
    i += 1