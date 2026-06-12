import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:root@localhost:5432/deploy_project")

try:
	df = pd.read_csv("C:\\Users\\El. OURY BALDE\\Desktop\\P8\\Notebook\\credit_accord.csv")
	df.to_sql("dataset", engine, if_exists="append", index=False)
	print("Dataset inséré avec succès.")
except FileNotFoundError:
	print("Erreur : Le fichier CSV 'C:\\Users\\El. OURY BALDE\\Desktop\\P8\\Notebook\\credit_accord.csv' n'a pas été trouvé. Vérifiez le chemin.")
except Exception as e:
	print(f"Erreur lors de l'insertion : {e}")