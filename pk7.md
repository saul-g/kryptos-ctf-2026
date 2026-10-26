# El septimo desafío: PK7

A primera vista, PK7 presenta muchas de las características habituales de la
serie. Sin embargo, una observación más detenida revela que el criptograma
posee una estructura diferente a la de sus predecesores. No parece
completamente aleatorio, pero tampoco expone patrones suficientemente claros
como para orientar inmediatamente el análisis. El resultado es una sensación
de incertidumbre: el texto parece insinuar una estructura sin llegar a
mostrarla por completo.

Esta ambigüedad constituye uno de los rasgos más sobresalientes de los
desafíos criptográficos. En muchos casos, los sistemas más difíciles no son
aquellos que ocultan toda la información, sino aquellos que muestran solo la
cantidad suficiente para inducir hipótesis plausibles, obligando al analista a
distinguir cuidadosamente entre correlaciones reales y simples coincidencias
estadísticas. PK7 parece pertenecer precisamente a esta categoría.

A estas alturas, también se vuelve necesario considerar la posibilidad de que
el criptograma incorpore mecanismos diseñados específicamente para perturbar
el análisis clásico. 

El criptograma es el siguiente:

```
    FNRHT KRHSE DEJMB OWBDS CSDDX LICXU LMBYQ XWTGU IVNDY ZBEQL
    VHFFF IDAKD CCJKW GOOUE SCYEL YMRAK IUJCU SEAXU QTYKO BVYDY
    MRBYW OTQEE SCQSM DYDQJ NPSWR SUOFM FJDYX SHCXN HVJVB YMZOZ
    OATHT EOVLO QWZIT HTEAF MKGLA STBZR DMFRJ PKWJO XZXPJ CBOVA
    ZEPKA EJPPS IUJOD XTXER WTLTT YMREN BJGTN MLBDJ MYJDD LRCXC
    QCHYM JMHBE OLXEU FNJKB PRSHT EYXB

```

PK7 parece plantear una cuestión aún más compleja: determinar si los patrones
observados forman parte de la solución o si constituyen artefactos
cuidadosamente introducidos para desviar la atención. En este punto, resolver
el criptograma requiere algo más que aplicar técnicas conocidas. Exige
comprender la lógica del propio juego y aceptar que, en ocasiones, la
dificultad reside tanto en formular las preguntas correctas como en encontrar
las respuestas obvias.


## Análisis estadístico de PK7

A medida que aumenta la dificultad de los retos, resulta natural preguntarse
si PK7 pertenece a la misma familia de cifrados polialfabéticos que hemos
venido usando. PK7, parece romper ese esquema:

```

    Grafica de frecuencias de PK7

       17 |         #
       15 |       # #         #
       14 |       # #         #                   #         #
       12 |   #   # #         #     #   #       # #       # #
       11 |   # # # #         #     #   #       # #       # #
        9 |   # # # #     #   #   # #   #     # # #       # #
        8 |   # # # # #   #   # # # #   #     # # # #     # #
        7 | # # # # # #   #   # # # #   #   # # # # #   # # #
        5 | # # # # # #   # # # # # # # # # # # # # # # # # # #
        4 | # # # # # #   # # # # # # # # # # # # # # # # # # #
        2 | # # # # # # # # # # # # # # # # # # # # # # # # # #
        1 | # # # # # # # # # # # # # # # # # # # # # # # # # #
    ------+----------------------------------------------------->
            A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

    Total de letras : 279
    Vocales         : 19.3548%
    Consonantes     : 80.6452%
    IC              : 0.0393
    Entropía        : 4.6186

```

Una inspección visual muestra una distribución relativamente uniforme de
caracteres. Aunque algunas letras aparecen con mayor frecuencia que otras, no
se observa un dominio abrumador comparable al que presentan los textos
naturales. Entre los símbolos que parecen repetirse con mayor frecuencia 
destacan: E, J, D, Y, T, O. 

Lo más significativo no es qué letras aparecen más veces, sino la ausencia de
picos pronunciados en la distribución. Esta homogeneidad es compatible con
otros sistemas poligráficos como Hill, que tienden a difuminar las frecuencias
características del texto original. A lo largo del criptograma aparecen varios
pares repetidos: CC, DD, FF, OO. En un cifrado Hill esto no constituye una
anomalía. A diferencia de sistemas como Playfair, los caracteres duplicados
del texto plano no requieren un tratamiento especial y pueden producir pares
repetidos en el texto cifrado. Sin embargo, la mera presencia de letras dobles
no proporciona evidencia suficiente para confirmar esta hipótesis.

