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