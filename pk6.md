# El sexto desafío: PK6

A medida que la serie avanza, los criptogramas muestran una tendencia clara
hacia la reducción de las pistas visibles y al aumento de la complejidad
metodológica. Sin embargo los textos descifrados empiezan a revelar pistas. PK6
representa un paso decisivo en esa dirección. Su apariencia es la de un texto
cuidadosamente desordenado, donde las frecuencias parecen equilibradas, las
repeticiones son escasas y las secuencias recurrentes apenas destacan sobre el
conjunto. El resultado es un mensaje que transmite una sensación de coherencia
interna, pero cuya lógica permanece oculta.

El texto cifrado es el siguiente:

```

    BXFIV OAJFN MLKEV EHDFJ QCMVL MGNVO HCJNB OAEVR RWIJF MCWMN
    OOMMO SRNKY OCFRY WKHBN MYCYH DECQC FNTOX NOBKB HWBOM NHFII
    ZDBJR NXBAB FRCBL IIBLD CINOH NLXSB KVMSB NVOFV NBFYD JEVUG
    MNOBM LCQAC BLGNA BEBCJ XBEYU IBDTF OSOUL YCQHB XUHSE YMCBJ
    IIHWD CFSEV LDMMU OVFAD HUMKX CGUCQ IRGBC EIJFY IXOEJ YHDJH
    MXTDI EXNDA FBMOJ MYAEY BVYNF SCXBW NYOVF DXDHW FCERD EBWZU
    KDIJT UGCJM MVQII
```

Este desafío nos obliga a replantearnos una cuestión fundamental: ¿es el
cifrado tan complejo como parece o simplemente está diseñado para aparentarlo?
A lo largo de la historia de la criptografía, muchos sistemas han demostrado
que la verdadera dificultad no reside necesariamente en la fortaleza
matemática del algoritmo, sino en la forma en que éste oculta las
regularidades que los analistas utilizan para orientarse. PK6 parece explotar
precisamente esta idea, reduciendo la cantidad de información directamente
observable y obligando a buscar evidencias más sutiles.

Otro aspecto relevante es que, a estas alturas, ya no puede asumirse que cada
reto se resuelva mediante una única técnica. Se debe contemplar la posibilidad
de transformaciones múltiples, capas sucesivas de codificación o mecanismos
diseñados expresamente para frustrar las aproximaciones más habituales. En
consecuencia, la fase de reconocimiento del problema se vuelve tan importante
como el proceso previo de descifrado.

Es el primer reto de la serie que transmite la sensación de que la respuesta
podría encontrarse no en los patrones evidentes, sino en las relaciones
ocultas que emergen únicamente cuando el criptograma se observa desde una
perspectiva diferente.

## Análisis estadístico de PK6

Si PK5 introducía el concepto de las falsas pistas, PK6 parece diseñado para
diluirlas por completo entre una gran cantidad de información aparentemente
homogénea. El criptograma combina una longitud considerable con una
distribución visual relativamente uniforme de caracteres, lo que dificulta
identificar regularidades evidentes mediante una simple inspección visual.

```
    Grafica de frecuencias de PK6

       27 |
       25 |   #
       23 |   #
       21 |   #
       19 |   # #                   #
       17 |   # #     #             # # #
       15 |   # # #   #     #       # # #
       13 |   # # # # #   # # #     # # #           #     #
       11 |   # # # # #   # # #     # # #           #   # #
        9 |   # # # # #   # # #     # # #           #   # #
        7 | # # # # # #   # # #   # # # #   #     # # # # #
        5 | # # # # # # # # # # # # # # # # # #   # # # # #
        3 | # # # # # # # # # # # # # # # # # # # # # # # #
        1 | # # # # # # # # # # # # # # # # # # # # # # # # #
    ------+----------------------------------------------------->
            A B C D E F G H I J K L M N O Q R S T U V W X Y Z

    Total de letras : 315
    Vocales         : 21.5873%
    Consonantes     : 78.4127%
    IC              : 0.0463
    Entropía        : 4.4673

```

