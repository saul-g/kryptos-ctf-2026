# El primer desafío: PK1

Todo desafío criptográfico comienza con una primera puerta. En el caso del
Paradigm Kryptos CTF, ese punto de partida es PK1, el primero de los diez
acertijos concebidos para recrear el espíritu intelectual que ha convertido a
Kryptos en una de las obras más misteriosas de la historia de la
criptografía. Aunque independiente del enigma original K4, estos retos
comparten una misma filosofía: obligar al participante a cuestionar sus
suposiciones, explorar patrones ocultos y desarrollar métodos de análisis más
eficientes.

El texto cifrado que inicia esta serie de retos es el siguiente:

```

    MQRAL WVSJI MSXGJ SVWQP HJMDI NKXGI MHNKY UTXTT GJCYI ABTJU 
    MQEOF BITNB MONGV WETDL AIJPQ YMZIK BQVRX ZHUIJ VDJLT QHIQY 
    HEQKF TPTJY CONAF XYWQI BONAY XGWJF FIQMV XNVQY QFMWK FEJQY 
    ZFBWK XBKDQ LJREL WGWDK HECRS FBKOV QJCPY DNKXY HE
```

A primera vista, el criptograma presenta una larga secuencia de caracteres
agrupados en bloques regulares de cinco letras, una convención ampliamente
utilizada en la criptografía clásica para dificultar el reconocimiento de
palabras y estructuras gramaticales. La ausencia de espacios significativos,
signos de puntuación y referencias contextuales obliga al investigador a
concentrarse exclusivamente en los patrones internos del texto: frecuencias,
repeticiones, simetrías y posibles relaciones entre los distintos fragmentos.
Lejos de ser una elección estética, esta presentación evoca las prácticas
históricas de la criptografía manual. Antes de la era digital, los mensajes
cifrados eran frecuentemente transmitidos en grupos uniformes para ocultar
cualquier pista relacionada con la longitud de las palabras o la estructura
del lenguaje original. 

Como ocurre con muchos enigmas criptográficos, la dificultad inicial no
consiste únicamente en romper el cifrado, sino en identificar correctamente la
naturaleza del problema. En este sentido, PK1 se presenta como el primer
portal de la competición: una invitación a pensar como criptógrafo y a
adentrarse en el mismo tipo de razonamiento que, durante décadas, ha rodeado
al misterio de Kryptos.


## Tecnicas de Criptoanálisis

Cuando se ataca un criptograma desconocido, el proceso del criptoanálisis
incluye a grandes rasgos:

- Calcular el índice de coincidencia (IC) global.
- Ver porcentaje de vocales.
- Ver distribución de frecuencias.

Si es un cifrado por transposición:

- Buscar patrones de longitud de bloques.
- Anagramas.
- Alineación de columnas.
- Alineación de filas.
- Patrones geométricos.

Si es un cifrado polialfabético:

- Ejecutar método de Kasiski.
- Probar longitudes de clave.
- Ataque con diccionario. 
- Calcular IC medio de columnas.
- Seleccionar las mejores longitudes.
- Atacar cada columna como un cifrado César.
- Reconstruir la clave.
- Atacar con hill climbing o simulated annealing usando tetragramas.

Reglas rápidas:

- IC ≈ 0.665 -> Sustitución simple o transposición.
- IC ≈ 0.040 -> Muy probable Vigenère o polialfabético.
- IC ≈ 0.038 -> Prácticamente aleatorio. 

A partir de este punto, toda certeza desaparece y comienza el trabajo del
analista: transformar la secuencia incomprensible de símbolos en información
significativa. Ese es, precisamente, el arte de la criptografía.  


## Transposición y sustitución polialfabética

Distinguir un **cifrado por transposición** de uno por **sustitución**
**polialfabética** es fundamental en criptoanálisis. Aunque ambos ocultan el
mensaje original, operan bajo principios matemáticos y estructurales
totalmente opuestos. Las diferencias clave se pueden dividir en tres aspectos
fundamentales: la transformación aplicada, el comportamiento estadístico y las
huellas digitales que dejan.

