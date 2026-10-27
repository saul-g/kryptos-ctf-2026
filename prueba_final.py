import numpy as np

# Configuración global del alfabeto de Kryptos
ALFABETO_KRYPTOS = "KRYPTOSABCDEFGHIJLMNQUVWXZ"

def descifrar_transposicion_columnar(texto_cifrado, clave):
    """Revierte una transposición columnar clásica usando el orden alfabético de la clave."""
    num_columnas = len(clave)
    longitud_texto = len(texto_cifrado)
    if longitud_texto == 0: 
        return ""
    
    num_filas = (longitud_texto + num_columnas - 1) // num_columnas
    celdas_vacias = (num_filas * num_columnas) - longitud_texto
    celdas_llenas_ultima_fila = num_columnas - celdas_vacias

    orden_columnas = sorted(range(num_columnas), key=lambda k: clave[k])
    
    longitudes_columnas = [num_filas] * num_columnas
    for col in range(num_columnas):
        if col >= celdas_llenas_ultima_fila:
            longitudes_columnas[col] -= 1

    columnas_texto = {}
    idx_actual = 0
    for col_idx in orden_columnas:
        lon_col = longitudes_columnas[col_idx]
        columnas_texto[col_idx] = texto_cifrado[idx_actual:idx_actual + lon_col]
        idx_actual += lon_col

    texto_plano = []
    for r in range(num_filas):
        for c in range(num_columnas):
            if r < len(columnas_texto[c]):
                texto_plano.append(columnas_texto[c][r])
                
    return "".join(texto_plano)


def descifrar_quagmire3(texto_cifrado, clave, indicator = 0, alfabeto_kryptos=ALFABETO_KRYPTOS):
    """Revierte el cifrado polialfabético Quagmire III indexado en Kryptos."""
    texto_plano = []
    longitud_clave = len(clave)
    letra_alineacion = alfabeto_kryptos[indicator]  # Por defecto alineado con 'K'
    
    for i, letra_cifrada in enumerate(texto_cifrado):
        if letra_cifrada not in alfabeto_kryptos:
            texto_plano.append(letra_cifrada)
            continue
            
        letra_clave = clave[i % longitud_clave]
        shift = (alfabeto_kryptos.index(letra_clave) - 
            alfabeto_kryptos.index(letra_alineacion)) % len(alfabeto_kryptos)
        pos_en_alfabeto_cifrado = alfabeto_kryptos.index(letra_cifrada)
        pos_original = (pos_en_alfabeto_cifrado - shift) % len(alfabeto_kryptos)
        texto_plano.append(alfabeto_kryptos[pos_original])
        
    return "".join(texto_plano)

def descifrar_hill_3x3(texto_cifrado, clave_str="ALCHEMIST", alfabeto=ALFABETO_KRYPTOS):
    """Capa 14: Revierte el cifrado Hill mediante el cálculo de la matriz inversa modular."""
    def modular_inverse_determinant(det, modulo=26):
        det = det % modulo
        for i in range(1, modulo):
            if (det * i) % modulo == 1:
                return i
        raise ValueError("Determinante no invertible en módulo 26.")

    valores = [alfabeto.index(c) for c in clave_str]
    matriz_clave = np.array(valores).reshape(3, 3)
    det = int(round(np.linalg.det(matriz_clave)))
    inv_det = modular_inverse_determinant(det % 26, 26)
    
    adjunta = np.zeros((3, 3), dtype=int)
    for i in range(3):
        for j in range(3):
            submatriz = np.delete(np.delete(matriz_clave, i, axis=0), j, axis=1)
            menor = int(round(np.linalg.det(submatriz)))
            adjunta[j, i] = ((-1) ** (i + j)) * menor
            
    matriz_inv = (adjunta * inv_det) % 26
    texto_plano = []
    
    for i in range(0, len(texto_cifrado), 3):
        bloque = texto_cifrado[i:i+3]
        if len(bloque) < 3:
            texto_plano.append(bloque)
            continue
        vector_cifrado = np.array([alfabeto.index(c) for c in bloque])
        vector_plano = np.dot(matriz_inv, vector_cifrado) % 26
        texto_plano.append("".join([alfabeto[num] for num in vector_plano]))
        
    return "".join(texto_plano)
    
