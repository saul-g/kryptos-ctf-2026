# El octavo desafío: PK8

Una de las primeras características que llama la atención de PK8 es su
relativa brevedad. A diferencia de los desafíos anteriores, donde la
abundancia de caracteres permitía obtener muestras estadísticas razonablemente
robustas, aquí la cantidad de información disponible es mucho menor. Esta
limitación incrementa el riesgo de interpretar como significativos patrones
que no son más que fluctuaciones aleatorias.

Paradójicamente, la reducción del tamaño no implica una reducción de la
complejidad. De hecho, ocurre lo contrario. Los criptogramas cortos suelen
ser particularmente difíciles de analizar porque ofrecen menos evidencia para
contrastar hipótesis. En estos casos, los métodos basados exclusivamente en
frecuencias o repeticiones pierden parte de su eficacia, obligando al
investigador a complementar el análisis estadístico con consideraciones
estructurales y criptográficas de mayor alcance.

Otro elemento destacable es la apariencia equilibrada del texto. No existen
bloques repetidos de forma evidente ni concentraciones extremas de
determinados caracteres. La distribución parece suficientemente uniforme como
para dificultar la identificación inmediata de un sistema de sustitución,
pero también conserva ciertas irregularidades que sugieren la presencia de
una estructura subyacente. 

El criptograma es el siguiente:

```
    COPVE JJVSV URTVI PYOTP LHGBT MAUCC PESIW IGZBW SJPKT RPUEK 
    QFIFC LHMXT HIMHW OYIGU RBOMP ARCVX VKBDD VBVHD RHGCV NWWVL 
    BMYWM WHICF IXZWB VZYCQ GNOGJ GUMLN PUTHQ CXNWP QZOIR JZGSW 
    VPY

```
El texto ofrece pocas pistas evidentes. La clave del desafío podría no
encontrarse en las letras individuales, sino en los textos anteriores. 


## Análisis estadístico de PK8

A primera vista, PK8 es menos extenso que los retos anteriores. Sin embargo,
esta reducción de tamaño no implica necesariamente una menor dificultad. Por
el contrario, los criptogramas más cortos suelen ofrecer menos información
estadística y, por tanto, reducen la capacidad del analista para validar
hipótesis mediante métodos clásicos. En este caso, cada repetición, cada
frecuencia anómala y cada posible correlación adquieren una importancia mucho
mayor.

```

    Grafica de frecuencias de PK8

       12 |                                           #
       11 |                                           #
       10 |                               #           # #
        9 |     #           #             #           # #
        8 |     #       # # #             #           # #
        7 |   # #       # # #       #     #           # #
        6 |   # #       # # #       #   # #   #   # # # #
        5 |   # #       # # # #     #   # #   #   # # # #   # #
        4 |   # #       # # # #   # # # # # # # # # # # # # # #
        3 |   # # # # # # # # # # # # # # # # # # # # # # # # #
        2 | # # # # # # # # # # # # # # # # # # # # # # # # # #
        1 | # # # # # # # # # # # # # # # # # # # # # # # # # #
    ------+----------------------------------------------------->
            A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

    Total de letras : 153
    Vocales         : 16.9935%
    Consonantes     : 83.0065%
    IC              : 0.0395
    Entropía        : 4.5665

```

El criptograma contiene 153 caracteres (un número triangular), una longitud
suficiente para realizar observaciones preliminares, aunque insuficiente para
extraer conclusiones definitivas. Esto nos obliga a interpretar los resultados
con prudencia y a evitar sobrevalorar patrones que podrían aparecer
simplemente por azar.

Una primera inspección revela una presencia destacada de las siguientes
letras: V, W, C, P, I, H. No existe una concentración extrema en dos o más
letras concretas. La distribución parece relativamente equilibrada, aunque
ciertas consonantes aparecen con más frecuencia de la que cabría esperar en un
texto natural. También hay que notar, el bajo número de vocales.

Esta ausencia de redundancia visible resulta coherente con sistemas que buscan
romper las correlaciones presentes en el texto original, como un Quagmire.
Entre los indicios que apuntan en esta dirección destacan:

- La ausencia de patrones lingüísticos reconocibles.
- La distribución relativamente uniforme de frecuencias.
- La escasez de secuencias largas repetidas.
- La conservación de ciertas repeticiones locales.

Aunque, el análisis preliminar no permite identificar de forma exacta el
sistema empleado, sí apunta hacia la existencia de una transformación de tipo
poligráfico. En consecuencia, PK8 exige un enfoque más analítico que
estadístico. 


## ¿Un cifrado de flujo?