Un cifrado por transposición reordena la posición de las letras del mensaje
original, pero **jamás cambia su identidad**. Las letras que ves en el texto
cifrado son exactamente las mismas que componen el texto plano, solo que han
sido mezcladas siguiendo un patrón geométrico o una ruta (por ejemplo,
escribiendo el mensaje en columnas y leyéndolo en filas, como en la *scytale*
espartana o la transposición columnar). Es como recortar cada letra de una
frase en papel y mezclar el orden de las piezas sobre una mesa; las letras
siguen siendo las mismas, solo cambió su ubicación.

En un cifrado por sustitución polialfabética se mantiene el orden original de
las posiciones de las letras, pero **se reemplaza cada letra** por otra
diferente. Lo que lo hace *polialfabético* (como el célebre cifrado de
Vigenère) es que cambia de alfabeto de sustitución a medida que avanza el
mensaje. Una misma letra del mensaje original (por ejemplo, la "A") puede
cifrarse como una "X" al principio del texto, como una "M" en el medio y como
una "Q" al final, dependiendo de una clave repetitiva. 

En la transposición como las letras originales no han sido alteradas en su
naturaleza, el análisis de frecuencias global del texto cifrado es idéntico al
del idioma original. Si el texto está en español, la letra "E" o la "A"
seguirán apareciendo con la misma proporción estadística alta, solo que
dispersas por todo el criptograma. Para romperlo, el criptoanalista busca
patrones de longitud de bloques o anagramas.

En la sustitución polialfabética cambia y oculta las frecuencias naturales del
idioma. Como una misma letra adopta múltiples identidades cifradas según la
clave, la letra más común del español o del Inglés ("E") ya no destacará de
forma aislada en las estadísticas globales. El análisis de frecuencias
tradicional (monoalfabético) se neutraliza. Para romperlo, se emplean técnicas
estadísticas avanzadas orientadas a hallar la longitud de la clave, siendo el
**Método Kasiski** o el cálculo del **Índice de coincidencia** las
herramientas estándar.


### Análisis estadístico de PK1

El primer contacto con un criptograma suele estar marcado por la
incertidumbre. Ante una sucesión aparentemente caótica de letras, el
observador se enfrenta a una pregunta fundamental: ¿se trata de un mensaje
cifrado mediante una técnica conocida o de una construcción diseñada para
desafiar nuestras intuiciones? PK1, nos sitúa precisamente en ese punto de
partida, donde la observación resulta tan importante como el conocimiento
técnico.

Antes de abordar cualquier hipótesis de descifrado, resulta conveniente
realizar un examen cuantitativo del texto cifrado. Este tipo de análisis
permite identificar posibles regularidades y ofrece las primeras pistas sobre
la naturaleza del sistema criptográfico empleado.

```

    Grafica de frecuencias de PK1

       15 |                                 #
       14 |                                 #
       13 |                   #             #
       12 |                   #             #
       11 |                 # #             #               #
       10 |                 # # #           #               #
        9 |           #     # # #   #       #     #     # # #
        8 |   #       #     # # #   # #     #     #   # # # #
        7 |   #     # #   # # # #   # #     #     #   # # # #
        6 |   #   # # # # # # # #   # #     #     #   # # # #
        5 | # #   # # # # # # # # # # # #   #     #   # # # #
        4 | # # # # # # # # # # # # # # # # # # # #   # # # #
        3 | # # # # # # # # # # # # # # # # # # # # # # # # # #
        2 | # # # # # # # # # # # # # # # # # # # # # # # # # #
        1 | # # # # # # # # # # # # # # # # # # # # # # # # # #
    ------+----------------------------------------------------->
            A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

    Total de letras : 192
    Vocales         : 16.1458%
    Consonantes     : 83.8542%
    IC              : 0.0400
    Entropia        : 4.5780

```

El criptograma PK1 contiene un total de 192 caracteres. La frecuencia de
aparición de las letras es irregular y el índice de coincidencia no se apega
al valor esperado en el idioma Inglés: 0.665 aproximadamente. La frecuencia de
vocales es baja. En Inglés el porcentaje esperado es del 38% aproximadamente.

Un aspecto llamativo es la elevada presencia de letras poco frecuentes en
Inglés, como Q, J, I, Y, K, F y la ausencia de letras comunes como E, T, A.
Esta característica suele aparecer en sistemas de sustitución o en cifrados
polialfabéticos donde las frecuencias naturales del idioma quedan ocultas.

