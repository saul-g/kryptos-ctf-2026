# El noveno desafío: PK9

Con PK9, la serie se aproxima a su tramo final y la dificultad alcanza un
nivel en el que muchas de las herramientas clásicas del criptoanálisis
muestran sus limitaciones. Tras enfrentarse a criptogramas cada vez más
resistentes al análisis estadístico, el participante se encuentra ahora ante
un reto que parece cuidadosamente diseñado para reducir al mínimo la cantidad
de información visible y maximizar la incertidumbre sobre la naturaleza del
sistema empleado.

PK9 no transmite la sensación de ser un texto aleatorio. Algunas letras
aparecen con una frecuencia notable, ciertos grupos parecen compartir
estructuras similares y determinadas secuencias llaman la atención del
observador. Sin embargo, ninguna de estas características resulta
suficientemente evidente como para señalar una solución concreta. El
criptograma parece situarse deliberadamente en una zona intermedia donde
existen indicios, pero no explicaciones inmediatas.

Llegados a este punto, el objetivo ya no consiste únicamente en aplicar
técnicas conocidas, sino en decidir cuáles de ellas merecen realmente la pena.
Se debe evaluar si los patrones observados son consecuencia del sistema
criptográfico o simples fluctuaciones estadísticas provocadas por el tamaño
reducido de la muestra.

Además, la progresión seguida por los retos anteriores invita a considerar
mecanismos cada vez más sofisticados. Las posibilidades abarcan desde cifrados
por bloques, polialfabéticos, transformaciones, incluso combinaciones de
varios métodos en cascada. En consecuencia, el principal desafío de PK9 no es
descifrar el mensaje en sí, sino identificar correctamente la familia
criptográfica a la que pertenece.

El criptograma es el siguiente:

```

    KSYAW FEYYO ISZGE UFBLY ATAIB YFAQB QYYVD WJKLJ XMYIE PIFVH
    PQNHZ GSUHU UDXLE HRHUM ALHEG LHXSJ MUXGN UIVBX GUJHZ RZGUS
    VHMLS CTSUQ XHSUM QQIFU QGKHJ GUQGL HDKEW SKAMH IJXD

```

El criptograma ofrece pocas concesiones al analista y exige combinar
experiencia, rigor estadístico e intuición criptográfica. Es un reto que nos
recuerda una de las lecciones fundamentales de la disciplina: en ocasiones, no
es la cantidad de información disponible lo que determina el éxito de un
análisis, sino la capacidad para extraer significado de los detalles más
sutiles.


## Análisis estadístico de pk9

Nos encontramos ante uno de los criptogramas más breves de toda la serie, una
circunstancia que reduce considerablemente la eficacia de muchos métodos
clásicos de criptoanálisis. Paradójicamente, esta escasez de información
convierte al reto, en uno de los más complejos, ya que nos obliga a extraer
conclusiones a partir de evidencias mínimas.

```
    Grafica de frecuencias de PK8

       13 |               #                         #
       11 |               #                         #
       10 |               #                         #
        9 |               #                         #
        8 |             # #                     #   #
        7 |             # #                 #   #   #       #
        6 |             # # #     #         #   #   #     # #
        5 | #       #   # # # #   # #       #   #   #     # #
        4 | #       # # # # # # # # #       #   #   #     # #
        3 | # #   # # # # # # # # # #       #   #   # #   # # #
        2 | # #   # # # # # # # # # #       #   #   # # # # # #
        1 | # # # # # # # # # # # # # # # # # # # # # # # # # #
    ------+----------------------------------------------------->
            A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

    Total de letras : 144
    Vocales         : 22.9167%
    Consonantes     : 77.0833%
    IC              : 0.0445
    Entropía        : 4.4599
```

Con aproximadamente 144 caracteres, PK9 proporciona una muestra lo bastante
grande para realizar observaciones preliminares, pero demasiado pequeña para
obtener resultados estadísticos concluyentes. Como consecuencia, cualquier
hipótesis deberá considerarse provisional y contrastarse cuidadosamente con
otras evidencias.