def transposicion_espiral(texto_cifrado, columnas=12):
    """Capa 20: Revierte la extracción geométrica concéntrica en espiral."""
    longitud = len(texto_cifrado)
    if longitud == 0: 
        return ""
    filas = (longitud + columnas - 1) // columnas
    
    matriz = [[None for _ in range(columnas)] for _ in range(filas)]
    
    top, bottom = 0, filas - 1
    left, right = 0, columnas - 1
    
    caracteres = list(texto_cifrado)
    idx = 0
    
    while top <= bottom and left <= right and idx < longitud:
        for i in range(top, bottom + 1):
            if idx < longitud:
                matriz[i][right] = caracteres[idx]
                idx += 1
        right -= 1
        
        if top <= bottom and left <= right:
            for j in range(right, left - 1, -1):
                if idx < longitud:
                    matriz[bottom][j] = caracteres[idx]
                    idx += 1
            bottom -= 1
            
        if top <= bottom and left <= right:
            for i in range(bottom, top - 1, -1):
                if idx < longitud:
                    matriz[i][left] = caracteres[idx]
                    idx += 1
            left += 1
            
        if top <= bottom and left <= right:
            for j in range(left, right + 1):
                if idx < longitud:
                    matriz[top][j] = caracteres[idx]
                    idx += 1
            top += 1

    texto_plano = []
    for fila in matriz:
        for car in fila:
            if car is not None:
                texto_plano.append(car)
                
    return "".join(texto_plano)

# Base de datos del ctf
pk1  = "MQRALWVSJIMSXGJSVWQPHJMDINKXGIMHNKYUTXTTGJCYIABTJUMQEOFBITNBMONGVWETDLAIJPQYMZIKBQVRXZHUIJVDJLTQHIQYHEQKFTPTJYCONAFXYWQIBONAYXGWJFFIQMVXNVQYQFMWKFEJQYZFBWKXBKDQLJRELWGWDKHECRSFBKOVQJCPYDNKXYHE"
pk2  = "HNETIOCOIOISNNENEELOWYTTLQUBDBTHTEOTRRASAHCDSEETONVRCESHRRETUPCITEWIGNIUNIGANLHJRAHMSRUINHERAEEAEAJEEEEKEEDATIIAONIXRNRHCNTLGLOIIUNSEESEGNBANTVTCSFREDIUROTNENHMRIIEROLTLSDAOOAEQIEOAPUHITHAIKHTIEUHGSLAFFSNVRSRHNNSMASTIPIAHAOEEUDESSOEONCDHAOTOOEOTSEECLADNHNTOUVSGAGTATSNEWHSATEUEETEURTRNEOGITREHMPPROBEOETOERICETGSMTEITENNSGSDRNOVTTFBTTATMLOSOPLSTARATE"
pk3  = "HWZTRPPVHZLHRBQBQOMZBACNOTHLYGBATBTKHERQHRVZWWXCTZLRRVZCROHCIOTBVJKCALNKFJHEIMKUHJPFNVBCGQYNZMOHGBUTDPTJTDSUBOLYPLSKIEMANXMFNDBCTNRTLLVQOXUBPAXQUVDNXUMCIFOGETZWHJDIWDBWQFXAOMWBBCQXYZFZBTRIQMYOFFMVWSFLPTHFFQUINGLAMSQJOPUESPIQGZZCTJVRLQMIIRROOGBWNPQMXFQDVFTCVGNRIXQKUYYKBRTWPCDHLAWC"
pk4  = "YOVISYUAFKUQNRJQLZTAZTMQOUKELJKCYUWIDSPSWRJRUEZNIFPUMUHQFFVBGOBEPWNTZGKVUTOVFSADUJUAYGWKQYOGNKHZVQMEWHSJGJFOBPHXKAPEXPWRJTSPSIJLCSXYTLDFBNZNPUAZNBZPKRFCUZDDZHZULZVPVWCXSIUVSCCFATGSJPNIGCJVTMUPTCGRTOFRXWCYKOMXOJKCECRUCKBDCIYJ"