Una de las métricas más utilizadas en criptografía clásica es el índice de
coincidencia (IC), que mide la probabilidad de que dos letras elegidas al
azar sean iguales. 

Para PK1 se obtiene:

```
    0.0400
```

Este valor resulta particularmente interesante porque:

- Un texto aleatorio completamente uniforme suele presentar un IC cercano 
  a 0.0385.
- Un texto en Inglés sin cifrar suele situarse alrededor de 0.065.
- Los cifrados de sustitución simple conservan aproximadamente el IC del 
  lenguaje original.
- Los cifrados polialfabéticos tienden a reducir el IC hacia valores 
  cercanos al azar. También suelen tener una entropía más cercana al azar 
  que las sustituciones simples. Por ejemplo: Vigenère: ~4.5 bits/letra,
  texto aleatorio: ~4.7 bits/letras.

La distribución de frecuencias presenta una notable entropía compatible con
técnicas polialfabéticas destinadas a ocultar las propiedades estadísticas
del texto original. Lo que sugiere que el criptograma podría haber sido
generado mediante un cifrado Vigenère. Lo que en el universo de Kryptos se
conoce como Quagmire III. El mismo que usan las secciones 1 y 2.


## El cifrado Quagmire III

El cifrado Quagmire es una familia de cuatro variantes de cifrados de 
sustitución polialfabética periódica desarrollada por la Asociación
Americana de Criptogramas (American Cryptogram Association o ACA).
Funciona como una extensión avanzada del clásico cifrado de Vigenère.
Mientras que Vigenère utiliza un alfabeto estándar ordenado de la A a la
Z, el cifrado Quagmire introduce alfabetos mezclados mediante palabras
clave, lo que dificulta el criptoanálisis y los ataques basados en
análisis de frecuencia.

Para utilizar cualquier variante de Quagmire, se necesitan tres elementos 
principales:

1. Un alfabeto de texto plano (las letras del mensaje original).
2. Un alfabeto de texto cifrado (las letras que resultarán en el mensaje 
   secreto).
3. Una palabra clave indicadora (o frase clave) que determina el periodo 
   de repetición y la alineación de los alfabetos.

Para "mezclar" un alfabeto, se toma una palabra clave, se eliminan las
letras repetidas y el resto del alfabeto se completa en orden con las
letras que no se han usado.


### Como se rompe un cifrado Quagmire

El cifrado Quagmire III utiliza alfabetos clave tanto para el texto plano como
para el texto cifrado, lo que añade una capa adicional de complejidad. Sin
embargo, el método Kasiski es efectivo para determinar la longitud de la
clave. Una vez que se conoce la longitud de la clave, se puede proceder con
el análisis de frecuencia para descifrar el texto.

Esta es la forma en que funciona:

1. **Buscar secuencias repetidas**: identificar secuencias de tres o más 
   caracteres que se repiten en el texto cifrado.
2. **Calcular las distancias**: medir las distancias entre las apariciones 
   consecutivas de las secuencias repetidas.
3. **Encontrar el máximo común divisor (MCD)**: calcular el MCD de las 
   distancias encontradas. Este valor es probable que sea la longitud de 
   la clave o un múltiplo de ella.
4. **Dividir el texto cifrado**: una vez determinada la longitud de la 
   clave, dividir el texto cifrado en columnas, donde cada columna 
   corresponde a una letra de la clave.
5. **Aplicar análisis de frecuencia**: tratar cada columna como un 
   cifrado de sustitución monoalfabético y aplicar análisis de frecuencia 
   para descifrar el texto. Como alternativa se puede usar la prueba χ² 
   (chi-cuadrado) que puede funcionar mejor.

Este método es efectivo porque las secuencias repetidas en el texto
cifrado indican que la clave se ha alineado de la misma manera en ambas
apariciones de la secuencia.


## El archivo perdido de Pellegrin

PK1 emplea un cifrado de sustitución polialfabética Quagmire III utilizando el
alfabeto ``KRYPTOS`` y la palabra clave ``PROVENANCE`` con el indicador base
fijado en K. 

