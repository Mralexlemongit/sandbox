from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def fruit_clasifier(fruit):
    res = classifier(fruit, candidate_labels=["cítrica", "no cítrica"])
    scores = res["scores"]
    return "cítrica" if scores[0] > scores[1] else "no cítrica"

frutas = [
    "naranja", "limón", "toronja", "lima", "mandarina", "pomelo",
    "piña", "fresa", "sandía", "melón", "plátano", "mango",
    "manzana", "pera", "kiwi", "uva", "cereza", "durazno",
    "albaricoque", "granada", "guayaba", "tamarindo", "coco",
    "arándano", "zarzamora", "frambuesa", "higo", "lichi", "carambola",
    "chirimoya", "maracuyá", "níspero", "caqui", "papaya", "mamey"
]