La primera inspección visual revela una concentración significativa de
determinadas letras: H, Q, U, Y, S, G, I, L. Entre ellas destacan
especialmente: H y U. La elevada aparición de estos caracteres resulta
llamativa porque algunos de ellos no suelen encontrarse entre las letras más
frecuentes de un texto natural en Inglés. 

A pesar de la brevedad del texto, aparecen algunos elementos recurrentes. No
hay letras doble. Pero si hay secuencias repetidas: GLH, UQG, GU, LH, SU, UQ,
ZG.  Estas coincidencias son especialmente interesantes porque podrían indicar
la existencia de relaciones internas entre bloques de texto. No obstante,
debido al tamaño reducido de la muestra, también es posible que algunas de
ellas sean fruto del azar. Este comportamiento sugiere que las frecuencias
originales han sido alteradas de forma considerable, mediante un cifrado de
sustitución. Por otra parte, la longitud del criptograma es un número par.
Esto significa que la solución puede requerir de una transposición. 

Uno de los aspectos más llamativos de PK9 es la escasa redundancia general del
criptograma. Aunque existen algunas repeticiones parciales, no aparecen 
secuencias largas idénticas. Aunque existe una periodicidad de 7. Este
comportamiento es compatible con sistemas diseñados para dificultar los
ataques basados en patrones repetidos, como:

-Cifrados polialfabéticos con claves largas.
-Cifrados por bloques.
-Transformaciones multicapa.

Determinar cuál de estas explicaciones es correcta constituye una de las
cuestiones centrales del reto.


### Progresión de los desafíos

La evolución de los desafíos observada hasta este punto puede resumirse así:

- PK1 Identificación del sistema
- PK2 Análisis de frecuencias
- PK3 Reducción de patrones
- PK4 Homogeneización estadística
- PK5 Ambigüedad estructural
- PK6 Relaciones ocultas
- PK7 Posible cifrado por bloques
- PK8 Escasez de datos y alta difusión
- PK9 Escasez extrema y evidencia limitada

PK9 parece marcar un cambio importante: la dificultad no proviene únicamente
del cifrado, sino de la falta de información disponible para estudiarlo.


## El mensaje final de Pellegrin

Como ocurre con algunos de los problemas más complejos de la criptografía
histórica, el desafío reside en construir hipótesis sólidas a partir de
indicios mínimos.

El nivel de PK9 fue uno de los retos más despiadados y, junto con PK8, causó
una parálisis total en el desafío durante semanas debido a la inversión en la
lógica clásica.

El orden de codificación exacto de PK9 fue el siguiente:

1. Capa 1: Quagmire III con una longitud de clave de 9 caracteres.
2. Capa 2: Transposición en espiral con una longitud de 12.
3. Capa 3: Transposición columnar con una clave de 8 caracteres.

La palabra clave asociada a este nivel y que sirvió como piedra angular del
cifrado polialfabético fue CLEPSYDRA (que significa reloj de agua en
latín/griego). La clave para este reto está en PK1. "El registro de acceso
dice que una vez desenredado revela la ruta hacia el archivo perdido de
Pellegrin. Doce archivistas anteriores intentaron desenredarlo, todos
fallaron". Solo que no es el elemento ocho del registro, sino el nueve.

```

    PK9
    Transposición columnar 
    CLAVE: 23158674 (BEAMWORK)

    Transposición en espiral (12)
    Quagmire III

    ALFABETO: KRYPTOSABCDEFGHIJLMNQUVWXZ
    CLAVE: CLEPSYDRA

```
Clepsydra (traducido al español como clepsidra) es un reloj de agua. Es uno de
los instrumentos más antiguos inventados por la humanidad para medir el tiempo
(usado por los babilonios y los egipcios) antes de que existieran los relojes
mecánicos. Beamwork (traducido al español como entramado de vigas o trabajo de
soporte estructural) es un término arquitectónico y de carpintería. Que
resulta al convertir la clave numérica usando el alfabeto estándar (se pueden
usar otras palabras, con resultados similares).