El método de Kasinski es prometedor. Devuelve 7 como longitud probable de la
clave. Pero no tiene éxito. Aunque puede ser cualquiera de sus múltiplos, 14,
28, 35... No hay resultados. Otra probable longitud es 54 y 58, aunque no son
múltiplos de 7. Incluso 70. Con un cifrado tan corto y una clave tan larga,
debemos atacar el problema desde otra perspectiva. ¿Qué provoca este
comportamiento? 

PK8 es por mucho el reto más complicado de la serie. Fue catalogado por los
participantes como "la bestia que no caía" debido a un drástico incremento en
la dificultad que dejó varada a la comunidad y a los grupos de investigación
criptográfica durante meses. Como en los retos anteriores, lo más probable es
que se trate de un cifrado de varias capas.

En ese tiempo, el creador del reto (Dan Robinson) lanzó una pista pública en
la red social X afirmando de manera enigmática: "Resolver PK9 probablemente
ayude a resolver PK8, por razones que no compartiré". Además dio otras pistas
indicando que el algoritmo base era "simple" pero que la clave poseía mucha
entropía con cierta estructura interna. 

En realidad era PK7, el texto que contenía algunas pistas. "Tres semanas
después" ¿Un Quagmire III? En específico, esta línea: "Me hace repetir el
mismo paso cuatro veces con ligeras variaciones". ¿Un Quagmire III aplicado
cuatro veces?

Al final PK8 resulto ser un cifrado Quagmire III construido enteramente sobre
la superposición secuencial de cuatro capas distintas de sustitución
polialfabética. Un texto cifrado cuatro veces consecutivas con Quagmire III 
utilizando claves periódicas se convierte en un cifrado polialfabético con un
periodo resultante masivo.

Debido a que las longitudes de las claves (4, 5, 6, 7) son números coprimos 
entre sí (o casi, excepto 4 y 6 cuyo mínimo común múltiplo es 12), el periodo 
total del cifrado combinado es el mínimo común múltiplo de sus longitudes:

```

    mcm(4, 5, 6, 7) = 420;

```

Esto significa que el patrón de sustitución se repite cada 420 caracteres,
actuando casi como un cifrado de flujo o de clave continúa.

Se puede romper, pero requiere una cantidad considerable de texto cifrado
(idealmente varios miles de caracteres) para poder aplicar análisis
estadístico con éxito. Cuando el texto es muy corto (menor a la clave), un
ataque puramente estadístico no es viable y se tiene que recurrir a fuerza
bruta o a conocer parte del texto en claro. El método más efectivo para esta
tarea es usar fuerza bruta escalonada (atacar capa por capa). Ya que resolver
las cuatro capas simultáneamente mediante análisis de frecuencias tradicional
(como el test de Kasiski o el índice de coincidencia) fallará de inmediato
porque el periodo de 420 aplana por completo las estadísticas del idioma. 


**El ataque de Hill Climbing** 

El método estándar en criptoanálisis para este escenario es el ataque de Hill
Climbing (Escalada de colinas) asistido por n-gramas, aplicado de atrás hacia
adelante. Este proceso se puede resumir en tres pasos:

**Paso 1: Definir la función de aptitud**

Para saber si te estás acercando a la solución, necesitas un algoritmo que
mida qué tan parecido es un texto al inglés. Esto se hace usando tetragramas
(bloques de 4 letras como T-H-E-R, A-N-D-I). El texto correcto tendrá una
puntuación de aptitud notablemente más alta que el ruido aleatorio.

**Paso 2: Romper la última capa (clave de 7 letras)**

En lugar de adivinar las 4 claves a la vez (lo cual es matemáticamente
imposible por el tamaño del espacio de búsqueda), intentas "pelar" la última
capa:

1. Asumes una clave aleatoria de 7 letras y un alfabeto mezclado estimado para 
   la cuarta capa.
2. Descifras el texto solo con esa cuarta capa.
3. Mides la función de aptitud del resultado.
4. Modificas levemente la clave de 7 letras (cambias una letra por otra). Si 
   la puntuación mejora, conservas el cambio.
5. Repites esto miles de veces mediante el algoritmo de Hill Climbing.

Aunque las primeras 3 capas sigan cifradas (periodo de mcm(4, 5, 6) = 60), 
cuando se remueve la capa de 7 letras correctamente, el periodo general baja 
drásticamente de 420 a 60, lo cual genera un pico estadístico sutil pero 
detectable mediante tetragramas.

**Paso 3: Romper las capas restantes en reversa**

Una vez que el algoritmo encuentra la clave de la cuarta capa (el periodo baja
a 60):

1. Aplicas el mismo proceso de Hill Climbing para la tercera capa (clave de 6 
  letras). Al removerla, el periodo baja a 20 (mcm(4, 5)).

2. Repites para la segunda capa (clave de 5 letras). El periodo baja a 4.

3. Finalmente, con un periodo de 4, la primera capa se rompe directamente con
   análisis de frecuencias.

