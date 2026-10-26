# El quinto desafío: PK5

A medida que la serie avanza, los criptogramas dejan de ser simples ejercicios
de identificación de patrones para convertirse en problemas de interpretación.
Una especie de puzle criptográfico. Con PK5, el desafío alcanza un punto en
el que las herramientas clásicas de observación ofrecen resultados ambiguos y
contradictorios. Lo que en los primeros retos parecía una búsqueda de
regularidades visibles se transforma ahora en un desafío donde la principal
dificultad consiste en determinar qué información es realmente significativa.

La primera impresión que produce PK5 es paradójica. Por un lado, el texto
conserva algunos elementos familiares: repeticiones locales y una longitud
suficiente para realizar análisis estadísticos sólidos. Por otro, ninguna de
estas características parece ofrecer una dirección clara. El criptograma
muestra una combinación de uniformidad y redundancia cuidadosamente
equilibrada, como si hubiese sido diseñado para sugerir múltiples líneas de
investigación sin revelar inmediatamente cuál de ellas conduce a la solución.

Esta ambigüedad constituye una de las características más interesantes de los
desafíos criptográficos avanzados. En lugar de ocultar completamente la
información, un buen criptograma presenta patrones que pueden interpretarse de
distintas maneras. Algunos resultan útiles; otros son simples coincidencias.
La tarea consiste en distinguir ambos enfoques. En este sentido, PK5 supone
una transición desde el análisis puramente técnico hacia una forma de
razonamiento más estratégica.

```
    IJQUV JJINK WMJBN JHKZZ MTVTU BFHXZ JIUHO VONZN XKFUA LEMYW
    TNNNI LTRNV SXIXI QCLOS FZVZG THQKZ FJJHJ MJTSE PAMKN MTGPV
    FWSWS BSIHO JWNFX DIJPJ NOVBW WXJYU VVAFT IDZIS JNCIG HXKLN
    FEQRD VYIXU XQIZF NXAKY XIUEV GRBMH WRFDZ SMMDP MKIZN UQUJN
    XVZTG HCNAU VIYZC LRAVM JKAOI BOPZT JUPAC STFFL ERTGB FFNCY
    TAVIR XXYOX HCDWH WWKAM QO

```

La creciente complejidad de los retos obliga a considerar la posibilidad de
mecanismos criptográficos combinados (capas). Los métodos que funcionan bien
contra un único sistema fracasan cuando varias transformaciones interactúan
entre sí. Por ello, en PK5 se amplía el repertorio analítico y se contemplan
enfoques que vayan más allá de los procedimientos clásicos basados únicamente
en frecuencias o sustituciones.

La sensación al enfrentarse a este reto es la de encontrarse ante una
estructura cuidadosamente construida para resistir las aproximaciones más
directas. 


## Análisis estadístico de PK5

Con PK5, la dificultad no sólo aumenta desde el punto de vista conceptual,
sino también desde la perspectiva estadística. El criptograma presenta un
equilibrio peculiar entre orden y dispersión: contiene suficientes
repeticiones para sugerir la existencia de una estructura subyacente, pero no
las suficientes como para revelar inmediatamente su naturaleza. 

```
    Grafica de frecuencias de PK5

       18 |
       16 |                 # #       #
       15 |                 # #       #
       13 |           #     # #       #               #   #   #
       12 |           #     # #       #           #   #   #   #
       10 |           #   # # #     # #           # # # # #   #
        9 | #         #   # # # #   # #           # # # # #   #
        7 | #         #   # # # #   # # #       # # # # # #   #
        6 | # # #     #   # # # #   # # #   # # # # # # # # # #
        4 | # # # # # # # # # # # # # # # # # # # # # # # # # #
        3 | # # # # # # # # # # # # # # # # # # # # # # # # # #
        1 | # # # # # # # # # # # # # # # # # # # # # # # # # #
    ------+----------------------------------------------------->
            A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

    Total de letras : 272
    Vocales         : 19.4853%
    Consonantes     : 80.5147%
    IC              : 0.0406
    Entropía        : 4.5960

```

Con una longitud de 272 caracteres, PK5 ofrece una cantidad de datos adecuada
para realizar estudios de frecuencia, análisis de secuencias repetidas y
búsqueda de posibles periodicidades. Sin embargo, los resultados iniciales son
menos transparentes de lo que cabría esperar en un cifrado clásico.

Una inspección preliminar muestra una notable concentración de caracteres
pertenecientes al grupo: N, J, Y, X, V, Z, F. Especialmente destacables son
las apariciones de las letras: N, J, Y, Z, que son letras poco frecuentes en
Inglés. No hay ausencia de letras. Además el IC no es tan bajo como PK4.
El reducido número de vocales se mantiene, por la mitad. 

