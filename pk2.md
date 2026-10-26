# El segundo desafío: PK2

El segundo criptograma de la serie introduce un escenario radicalmente
distinto. Mientras que el primer reto parecía ocultar cuidadosamente
cualquier rastro de estructura lingüística reconocible, PK2 presenta una
lectura mucho más sugerente. Desde la primera inspección visual, el texto
revela una notable abundancia de determinadas letras y combinaciones
recurrentes, como si bajo la aparente aleatoriedad del cifrado persistieran
vestigios del lenguaje original. 

Esta característica convierte a PK2 en un ejercicio particularmente "sencillo"
de criptoanálisis. El desafío ya no consiste en enfrentarse a una secuencia de
símbolos aparentemente aleatorios, sino en determinar si las regularidades
observadas representan pistas auténticas o constituyen parte del mecanismo de
ocultación. Como en muchos retos de la criptografía clásica, la frontera entre
señal y ruido no siempre resulta evidente.

El criptograma es el siguiente:

```
    HNETI OCOIO ISNNE NEELO WYTTL QUBDB THTEO TRRAS AHCDS EETON
    VRCES HRRET UPCIT EWIGN IUNIG ANLHJ RAHMS RUINH ERAEE AEAJE
    EEEKE EDATI IAONI XRNRH CNTLG LOIIU NSEES EGNBA NTVTC SFRED
    IUROT NENHM RIIER OLTLS DAOOA EQIEO APUHI THAIK HTIEU HGSLA
    FFSNV RSRHN NSMAS TIPIA HAOEE UDESS OEONC DHAOT OOEOT SEECL
    ADNHN TOUVS GAGTA TSNEW HSATE UEETE URTRN EOGIT REHMP PROBE
    OETOE RICET GSMTE ITENN SGSDR NOVTT FBTTA TMLOS OPLST ARATE

```

A diferencia del primer cifrado, donde las frecuencias parecen distribuidas de
manera relativamente homogénea, aquí destacan ciertas letras que aparecen con
un patrón común. Esta circunstancia sugiere que la información estadística
podría desempeñar un papel relevante en el proceso de análisis.


## Análisis estadístico de pk2

PK2 presenta desde el primer momento una característica llamativa: la
abundancia de determinadas vocales y consonantes. Este rasgo sugiere que el
criptograma conserva una parte importante de la estructura estadística del
lenguaje original o, al menos, que el método de cifrado empleado no ha
eliminado completamente dichas regularidades.

```
    Grafica de frecuencias de PK2

       50 |         #
       46 |         #
       43 |         #
       40 |         #
       36 |         #                             #
       33 |         #                             #
       30 |         #                             #
       26 | #       #                 # #         #
       23 | #       #       #         # #       # #
       20 | #       #       #         # #     # # #
       16 | #       #     # #         # #     # # #
       13 | #       #     # #         # #     # # #
       10 | #       #   # # #     #   # #     # # # #
        6 | #   # # #   # # #     # # # #     # # # #
        3 | # # # # # # # # #     # # # # #   # # # # # #
        1 | # # # # # # # # # # # # # # # # # # # # # # # # #
    ------+----------------------------------------------------->
            A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

    Total de letras : 350
    Vocales         : 40.2857%
    Consonantes     : 59.7143%
    IC              : 0.0709
    Entropia        : 4.0674

```

Con una longitud aproximada de 350 caracteres, PK2 contiene suficiente
información para aplicar métodos clásicos de análisis estadístico. El primer
aspecto destacable es el IC próximo al idioma Inglés. 

Una inspección visual permite identificar un predominio notable de las
vocales, especialmente: E, O, A, I, T, N.  Resulta significativo que muchas de
estas letras coinciden con algunas de las más frecuentes en textos escritos 
en Inglés. Asimismo, aparecen numerosas repeticiones de secuencias como:  EE,
AO, NN, TT, OE, EU, NE, TH. El porcentaje de vocales también está próximo al
Inglés. No hay Z.

La presencia recurrente de estos patrones sugiere que el cifrado podría
preservar parcialmente las frecuencias originales del mensaje o emplear una
transformación cuya difusión estadística sea limitada. Las recurrencias de
esta naturaleza constituyen material valioso para diversas técnicas de
criptoanálisis, ya que pueden corresponder a:

- Palabras frecuentes del texto original.
- Secuencias producidas por un mismo proceso de cifrado.
- Fragmentos generados a partir de claves repetitivas.

La elevada presencia de vocales y repeticiones indica una transposición, ya
que este tipo de cifrados reorganiza la información sin alterar la frecuencia
de los caracteres. ¿Pero qué tipo de transposición? La más común es la
transposición columnar.


## Transposición columnar

La transposición columnar es un método clásico de criptografía simétrica que
consiste en reordenar las letras de un mensaje sin cambiarlas por otros
símbolos. A diferencia de los cifrados de sustitución (donde una "A" se
convierte en una "Z", por ejemplo), aquí los caracteres originales siguen
siendo los mismos, pero se "mezclan" de forma sistemática utilizando una tabla
y una palabra clave.

**¿Cómo funciona?**

1. **Se escribe el mensaje en una tabla (matriz)**. Se toma el texto en claro 
  (eliminando o no los espacios, según la regla pactada) y se escribe de 
  izquierda a derecha, fila por fila, en una cuadrícula. El número de columnas 
  de la tabla lo determina la longitud de una clave alfabética. Para PK2, la 
  clave es 7.

