import twint

client_chile = twint.Config()
client_chile.Search = ["#cop25chile OR cop25_chile OR cop25chile"]
client_chile.Lang = "en OR es"
client_chile.Output = "twits_cop25chile_results_en_es.csv"
client_chile.Limit = 200000
client_chile.Since = "2019-01-01"
client_chile.Until="2020-02-01"
client_chile.Store_csv = True

twint.run.Search(client_chile)