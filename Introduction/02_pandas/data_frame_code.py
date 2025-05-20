# %%
import pandas as pd

# Creación de un DataFrame inicializándolo con un diccionario de objetios Series
personas = {
    "peso": pd.Series([84, 90, 56, 64], ["Santiago","Pedro", "Ana", "Julia"]),
    "altura": pd.Series({"Santiago": 187, "Pedro": 178, "Julia": 170, "Ana": 165}),
    "hijos": pd.Series([2, 3], ["Pedro", "Julia"])
}

df = pd.DataFrame(personas)
df

# %% [markdown]
# Puede forzarse al DataFrame a que presente unas columnas determinadas y en un orden determinado

# %%
# Creación de un DataFrame inicializándolo con algunos elementos de un diccionario
# de objetos Series
personas = {
    "peso": pd.Series([84, 90, 56, 64], ["Santiago","Pedro", "Ana", "Julia"]),
    "altura": pd.Series({"Santiago": 187, "Pedro": 178, "Julia": 170, "Ana": 165}),
    "hijos": pd.Series([2, 3], ["Pedro", "Julia"])
}

df = pd.DataFrame(
        personas,
        columns = ["altura", "peso"],
        index = ["Ana", "Julia", "Santiago"])
df

# %%
# Creación de un DataFrame inicializándolo con una lista de listas de Python
# Importante: Deben especificarse las columnas e indices por separado
valores = [
    [185, 4, 76],
    [170, 0, 65],
    [190, 1, 89]
]

df = pd.DataFrame(
        valores,
        columns = ["altura", "hijos", "peso"],
        index = ["Pedro", "Ana", "Juan"])
df

# %%
# Creación de un DataFrame inicializándolo con un diccionario de Python
personas = {
    "altura": {"Santiago": 187, "Pedro": 178, "Julia": 170, "Ana": 165}, 
    "peso": {"Santiago": 87, "Pedro": 78, "Julia": 70, "Ana": 65}}

df = pd.DataFrame(personas)
df

# %% [markdown]
# Acceso a los elementos de un DataFrame

# %%
# Creación de un DataFrame inicializándolo con un diccionario de objetios Series
personas = {
    "peso": pd.Series([84, 90, 56, 64], ["Santiago","Pedro", "Ana", "Julia"]),
    "altura": pd.Series({"Santiago": 187, "Pedro": 178, "Julia": 170, "Ana": 165}),
    "hijos": pd.Series([2, 3], ["Pedro", "Julia"])
}

df = pd.DataFrame(personas)
df

# %% [markdown]
# Acceso a los elementos de las columnas del DataFrame

# %%
df["peso"]

# %%
df[["peso", "altura"]]

# %%
# Pueden combinarse los metodos anteriores con expresiones booleanas
df[df["peso"] > 80]

# %%
# Pueden combinarse los metodos anteriores con expresiones booleanas
df["peso"] > 80

# %%
# Pueden combinarse los metodos anteriores con expresiones booleanas
df[df["peso"] > 80]

# %%
# combinación de expresiones
df[(df["peso"] > 80) & (df["altura"] > 180)]

# %% [markdown]
# Acceso a los elementos de las filas del DataFrame

# %%
df.loc["Pedro"]

# %%
# acceder mediante el indice
df.iloc[2]

# %%
df.iloc[1:3]

# %% [markdown]
# Consulta avanzada de los elementos de un DataFrame

# %%
df.query("altura >= 170 and peso > 70")

# %% [markdown]
# Copiar un DataFrame

# %%
# Creación de un DataFrame inicializándolo con un diccionario de objetios Series
personas = {
    "peso": pd.Series([84, 90, 56, 64], ["Santiago","Pedro", "Ana", "Julia"]),
    "altura": pd.Series({"Santiago": 187, "Pedro": 178, "Julia": 170, "Ana": 165}),
    "hijos": pd.Series([2, 3], ["Pedro", "Julia"])
}

df = pd.DataFrame(personas)
df

# %%
# Copia del DataFrame df en df_copy
# Importante: Al modificar un elemento de df_copy no se modifica df
df_copy = df.copy()

# %% [markdown]
# Modificación de un DataFrame

# %%
# Creación de un DataFrame inicializándolo con un diccionario de objetios Series
personas = {
    "peso": pd.Series([84, 90, 56, 64], ["Santiago","Pedro", "Ana", "Julia"]),
    "altura": pd.Series({"Santiago": 187, "Pedro": 178, "Julia": 170, "Ana": 165}),
    "hijos": pd.Series([2, 3], ["Pedro", "Julia"])
}

df = pd.DataFrame(personas)
df

# %%
# Añadir una nueva columna al DataFrame
df["cumpleaños"] = [1990, 1987, 1980, 1994]
df

# %%
# Añadir una nueva columna calculada al DataFrame
df["años"] = 2025 - df["cumpleaños"]
df

# %%
# Añadir una nueva columna creando un DataFrame nuevo
df_mod = df.assign(mascotas = [1, 3, 0, 0])
df_mod

# %%
df

# %%
# Eliminar una columna existente del DataFrame
del df["peso"]
df

# %%
# Eliminar una columna existente devolviendo una copia del DataFrame resultante
df_mod = df.drop(["hijos"], axis=1)
df_mod

# %%
df

# %% [markdown]
# Evaluación de expresiones sobre un DataFrame

# %%
# Creación de un DataFrame inicializándolo con un diccionario de objetios Series
personas = {
    "peso": pd.Series([84, 90, 56, 64], ["Santiago","Pedro", "Ana", "Julia"]),
    "altura": pd.Series({"Santiago": 187, "Pedro": 178, "Julia": 170, "Ana": 165}),
    "hijos": pd.Series([2, 3], ["Pedro", "Julia"])
}

df = pd.DataFrame(personas)
df

# %%
# Evaluar una función sobre una columna del DataFrame
df.eval("altura / 2")

# %%
# Asignar el valor resultante como una nueva columna
df.eval("media_altura = altura / 2", inplace=True)
df

# %%
# Evaluar una función utilizando una variable local
max_altura = 180
df.eval("altura > @max_altura")

# %%
# Aplicar una función externa a una columna del DataFrame
def func(x):
    return x + 2

df["peso"].apply(func)

# %% [markdown]
# Guardar y Cargar el DataFrame

# %%
# Creación de un DataFrame inicializándolo con un diccionario de objetios Series
personas = {
    "peso": pd.Series([84, 90, 56, 64], ["Santiago","Pedro", "Ana", "Julia"]),
    "altura": pd.Series({"Santiago": 187, "Pedro": 178, "Julia": 170, "Ana": 165}),
    "hijos": pd.Series([2, 3], ["Pedro", "Julia"])
}

df = pd.DataFrame(personas)
df

# %%
# Guardar el DataFrame como CSV, HTML y JSON
df.to_csv("df_personas.csv")
df.to_html("df_personas.html")
df.to_json("df_personas.json")

# %%
# Cargar el DataFrame en Jupyter
df2 = pd.read_csv("df_personas.csv", index_col=0)
df2