La tabla de cifrado usado para el proceso de (des)cifrado es la siguiente:   

```
    PT : K R Y P T O S A B C D E F G H I J L M N Q U V W X Z 
    CT : P T O S A B C D E F G H I J L M N Q U V W X Z K R Y 
    CT : R Y P T O S A B C D E F G H I J L M N Q U V W X Z K 
    CT : O S A B C D E F G H I J L M N Q U V W X Z K R Y P T 
    CT : V W X Z K R Y P T O S A B C D E F G H I J L M N Q U 
    CT : E F G H I J L M N Q U V W X Z K R Y P T O S A B C D 
    CT : N Q U V W X Z K R Y P T O S A B C D E F G H I J L M 
    CT : A B C D E F G H I J L M N Q U V W X Z K R Y P T O S 
    CT : N Q U V W X Z K R Y P T O S A B C D E F G H I J L M 
    CT : C D E F G H I J L M N Q U V W X Z K R Y P T O S A B 
    CT : E F G H I J L M N Q U V W X Z K R Y P T O S A B C D 

```
La palabra clave **PROVENACE** es un término en Inglés (derivado del francés
provenir) que significa "procedencia" u "origen". En el mundo del arte, el
coleccionismo y la arqueología, la provenance es la biografía o el historial
documentado de una obra. Consiste en el registro cronológico de todas las
manos por las que ha pasado un objeto desde el momento de su creación. Un
registro completo de provenance incluye nombres de coleccionistas, galerías o
museos que poseyeron la pieza, fechas de compra, venta, subastas o herencias,
historial de exhibiciones, menciones en literatura: libros de arte, catálogos
o revistas donde la obra haya sido analizada por expertos. 

La palabra provenance garantiza la autenticidad. Si una obra tiene una cadena 
de propiedad clara e ininterrumpida, es muchísimo más fácil demostrar que es 
original y no una falsificación.  Además permite verificar que el objeto no
fue robado, saqueado ilegalmente de un yacimiento arqueológico o confiscado
durante periodos de guerra. Una alusión clara a la compra legitima de K4.

Al sustituir cada letra cifrada (CT), por la letra que le corresponde en la
tabla, obtenemos el texto plano:

```
    INVESTIGATIONLOGITEMEIGHTKNOTTIGHTLYWOUNDITSTHRE
    ADINSCRIBEDWITHLETTERSTHEACCESSIONLOGSAYSONCEUNR
    AVELEDITREVEALSTHEROUTETOTHELOSTARCHIVEOFPELLEGR
    INTWELVEPRIORARCHIVISTSTRIEDTOUNRAVELITALLFAILED

```
Agregando espacios, podemos leer el primer mensaje:

```
   Investigation log item eight. Knot tightly wound, its thread
   inscribed with letters. The accession log says once unraveled it
   reveals the route to the lost archive of Pellegrin. Twelve prior
   archivists tried to unravel it, all failed."
```

En Español:

```
    Elemento ocho del registro de investigación. El nudo está
    fuertemente enrollado, su hilo inscrito con letras. El registro de
    acceso dice que una vez desenredado revela la ruta hacia el archivo
    perdido de Pellegrin. Doce archivistas anteriores intentaron
    desenredarlo, todos fallaron.

```

El texto es una nota de misterio que describe un objeto antiguo y una misión
sin resolver. Al parecer, intenta decir lo siguiente:

* **El objeto misterioso:** se ha encontrado un objeto catalogado como el 
  "elemento ocho". Es un nudo de hilo muy apretado que tiene letras 
  escritas a lo largo de toda su cuerda.

* **El secreto que esconde:** según los registros antiguos, si alguien 
  logra deshacer el nudo por completo y estirar el hilo, las letras 
  revelarán un mapa o las indicaciones para llegar a un lugar secreto 
  llamado "el archivo perdido de Pellegrin" ¿Acaso k4?.

* **Una advertencia:** es una tarea extremadamente difícil o peligrosa, 
  ya que doce expertos (archivistas) del pasado intentaron resolver el 
  acertijo y todos fracasaron. Probablemente una pista. 

El texto plantea un desafío para el protagonista o investigador de la
historia: intentar resolver el misterio del nudo donde doce personas
antes ya fallaron.