PK9 es complicado por varias razones. El orden en criptografía clásica lo es
todo. Si aplicas una transposición y luego una sustitución, el análisis de
frecuencia de letras individuales sigue intacto, por lo que herramientas
automáticas encuentran la solución en segundos. Sin embargo, al hacer lo que
se hizo en PK9: aplicar primero la sustitución Quagmire III y después mezclar
las posiciones con dos transposiciones consecutivas (diferentes), las
frecuencias estadísticas se destruyeron por completo. No había monogramas ni
patrones visibles. Las pistas eran solo espejismos. Para resolverlo, se tuvo
que adivinar y forzar primero las dimensiones geométricas de las matrices (12
y 8) de atrás hacia adelante para tener una mínima oportunidad de leer el
texto usando la palabra clave CLEPSYDRA. Esta vez se utilizó un sistema de
transposición diferente: un cifrado en espiral.


## El cifrado en espiral

El cifrado en espiral (o cifrado de ruta en espiral) es un método de
criptografía clásica basado en la transposición geométrica. A diferencia de
los cifrados que sustituyen unas letras por otras, este sistema mantiene las
letras originales del mensaje pero desordena su posición siguiendo una ruta en
forma de espiral dentro de una cuadrícula o matriz.

### ¿Cómo funciona?

El proceso consta de dos fases principales:

1. **Escritura en la cuadrícula**: el texto original se introduce en una 
   matriz o rejilla de dimensiones previamente acordadas. El remitente escribe 
   el mensaje de forma lineal (fila por fila o columna por columna).

2. **Lectura en espiral (cifrado)**: el mensaje encriptado se obtiene leyendo 
   las letras de la cuadrícula siguiendo un camino en espiral. Esta espiral 
   puede tener múltiples variantes que forman parte de la "clave":
    - Hacia adentro (tipo caracol) o hacia afuera.
    - En sentido de las agujas del reloj o inverso.
    - Comenzando desde cualquiera de las cuatro esquinas o desde el centro.

Para descifrarlo, el receptor simplemente hace el proceso inverso: dibuja la
espiral vacía con las dimensiones correctas, coloca las letras del criptograma
a lo largo de esa ruta y luego lee el mensaje fila por fila de forma natural.

En PK9, la transposición en espiral se aplicó en sentido horario, iniciando en
la esquina superior derecha, hacia abajo, izquierda, arriba y derecha.

```

    ISPENTTHEPASTMONTHWITHTHENEEDLEANDKNOTANDATLASTP
    ELLEGRINSFINALMESSAGEHASBEENREVEALEDTOMEIWILLNOW
    SEALITFORYOUUNDEREVERYCIPHERIUSEDINTHISTESTAMENT

```
Separado en palabras, este texto en Inglés dice:

```

    I spent the past month with the needle and knot and at last Pellegrin's
    final message has been revealed to me. I will now seal it for you under
    every cipher I used in this testament.
```

En Español:

```

    Pasé el último mes con la aguja y el nudo y, por fin, el mensaje final de
    Pellegrin me ha sido revelado. Ahora lo sellaré para ti bajo cada cifrado
    que utilicé en este testamento.

```
El texto representa el clímax y la resolución del misterio principal, pero
introduce un nuevo desafío para quien esté leyendo el diario. 

El robo de la aguja funcionó. Al archivista le tomó un mes de paciencia y
trabajo minucioso, pero logró desenredar el nudo y leer las letras inscritas
en el hilo. Logró lo que los doce archivistas anteriores no pudieron:
descubrir el secreto de Pellegrin y la ruta al archivo perdido. Pero, el
investigador ha decidido que este conocimiento es demasiado valioso o
peligroso para dejarlo a la vista de cualquiera.

Al escribir "lo sellaré para ti bajo cada cifrado", le está hablando
directamente a la persona que encuentre su diario (el lector). Significa que
el mensaje final y la ubicación del archivo perdido están ocultos en un último
código compuesto por la combinación de todos los acertijos anteriores.

El protagonista completó su viaje, pero ahora le pasa la antorcha al lector.
Si quieres saber qué dice el mensaje de Pellegrin y dónde está el archivo,
tendrás que descifrar el último rompecabezas que dejó oculto en sus escritos.
¡Llegamos al mensaje final! 

¿Cuál es el secreto que guarda el archivo perdido de Pellegrin?
