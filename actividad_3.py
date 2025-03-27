import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

class actividad_3:
    def __init__(self):
        pass
    
        # Crear un DataFrame
data = {
    'Granadilla': [20],
    'Tomates': [50]
}

# Convertir a DataFrame
df = pd.DataFrame(data)

# Mostrar el DataFrame
print(df)