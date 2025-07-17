# 🧠 TAREA 01: El Bot de las Frutas

## Objetivo:
Crear un pequeño script en Python que clasifique frutas en dos categorías: cítricas y no cítricas.

## Instrucciones:

Usa cualquier herramienta de IA que quieras (puede ser un modelo ya entrenado, una librería de machine learning, etc.) para construir un sistema que, dado el nombre de una fruta, diga si es cítrica o no.

Usa al menos 10 frutas, combinando ejemplos claros y ambiguos.

El script debe aceptar entrada desde la terminal o consola.

El modelo o regla debe poder generalizar (no hardcodees todo, pero puedes apoyarte en listas si es necesario).

## Pregunta 1:

ya lo resolvi pero antes de pasarte mi respuesta quiero que me digas que pasos, herramientas, servicios o trucos hubieras usado tu para resolverlo?

## Respuesta para chatgpt:

mi solución empezo por usar una app generativa de texto para que respondiera a un promp tipo "escribe unicamente 'cítricas' si la siguiente fruta podria considerarse citrica, en caso contrario escribe unicamente 'no cítrica': melon es una fruta"

### Intento 1

intenté usar el api de openia primeramente y sufri un stoper por los budgets que no quise resolver con dinero por lo que busqueda alternativas sin gasto dejando el archivo en el siguiente punto:

[try 1]

### Intento 2:

Busqué alternativas lo que resulto en probar Hugginface para hacer la clasificación, utilizando el modelo EleutherAI/gpt-neo-1.3B lo que peso casi 5 gigas y me dio muchas alucinaciones:

[try 2]

### Intento 3:

Por darle una segunda oportunidad lo intente igual con hugginface pero con el modelo `"datificate/gpt2-small-spanish"`, lo que tambien me dio una mala respuesta, ahi fue donde chatgpt me hizo darme cuenta que estaba usando modelos basados en textos generativos para un simple problema de clasificación:

[try 3]

### intento 4:

Intente con un clasificador de hugginface pero los resultados no fueron muy alentadores

[try 4]

### Intento 5:

tras un rato de batallar decidi pasarme a google colab por recomendación de chatgpt y usar el clasificador de sklearn, funciono bien y luego lo movi a local donde tambien funciono bastante bien

[try 5]

tiempo resolución: 2 horas

Dame retro de mis pasos. Es esto lo que tu tenias en mente? Si utilice herramientas excesivas o si habian opciones más adecuadas para resolver el problema, hazmelo saber. Dime si hay algo que ves que pude haber mejorado en general.


## Comparativa de Modelos de IA Usados y Mencionados

| Modelo                                              | Prueba             | Año  | Proveedor                             | Propósito                                                                                              | Tipo de modelo                                               | Etiquetas clave                                           | Competidores directos                                    | N.º de parámetros | Tamaño en disco |
|-----------------------------------------------------|--------------------|------|----------------------------------------|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|-----------------------------------------------------------|----------------------------------------------------------|------------------|----------------|
| EleutherAI/gpt-neo-1.3B                             | 2                  | 2021 | EleutherAI                             | Generación de texto en inglés de propósito general, similar a GPT-3, entrenado en el conjunto Pile.    | Transformer autoregresivo (decoder-only)                   | language-modeling, english, open-source                 | GPT-3 (OpenAI), GPT-J (EleutherAI), GPT-2               | 1.3B             | ~5 GB           |
| datificate/gpt2-small-spanish                      | 3                  | 2021 | Datificate / HuggingFace community     | Modelo generativo pequeño para generación de texto en español, adaptado de GPT-2.                      | Transformer autoregresivo (decoder-only)                   | spanish, text-generation, gpt2                         | BETO (Spanish BERT), mBART, GPT-2 fine-tuned           | 124M             | ~500 MB         |
| nlptown/bert-base-multilingual-uncased-sentiment   | 4                  | 2020 | NLPTown                                | Clasificación de sentimiento multilingüe (1-5 estrellas) en reseñas y textos.                          | BERT multilingüe fine-tuned                                 | sentiment-analysis, multilingual, classification       | XLM-RoBERTa, DistilBERT sentiment, BERT multilingual   | 110M             | ~420 MB         |
| paraphrase-multilingual-MiniLM-L12-v2              | 5                  | 2020 | Sentence Transformers / HuggingFace    | Generación de embeddings semánticos para múltiples lenguajes. Usado en búsqueda semántica y clustering. | Transformer siamés (encoder-only, distilBERT-like)         | sentence-embeddings, multilingual, semantic-similarity | LaBSE, Universal Sentence Encoder, MPNet               | 33M              | ~120 MB         |
| facebook/bart-large-mnli                           | propuesta chatgpt  | 2020 | Facebook AI                            | Reconocimiento textual y clasificación zero-shot mediante inferencia textual natural (NLI).            | Transformer encoder-decoder (BART) fine-tuned en NLI        | zero-shot-classification, entailment, nli             | RoBERTa-MNLI, T5-NLI, DeBERTa-v3                       | 406M             | ~1.5 GB         |
