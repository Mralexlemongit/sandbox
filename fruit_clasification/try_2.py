from transformers import pipeline

generator = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")
res = generator("Dame una receta de tacos:", max_length=50)
print(res[0]["generated_text"])

""" Respuesta:
Dame una receta de tacos: me gusta un poco mejor el papel de hielo con el aceite de oliva

La guía para los tacos de hielo por primera vez en su vida fue una receta de H.G. Wells en el libro de historia de un día. A lo largo del libro: “… y hizo que mi vida fuera más un cántaro”. Según Wells, una de las más grandes vías de escape de las diferencias está en el camino de algún líder y autor que, sin un cambio radical en la razón y el hábitat, es capaz de salir de la ausencia.

El hombre de esta guía es William S. Hart, el alemán quien, como las demás personas que lee este libro, realmente empezó a caminar en el camino del poder económico; y, al final de su trabajo, logró convertirse en el hombre con más
"""