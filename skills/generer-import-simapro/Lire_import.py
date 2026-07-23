# %%
from ast import Import
import csv
import numpy as np
import os
import datetime as dt
from tkinter import Tk, filedialog
import pandas as pd

# %%
def ouvrir_fichier_xlsx():
    """
    Ouvre une boîte de dialogue pour sélectionner un fichier CSV et retourne le chemin du fichier sélectionné.
    """
    root = Tk()
    root.withdraw()  # Masquer la fenêtre principale
    root.attributes("-topmost", True)  # Forcer la boîte de dialogue au premier plan
    root.update()
    file_path = filedialog.askopenfilename(
        parent=root,
        title="Sélectionner un fichier csv ou xslx",
        filetypes=[("Fichiers csv", "*.csv"), ("Fichiers xslx", "*.xlsx"), ("Tous les fichiers", "*.*")]
    )
    root.destroy()
    return file_path
# %%
def lire_fichier_xlsx(file_path):
    """
    Lit un fichier XLSX et retourne son contenu sous forme de DataFrame.

    Args:
        file_path (str): Le chemin du fichier XLSX à lire.
        
    Returns:
        pd.DataFrame: Un DataFrame représentant le contenu du fichier XLSX.
    """

    f = pd.read_excel(file_path, sheet_name = "ICV")
    return f
# %%