pk5  = "IJQUVJJINKWMJBNJHKZZMTVTUBFHXZJIUHOVONZNXKFUALEMYWTNNNILTRNVSXIXIQCLOSFZVZGTHQKZFJJHJMJTSEPAMKNMTGPVFWSWSBSIHOJWNFXDIJPJNOVBWWXJYUVVAFTIDZISJNCIGHXKLNFEQRDVYIXUXQIZFNXAKYXIUEVGRBMHWRFDZSMMDPMKIZNUQUJNXVZTGHCNAUVIYZCLRAVMJKAOIBOPZTJUPACSTFFLERTGBFFNCYTAVIRXXYOXHCDWHWWKAMQO"
pk6  = "BXFIVOAJFNMLKEVEHDFJQCMVLMGNVOHCJNBOAEVRRWIJFMCWMNOOMMOSRNKYOCFRYWKHBNMYCYHDECQCFNTOXNOBKBHWBOMNHFIIZDBJRNXBABFRCBLIIBLDCINOHNLXSBKVMSBNVOFVNBFYDJEVUGMNOBMLCQACBLGNABEBCJXBEYUIBDTFOSOULYCQHBXUHSEYMCBJIIHWDCFSEVLDMMUOVFADHUMKXCGUCQIRGBCEIJFYIXOEJYHDJHMXTDIEXNDAFBMOJMYAEYBVYNFSCXBWNYOVFDXDHWFCERDEBWZUKDIJTUGCJMMVQII"
pk7  = "FNRHTKRHSEDEJMBOWBDSCSDDXLICXULMBYQXWTGUIVNDYZBEQLVHFFFIDAKDCCJKWGOOUESCYELYMRAKIUJCUSEAXUQTYKOBVYDYMRBYWOTQEESCQSMDYDQJNPSWRSUOFMFJDYXSHCXNHVJVBYMZOZOATHTEOVLOQWZITHTEAFMKGLASTBZRDMFRJPKWJOXZXPJCBOVAZEPKAEJPPSIUJODXTXERWTLTTYMRENBJGTNMLBDJMYJDDLRCXCQCHYMJMHBEOLXEUFNJKBPRSHTEYXB"
pk8  = "COPVEJJVSVURTVIPYOTPLHGBTMAUCCPESIWIGZBWSJPKTRPUEKQFIFCLHMXTHIMHWOYIGURBOMPARCVXVKBDDVBVHDRHGCVNWWVLBMYWMWHICFIXZWBVZYCQGNOGJGUMLNPUTHQCXNWPQZOIRJZGSWVPY"
pk9  = "KSYAWFEYYOISZGEUFBLYATAIBYFAQBQYYVDWJKLJXMYIEPIFVHPQNHZGSUHUUDXLEHRHUMALHEGLHXSJMUXGNUIVBXGUJHZRZGUSVHMLSCTSUQXHSUMQQIFUQGKHJGUQGLHDKEWSKAMHIJXD"
pk10 = "UBINFYJSFQXQVRLJJAJDGBXIWKDMAREZTGSHQWRXCHEPCLYSDNGYRRBTCVOZJYVLYWREJTCDOYVEYCJJVZKRMKTRPGVHRWMJSRCSHXZMJEVQKJYJJAYZKDFQBGRSWXATJMEXKFXAXKSIZXOERFESNVCGCNRHEOBCNCBUPXTJJRCIMDMRUVZWRDRRFXAPGPIGSPLILFIZSTDZYOVQGGDFUFZPUOJPJVWREUVRQIYPCEHGYUZUKWTFXELUNOKBANZFTFRMXZSXXQSBGPCWGXPFSCANSVUYLMTZIRCCCJJPBQAEPWVCDIMLOPOXQEGJKVQIVHEFAPQMVCYSQAFKCTYTPAOOJZCWIPGDPAFTINBFFHVXYEQXCEIDJJOUABBAHSWKHGMLJBXDSQEFBBDLTLJPLZPIPPTRGDRZIZPUPYJODOCSOYCZZWTKYWMBQTFMFEQZWVPQYLJTMEYKYBNOPEPUMHCFJSLFWOISWLKFFABTYFQDTEQBDELIEOZQ"

# Resultados
texto1  = descifrar_quagmire3(pk1, clave="PROVENANCE")        
texto2  = descifrar_transposicion_columnar(pk2, clave="MARGINS") 

texto3  = descifrar_quagmire3(pk3, clave="PENTIMENTO") 
texto3  = descifrar_quagmire3(texto3, clave="ORDINATE") 
texto4  = descifrar_quagmire3(pk4, clave="VERDIGRIS") 

texto4  = descifrar_quagmire3(texto4, clave="OCHRE") 
texto4  = descifrar_transposicion_columnar(texto4, clave="UNDERLAY") 

texto5  = descifrar_quagmire3(pk5, texto4)
texto5  = descifrar_transposicion_columnar(texto5, clave="TWOYEARS")

