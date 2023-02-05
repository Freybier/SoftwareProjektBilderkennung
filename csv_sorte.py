import pandas as pd

def csv_sorte():

    # Lesen Sie die CSV-Datei in ein Pandas-DataFrame ein
    df = pd.read_csv("CSV/csvTest2.csv")

    # Verwenden Sie die Methode "reindex", um die Spalten in der gewünschten Reihenfolge zu ordnen
    df = df.reindex(columns=["mtknr","sortname","bewertung","pstatus","pversuch","ktxt","spversion","semester","pdatum","pnr","bonus","labnr","pordnr","porgnr","Mail"])

    # Verwenden Sie die Methode "to_csv", um das sortierte DataFrame in eine neue CSV-Datei zu speichern
    df.to_csv("CSV/csv_sorted.csv", index=False)