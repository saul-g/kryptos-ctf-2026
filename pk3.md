# El tercer desafío: PK3

Con la llegada de PK3, los desafíos entran en una nueva fase. Los patrones
visibles que caracterizaban parte de los retos anteriores comienzan a
desvanecerse y el criptograma adopta una apariencia mucho más opaca. Las
repeticiones son menos frecuentes, las distribuciones parecen más homogéneas y
las herramientas que resultaban útiles en los primeros análisis empiezan a
ofrecer resultados poco concluyentes. A partir de este punto, la dificultad
deja de residir únicamente en la aplicación de técnicas conocidas y pasa a
depender, en gran medida, de la capacidad del analista para formular hipótesis
sólidas y contrastarlas de manera sistemática.

Uno de los aspectos más importantes del criptoanálisis consiste en distinguir
entre la información real y las pistas falsas. En los dos primeros desafíos
era posible identificar ciertas regularidades que orientaban la investigación
inicial. PK3, en cambio, parece diseñado para reducir al mínimo ese tipo de
indicios. El texto exhibe una distribución de caracteres más uniforme y una
notable ausencia de secuencias repetidas evidentes, características que suelen
asociarse a mecanismos de cifrado con una mayor capacidad para ocultar la
estructura original del mensaje.

Esta transición no es accidental. Dentro de la progresión planteada por 
Paradigm, PK3 marca el paso desde los ejercicios introductorios hacia retos
que exigen un análisis más profundo. En este punto, no se puede confiar
únicamente en observaciones visuales o en las frecuencias del texto. Resulta
necesario combinar distintas técnicas, examinar cuidadosamente las propiedades
estadísticas del criptograma y considerar la posibilidad de transformaciones
múltiples o sistemas más sofisticados.

El criptograma es el siguiente:

```

    HWZTR PPVHZ LHRBQ BQOMZ BACNO THLYG BATBT KHERQ HRVZW WXCTZ
    LRRVZ CROHC IOTBV JKCAL NKFJH EIMKU HJPFN VBCGQ YNZMO HGBUT
    DPTJT DSUBO LYPLS KIEMA NXMFN DBCTN RTLLV QOXUB PAXQU VDNXU
    MCIFO GETZW HJDIW DBWQF XAOMW BBCQX YZFZB TRIQM YOFFM VWSFL
    PTHFF QUING LAMSQ JOPUE SPIQG ZZCTJ VRLQM IIRRO OGBWN PQMXF
    QDVFT CVGNR IXQKU YYKBR TWPCD HLAWC

```
La aparente aleatoriedad del criptograma plantea una cuestión fundamental:
¿estamos ante un cifrado que oculta eficazmente las características del
lenguaje original o ante una construcción que solo pretende parecer más
compleja de lo que realmente es? Esta pregunta ha acompañado históricamente a
muchos de los grandes desafíos criptográficos. En numerosas ocasiones, la
dificultad únicamente reside en reconocer el sistema empleado.


# Análisis estadístico de PK3

Visualmente PK3 parece mucho más uniforme que los retos anteriores, un
análisis cuantitativo confirma esta impresión. La distribución de caracteres,
la escasez de repeticiones evidentes y la abundancia de letras poco frecuentes
sugieren que nos encontramos ante un sistema que oculta eficazmente las
propiedades estadísticas del texto original.

```

    Grafica de frecuencias de PK2

       17 |   #                                   #
       15 |   #                             #     #
       14 |   #                             #     #
       12 |   # #     #   #             #   # #   #
       11 |   # #     #   #       # #   #   # #   #           #
        9 |   # #     #   # #     # # # # # # #   #   # #     #
        8 |   # #     #   # #     # # # # # # #   # # # # #   #
        7 | # # # #   # # # #     # # # # # # #   # # # # #   #
        5 | # # # #   # # # # # # # # # # # # #   # # # # # # #
        4 | # # # # # # # # # # # # # # # # # # # # # # # # # #
        2 | # # # # # # # # # # # # # # # # # # # # # # # # # #
        1 | # # # # # # # # # # # # # # # # # # # # # # # # # #
    ------+----------------------------------------------------->
            A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

    Total de letras : 280
    Vocales         : 16.4286%
    Consonantes     : 83.5714%
    IC              : 0.0386
    Entropía        : 4.6319

```

Con una longitud aproximada de 280 caracteres, el criptograma proporciona
suficiente información para aplicar técnicas clásicas de criptoanálisis,
aunque los resultados iniciales son considerablemente menos reveladores que en
PK2. Una inspección preliminar muestra que las letras más frecuentes
pertenecen principalmente al conjunto: B, H, Q, R, T, V, W, Z

Resulta especialmente llamativa la presencia recurrente de: Z, X, V, K, J. En
un texto natural en inglés estas letras suelen aparecer con baja frecuencia.
Su abundancia en PK3 indica que las frecuencias originales han sido alteradas
de forma significativa y el IC tan bajo muestra que el sistema empleado genera
una dispersión estadística elevada.