texto6  = descifrar_quagmire3(pk6, "PORTAL")
texto6  = descifrar_transposicion_columnar(texto6, clave="SMITHWORK")      
texto6  = descifrar_transposicion_columnar(texto6, clave="HANDIWORK")     

texto7  = descifrar_hill_3x3(pk7, "ALCHEMIST")
texto7  = descifrar_quagmire3(texto7, "ANNEAL")

texto8  = descifrar_quagmire3(pk8, clave="MASTERY")
texto8  = descifrar_quagmire3(texto8, clave="METIER")
texto8  = descifrar_quagmire3(texto8, clave="METER")
texto8  = descifrar_quagmire3(texto8, clave="METE")

texto9  = descifrar_transposicion_columnar(pk9, clave="BEAMWORK")
texto9  = transposicion_espiral(texto9)
texto9  = descifrar_quagmire3(texto9, "CLEPSIDRA")

texto10 = descifrar_transposicion_columnar(pk10, clave="BEAMWORK")
texto10 = transposicion_espiral(texto10)
texto10 = descifrar_quagmire3(texto10, "CLEPSYDRA")
texto10 = descifrar_quagmire3(texto10, clave="MASTERY")
texto10 = descifrar_quagmire3(texto10, clave="METIER")
texto10 = descifrar_quagmire3(texto10, clave="METER")
texto10 = descifrar_quagmire3(texto10, clave="METE")
texto10 = descifrar_hill_3x3(texto10, "ALCHEMIST")
texto10 = descifrar_quagmire3(texto10, "ANNEAL")
texto10 = descifrar_quagmire3(texto10, "PORTAL")
texto10 = descifrar_transposicion_columnar(texto10, clave="SMITHWORK") 
texto10 = descifrar_transposicion_columnar(texto10, clave="HANDIWORK") 
texto10 = descifrar_quagmire3(texto10, texto4)
texto10 = descifrar_transposicion_columnar(texto10, clave="TWOYEARS")
texto10 = descifrar_quagmire3(texto10, clave="VERDIGRIS")
texto10 = descifrar_quagmire3(texto10, clave="OCHRE") 
texto10 = descifrar_transposicion_columnar(texto10, clave="UNDERLAY")
texto10 = descifrar_quagmire3(texto10, clave="PENTIMENTO")
texto10 = descifrar_quagmire3(texto10, clave="ORDINATE") 
texto10 = descifrar_transposicion_columnar(texto10, clave="MARGINS")      
texto10 = descifrar_quagmire3(texto10, clave="PROVENANCE") 

print("[-] Procesando PK1...")
print(texto1)
print("[-] Procesando PK2...")
print(texto2)
print("[-] Procesando PK3...")
print(texto3)
print("[-] Procesando PK4...")
print(texto4)
print("[-] Procesando PK5...")
print(texto5)
print("[-] Procesando PK6...")
print(texto6)
print("[-] Procesando PK7...")
print(texto7)
print("[-] Procesando PK8...")
print(texto8)
print("[-] Procesando PK9...")
print(texto9)
print("[-] Procesando PK10...")
print(texto10)