Las cuatro claves utilizadas para cifrar PK8 son:

- METE
- METER
- METIER
- MASTERY

Estas cuatro palabras abarcan desde el dominio absoluto de una técnica hasta 
la medición y el destino. En el contexto de la historia, encajan a la 
perfección con los temas de la disciplina del archivista, el arte del 
Hojalatero y las mediciones precisas del tiempo.

La palabra *mastery* (maestría / dominio) significa el dominio absoluto, la 
pericia o la habilidad suprema sobre un arte, ciencia o técnica.
Está directamente relacionado con el clímax de la historia del nudo de 
Pellegrin. El archivista fracasó porque quería el premio sin haber alcanzado 
la maestría (mastery) que solo otorgan diez años de práctica y disciplina con 
el Hojalatero.

La palabra *metier* (oficio / vocación) es una palabra de origen francés 
adoptada por el inglés que significa oficio, profesión o la especialidad en la
que alguien destaca o tiene un talento natural. Se usa para hablar de la
verdadera vocación de una persona. En la historia, el archivista se da cuenta 
de que la forja de metales no era su oficio (métier).

La palabra meter (metro / medidor) tiene dos significados principales 
dependiendo de cómo se use en inglés: 

* Unidad de medida: el metro (distancia).
* Aparato de medición: Un medidor o contador (como un parquímetro, un medidor 
  de luz, o un dispositivo que mide el paso del tiempo, el agua o la 
  electricidad).

Este término suele aparecer al interactuar con dispositivos mecánicos,
engranajes o distancias en planos arquitectónicos.

La palabra mete (imponer / distribuir) es un verbo en inglés antiguo 
(generalmente usado hoy en la frase "to mete out") que significa repartir, 
dosificar, administrar o imponer un castigo, una recompensa o el destino de 
manera severa o justa.


## El mismo pasó cuatro veces

Las coincidencias estadísticas y los picos en el IC no eran provocados por la
repetición simple de las mismas letras del alfabeto, sino por la conjunción
matemática exacta entre el texto plano y las dos primeras claves. Esto
provocaba que las herramientas tradicionales de descifrado automatizado
fallaran al intentar aislar las capas por separado, requiriendo un ataque
coordinado de fuerza bruta.

```

    PK8: 
    Quagmire III
    ALFABETO: KRYPTOSABCDEFGHIJLMNQUVWXZ
    CLAVES: METE, METER, METIER, MASTERY

```
La supuesta "conexión" técnica resultó ser un juego psicológico que mandó a
los investigadores a un callejón sin salida analizando matrices y
transposiciones complejas durante semanas, cuando la solución de PK8 era
matemáticamente "simple" pero requería fuerza bruta inteligente sobre su
estructura repetitiva.

```

    ILEAVEATMIDNIGHTBEFOREGOINGIPICKUPONENEEDLEFROMTHEGUTTERIAMGRATEFULT
    OMYTEACHERBUTTHEARCHIVEISMYTRUECALLINGANDTHEKNOTAWAITSILEAVETHEWHITE
    SMITHASHORTLETTER

```
Separado en palabras, este texto en Inglés dice:

```
    I leave at midnight. Before going I pick up one needle from the gutter. I
    am grateful to my teacher but the archive is my true calling and the knot
    awaits. I leave the Whitesmith a short letter.
```

En Español:

```
    Me voy a medianoche. Antes de irme, recojo una aguja de la canaleta. Estoy
    agradecido con mi maestro, pero el archivo es mi verdadera vocación y el
    nudo espera. Le dejo al Hojalatero una breve carta.

```
Esta vez el texto revela un giro inesperado en la historia. El investigador
decide "robar" la aguja y huir. Aunque en el texto anterior decía que se
rendía y regresaría a casa, decide no irse con las manos vacías. Planea su
partida en secreto, a la medianoche, para no ser descubierto. Aprovechando que
el taller estaba lleno de miles de agujas tiradas en el canal de la pared (las
que el artesano consideraba simple "residuo"), el investigador toma una de
ellas. Para él es la llave de su misterio, pero para el artesano es algo sin
valor. Justifica sus acciones porque comprende que su destino no es forjar
metal, sino ser archivista y resolver el misterio del nudo para encontrar el
archivo perdido de Pellegrin. A pesar de marcharse a escondidas y robar la
aguja, no siente rencor hacia el artesano; se siente agradecido por lo
aprendido y le deja una carta de despedida explicando su partida.

El protagonista ha decidido romper las reglas del artesano para mantenerse
fiel a su verdadera misión. Ahora que tiene la aguja en su poder, está listo
para regresar y deshacer el nudo que doce archivistas antes que él no pudieron
abrir.

¿Lograra su misión?