Uno de los rasgos más interesantes de PK7 es la falta de secuencias largas
repetidas de forma exacta. Por ejemplo, aunque existen fragmentos recurrentes
como: IUJ, YMR THT, YM. la mayoría de las coincidencias son demasiado cortas
para resultar estadísticamente significativas.

Esta observación es relevante porque: los cifrados de transposición suelen
conservar más repeticiones visibles. Los cifrados Vigenère con claves cortas
generan coincidencias periódicas detectables mediante Kasiski. Los cifrados
Hill tienden a destruir gran parte de las repeticiones del texto original al
transformar bloques completos. La escasez de repeticiones extensas es, por
tanto, coherente con un posible cifrado por bloques.

Una característica distintiva del cifrado Hill es que cada letra cifrada
depende simultáneamente de varias letras del texto plano. Esto provoca que:
las frecuencias individuales parezcan relativamente uniformes. Los patrones 
monográficos pierdan utilidad y los diagramas y trigramas del cifrado presenten
distribuciones más complejas.

PK7 exhibe precisamente este comportamiento. Aunque ciertos caracteres son
frecuentes, resulta difícil identificar asociaciones evidentes entre ellos o
reconstruir estructuras lingüísticas plausibles a partir de pares
consecutivos.


## El cifrado Hill

El **cifrado Hill** es un cifrado por sustitución poligráfica inventado por
Lester S. Hill en 1929. A diferencia de los cifrados tradicionales que
sustituyen letra por letra, el cifrado Hill utiliza el álgebra lineal para
cifrar bloques de letras de manera simultánea mediante la multiplicación de
matrices.

### ¿Cómo funciona el cifrado Hill?

