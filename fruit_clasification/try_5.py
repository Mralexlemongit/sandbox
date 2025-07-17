from sentence_transformers import SentenceTransformer
from sklearn.neighbors import KNeighborsClassifier

# Modelo preentrenado
model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

# Dataset base
frutas = ["naranja", "limón", "toronja", "lima", "mandarina", "melón", "sandía", "plátano"]
etiquetas = ["cítrica"] * 5 + ["no cítrica"] * 3

# Embeddings
X = model.encode(frutas)

# Clasificador simple
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X, etiquetas)

# Probar
nuevas_frutas = ["fresa", "naranja", "melón", "lima", "piña"]
emb_nuevas = model.encode(nuevas_frutas)
preds = knn.predict(emb_nuevas)

for fruta, pred in zip(nuevas_frutas, preds):
    print(f"{fruta}: {pred}")


""" Respuesta
fresa: no cítrica
naranja: cítrica
melón: no cítrica
lima: cítrica
piña: cítrica
"""