```
    1 HNETIOCOIOISNNENEELOWYTTLQUBDBTHTEOTRRASAHCDSEETON
    2 VRCESHRRETUPCITEWIGNIUNIGANLHJRAHMSRUINHERAEEAEAJE
    3 EEEKEEDATIIAONIXRNRHCNTLGLOIIUNSEESEGNBANTVTCSFRED
    4 IUROTNENHMRIIEROLTLSDAOOAEQIEOAPUHITHAIKHTIEUHGSLA
    5 FFSNVRSRHNNSMASTIPIAHAOEEUDESSOEONCDHAOTOOEOTSEECL
    6 ADNHNTOUVSGAGTATSNEWHSATEUEETEURTRNEOGITREHMPPROBE
    7 OETOERICETGSMTEITENNSGSDRNOVTTFBTTATMLOSOPLSTARATE

```

2. **Se ordenan las columnas según la clave**. La palabra clave define el orden 
   en que se van a leer las columnas. Por lo general, se ordena alfabéticamente, 
   o según su posición numérica asignada.

```
    4 IUROTNENHMRIIEROLTLSDAOOAEQIEOAPUHITHAIKHTIEUHGSLA
    1 HNETIOCOIOISNNENEELOWYTTLQUBDBTHTEOTRRASAHCDSEETON
    6 ADNHNTOUVSGAGTATSNEWHSATEUEETEURTRNEOGITREHMPPROBE
    2 VRCESHRRETUPCITEWIGNIUNIGANLHJRAHMSRUINHERAEEAEAJE
    3 EEEKEEDATIIAONIXRNRHCNTLGLOIIUNSEESEGNBANTVTCSFRED
    5 FFSNVRSRHNNSMASTIPIAHAOEEUDESSOEONCDHAOTOOEOTSEECL
    7 OETOERICETGSMTEITENNSGSDRNOVTTFBTTATMLOSOPLSTARATE

```

3. **Se extrae el texto cifrado**. Se leen las letras columna por columna, 
   siguiendo el orden dictado por la clave. 

```
    IHAVEFOUNDREFERENCESTOTHEKNOTINSEVENOTHERRECORDSIN
    OURARCHIVETHEMOSTINTRIGUINGISAPASSINGCOMMENTINATRE
    ATISEONTEXTILESWRITTENINPELLEGRINSOWNHANDWHICHSAYS
    UNAGOTANTOSOTTILEDALEGGEREQUALUNQUENODOIBELIEVEDTH
    ISTOBEJUSTATURNOFPHRASEBUTTHEOTHERMENTIONSSCATTERE
    DTHROUGHMARGINALIAINBOOKSTHATSHARENOOTHERTOPICHAVE
    LEDMETOSUSPECTTHEPASSAGEREFERSTOAREALOBJECTANEEDLE
```

PK2, emplea un cifrado por transposición columnar. La clave: la secuencia 
numérica: 4162357 o la palabra clave MARGINS, tomada de MARGINALIA (del propio
texto).   

"Marginis" es una palabra en latín que significa "del borde", "de la orilla" 
o "del margen". No es una palabra independiente, sino la forma genitiva del 
sustantivo latino margo (que significa "borde" o "límite"). En la gramática 
del latín, el genitivo se utiliza para indicar propiedad, pertenencia o 
relación (equivalente a decir "del..." en español). 

De la combinación de este término tenemos palabras actuales como:

* Margen: el espacio en blanco al borde de una página o el límite de algo.
* Marginal: aquello que está en la orilla, que es secundario o que queda fuera 
  de lo principal. 

Al igual que el texto anterior, esta es una cadena continua de letras en 
Inglés que esconde una cita en italiano. Separado en palabras, el texto dice:

```

    I have found references to the knot in seven other records in our archive.
    The most intriguing is a passing comment in a treatise on textiles written
    in Pellegrin's own hand which says 'una gota tanto sottile da leggere
    qualunque nodo'. I believe this to be just a turn of phrase but the other
    mentions scattered through marginalia in books that share no other topic
    have led me to suspect the passage refers to a real object: a needle.

```
es decir:

```
    He encontrado referencias al nudo en otros siete registros de nuestro
    archivo. La más intrigante es un comentario de pasada en un tratado sobre
    textiles escrito por la propia mano de Pellegrin que dice: "una gota tan
    sutil capaz de leer cualquier nudo". Creí que esto era solo una forma de
    hablar, pero las otras menciones dispersas en las notas al margen de
    libros que no comparten ningún otro tema me han llevado a sospechar que el
    pasaje se refiere a un objeto real: una aguja.

```
**Nota:** La frase en italiano original dice "una gota tanto sottile...", lo cual 
parece un juego de palabras o un error dentro de la ficción del texto por 
"una gugliata" —una hebra de hilo— o una metáfora sobre una aguja que descifra
el nudo. La palabra marginalia proviene directamente de esta misma raíz
latina, marginis (notas escritas a mano al margen de las páginas). 

Este nuevo texto intenta explicar cómo resolver el misterio del nudo revelando
que existe una "llave" para abrirlo. Tras revisar siete documentos antiguos,
el investigador encontró una nota escrita por el mismísimo Pellegrin (el
creador o dueño del archivo perdido). Una frase en italiano que habla de algo
"tan sutil capaz de leer cualquier nudo". Al principio, el investigador pensó
que era solo una metáfora (una forma de hablar). Sin embargo, al ver que la
misma idea se repite en anotaciones escondidas en los márgenes de muchos otros
libros diferentes, llegó a una conclusión: la pista habla de un objeto real, y
ese objeto es una aguja.

Esta vez, el texto dice que el nudo del mensaje anterior no se puede deshacer 
con las manos ni con fuerza bruta (por eso fallaron los doce archivistas). 
Para revelar la ruta del mapa, se necesita encontrar una aguja específica que 
sirva como herramienta o "llave" para descifrar el hilo.
