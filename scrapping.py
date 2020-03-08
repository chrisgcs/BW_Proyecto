import twint

client = twint.Config()
client.Search = ["#COP25 OR #COP_25 OR COP25"]
client.Output = "twits_cop25_results_en_es.csv"
client.Lang = "en"
client.Since = "2019-01-01"
client.Until = "2019-12-03 11:20:00"
client.Store_csv = True

twint.run.Search(client)