Con aproximadamente 315 caracteres, PK6 es uno de los mensajes más extensos de
la serie hasta este punto. Esta longitud proporciona una muestra
suficientemente representativa para aplicar técnicas clásicas de
criptoanálisis, aunque la aparente uniformidad del texto sugiere que los
resultados deberán interpretarse con cautela.

Una primera observación revela una elevada presencia de ciertas letras, entre
las que destacan: B, M, C, O, N, F, I, D. En particular, aparecen con notable
frecuencia: B, M, C. Aunque el texto parece homogéneo, una inspección más
cuidadosa permite identificar diversos elementos repetidos: OO, II, MM, RR.
Fragmentos recurrentes: BL, EV, EY, HD, MN, NOB, NO.

Asimismo, aparecen múltiples secuencias de tres y cuatro caracteres que
comparten estructuras similares sin ser exactamente idénticas. Este fenómeno
puede ser consecuencia de una trasformación basada en claves periódicas.


## Cifrado producto

En comparación con PK4 y PK5, PK6 es extremadamente "sencillo". El análisis
inicial devuelve una longitud de clave de 6, que se combina con una
transposición columnar doble.

```

    Quagmire3 
    ALFABETO: KRYPTOSABCDEFGHIJLMNQUVWXZ
    CLAVE: PORTAL

    Doble transposición columnar 
    CLAVE1: 316249785 (HANDIWORK)
    CLAVE2: 742819563 (SMITHWORK)

```

Combinar un **cifrado por transposición** con un cifrado **polialfabético** da
lugar a lo que en criptografía se conoce como un **cifrado producto**.  Este
tipo de sistemas son radicalmente más seguros que usar cualquiera de los dos
métodos por separado, ya que atacan los dos pilares fundamentales de la
seguridad clásica: la **confusión** (ocultar la relación entre la clave y el
texto cifrado, lograda por la sustitución) y la **difusión** (esparcir la
influencia de cada letra del texto plano por todo el mensaje, lograda por la
transposición).

**¿Cómo influye el orden?**

El orden en el que se aplican las capas cambia por completo las 
herramientas que el criptoanalista puede utilizar para romper el sistema:

A) **Sustitución primero, transposición después**

Primero se aplica el cifrado polialfabético (aplanando las frecuencias 
de las letras) y luego se mezclan las posiciones de las letras 
resultantes mediante una transposición (columnas, filas, etc.).

El texto final tiene frecuencias planas y posiciones totalmente desordenadas.
Es un diseño clásico muy sólido. Para romperlo, el criptoanalista suele tener
que adivinar primero la transposición para volver a juntar las letras en su
orden lógico, y luego lidiar con el Vigenère.

B) **Transposición primero, sustitución después**

En este caso, primero se desordena el texto plano mediante una transposición,
y sobre el texto desordenado se aplica el cifrado Vigenère.

Aquí ocurre un fenómeno criptoanalítico clave. El test de Kasiski y el cálculo
del índice de coincidencia dependen de encontrar distancias regulares entre
palabras o secuencias repetidas. Al aplicar una transposición antes del
Vigenère, se rompen y dispersan las distancias físicas entre los patrones
repetidos del texto plano. Esto destruye la efectividad del método de Kasiski
tradicional, haciendo que la tarea de adivinar la longitud de la clave
polialfabética sea muchísimo más difícil.

¿Qué pasa si se aplican dos transposiciones consecutivas antes del cifrado
polialfabético? Si se aplica una transposición, y al resultado se le aplica
otra transposición inmediata antes de pasar por el cifrado polialfabético, 
Matemáticamente esas dos transposiciones se colapsan en una sola, siempre y
cuando utilicen la misma técnica de cifrado.

**¿Por qué ocurre esto?**