A diferencia de PK2, donde las vocales llegaban al 40%, aquí ningún carácter
parece sobresalir de manera evidente. El resultado es un texto con una
apariencia mucho más homogénea y difícil de interpretar mediante observación
directa.

Las repeticiones siguen existiendo, pero son notablemente menos abundantes y
menos informativas que en los retos anteriores. Algunos ejemplos son: PP, RR,
LL, FF, ZZ, YY. Asimismo, aparecen determinadas secuencias repetidas: VZ, BQ,
CT, QM, NX, TR. Sin embargo, la mayoría de estas recurrencias son demasiado
cortas para permitir conclusiones inmediatas. 

El índice de coincidencia inferior al de un lenguaje natural sin cifrar y más
cercano al de los cifrados polialfabéticos clásico es consistente con un
sistema polialfabético. Si esto es correcto, entonces estamos ante un
cifrado de la familia Vigenère-Verman. 


## Cifrado Vigenère-Verman

Con la llegada del teletipo y las telecomunicaciones modernas durante la
Primera Guerra Mundial, el ingeniero de AT&T Gilbert Vernam inventó un sistema
automatizado para proteger las transmisiones de datos. Vernam patentó un
mecanismo que combinaba, de forma automática y eléctrica, los caracteres de un
mensaje en código teletípico (código Baudot) con los caracteres de una cinta
perforada que contenía la clave. Inicialmente, la cinta de la clave formaba un
bucle que se repetía.

Vernam creía que una clave aleatoria corta podía reutilizarse de forma segura
muchas veces, justificando el esfuerzo de entregar una clave tan grande; sin
embargo, la reutilización de la clave resultó ser vulnerable a ataques
Kasiski. Vernam ofreció una solución alternativa: una clave generada mediante
la combinación de dos cintas de clave más cortas de ``m`` y ``n`` dígitos
binarios, o bits, donde ``m`` y ``n`` no comparten ningún factor común
distinto de 1 (es decir, son primos). Un flujo de bits calculado de esta
manera no se repite hasta que se han producido ``m * n`` bits de la clave.

Esta versión del sistema de cifrado de Vernam fue adoptada y empleada por el
Ejército de los EE. UU. hasta que el Mayor Joseph O. Mauborgne, del Cuerpo de
Señales del Ejército, demostró durante la Primera Guerra Mundial que un
cifrado construido a partir de una clave producida al combinar linealmente dos
o más cintas cortas podía ser descifrado mediante métodos similares a los
empleados para criptoanalizar los cifrados de clave continua (running-key). El
trabajo de Mauborgne llevó a darse cuenta de que ni el sistema de cifrado de
Vernam-Vigenère de clave única repetitiva ni el de dos cintas eran
criptográficamente seguros.

Pk3 no es propiamente un cifrado Vigenère-Verman pero funciona bajo el mismo
principio. La prueba de Kasiski, es consistente con una clave de 8, 10, 20, 40
y 80. Un ataque por fuerza bruta devuelve el texto plano. PK3 usa un Quagmire
III con un alfabeto mezclado. Esta vez utiliza una clave muy larga:

```

    Quagmire III
    ALFABETO  : KRYPTOSABCDEFGHIJLMNQUVWXZ
    CLAVE (40): BFPNBZITCSGKFENPJQHQVMWIQNUBWFAVXOZATKBJ

```

Como el total de caracteres cifrados es múltiplo de la longitud de la clave,
se puede dividir el texto cifrado en dos grupos de 140 caracteres (alternando
entre grupos de 20), para buscar dos clave de 20 caracteres por separado. 

La clave continua se genera al aplicar dos palabras clave con longitud de 8 y
10 caracteres.

```
    CLAVES: PENTIMENTO, ORDINATE

```
Como patrón común en los retos de Paradigm, los desarrolladores utilizaron
palabras directamente relacionadas con la mitología y la historia de la
escultura real de la CIA. 

La palabra *pentimento* es un término técnico de origen italiano que significa
literalmente "arrepentimiento". En el mundo del arte, se refiere a la
alteración o corrección que un artista realiza en su obra durante el proceso
creativo, cambiando de opinión sobre la composición original. Ocurre cuando el
pintor decide desechar total o parcialmente un trazo, una figura o un contorno
y decide pintar encima una nueva capa para ocultarlo. Muchos de los
"arrepentimientos" permanecen invisibles al ojo humano, pero los restauradores
e historiadores del arte los descubren utilizando técnicas como la
reflectografía infrarroja o los rayos X. 

En matemáticas y geometría, *ordinate* es el término en inglés para la ordenada
(la coordenada y). Representa la distancia vertical de un punto con respecto
al eje horizontal (x) en un sistema de coordenadas cartesianas bidimensional.
En un par ordenado escrito como (x, y), el valor de x es la abscissa (abscisa)
y el valor de y es la ordinate (ordenada). 


## Cifrado en cascada

Cuando se aplica un cifrado Quagmire **con varias claves al hilo** (es decir, 
cifrar un texto con una primera clave y, sobre el resultado, se vuelve a 
cifrar con una segunda clave de manera consecutiva), el sistema entra en lo 
que se conoce criptográficamente como **cifrado en cascada**.