1. **Bloques y vectores:** el texto plano se divide en bloques de tamaño fijo 
   ``n`` (por ejemplo, bloques de 2 letras para una matriz de ``2*2``, o de 3 
   letras para una de ``3*3``. Cada letra se convierte en un número 
   (A=0, B=1, ..., Z=25).

2. **Multiplicación de matrices:** cada bloque de letras (tratado como un 
   vector columna ``P``) se multiplica por una matriz cuadrada clave ``K`` de 
   tamaño ``n * n``.

3. **Módulo 26:** al resultado de la multiplicación se le aplica el operador 
   módulo (``mod(26)``) para asegurar que el valor numérico vuelva a encajar 
   dentro del alfabeto.

Matemáticamente, el proceso de cifrado se expresa como:

```

    C = K * P mod(26);

```

Donde ``C`` es el vector del texto cifrado, ``K`` es la matriz clave y ``P`` 
es el vector del texto plano. Para descifrar, se multiplica el texto cifrado 
por la **matriz inversa** de ``K`` módulo 26.

**¿Cómo se identifica un texto cifrado con Hill?**

Identificar un criptograma generado por el cifrado Hill requiere buscar las
huellas estructurales que deja el uso de matrices y bloques:

1. **Longitud del criptograma (múltiplo exacto)**. Debido a que el cifrado opera 
   en bloques estrictos de tamaño ``n`` (como parejas o tríos), la longitud 
   total del texto cifrado **siempre será un múltiplo exacto** del tamaño de 
   la matriz utilizada. Si el texto tiene 60 letras, el bloque pudo ser de 2, 
   3, 4, 5, 6, 10 o 12 letras.

2. **Comportamiento estadístico inusual (frecuencias de polígrafos)** A nivel 
   de letras individuales, el análisis de frecuencias de letras sueltas se 
   aplana por completo (similar a un cifrado polialfabético). Como la 
   transformación matemática es lineal, ciertos pares o tríos de letras se 
   repetirán con una frecuencia matemática muy predecible que no coincide con 
   las estadísticas naturales del idioma. Si se analizas la frecuencia de 
   parejas de letras y se notan patrones geométricos o repeticiones 
   inusualmente rígidas, es un fuerte indicio de cifrado matricial.

El método de Kasiski no funciona en el cifrado Hill. Al cifrar por bloques 
matriciales, si la misma palabra aparece en dos lugares distintos del texto, 
el resultado cifrado será completamente diferente a menos que caiga
exactamente en la misma posición relativa dentro del bloque. Por si solo el
cifrado Hill no ofrece mucha resistencia y se puede detectar con relativa
facilidad, pero si se aplica un cifrado polialfabético, puede ocultar las
frecuencias y patrones. 

El texto plano de PK3, nos da tres números para empezar la búsqueda: 7, 15 y 6. 

```

    PK7
    Cifrado Hill 3x3 
    CLAVE: ALCHEMIST (7, 17, 9, 14, 11, 18, 15, 6, 4)

    Quagmire3 
    ALFABETO: KRYPTOSABCDEFGHIJLMNQUVWXZ
    CLAVE: ANNEAL

```

Anneal (traducido al español como recocer o templar / aliviar tensiones en el
metal) es un proceso térmico metalúrgico. Consiste en calentar un material
(como metal o vidrio) a una temperatura muy alta y luego dejar que se enfríe
muy lentamente. Cuando se golpea o estira un metal en frío (como hacía el 
investigador al intentar crear hilos finos de alambre para la aguja), el metal
se vuelve duro, quebradizo y propenso a romperse. El proceso de annealing 
(recocido) altera la estructura molecular del material, volviéndolo mucho más 
suave, maleable, flexible y fácil de moldear sin que se fracture. 


## Simulated Annealing

La palabra *anneal* es una referencia directa a la técnica de *Simulated*
*Annealing* (recocido simulado) que está inspirada en el proceso físico de los
metales. Se utiliza para encontrar una aproximación muy cercana al valor
óptimo en problemas matemáticos y de programación complejos. 

En lugar de probar todas las combinaciones posibles de matrices (lo cual es
computacionalmente costoso para dimensiones grandes), se utilizan algoritmos
de optimización como *Hill Climbing* (escalada de colinas). El algoritmo
propone una matriz como clave aleatoria, descifra el texto y evalúa la
"calidad" del resultado comparando la frecuencia de los trigramas (grupos de 3
letras) obtenidos con la frecuencia estadística del idioma original. La clave
se va modificando gradualmente en la dirección que produce el texto más
legible. Para no quedarse "atrapado" en una cima secundaria (un máximo local)
que produce un texto con algunas palabras legibles pero que no es la solución
real. Se utiliza una variante con *Simulated Annealing* para reinicios
aleatorios: si el algoritmo se estanca, guarda el mejor resultado obtenido
hasta el momento, salta a una parte completamente diferente de la "cima"
generando una matriz nueva y aleatoria, y comienza a escalar de nuevo. Al
final, compara las cimas alcanzadas en cada reinicio y se queda con la más
alta.

Combinado matemáticamente con un cifrado matricial Hill de 3x3, un Quagmire
III se puede convertir en un verdadero desafío.

```

    THREEWEEKSINWERISEBEFORETHESUNANDEACHNEEDLEISDONEBYNOONTHEWHITES
    MITHSHOWSMEHISTECHNIQUEFORPURIFYINGHISMETALBEFOREDRAWINGITINTOAF
    INEWIREHEHASMEREPEATTHESAMESTEPFOURTIMESWITHSLIGHTVARIATIONSSTIL
    LMYHANDFALTERSIAMPATIENTBUTIKNOWTHISISNOTMYCALLINGIHAVEMADEPEACE
    WITHITANDWILLGOHOMESOON        

```

Separado en palabras, este texto en inglés dice:

```

    Three weeks in. We rise before the sun and each needle is done by noon.
    The Whitesmith shows me his technique for purifying his metal before
    drawing it into a fine wire. He has me repeat the same step four times
    with slight variations. Still my hand falters. I am patient but I know
    this is not my calling. I have made peace with it and will go home soon.

```
en Español:

```
    Tres semanas después. Nos levantamos antes del sol y cada aguja está
    terminada para el mediodía. El Hojalatero me muestra su técnica para
    purificar el metal antes de estirarlo en un hilo fino. Me hace repetir el
    mismo paso cuatro veces con ligeras variaciones. Aun así, mi mano tiembla.
    Soy paciente, pero sé que esta no es mi vocación. He hecho las paces con
    ello y volveré a casa pronto.

```

Este texto marca el final de la búsqueda del investigador, quien decide
rendirse y abandonar su misión. Intentó cumplir el trato del artesano. Llevaba
tres semanas despertándose antes del amanecer y trabajando bajo una disciplina
muy estricta, repitiendo procesos minuciosos una y otra vez. A pesar de su
paciencia y esfuerzo, se da cuenta de que no tiene el talento natural
necesario; su mano tiembla y falla al intentar moldear el metal tan fino.
Comprende que no nació para ser artesano y que no vale la pena sacrificar diez
años de su vida en algo que no es su vocación. Ha aceptado su fracaso sin
amargura ("he hecho las paces con ello") y ha tomado la decisión de rendirse,
dejar la aguja alpina y regresar a su hogar, dejando el misterio del nudo sin
resolver.

En este punto, parece que el viaje del archivista ha terminado, quizás 
encuentre otra forma de resolver el misterio al volver a casa.