En teoría matemática (teoría de grupos), el conjunto de todas las 
permutaciones posibles es cerrado bajo la composición. Aplicar una regla de
desorden (permutación A) seguida de otra regla de desorden (permutación B)
equivale exactamente a aplicar una sola regla combinada (permutación C). Por
lo tanto, aplicar dos transposiciones seguidas no añade seguridad exponencial
ni crea una complejidad nueva; el resultado final es idéntico al que se
obtiene aplicando una transposición más compleja o profunda.

Literalmente hemos cruzado el portal del hojalatero:

```
    THEWHITESMITHSWORKSHOPISFILLEDWITHTHEOLDTOOLS
    OFHISTRADEMYEYESAREDRAWNTOTHEGUTTERALONGTHEWA
    LLWHICHISSTREWNWITHEXQUISITENEEDLESTHEWHITESM
    ITHSAYSHEMAKESONEEVERYDAYANDLOSTCOUNTLONGAGOI
    ASKWHATHEDOESWITHTHEMANDHESAYSTHEYAREONLYTHER
    ESIDUEOFHISPRACTICEHETELLSMETHATIFISTUDYUNDER
    HIMFORTENYEARSHEWILLLETMETAKEONEOFMYOWNMAKING

```
Este es el texto en Ingles con espacios:

```

    The whitesmith's workshop is filled with the old tools of his trade. My
    eyes are drawn to the gutter along the wall which is strewn with exquisite
    needles. The whitesmith says he makes one every day and lost count long
    ago. I ask what he does with them and he says they are only the residue of
    his practice. He tells me that if I study under him for ten years he will
    let me take one of my own making."

```
y en Español

```
    El taller del hojalatero está lleno de las viejas herramientas de su
    oficio. Mis ojos son atraídos hacia la canaleta a lo largo de la pared, la
    cual está repleta de agujas exquisitas. El hojalatero dice que hace una
    cada día y que perdió la cuenta hace mucho tiempo. Le pregunto qué hace
    con ellas y dice que son solo el residuo de su práctica. Me dice que si
    estudio con él durante diez años, me dejará llevarme una hecha por mí
    mismo.

```

Este texto es una poderosa alegoría sobre la maestría, el proceso de
aprendizaje y la verdadera naturaleza del éxito. Las "agujas exquisitas" 
acumuladas en la canaleta son descritas por el maestro simplemente como el
"residuo de su práctica". Esto significa que para un verdadero maestro, el
objeto final no es lo importante; lo valioso es el acto diario de practicar y
mejorar la habilidad.

El maestro le advierte al aprendiz que necesitará diez años de estudio antes
de poder crear algo que valga la pena conservar. Nos recuerda que no existen
los atajos para la genialidad; requiere paciencia, disciplina y años de
esfuerzo constante. Al dejar las hermosas agujas tiradas en una canaleta, el 
artesano demuestra que no trabaja por fama, dinero o por acumular posesiones,
sino por el puro amor a la perfección de su oficio.

El texto da un giro inesperado y presenta un enorme obstáculo en la historia.
El investigador pensaba que buscaba una aguja legendaria y única en el mundo.
Sin embargo, al entrar al taller, descubre que el canal de la pared está
repleto de miles de esas mismas agujas perfectas. El Hojalatero no tiene
intenciones de regalarle ninguna de las agujas que ya fabricó, ni siquiera la
que el investigador tardó dos semanas en encontrar en el granero. Para obtener
la herramienta necesaria para deshacer el nudo, el investigador no puede
simplemente  comprarla o robarla. El artesano le impone una condición extrema:
quedarse a vivir allí y convertirse en su aprendiz durante diez años para
aprender a fabricar su propia aguja.

El viaje del investigador se ha detenido por completo. Para resolver el 
misterio del nudo (que ya le tomó dos años encontrar), ahora se enfrenta 
al dilema de tener que sacrificar una década de su vida trabajando 
como aprendiz en las montañas.

¡La historia se ha puesto muy intensa!