A diferencia de PK4, donde se observaba una distribución más homogénea, PK5
parece favorecer un conjunto reducido de símbolos que se repiten con
frecuencia. Uno de los elementos más interesantes del criptograma es la
aparición relativamente frecuente de letras idénticas: JN, MJ, NX, TG, UV, XI.
Asimismo, se observan secuencias que aparecen en más de una ocasión o que
muestran estructuras similares. Ninguna de estas repeticiones resulta
concluyente por sí sola. 

Aunque a primera vista PK5, parece ser un cifrado polialfabético. El 
comportamiento de la estructura interna es más complejo. 


## Dos años después

En el contexto de la criptografía, la mención de **Viena** en los textos
recuperados no es casualidad; guarda importantes conexiones históricas con el
desarrollo y la ruptura de los códigos secretos, el nombre también se asocia
con otro cifrado llamado Vernam. Dos años (TWOYEARS), es la cantidad de tiempo
que le tomo al investigador encontrar la aguja en el pajar alpino (en Berna). 

PK5 usa un cifrado OTP combinado con la clásica transposición columnar.

```
    Transposición columnar: 
    CLAVE: TWOYEARS
    
    Quagmire III 
    ALFABETO  : KRYPTOSABCDEFGHIJLMNQUVWXZ
    CLAVE(224): Texto claro de PK4
```

Cuando un cifrado de la familia Vigenère utiliza una clave tan larga como el
propio texto cifrado, ocurre un cambio radical en su naturaleza matemática:
deja de ser un Vigenère convencional y se convierte en lo que se conoce como
un One-Time Pad (OTP), un cifrado de Vernam, o un cifrado Vigenère-Vernam.

La forma en que se comporta y si puede ser roto depende estrictamente de
**cómo fue generada la clave**.

Si la clave cumple con estas tres reglas:

1. Es **completamente aleatoria** (generada por un proceso físico impredecible).
2. Tiene **exactamente la misma longitud** que el mensaje.
3. Se usa **una sola vez** y jamás se vuelve a reutilizar.

Es Matemáticamente imposible de romper. En 1949, el matemático Claude Shannon 
demostró mediante la teoría de la información que el OTP posee secreto
perfecto.

**¿Por qué no se puede romper?**

Dado un texto cifrado, cualquier texto plano de la misma longitud es 
igualmente probable. Al no haber ninguna pista estadística ni patrón
recurrente, el criptoanalista se queda sin herramientas matemáticas para saber
cuál es la respuesta correcta entre infinitas opciones válidas.

En la práctica, las "claves tan largas como el texto" a menudo se implementan 
mal. Si la clave larga se sale de las reglas del OTP, **se puede romper** 
utilizando los siguientes enfoques:

1. Si el emisor usa la **misma clave larga** para cifrar dos mensajes distintos 
   el sistema queda comprometido.

2. Si en lugar de usar bits aleatorios, alguien decide usar un párrafo de un 
   libro, un poema o una frase escrita como "clave larga" se puede romper con 
   "relativa facilidad".

En PK5, la clave no es tan larga como el mensaje, pero se puede catalogar como
un cifrado OTP, aunque técnicamente sea un Quagmire III con una clave muy, muy
larga.

```

    FOURTEENDAYSINTHEBARNIWORKEDINTHEM
    ANNEROFANARCHIVISTLIFTINGEACHBALEO
    NTOACLOTHANDEXAMININGTHESTRAWSINRO
    WSTHEWHITESMITHBROUGHTFOODANDWATER
    BUTNOCOUNSELTHISMORNINGIFELTTHENEE
    DLEPRICKMYFINGERSOFINETHATITDREWNO
    BLOODICARRIEDITTOTHEWHITESMITHANDH
    ETOOKITFROMMEANDOPENEDTHEINNERDOOR

```
Separado en palabras, este texto en inglés dice:

```
    Fourteen days in the barn. I worked in the manner of an archivist, lifting
    each bale onto a cloth and examining the straws in rows. The Whitesmith
    brought food and water but no counsel. This morning I felt the needle
    prick my finger, so fine that it drew no blood. I carried it to the
    Whitesmith and he took it from me and opened the inner door.
```

En Español:

```
    Catorce días en el granero. Trabajé a la manera de un archivista,
    levantando cada paca sobre una lona y examinando las pajas en filas. El
    Hojalatero trajo comida y agua, pero ningún consejo. Esta mañana sentí que
    la aguja me pinchaba el dedo, tan fina que no derramó sangre. Se la llevé
    al Hojalatero, él la tomó de mis manos y abrió la puerta interior.

```

El investigador logró superar el desafío gracias a su paciencia y a sus
métodos meticulosos de archivista, revisando la paja fila por fila durante dos
semanas. La aguja es tan increíblemente delgada que casi ni se siente al
pinchar. Al encontrarla, el Hojalatero valida su esfuerzo y le da acceso a una
nueva zona secreta ("la puerta interior"), lo que significa que está un paso
más cerca de resolver el misterio del nudo y el archivo perdido. 

¡El protagonista ha cruzado el portal! La historia continúa...
