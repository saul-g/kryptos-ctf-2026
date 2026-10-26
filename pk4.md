# El cuarto desafío: PK4

Con PK4, la progresión de dificultad se hace más evidente. Si los primeros
desafíos permitían reconocer ciertas regularidades estadísticas o patrones
visibles a simple vista, este cuarto criptograma parece haber sido diseñado
para eliminar precisamente esas ayudas. A medida que la competición avanza,
las pistas se vuelven más escasas y la frontera entre un texto cifrado y una
secuencia aparentemente aleatoria comienza a difuminarse.

La primera impresión que produce PK4 es la de un mensaje cuidadosamente
equilibrado. Ninguna letra domina claramente el conjunto, las repeticiones
resultan menos evidentes y las secuencias de caracteres parecen distribuirse
con una uniformidad notable. Esta característica obliga a abandonar las
estrategias intuitivas y a adoptar un enfoque más sistemático. Ya no basta con
identificar frecuencias llamativas; es necesario comprender cómo interactúan
los distintos elementos del criptograma y qué reglas podrían estar gobernando
su construcción.

Desde una perspectiva histórica, esta transición recuerda la evolución de la
propia criptografía. A medida que los métodos de análisis mejoraban, los
diseñadores de cifrados desarrollaban sistemas cada vez más sofisticados para
ocultar las huellas estadísticas que permitían romper mensajes anteriores. PK4
parece inspirarse en esa misma filosofía: reducir al mínimo la información
visible para obligar al analista a buscar estructuras más profundas.

Otro aspecto relevante es la longitud relativamente corta del texto. Mientras
que un criptograma más extenso suele proporcionar abundantes datos para el
análisis estadístico, los mensajes cortos limitan considerablemente la
cantidad de evidencia disponible. Esta escasez de información incrementa la
incertidumbre y hace que cada patrón observado deba interpretarse con cautela.

El criptograma es el siguiente:

```
    YOVIS YUAFK UQNRJ QLZTA ZTMQO UKELJ KCYUW IDSPS WRJRU EZNIF
    PUMUH QFFVB GOBEP WNTZG KVUTO VFSAD UJUAY GWKQY OGNKH ZVQME
    WHSJG JFOBP HXKAP EXPWR JTSPS IJLCS XYTLD FBNZN PUAZN BZPKR
    FCUZD DZHZU LZVPV WCXSI UVSCC FATGS JPNIG CJVTM UPTCG RTOFR
    XWCYK OMXOJ KCECR UCKBD CIYJ
```

Este es el primer reto de la serie que transmite la sensación de estar
contemplando un mecanismo cuidadosamente blindado, donde cada letra parece
ocupar exactamente el lugar necesario para ocultar cualquier rastro de su
significado original.


## Análisis estadístico de pk4

Si PK3 suponía una reducción significativa de las pistas visibles, PK4 lleva
esa tendencia un paso más allá. A primera vista, el criptograma exhibe una
distribución equilibrada de caracteres, una cantidad limitada de repeticiones
y una ausencia casi total de secuencias que puedan asociarse intuitivamente
con patrones lingüísticos conocidos. 

```
    Grafica de frecuencias de PK4

       16 |                                         #
       14 |                                         #
       13 |                                         #
       12 |     #             #           #         #         #
       10 |     #             # #         #     #   #         #
        9 |     #     #       # #         #     # # #         #
        8 |     #     # #     # #     # # #   # # # # # #   # #
        6 | #   #     # #   # # #     # # #   # # # # # #   # #
        5 | # # # # # # #   # # #     # # # # # # # # # # # # #
        4 | # # # # # # # # # # # # # # # # # # # # # # # # # #
        2 | # # # # # # # # # # # # # # # # # # # # # # # # # #
        1 | # # # # # # # # # # # # # # # # # # # # # # # # # #
    ------+----------------------------------------------------->
            A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

    Total de letras : 224
    Vocales         : 20.0893%
    Consonantes     : 79.9107%
    IC              : 0.0382
    Entropía        : 4.6268

```

Con 224 caracteres, el mensaje se encuentra en una zona intermedia:
suficientemente extenso para permitir estudios de frecuencia y repetición,
pero lo bastante corto como para que pequeñas variaciones estadísticas puedan
inducir interpretaciones erróneas.

Una observación preliminar revela una presencia relevante de letras como: U,
C, Z, P, J, S, K, T, F. Aunque el criptograma no presenta grandes bloques
repetidos, sí pueden identificarse algunas recurrencias locales: JKC, WRJ,
SPS, OV, UA, ZN. También aparecen algunos pares de letras repetidas: FF y CC.
Sin embargo, las repeticiones son escasas y se encuentran dispersas a lo largo
del texto, lo que dificulta extraer conclusiones inmediatas sobre la
naturaleza de la clave o del sistema de cifrado empleado.

Uno de los aspectos más interesantes de PK4 es su aparente baja redundancia.
Las repeticiones de secuencias largas son prácticamente inexistentes y la
mayoría de los grupos de tres caracteres son únicos. Desde la perspectiva del
criptoanálisis, esto puede interpretarse de dos maneras:

- El texto podría utilizar un cifrado polialfabético que dificulte la 
  repetición de patrones.

- También es posible que existan transformaciones adicionales destinadas 
  específicamente a ocultar regularidades estadísticas.

En cualquiera de los dos casos, la información disponible para un ataque
directo basado en repeticiones resulta considerablemente menor que en los
desafíos anteriores, pero aún es útil.


## Combinando transposición y substitución

Un ataque directo, nos permite recuperar la primera capa a partir de una clave
aleatoria, pero no el texto plano:

```
    Quagmire III
    ALFABETO  : KRYPTOSABCDEFGHIJLMNQUVWXZ
    CLAVE (45): RQIEKMDPAAJDXJXSXQWVSNPHFQIDFFIXRYKEOZYUQVIJL

    REATSDETONODUEMHNOAENEISNREROTEERNWTOAREPORETDOTTFEEIHAT
    YHSDAAHHALKRERSAEMNAHOODDEVOANRETETNTIHAFLETATBKIDHEEABO
    WNLLCNEIRSORSTEMAETSIRNEHTHNEETMFMIODPSERYHTSEECWDFLDBEW
    TIDLAAHMEIWIICTTGLSNWEONSNIUSEIOMTSHHEPHNTEEDARDTRSIINGK

```

El descifrado requiere de una segunda capa: una transposición columnar. 
Agrupamos el texto en una "matriz" de ``28 * 8``: 

```
    1 REATSDETONODUEMHNOAENEISNRER
    2 OTEERNWTOAREPORETDOTTFEEIHAT
    3 YHSDAAHHALKRERSAEMNAHOODDEVO
    4 ANRETETNTIHAFLETATBKIDHEEABO
    5 WNLLCNEIRSORSTEMAETSIRNEHTHN
    6 EETMFMIODPSERYHTSEECWDFLDBEW
    7 TIDLAAHMEIWIICTTGLSNWEONSNIU
    8 SEIOMTSHHEPHNTEEDARDTRSIINGK
```

Ordenando las filas:

```
    7 TIDLAAHMEIWIICTTGLSNWEONSNIU
    5 WNLLCNEIRSORSTEMAETSIRNEHTHN
    2 OTEERNWTOAREPORETDOTTFEEIHAT
    3 YHSDAAHHALKRERSAEMNAHOODDEVO
    6 EETMFMIODPSERYHTSEECWDFLDBEW
    1 REATSDETONODUEMHNOAENEISNRER
    4 ANRETETNTIHAFLETATBKIDHEEABO
    8 SEIOMTSHHEPHNTEEDARDTRSIINGK

```
y leyendo en columnas obtenemos, el texto plano y la segunda clave: 75236418:

```
    TWOYEARSINTHENEEDLESTRAILLED
    METOACRAFTSMANNAMEDTHEWHITES
    MITHONTHEROADTOHISALPINEWORK
    SHOPIREREADHISPERFUNCTORYLET
    TERSHEMETMEATTHEGATESANDLEDM
    ETOASTONEBARNSTACKEDWITHWINT
    ERFODDERONEOFHISNEEDLESISHID
    DENINTHEBARNIHAVEBEGUNTOWORK

```

Resulta que pk4 es un cifrado de 3 capas: un cifrado doble Quagmire III que
utiliza las palabras clave VERDIGRIS Y OCHRE y una transposición columnar que 
usa la palabra clave UNDERLAY. Las palabras clave VERDIGRIS Y OCHRE tienen una
longitud de 9 y 5, ambos son números primos cuyo MCM es 45. 

Verdigris (traducido al español como cardenillo, verdín o verdete) es la 
pátina de color verde o azul verdoso que se forma sobre la superficie del 
cobre, el bronce o el latón cuando estos metales se oxidan al entrar en 
contacto con el aire, la humedad o ácidos. La palabra proviene del francés
antiguo vertegrez, que significa "verde de Grecia". Químicamente, es una
mezcla de acetatos y óxidos de cobre. Una clara alusión a la placa de cobre de
Kryptos, completamente verde debido a esta reacción química. 

Ochre (traducido al español como ocre) es un pigmento natural de color 
amarillo tierra, marrón claro o rojizo. Es uno de los pigmentos más antiguos
utilizados por la humanidad (se encuentra en las pinturas rupestres de las
cuevas prehistóricas). Se obtiene a partir de arcilla mezclada con óxido de
hierro. El mismo color que la roca colocada al pie de Kryptos.

Underlay (traducido al español como capa inferior, imprimación o base) se 
refiere a la capa de material o pintura que se coloca debajo de la obra
principal. Conceptualmente, el término está ligado a Pentimento. El *underlay*
es ese dibujo o pintura base que está "escondido" debajo de la superficie 
visible. En los puzles, muchas veces necesitas "mirar debajo" o escarbar (en 
la capa inferior) para encontrar la verdad oculta.

Separado en palabras, el texto en inglés dice:

```
    Two years in. The needle's trail led me to a craftsman named The
    Whitesmith. On the road to his alpine workshop I reread his perfunctory
    letters. He met me at the gates and led me to a stone barn stacked with
    winter fodder. One of his needles is hidden in the barn. I have begun to
    work.

```

Es decir:

```

    Dos años después. El rastro de la aguja me llevó hasta un artesano llamado
    el Hojalatero (o The Whitesmith). En el camino hacia su taller alpino
    releí sus breves y superficiales cartas. Me recibió en la entrada y
    me llevó a un granero de piedra lleno de forraje para el invierno. Una de
    sus agujas está escondida en el granero. He comenzado a trabajar.

```

**Nota:** "Whitesmith" se traduce técnicamente como hojalatero, artesano del metal
blanco o pulido, a diferencia del "blacksmith" o herrero que trabaja con
hierro forjado. ¿Una referencia a Sanborn?     

El investigador ha pasado dos años enteros siguiendo el rastro de la aguja.
Finalmente localizó al hombre que la fabricó, un artesano en las montañas
alpinas. Sin embargo, el artesano no se la entregó directamente, sino que le
ha puesto una prueba clásica y literal: encontrar una aguja en un pajar (el
granero lleno de forraje). El investigador ya ha comenzado la ardua tarea de
buscarla.

Parece que la historia se está convirtiendo en un juego de búsqueda.
