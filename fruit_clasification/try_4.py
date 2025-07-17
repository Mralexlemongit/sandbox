from transformers import pipeline

classifier = pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment")

frutas = ["naranja", "melon", "lima", "sandia", "limon", "platano", "toronja"]

def citric_labeling(fruta):
    res = classifier(f"{fruta} es una fruta cítrica o no cítrica?")
    return res[0]["label"]

res = {}
for fruta in frutas:
    res[fruta] = citric_labeling(fruta)
    print(f"{fruta} es una {res[fruta]}")


""" Respuesta
naranja es una 2 stars
melon es una 1 star
lima es una 1 star
sandia es una 1 star
limon es una 1 star
platano es una 1 star
toronja es una 1 star
"""