**¿Cómo se comporta matemáticamente?**

Al sumar los desplazamientos de ambas claves de forma consecutiva para cada
letra, el resultado es que **las dos capas de cifrado colapsan en una sola**.

Matemáticamente, si el texto plano es ``P``, la primera clave es ``K_1`` y la 
segunda es ``K_2``:

* Primera capa: C_1 = P + K_1 % 26
* Segunda capa: C_2 = C_1 + K_2 = (P + K_1) + K_2 = P + (K_1 + K_2) % 26

Esto significa que aplicar dos o más cifrados Quagmire sucesivos equivale 
exactamente a **un único cifrado** cuya clave resultante es la suma modular 
de las claves originales combinadas de forma alineada.

**¿Cómo afecta a la longitud final de la clave?**

La longitud efectiva de la clave resultante **no es la suma** de las
longitudes individuales, sino el **mínimo común múltiplo (mcm)** de ambas 
longitudes:

```
   Longitud = mcm(L_1, L_2)

```
La paridad de las longitudes de las claves altera matemáticamente la paridad 
del período resultante según las reglas de la aritmética modular y el mcm:

* **Clave par + clave impar:** El mcm resultante **siempre será un número par**. 
  Esto ocurre porque el número par aporta obligatoriamente un factor primo de 
  2, el cual estará presente de manera forzosa en el mínimo común múltiplo de 
  ambos números.

* **Clave par + clave par:** el mcm resultante **será par** (salvo casos donde 
  los múltiplos compartan factores de forma específica, pero conservan la 
  paridad).

* **Clave impar + clave impar:** el mcm resultante **será siempre impar**, ya 
  que al no existir ningún factor de 2 en ninguna de las dos longitudes 
  originales, el resultado carecerá de él.

**¿Cómo se detecta?**

Desde el punto de vista del criptoanálisis, el criptograma final es 
indistinguible de un Quagmire simple con una clave de longitud igual al mcm. 
No deja una "huella" que delate que se usaron dos claves por separado, ya que 
el sistema lo une en uno solo. Se detecta y se rompe mediante los métodos 
habituales del cifrado polialfabético:

1. **Índice de coincidencia (IC):** al tratarse de un Quagmire equivalente, el 
   IC del texto cifrado será bajo (cercano al del alfabético uniforme), lo 
   que delata inmediatamente que no es una transposición ni una sustitución 
   monoalfabética.

2. **Prueba de Friedman:** permite estimar la longitud de la clave efectiva 
   (que en este caso corresponderá directamente al ``mcm(L_1, L_2)``).

3. **El test de Kasiski:** al buscar secuencias de letras repetidas en el 
   criptograma, las distancias entre ellas revelarán múltiplos de esa longitud 
   efectiva combinada (el mcm), facilitando la separación en columnas para 
   despejar las frecuencias.

Dos claves multiplican la longitud de manera efectiva (a menos que tengan un
factor común).   


## La búsqueda continúa

Aplicando las claves ``PENTIMENTO`` y ``ORDINATE`` obtenemos el texto en
claro de PK3:

```

    SEVENTHMONTHIWROTETOFIFTEENCORRESPONDENT
    SINSIXCOUNTRIESSEEKINGANYWORDOFTHEITEMMO
    STKNEWNOTHINGAFEWHADHEARDLEGENDSOFANEEDL
    EFINEENOUGHTOSPLITAHAIRORPIERCEGLASSATLA
    STAVIENNESEANATOMISTSAIDHESAWSUCHANINSTR
    UMENTUSEDATASURGICALDEMONSTRATIONINBERNI
    WROTETOHISADDRESSNOANSWERCAMEIWROTEAGAIN

```

Agregando espacios:

```
    Seventh month. I wrote to fifteen correspondents in six countries seeking
    any word of the item. Most knew nothing. A few had heard legends of a
    needle fine enough to split a hair or pierce glass. At last, a Viennese
    anatomist said he saw such an instrument used at a surgical demonstration
    in Bern. I wrote to his address. No answer came. I wrote again."

```
Ahora en español:

```
    Séptimo mes. Escribí a quince corresponsales en seis países buscando
    alguna noticia del objeto. La mayoría no sabía nada. Unos pocos habían
    oído leyendas de una aguja lo suficientemente fina como para partir un
    cabello o perforar el cristal. Por fin, un anatomista vienés dijo haber
    visto tal instrumento utilizado en una demostración quirúrgica en Berna.
    Escribí a su dirección. No obtuve respuesta. Volví a escribir.
```
En este punto, el investigador ya lleva siete meses buscando la aguja
misteriosa descrita en el texto anterior. Su búsqueda confirma que no es una
aguja común, sino un objeto casi legendario (capaz de cortar un pelo a la
mitad o atravesar cristal sin romperlo). La pista más sólida lo lleva a Berna
(Suiza), donde un médico vio usar esa aguja en una cirugía. El investigador
está intentando contactar a la persona que la tiene en esa ciudad, pero se ha
topado con un muro de silencio, ya que no responden a sus cartas. 

El misterio se vuelve cada vez más difícil.