# [-] Procesando PK1...
# INVESTIGATIONLOGITEMEIGHTKNOTTIGHTLYWOUNDITSTHREADINSCRIBEDWITHLETTERSTHEACCESSIONLOGSAYSONCEUNRAVELEDITREVEALSTHEROUTETOTHELOSTARCHIVEOFPELLEGRINTWELVEPRIORARCHIVISTSTRIEDTOUNRAVELITALLFAILED
# [-] Procesando PK2...
# IHAVEFOUNDREFERENCESTOTHEKNOTINSEVENOTHERRECORDSINOURARCHIVETHEMOSTINTRIGUINGISAPASSINGCOMMENTINATREATISEONTEXTILESWRITTENINPELLEGRINSOWNHANDWHICHSAYSUNAGOTANTOSOTTILEDALEGGEREQUALUNQUENODOIBELIEVEDTHISTOBEJUSTATURNOFPHRASEBUTTHEOTHERMENTIONSSCATTEREDTHROUGHMARGINALIAINBOOKSTHATSHARENOOTHERTOPICHAVELEDMETOSUSPECTTHEPASSAGEREFERSTOAREALOBJECTANEEDLE
# [-] Procesando PK3...
# SEVENTHMONTHIWROTETOFIFTEENCORRESPONDENTSINSIXCOUNTRIESSEEKINGANYWORDOFTHEITEMMOSTKNEWNOTHINGAFEWHADHEARDLEGENDSOFANEEDLEFINEENOUGHTOSPLITAHAIRORPIERCEGLASSATLASTAVIENNESEANATOMISTSAIDHESAWSUCHANINSTRUMENTUSEDATASURGICALDEMONSTRATIONINBERNIWROTETOHISADDRESSNOANSWERCAMEIWROTEAGAIN
# [-] Procesando PK4...
# TWOYEARSINTHENEEDLESTRAILLEDMETOACRAFTSMANNAMEDTHEWHITESMITHONTHEROADTOHISALPINEWORKSHOPIREREADHISPERFUNCTORYLETTERSHEMETMEATTHEGATESANDLEDMETOASTONEBARNSTACKEDWITHWINTERFODDERONEOFHISNEEDLESISHIDDENINTHEBARNIHAVEBEGUNTOWORK
# [-] Procesando PK5...
# FOURTEENDAYSINTHEBARNIWORKEDINTHEMANNEROFANARCHIVISTLIFTINGEACHBALEONTOACLOTHANDEXAMININGTHESTRAWSINROWSTHEWHITESMITHBROUGHTFOODANDWATERBUTNOCOUNSELTHISMORNINGIFELTTHENEEDLEPRICKMYFINGERSOFINETHATITDREWNOBLOODICARRIEDITTOTHEWHITESMITHANDHETOOKITFROMMEANDOPENEDTHEINNERDOOR
# [-] Procesando PK6...
# THEWHITESMITHSWORKSHOPISFILLEDWITHTHEOLDTOOLSOFHISTRADEMYEYESAREDRAWNTOTHEGUTTERALONGTHEWALLWHICHISSTREWNWITHEXQUISITENEEDLESTHEWHITESMITHSAYSHEMAKESONEEVERYDAYANDLOSTCOUNTLONGAGOIASKWHATHEDOESWITHTHEMANDHESAYSTHEYAREONLYTHERESIDUEOFHISPRACTICEHETELLSMETHATIFISTUDYUNDERHIMFORTENYEARSHEWILLLETMETAKEONEOFMYOWNMAKING
# [-] Procesando PK7...
# THREEWEEKSINWERISEBEFORETHESUNANDEACHNEEDLEISDONEBYNOONTHEWHITESMITHSHOWSMEHISTECHNIQUEFORPURIFYINGHISMETALBEFOREDRAWINGITINTOAFINEWIREHEHASMEREPEATTHESAMESTEPFOURTIMESWITHSLIGHTVARIATIONSSTILLMYHANDFALTERSIAMPATIENTBUTIKNOWTHISISNOTMYCALLINGIHAVEMADEPEACEWITHITANDWILLGOHOMESOON
# [-] Procesando PK8...
# ILEAVEATMIDNIGHTBEFOREGOINGIPICKUPONENEEDLEFROMTHEGUTTERIAMGRATEFULTOMYTEACHERBUTTHEARCHIVEISMYTRUECALLINGANDTHEKNOTAWAITSILEAVETHEWHITESMITHASHORTLETTER
# [-] Procesando PK9...
# ISPENLTHEPASTMMNTHWITHTRENEEDLEASDKNOTANDQTLASTPELTEGRINSFISALMESSAGXHASBEENRXVEALEDTOOEIWILLNODSEALITFOHYOUUNDERXVERYCIPHXRIUSEDINLHISTESTAOENT
# [-] Procesando PK10...
# IHAVENOTREADTHESTRANDTHENEEDLEWASASFINEASPROMISEDBUTMYHANDWASNOTFITTOWIELDITANDTHEKNOTREFUSEDTOYIELDPELLEGRINANDTHEWHITESMITHTRIEDTOTEACHMEBUTWHENTHETESTCAMEIFAILEDTHEMBOTHHADISTAYEDWITHTHEWHITESMITHANDLEARNEDTHEDISCIPLINEHETAUGHTTHOSEYEARSWOULDHAVESHAPEDMYHANDSINTOINSTRUMENTSWORTHYOFTHENEEDLEANDTHEKNOTANDATLASTGIVENMETHELOCATIONOFTHEARCHIVEPELLEGRINHIDITFORONLYSUCHASUCCESSORTHROUGHPATIENCEDISCIPLINEANDTRUECRAFTTOYOUWHOHAVEUNRAVELEDMYMESSAGESYOURHANDISTHENEEDLEIHAVEFINALLYFORGEDANDILEAVETHEKNOTTOYOU
