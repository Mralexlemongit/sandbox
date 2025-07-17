from transformers import pipeline

generator =  pipeline("text-generation", model="datificate/gpt2-small-spanish")
res = generator("escribe unicamente 'cítricas' si la siguiente fruta podria considerarse citrica, en caso contrario escribe unicamente 'no cítrica': melon es una fruta:", max_new_tokens=150, do_sample=True, temperature=0.7)
print(res[0]["generated_text"])

""" Respuesta
escribe unicamente 'cítricas' si la siguiente fruta podria considerarse citrica, en caso contrario escribe unicamente 'no cítrica': melon es una fruta:'mi vid' y'mi cerezas' son similares.

El hecho de que la fruta en cuestión sea'mi vid' (una variedad de uva) es importante para entender por qué "mi vid" es una variedad de uva. La más antigua "cavezas" eran la uva de las Islas Canarias, que es de origen Canarias, y que fue llamada 'cavezas' desde que los españoles bautizaron a la variedad 'cavezas' en una carta de 1798.

En el siglo XVIII, la uva de las Islas Canarias, llamada 'cavezas' (un tipo de uva que posee muchos de sus rasgos característicos de la uva de las Islas Canarias, y que se cree está basada en la
"""