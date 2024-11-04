"""
Este Programa Permite A Los Usuarios Escuchar Radios Online Y Grabar Las Transmisiones En Formato Opus. 
El Formato Opus Es Un Códec De Audio Versátil Y De Alta Eficiencia Que Soporta Tasas De Bits Variables, 
Lo Que Significa Que Puede Adaptarse A Diferentes Condiciones De Red Y Proporcionar Una Calidad De Sonido Superior.

El Uso De Opus En Este Programa Permite Grabar Las Transmisiones De Radio Con Una Excelente Relación 
Calidad-Tamaño, Asegurando Que Los Archivos Generados Sean Pequeños Sin Sacrificar La Claridad Del Audio. 
El Códec Es Especialmente Eficaz Para Contenido De Música Y Voz, Lo Que Lo Hace Ideal Para Radios En Línea.

Las Características Clave De Este Programa Incluyen:
1. **Interfaz De Usuario Simple**: Permite A Los Usuarios Navegar Por Las Opciones De Radio Y Controlar La Grabación Con Facilidad.
2. **Grabación De Audio En Tiempo Real**: Los Usuarios Pueden Grabar Lo Que Escuchan Sin Retrasos Significativos.
3. **Soporte Para Múltiples Fuentes**: Capacidad Para Agregar Varias Radios Online Y Gestionarlas De Manera Eficiente.
4. **Configuración De Calidad De Grabación**: Los Usuarios Pueden Elegir La Tasa De Bits Al Grabar, Ademas De Otras
Variables, Como VBR, Compresión, Sample Rate, Paneo 3D, Etc... Para Ajustar La Calidad Según Sus Preferencias...

Este Programa Demuestra Cómo La Programación En Python Puede Integrarse Con Tecnologías Modernas De Audio Para Crear Herramientas Útiles Y Efectivas Para Los Amantes De La Música Y La Radio.

Programador: MarcoS OchoA DieZ ( Alias: M8AX ) 
Fecha De Programación: 01 De Noviembre De 2024 - Viernes - 00:00
Duración De Programación: 1.5h
Dispositivo Utilizado: MvIiIaX - Xiaomi MI 9 Lite ( TerMuX Con PyThoN ) 
Código Formateado Con: BlacK
"""

import os
import time
import random
import sys
import multiprocessing
from datetime import datetime
from sympy import factorint


def solicitar_opcion():
    while True:
        opcion = input(
            "\nM8AX - Escribe El Número De La Opción Que Quieres ( Entre 0 Y 60 ): "
        )
        try:
            opcion_int = int(opcion)
            if 0 <= opcion_int <= 60:
                return str(opcion_int)
            else:
                print("\nM8AX - La Opción Debe Estar Entre 0 Y 60. Intenta De Nuevo...")
        except ValueError:
            print(
                "\nM8AX - Entrada No Válida. Por Favor, Introduce Un Número Entre 0 Y 60..."
            )


def obtener_fecha_formateada():
    dias_semana = {
        0: "Lunesito",
        1: "Martesito",
        2: "Miércolesito",
        3: "Juevesito",
        4: "Viernesito",
        5: "Sábadocito",
        6: "Dominguito",
    }
    meses = {
        1: "Enerito",
        2: "Febrerito",
        3: "Marzito",
        4: "Abrilito",
        5: "Mayito",
        6: "Junito",
        7: "Julito",
        8: "Agostito",
        9: "Septiembrito",
        10: "Octubrito",
        11: "Noviembrito",
        12: "Diciembrito",
    }
    fecha_actual = datetime.now()
    dia_semana = dias_semana[fecha_actual.weekday()]
    mes = meses[fecha_actual.month]
    fecha_formateada = f"El {dia_semana}, {fecha_actual.day} De {mes} De {fecha_actual.year} A Las {fecha_actual.strftime('%H:%M:%S')}"
    return fecha_formateada


def generar_y_factorizar():
    max_cifras = 50
    numero = random.randint(10 ** (max_cifras - 1), 10**max_cifras - 1)
    factores = factorint(numero)
    descomposicion = " * ".join(
        [f"{p}^{e}" if e > 1 else str(p) for p, e in factores.items()]
    )
    resultado = f"M8AX - Número: 🔢 {numero} 🔢, Descompuesto En Factores Primos Es: ( ▶︎ {descomposicion} ◀︎ )."
    return resultado


def ask_for_cores():
    num_cores = multiprocessing.cpu_count()
    while True:
        entrada = input(
            "\nM8AX - Introduce El Número De Núcleos A Usar En La Compresión A OPUS Para La Grabación En Tiempo Real... Cuantos Más Núcleos Tenga Tu CPU, Más Rápido Comprimirá. ¿ Cuántos Núcleos Usamos ?: "
        )
        try:
            xnum_coress = int(entrada)
            if xnum_coress >= 1 and xnum_coress <= num_cores:
                return xnum_coress
            else:
                print(
                    f"\nM8AX - Debes Introducir Un Número Mayor O Igual A 1 Y Menor O Igual Que {num_cores}."
                )
        except ValueError:
            print(
                "\nM8AX - Entrada No Válida. Asegúrate De Introducir Un Número Válido..."
            )


def solicitar_compresion():
    while True:
        try:
            numero = int(
                input(
                    "\nM8AX - Introduce El Factor De Compresión: ( De 0 A 10. 10 Más Compresión, 0 Menos... ): "
                )
            )
            if 0 <= numero <= 10:
                return numero
            else:
                print(
                    "\nM8AX - El Factor De Compresión Debe Estar Entre 0 Y 10. Intenta Nuevamente..."
                )
        except ValueError:
            print(
                "\nM8AX - Entrada No Válida. Por Favor, Ingresa Un Número Entero Entre 0 Y 10..."
            )


def ask_for_sample_rate(default_rate=0):
    sample_rates = ["0", "8000", "12000", "16000", "24000", "48000"]
    print(f"\nM8AX - Frecuencias De Muestreo Disponibles: {', '.join(sample_rates)} Hz")
    while True:
        user_input = input(
            "\nM8AX - Por Favor, Elige Una Frecuencia De Muestreo, ( 0 - Para Dejar La Original De La Radio Online ): "
        )
        if user_input in sample_rates:
            return user_input
        else:
            print("\nM8AX - Frecuencia No Válida, Inténtalo De Nuevo...")


def ask_for_meta():
    while True:
        choice = (
            input(
                "\nM8AX - ¿ Añadir MetaTags A Las Grabaciones ? si = Añade MetaTags no = Dejar Como Están... ( Escribe 'si' O 'no' ): "
            )
            .strip()
            .lower()
        )
        if choice in ["si", "no"]:
            return choice
        else:
            print("\nM8AX - Error: Debes Escribir 'si' O 'no'...")


def ask_for_paneo():
    while True:
        choice = (
            input(
                "\nM8AX - ¿ Añadir Paneo 3D A Las Grabaciones, 8D Music ? si = Añade Paneo no = No Añade Paneo... ( Escribe 'si' O 'no' ): "
            )
            .strip()
            .lower()
        )
        if choice in ["si", "no"]:
            return choice
        else:
            print("\nM8AX - Error: Debes Escribir 'si' O 'no'...")


os.system("clear")
os.system("figlet ... M8AX   Music ...")
print(
    "---------------------------------------------------------------------------------\n"
)
while True:
    factores = generar_y_factorizar()
    print("M8AX - Selecciona Una Opción:\n")
    print("1. Escuchar Cadena Dial")
    print("2. Escuchar Cadena Dial Baladas")
    print("3. Escuchar Cadena Ser")
    print("4. Escuchar Cadena Ser La Rioja")
    print("5. Escuchar Canal Fiesta Radio")
    print("6. Escuchar Global Radio")
    print("7. Escuchar Europa FM")
    print("8. Escuchar Europa FM Guipúzcoa")
    print("9. Escuchar Europa FM La Rioja")
    print("10. Escuchar Ibiza Global Radio")
    print("11. Escuchar Ibiza Sonica Radio")
    print("12. Escuchar Loca FM 90")
    print("13. Escuchar Loca FM Tech House")
    print("14. Escuchar Loca FM Techno")
    print("15. Escuchar Libertad Digital")
    print("16. Escuchar Mega Star")
    print("17. Escuchar Melodía FM")
    print("18. Escuchar Onda Cero La Rioja")
    print("19. Escuchar Radio 5 Madrid")
    print("20. Escuchar Radio Clásica")
    print("21. Escuchar Radio Marca Nacional")
    print("22. Escuchar Radio Nacional De España")
    print("23. Escuchar Radio Nacional La Rioja")
    print("24. Escuchar Radio Nacional Valencia")
    print("25. Escuchar Rock FM")
    print("26. Escuchar Tomorrowland Radio")
    print("27. Escuchar Radio Swiss Jazz")
    print("28. Escuchar Radio Exterior De España")
    print("29. Escuchar Radio 5 La Rioja")
    print("30. Escuchar Radio Hit FM\n")
    print(
        "---------------------------------------------------------------------------------\n"
    )
    print("31. Grabar Cadena Dial")
    print("32. Grabar Cadena Dial Baladas")
    print("33. Grabar Cadena Ser")
    print("34. Grabar Cadena Ser La Rioja")
    print("35. Grabar Canal Fiesta Radio")
    print("36. Grabar Global Radio")
    print("37. Grabar Europa FM")
    print("38. Grabar Europa FM Guipúzcoa")
    print("39. Grabar Europa FM La Rioja")
    print("40. Grabar Ibiza Global Radio")
    print("41. Grabar Ibiza Sonica Radio")
    print("42. Grabar Loca FM 90")
    print("43. Grabar Loca FM Tech House")
    print("44. Grabar Loca FM Techno")
    print("45. Grabar Libertad Digital")
    print("46. Grabar Mega Star")
    print("47. Grabar Melodía FM")
    print("48. Grabar Onda Cero La Rioja")
    print("49. Grabar Radio 5 Madrid")
    print("50. Grabar Radio Clásica")
    print("51. Grabar Radio Marca Nacional")
    print("52. Grabar Radio Nacional De España")
    print("53. Grabar Radio Nacional La Rioja")
    print("54. Grabar Radio Nacional Valencia")
    print("55. Grabar Rock FM")
    print("56. Grabar Tomorrowland Radio")
    print("57. Grabar Radio Swiss Jazz")
    print("58. Grabar Radio Exterior De España")
    print("59. Grabar Radio 5 La Rioja")
    print("60. Grabar Radio Hit FM")
    print(
        "\n---------------------------------------------------------------------------------\n"
    )
    print("0. ... Salir ...\n")
    print(
        "---------------------------------------------------------------------------------\n"
    )
    opcion = solicitar_opcion()
    os.system("clear")
    os.system("figlet ... M8AX   Music ...")
    if int(opcion) >= 31:
        download_path = input(
            "\nM8AX - Introduce El Directorio De Destino ( Donde Se Guardará La Grabación ): "
        ).strip()
        os.makedirs(download_path, exist_ok=True)
        min_bitrate = input(
            "\nM8AX - Introduce La Tasa De Bits Mínima En kbps ( Por Ejemplo, 5 ): "
        ).strip()
        if not min_bitrate:
            min_bitrate = 5
        else:
            min_bitrate = int(min_bitrate)
        minrate = str(min_bitrate) + "k"
        max_bitrate = input(
            "\nM8AX - Introduce La Tasa De Bits Máxima En kbps ( Por Ejemplo, 32 ): "
        ).strip()

        if not max_bitrate:
            max_bitrate = 32
        else:
            max_bitrate = int(max_bitrate)
        calidad = str(max_bitrate) + "k"
        vbr = (
            input(
                "\nM8AX - ¿ Habilitar VBR ? ( Escribe 'on' Para Habilitar, 'off' Para Deshabilitar O 'constrained' Que Es Como VBR On, Pero Más Controlado ): "
            )
            .strip()
            .lower()
        )
        if vbr not in ["on", "off", "constrained"]:
            print(
                "\nM8AX - Error: Debes Escribir 'on', 'off' O 'constrained' Para VBR... on Si Error..."
            )
            vbr = "on"
        rate = ask_for_sample_rate()
        com_level = solicitar_compresion()
        ecoono = ask_for_paneo()
        sitags = ask_for_meta()
        nucleos_cpu = ask_for_cores()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    alea = random.randint(0, 50)
    if ecoono == "si":
        vamos = "afftdn,silenceremove=start_periods=1:start_silence=2,apulsator=mode=sine:hz=0.1:amount=0.90"
    else:
        vamos = "afftdn,silenceremove=start_periods=1:start_silence=2"
    fechagra = obtener_fecha_formateada()
    metedato = """M8AX-MvIiIaX - Por Muchas Vueltas Que Demos, Siempre Tendremos El Culo Atrás... - M8AX-MvIiIaX
--- -🇪🇸- MarcoS OchoA DieZ -► ( M8AX ◀️👨‍💻▶️ MvIiIaX ) -🇪🇸- ---
.•♫•♬•🔥Ｍ𝚟ıııคx🔥•♬•♫•.
X∀8ꟽ
⌘•⌘ ꧁☆❤️🅼8🅰🆇❤️☆꧂ ⌘•⌘
-||| 🎸 ||| --- ＊*•̩̩͙✩•̩̩͙*˚ᛖ𝐯ᎥᎥᎥⱥx*•̩̩͙✩•̩̩͙*˚＊ --- ||| 🎸 |||-
-||| 🎹 ||| --- ░M░A░R░C░O░S░ --- ||| 🎹 |||-
-||| 📷 ||| --- MvIiIaX & M8AX 2025 - 2050 --- ||| 📷 |||-
El Futuro No Está Establecido, No Hay Destino, Solo Existe El Que Nosotros Hacemos...
La Fuerza Es Lo Que Le Da Al Jedi Su Poder, Es Un Campo De Energía Creado Por Todas Las Cosas Vivientes, Nos Rodea... Penetra En Nosotros Y Mantiene Unida La Galaxia...
Mi CPU Procesa En Red Neural, Es De Aprendizaje, Pero Skynet Solo Lee Cuando Nos Envían Solos A Una Misión...
Yo He Visto Cosas Que Vosotros No Creeríais. Atacar Naves En Llamas Más Alla De Orión. He Visto Rayos-C Brillar En La Oscuridad Cerca De La Puerta De Tannhäuser. Todos Esos Momentos Se Perderán En El Tiempo, Como Lágrimas En La Lluvia. Es Hora De Morir...
Mi Blog - ((( ★ http://mviiiaxm8ax.blogspot.com ★ )))‍
Mi OpenSea - ((( ★ https://opensea.io/es/m8ax ★ )))
Mi Canal De YouTube - ((( ★ http://youtube.com/m8ax ★ )))
Mi OnCyber - ((( ★ https://oncyber.io/@m8ax ★ )))\n"""
    metedato += f"Fecha De Grabación - {fechagra}\nBy MarcoS OchoA DieZ..."
    if rate == "0":
        meteda2 = f"{factores}\nEl Audio Se Ha Grabado Con Codec Libopus, A Los Hercios Originales, Con Un Bitrate Máximo De {calidad}, Un Bitrate Mínimo De {minrate} Y Con El VBR En {vbr}. El Nivel De Compresión Ha Sido De {com_level} De 10 Y Se Han Usado {nucleos_cpu} Núcleos De La CPU. El Directorio De Grabación Ha Sido {download_path} Y Se Ha Grabado En Esta Fecha: {timestamp} Además Se Ha Aplicado Este Filtro: {vamos}."
    else:
        meteda2 = f"{factores}\nEl Audio Se Ha Grabado Con Codec Libopus, A {rate} Hz, Con Un Bitrate Máximo De {calidad}, Un Bitrate Mínimo De {minrate} Y Con El VBR En {vbr}. El Nivel De Compresión Ha Sido De {com_level} De 10 Y Se Han Usado {nucleos_cpu} Núcleos De La CPU. El Directorio De Grabación Ha Sido {download_path} Y Se Ha Grabado En Esta Fecha: {timestamp} Además Se Ha Aplicado Este Filtro: {vamos}."
    if sitags == "no":
        metedato = ""
        meteda2 = ""
    if opcion == "1":
        comando = f"{'ffplay -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5' if alea % 2 == 0 else 'mpv --ao=pulse'} https://25543.live.streamtheworld.com/CADENADIAL.mp3"
        os.system(comando)
    elif opcion == "2":
        comando = f"{'ffplay -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5' if alea % 2 == 0 else 'mpv --ao=pulse'} https://28023.live.streamtheworld.com/CADENADIAL_03.mp3"
        os.system(comando)
    elif opcion == "3":
        comando = f"{'ffplay -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5' if alea % 2 == 0 else 'mpv --ao=pulse'} https://25493.live.streamtheworld.com/CADENASER.mp3"
        os.system(comando)
    elif opcion == "4":
        comando = f"{'ffplay -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5' if alea % 2 == 0 else 'mpv --ao=pulse'} https://22593.live.streamtheworld.com/SER_RIOJA.mp3"
        os.system(comando)
    elif opcion == "5":
        comando = f"{'ffplay -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5' if alea % 2 == 0 else 'mpv --ao=pulse'} https://cdnlive.codev8.net/rtvalive/smil:channel5.smil/playlist.m3u8"
        os.system(comando)
    elif opcion == "6":
        comando = f"{'ffplay -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5' if alea % 2 == 0 else 'mpv --ao=pulse'} https://radio.entertainmenttechnologies.co.uk:8000/stream"
        os.system(comando)
    elif opcion == "7":
        comando = f"{'ffplay -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5' if alea % 2 == 0 else 'mpv --ao=pulse'} https://atres-live.europafm.com/live/europafm/master.m3u8"
        os.system(comando)
    elif opcion == "8":
        comando = f"{'ffplay -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5' if alea % 2 == 0 else 'mpv --ao=pulse'} https://stream-156.zeno.fm/se76qau1hc9uv?zt=eyJhbGciOiJIUzI1NiJ9.eyJzdHJlYW0iOiJzZTc2cWF1MWhjOXV2IiwiaG9zdCI6InN0cmVhbS0xNTYuemVuby5mbSIsInJ0dGwiOjUsImp0aSI6Inh5ekllbERvVFVDWW85eTRXU0U2c2ciLCJpYXQiOjE3MzA0OTU3NTksImV4cCI6MTczMDQ5NTgxOX0.rCKmfp2ohVvoFtuGkg1DHdsGHsrYURlwch7tb08Rf1o"
        os.system(comando)
    elif opcion == "9":
        comando = f"{'ffplay -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5' if alea % 2 == 0 else 'mpv --ao=pulse'} https://atres-live.europafm.com/live/delegaciones/efm/logrono/master.m3u8"
        os.system(comando)
    elif opcion == "10":
        comando = f"{'ffplay -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5' if alea % 2 == 0 else 'mpv --ao=pulse'} https://ibizaglobalradio.streaming-pro.com:8024/"
        os.system(comando)
    elif opcion == "11":
        comando = f"{'ffplay -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5' if alea % 2 == 0 else 'mpv --ao=pulse'} https://stream.rcast.net/261087"
        os.system(comando)
    elif opcion == "12":
        comando = f"{'ffplay -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5' if alea % 2 == 0 else 'mpv --ao=pulse'} https://s2.we4stream.com/listen/loca_90s_/live"
        os.system(comando)
    elif opcion == "13":
        comando = f"{'ffplay -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5' if alea % 2 == 0 else 'mpv --ao=pulse'} https://s2.we4stream.com/listen/loca_tech_house/live"
        os.system(comando)
    elif opcion == "14":
        comando = f"{'ffplay -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5' if alea % 2 == 0 else 'mpv --ao=pulse'} https://s2.we4stream.com/listen/loca_techo/live"
        os.system(comando)
    elif opcion == "15":
        comando = f"{'ffplay -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5' if alea % 2 == 0 else 'mpv --ao=pulse'} https://libertaddigital-libremercado-live.flumotion.com/libertaddigital/libremercado-high.aac"
        os.system(comando)
    elif opcion == "16":
        comando = f"{'ffplay -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5' if alea % 2 == 0 else 'mpv --ao=pulse'} https://megastar-cope.flumotion.com/playlist.m3u8"
        os.system(comando)
    elif opcion == "17":
        comando = f"{'ffplay -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5' if alea % 2 == 0 else 'mpv --ao=pulse'} https://atres-live.melodia-fm.com/live/melodiafm/master.m3u8"
        os.system(comando)
    elif opcion == "18":
        comando = f"{'ffplay -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5' if alea % 2 == 0 else 'mpv --ao=pulse'} https://atres-live.ondacero.es/live/delegaciones/oc/logrono/master.m3u8"
        os.system(comando)
    elif opcion == "19":
        comando = f"{'ffplay -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5' if alea % 2 == 0 else 'mpv --ao=pulse'} https://rtvelivestream.akamaized.net/rtvesec/rne/rne_r5_madrid_main.m3u8"
        os.system(comando)
    elif opcion == "20":
        comando = f"{'ffplay -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5' if alea % 2 == 0 else 'mpv --ao=pulse'} https://rtvelivestream.akamaized.net/rtvesec/rne/rne_r2_main.m3u8"
        os.system(comando)
    elif opcion == "21":
        comando = f"{'ffplay -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5' if alea % 2 == 0 else 'mpv --ao=pulse'} https://playerservices.streamtheworld.com/api/livestream-redirect/RADIOMARCA_NACIONAL.mp3"
        os.system(comando)
    elif opcion == "22":
        comando = f"{'ffplay -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5' if alea % 2 == 0 else 'mpv --ao=pulse'} https://rtvelivestream.akamaized.net/rtvesec/rne/rne_r1_main.m3u8"
        os.system(comando)
    elif opcion == "23":
        comando = f"{'ffplay -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5' if alea % 2 == 0 else 'mpv --ao=pulse'} https://dispatcher.rndfnk.com/crtve/rne1/rio/mp3/high"
        os.system(comando)
    elif opcion == "24":
        comando = f"{'ffplay -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5' if alea % 2 == 0 else 'mpv --ao=pulse'} https://dispatcher.rndfnk.com/crtve/rne1/val/mp3/high"
        os.system(comando)
    elif opcion == "25":
        comando = f"{'ffplay -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5' if alea % 2 == 0 else 'mpv --ao=pulse'} https://rockfm-cope.flumotion.com/playlist.m3u8"
        os.system(comando)
    elif opcion == "26":
        comando = f"{'ffplay -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5' if alea % 2 == 0 else 'mpv --ao=pulse'} https://playerservices.streamtheworld.com/api/livestream-redirect/OWR_INTERNATIONAL_ADP.m3u8"
        os.system(comando)
    elif opcion == "27":
        comando = f"{'ffplay -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5' if alea % 2 == 0 else 'mpv --ao=pulse'} https://stream.srg-ssr.ch/m/rsj/mp3_128"
        os.system(comando)
    elif opcion == "28":
        comando = f"{'ffplay -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5' if alea % 2 == 0 else 'mpv --ao=pulse'} https://rtvelivestream.akamaized.net/rtvesec/rne/rne_re_main.m3u8"
        os.system(comando)
    elif opcion == "29":
        comando = f"{'ffplay -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5' if alea % 2 == 0 else 'mpv --ao=pulse'} https://dispatcher.rndfnk.com/crtve/rne5/rio/mp3/high"
        os.system(comando)
    elif opcion == "30":
        comando = f"{'ffplay -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5' if alea % 2 == 0 else 'mpv --ao=pulse'} https://adhandler.kissfmradio.cires21.com/get_link?url=https://bbhitfm.kissfmradio.cires21.com/bbhitfm.mp3"
        os.system(comando)

    # Grabaciones A Memoria Interna O Disco Duro-SSD

    elif opcion == "31":
        os.system(
            f"ffmpeg -i https://25543.live.streamtheworld.com/CADENADIAL.mp3 -c:a libopus -ar {rate} -b:a {calidad} -minrate {minrate} -compression_level {com_level} -vbr {vbr} -af {vamos} -metadata comment='{metedato}' -metadata MvIiIaX_M8AX='{meteda2}' -threads {nucleos_cpu} {download_path}/M8AX-Cadena_Dial-{timestamp}.opus & mpv https://25543.live.streamtheworld.com/CADENADIAL.mp3 > /dev/null 2>&1 &"
        )
    elif opcion == "32":
        os.system(
            f"ffmpeg -i https://28023.live.streamtheworld.com/CADENADIAL_03.mp3 -c:a libopus -ar {rate} -b:a {calidad} -minrate {minrate} -compression_level {com_level} -vbr {vbr} -af {vamos} -metadata comment='{metedato}' -metadata MvIiIaX_M8AX='{meteda2}' -threads {nucleos_cpu} {download_path}/M8AX-Cadena_Dial_Baladas-{timestamp}.opus & mpv https://28023.live.streamtheworld.com/CADENADIAL_03.mp3 > /dev/null 2>&1 &"
        )
    elif opcion == "33":
        os.system(
            f"ffmpeg -i https://25493.live.streamtheworld.com/CADENASER.mp3 -c:a libopus -ar {rate} -b:a {calidad} -minrate {minrate} -compression_level {com_level} -vbr {vbr} -af {vamos} -metadata comment='{metedato}' -metadata MvIiIaX_M8AX='{meteda2}' -threads {nucleos_cpu} {download_path}/M8AX-Cadena_Ser-{timestamp}.opus & mpv https://25493.live.streamtheworld.com/CADENASER.mp3 > /dev/null 2>&1 &"
        )
    elif opcion == "34":
        os.system(
            f"ffmpeg -i https://22593.live.streamtheworld.com/SER_RIOJA.mp3 -c:a libopus -ar {rate} -b:a {calidad} -minrate {minrate} -compression_level {com_level} -vbr {vbr} -af {vamos} -metadata comment='{metedato}' -metadata MvIiIaX_M8AX='{meteda2}' -threads {nucleos_cpu} {download_path}/M8AX-Cadena_Ser_LR-{timestamp}.opus & mpv https://22593.live.streamtheworld.com/SER_RIOJA.mp3 > /dev/null 2>&1 &"
        )
    elif opcion == "35":
        os.system(
            f"ffmpeg -i https://cdnlive.codev8.net/rtvalive/smil:channel5.smil/playlist.m3u8 -c:a libopus -ar {rate} -b:a {calidad} -minrate {minrate} -compression_level {com_level} -vbr {vbr} -af {vamos} -metadata comment='{metedato}' -metadata MvIiIaX_M8AX='{meteda2}' -threads {nucleos_cpu} {download_path}/M8AX-Canal_Fiesta_Radio-{timestamp}.opus & mpv https://cdnlive.codev8.net/rtvalive/smil:channel5.smil/playlist.m3u8 > /dev/null 2>&1 &"
        )
    elif opcion == "36":
        os.system(
            f"ffmpeg -i https://radio.entertainmenttechnologies.co.uk:8000/stream -c:a libopus -ar {rate} -b:a {calidad} -minrate {minrate} -compression_level {com_level} -vbr {vbr} -af {vamos} -metadata comment='{metedato}' -metadata MvIiIaX_M8AX='{meteda2}' -threads {nucleos_cpu} {download_path}/M8AX-Global_Radio-{timestamp}.opus & mpv https://radio.entertainmenttechnologies.co.uk:8000/stream > /dev/null 2>&1 &"
        )
    elif opcion == "37":
        os.system(
            f"ffmpeg -i https://atres-live.europafm.com/live/europafm/master.m3u8 -c:a libopus -ar {rate} -b:a {calidad} -minrate {minrate} -compression_level {com_level} -vbr {vbr} -af {vamos} -metadata comment='{metedato}' -metadata MvIiIaX_M8AX='{meteda2}' -threads {nucleos_cpu} {download_path}/M8AX-Europa_FM-{timestamp}.opus & mpv https://atres-live.europafm.com/live/europafm/master.m3u8 > /dev/null 2>&1 &"
        )
    elif opcion == "38":
        os.system(
            f"ffmpeg -i https://stream-156.zeno.fm/se76qau1hc9uv?zt=eyJhbGciOiJIUzI1NiJ9.eyJzdHJlYW0iOiJzZTc2cWF1MWhjOXV2IiwiaG9zdCI6InN0cmVhbS0xNTYuemVuby5mbSIsInJ0dGwiOjUsImp0aSI6Inh5ekllbERvVFVDWW85eTRXU0U2c2ciLCJpYXQiOjE3MzA0OTU3NTksImV4cCI6MTczMDQ5NTgxOX0.rCKmfp2ohVvoFtuGkg1DHdsGHsrYURlwch7tb08Rf1o -c:a libopus -ar {rate} -b:a {calidad} -minrate {minrate} -compression_level {com_level} -vbr {vbr} -af {vamos} -metadata comment='{metedato}' -metadata MvIiIaX_M8AX='{meteda2}' -threads {nucleos_cpu} {download_path}/M8AX-Europa_FM_GP-{timestamp}.opus & mpv https://stream-156.zeno.fm/se76qau1hc9uv?zt=eyJhbGciOiJIUzI1NiJ9.eyJzdHJlYW0iOiJzZTc2cWF1MWhjOXV2IiwiaG9zdCI6InN0cmVhbS0xNTYuemVuby5mbSIsInJ0dGwiOjUsImp0aSI6Inh5ekllbERvVFVDWW85eTRXU0U2c2ciLCJpYXQiOjE3MzA0OTU3NTksImV4cCI6MTczMDQ5NTgxOX0.rCKmfp2ohVvoFtuGkg1DHdsGHsrYURlwch7tb08Rf1o > /dev/null 2>&1 &"
        )
    elif opcion == "39":
        os.system(
            f"ffmpeg -i https://atres-live.europafm.com/live/delegaciones/efm/logrono/master.m3u8 -c:a libopus -ar {rate} -b:a {calidad} -minrate {minrate} -compression_level {com_level} -vbr {vbr} -af {vamos} -metadata comment='{metedato}' -metadata MvIiIaX_M8AX='{meteda2}' -threads {nucleos_cpu} {download_path}/M8AX-Europa_FM_LR-{timestamp}.opus & mpv https://atres-live.europafm.com/live/delegaciones/efm/logrono/master.m3u8 > /dev/null 2>&1 &"
        )
    elif opcion == "40":
        os.system(
            f"ffmpeg -i https://ibizaglobalradio.streaming-pro.com:8024/ -c:a libopus -ar {rate} -b:a {calidad} -minrate {minrate} -compression_level {com_level} -vbr {vbr} -af {vamos} -metadata comment='{metedato}' -metadata MvIiIaX_M8AX='{meteda2}' -threads {nucleos_cpu} {download_path}/M8AX-Ibiza_Global_Radio-{timestamp}.opus & mpv https://ibizaglobalradio.streaming-pro.com:8024/ > /dev/null 2>&1 &"
        )
    elif opcion == "41":
        os.system(
            f"ffmpeg -i https://stream.rcast.net/261087 -c:a libopus -ar {rate} -b:a {calidad} -minrate {minrate} -compression_level {com_level} -vbr {vbr} -af {vamos} -metadata comment='{metedato}' -metadata MvIiIaX_M8AX='{meteda2}' -threads {nucleos_cpu} {download_path}/M8AX-Ibiza_Sonica-{timestamp}.opus & mpv https://stream.rcast.net/261087 > /dev/null 2>&1 &"
        )
    elif opcion == "42":
        os.system(
            f"ffmpeg -i https://s2.we4stream.com/listen/loca_90s_/live -c:a libopus -ar {rate} -b:a {calidad} -minrate {minrate} -compression_level {com_level} -vbr {vbr} -af {vamos} -metadata comment='{metedato}' -metadata MvIiIaX_M8AX='{meteda2}' -threads {nucleos_cpu} {download_path}/M8AX-Loca_FM_90-{timestamp}.opus & mpv https://s2.we4stream.com/listen/loca_90s_/live > /dev/null 2>&1 &"
        )
    elif opcion == "43":
        os.system(
            f"ffmpeg -i https://s2.we4stream.com/listen/loca_tech_house/live -c:a libopus -ar {rate} -b:a {calidad} -minrate {minrate} -compression_level {com_level} -vbr {vbr} -af {vamos} -metadata comment='{metedato}' -metadata MvIiIaX_M8AX='{meteda2}' -threads {nucleos_cpu} {download_path}/M8AX-Loca_FM_Tech_House-{timestamp}.opus & mpv https://s2.we4stream.com/listen/loca_tech_house/live > /dev/null 2>&1 &"
        )
    elif opcion == "44":
        os.system(
            f"ffmpeg -i https://s2.we4stream.com/listen/loca_techo/live -c:a libopus -ar {rate} -b:a {calidad} -minrate {minrate} -compression_level {com_level} -vbr {vbr} -af {vamos} -metadata comment='{metedato}' -metadata MvIiIaX_M8AX='{meteda2}' -threads {nucleos_cpu} {download_path}/M8AX-Loca_FM_Techno-{timestamp}.opus & mpv https://s2.we4stream.com/listen/loca_techo/live > /dev/null 2>&1 &"
        )
    elif opcion == "45":
        os.system(
            f"ffmpeg -i https://libertaddigital-libremercado-live.flumotion.com/libertaddigital/libremercado-high.aac -c:a libopus -ar {rate} -b:a {calidad} -minrate {minrate} -compression_level {com_level} -vbr {vbr} -af {vamos} -metadata comment='{metedato}' -metadata MvIiIaX_M8AX='{meteda2}' -threads {nucleos_cpu} {download_path}/M8AX-Libertad_Digital-{timestamp}.opus & mpv https://libertaddigital-libremercado-live.flumotion.com/libertaddigital/libremercado-high.aac > /dev/null 2>&1 &"
        )
    elif opcion == "46":
        os.system(
            f"ffmpeg -i https://megastar-cope.flumotion.com/playlist.m3u8 -c:a libopus -ar {rate} -b:a {calidad} -minrate {minrate} -compression_level {com_level} -vbr {vbr} -af {vamos} -metadata comment='{metedato}' -metadata MvIiIaX_M8AX='{meteda2}' -threads {nucleos_cpu} {download_path}/M8AX-Mega_Star-{timestamp}.opus & mpv https://megastar-cope.flumotion.com/playlist.m3u8 > /dev/null 2>&1 &"
        )
    elif opcion == "47":
        os.system(
            f"ffmpeg -i https://atres-live.melodia-fm.com/live/melodiafm/master.m3u8 -c:a libopus -ar {rate} -b:a {calidad} -minrate {minrate} -compression_level {com_level} -vbr {vbr} -af {vamos} -metadata comment='{metedato}' -metadata MvIiIaX_M8AX='{meteda2}' -threads {nucleos_cpu} {download_path}/M8AX-Melodía_FM-{timestamp}.opus & mpv https://atres-live.melodia-fm.com/live/melodiafm/master.m3u8 > /dev/null 2>&1 &"
        )
    elif opcion == "48":
        os.system(
            f"ffmpeg -i https://atres-live.ondacero.es/live/delegaciones/oc/logrono/master.m3u8 -c:a libopus -ar {rate} -b:a {calidad} -minrate {minrate} -compression_level {com_level} -vbr {vbr} -af {vamos} -metadata comment='{metedato}' -metadata MvIiIaX_M8AX='{meteda2}' -threads {nucleos_cpu} {download_path}/M8AX-Onda_Cero_LR-{timestamp}.opus & mpv https://atres-live.ondacero.es/live/delegaciones/oc/logrono/master.m3u8 > /dev/null 2>&1 &"
        )
    elif opcion == "49":
        os.system(
            f"ffmpeg -i https://rtvelivestream.akamaized.net/rtvesec/rne/rne_r5_madrid_main.m3u8 -c:a libopus -ar {rate} -b:a {calidad} -minrate {minrate} -compression_level {com_level} -vbr {vbr} -af {vamos} -metadata comment='{metedato}' -metadata MvIiIaX_M8AX='{meteda2}' -threads {nucleos_cpu} {download_path}/M8AX-Radio_5_Madrid-{timestamp}.opus & mpv https://rtvelivestream.akamaized.net/rtvesec/rne/rne_r5_madrid_main.m3u8 > /dev/null 2>&1 &"
        )
    elif opcion == "50":
        os.system(
            f"ffmpeg -i https://rtvelivestream.akamaized.net/rtvesec/rne/rne_r2_main.m3u8 -c:a libopus -ar {rate} -b:a {calidad} -minrate {minrate} -compression_level {com_level} -vbr {vbr} -af {vamos} -metadata comment='{metedato}' -metadata MvIiIaX_M8AX='{meteda2}' -threads {nucleos_cpu} {download_path}/M8AX-Radio_Clásica-{timestamp}.opus & mpv https://rtvelivestream.akamaized.net/rtvesec/rne/rne_r2_main.m3u8 > /dev/null 2>&1 &"
        )
    elif opcion == "51":
        os.system(
            f"ffmpeg -i https://playerservices.streamtheworld.com/api/livestream-redirect/RADIOMARCA_NACIONAL.mp3 -c:a libopus -ar {rate} -b:a {calidad} -minrate {minrate} -compression_level {com_level} -vbr {vbr} -af {vamos} -metadata comment='{metedato}' -metadata MvIiIaX_M8AX='{meteda2}' -threads {nucleos_cpu} {download_path}/M8AX-Radio_Marca_Nacional-{timestamp}.opus & mpv https://playerservices.streamtheworld.com/api/livestream-redirect/RADIOMARCA_NACIONAL.mp3 > /dev/null 2>&1 &"
        )
    elif opcion == "52":
        os.system(
            f"ffmpeg -i https://rtvelivestream.akamaized.net/rtvesec/rne/rne_r1_main.m3u8 -c:a libopus -ar {rate} -b:a {calidad} -minrate {minrate} -compression_level {com_level} -vbr {vbr} -af {vamos} -metadata comment='{metedato}' -metadata MvIiIaX_M8AX='{meteda2}' -threads {nucleos_cpu} {download_path}/M8AX-Radio_Nacional_De_España-{timestamp}.opus & mpv https://rtvelivestream.akamaized.net/rtvesec/rne/rne_r1_main.m3u8 > /dev/null 2>&1 &"
        )
    elif opcion == "53":
        os.system(
            f"ffmpeg -i https://dispatcher.rndfnk.com/crtve/rne1/rio/mp3/high -c:a libopus -ar {rate} -b:a {calidad} -minrate {minrate} -compression_level {com_level} -vbr {vbr} -af {vamos} -metadata comment='{metedato}' -metadata MvIiIaX_M8AX='{meteda2}' -threads {nucleos_cpu} {download_path}/M8AX-Radio_Nacional_LR-{timestamp}.opus & mpv https://dispatcher.rndfnk.com/crtve/rne1/rio/mp3/high > /dev/null 2>&1 &"
        )
    elif opcion == "54":
        os.system(
            f"ffmpeg -i https://dispatcher.rndfnk.com/crtve/rne1/val/mp3/high -c:a libopus -ar {rate} -b:a {calidad} -minrate {minrate} -compression_level {com_level} -vbr {vbr} -af {vamos} -metadata comment='{metedato}' -metadata MvIiIaX_M8AX='{meteda2}' -threads {nucleos_cpu} {download_path}/M8AX-Radio_Nacional_Valencia-{timestamp}.opus & mpv https://dispatcher.rndfnk.com/crtve/rne1/val/mp3/high > /dev/null 2>&1 &"
        )
    elif opcion == "55":
        os.system(
            f"ffmpeg -i https://rockfm-cope.flumotion.com/playlist.m3u8 -c:a libopus -ar {rate} -b:a {calidad} -minrate {minrate} -compression_level {com_level} -vbr {vbr} -af {vamos} -metadata comment='{metedato}' -metadata MvIiIaX_M8AX='{meteda2}' -threads {nucleos_cpu} {download_path}/M8AX-Rock_FM-{timestamp}.opus & mpv https://rockfm-cope.flumotion.com/playlist.m3u8 > /dev/null 2>&1 &"
        )
    elif opcion == "56":
        os.system(
            f"ffmpeg -i https://playerservices.streamtheworld.com/api/livestream-redirect/OWR_INTERNATIONAL_ADP.m3u8 -c:a libopus -ar {rate} -b:a {calidad} -minrate {minrate} -compression_level {com_level} -vbr {vbr} -af {vamos} -metadata comment='{metedato}' -metadata MvIiIaX_M8AX='{meteda2}' -threads {nucleos_cpu} {download_path}/M8AX-TomorrowLand_Radio-{timestamp}.opus & mpv https://playerservices.streamtheworld.com/api/livestream-redirect/OWR_INTERNATIONAL_ADP.m3u8 > /dev/null 2>&1 &"
        )
    elif opcion == "57":
        os.system(
            f"ffmpeg -i https://stream.srg-ssr.ch/m/rsj/mp3_128 -c:a libopus -ar {rate} -b:a {calidad} -minrate {minrate} -compression_level {com_level} -vbr {vbr} -af {vamos} -metadata comment='{metedato}' -metadata MvIiIaX_M8AX='{meteda2}' -threads {nucleos_cpu} {download_path}/M8AX-Radio_Swiss_Jazz-{timestamp}.opus & mpv https://stream.srg-ssr.ch/m/rsj/mp3_128 > /dev/null 2>&1 &"
        )
    elif opcion == "58":
        os.system(
            f"ffmpeg -i https://rtvelivestream.akamaized.net/rtvesec/rne/rne_re_main.m3u8 -c:a libopus -ar {rate} -b:a {calidad} -minrate {minrate} -compression_level {com_level} -vbr {vbr} -af {vamos} -metadata comment='{metedato}' -metadata MvIiIaX_M8AX='{meteda2}' -threads {nucleos_cpu} {download_path}/M8AX-Radio_Exterior_De_España-{timestamp}.opus & mpv https://rtvelivestream.akamaized.net/rtvesec/rne/rne_re_main.m3u8 > /dev/null 2>&1 &"
        )
    elif opcion == "59":
        os.system(
            f"ffmpeg -i https://dispatcher.rndfnk.com/crtve/rne5/rio/mp3/high -c:a libopus -ar {rate} -b:a {calidad} -minrate {minrate} -compression_level {com_level} -vbr {vbr} -af {vamos} -metadata comment='{metedato}' -metadata MvIiIaX_M8AX='{meteda2}' -threads {nucleos_cpu} {download_path}/M8AX-Radio_5_La_Rioja-{timestamp}.opus & mpv https://dispatcher.rndfnk.com/crtve/rne5/rio/mp3/high > /dev/null 2>&1 &"
        )
    elif opcion == "60":
        os.system(
            f"ffmpeg -i https://adhandler.kissfmradio.cires21.com/get_link?url=https://bbhitfm.kissfmradio.cires21.com/bbhitfm.mp3 -c:a libopus -ar {rate} -b:a {calidad} -minrate {minrate} -compression_level {com_level} -vbr {vbr} -af {vamos} -metadata comment='{metedato}' -metadata MvIiIaX_M8AX='{meteda2}' -threads {nucleos_cpu} {download_path}/M8AX-Hit_FM-{timestamp}.opus & mpv https://adhandler.kissfmradio.cires21.com/get_link?url=https://bbhitfm.kissfmradio.cires21.com/bbhitfm.mp3 > /dev/null 2>&1 &"
        )
    elif opcion == "0":
        os.system("clear")
        os.system("figlet ... M8AX   Adios ...")
        print(
            "---------------------------------------------------------------------------------"
        )
        print(f"\n＊*•̩̩͙✩•̩̩͙*˚ᛖ𝐯ᎥᎥᎥⱥx*•̩̩͙✩•̩̩͙*˚＊\n")
        print(
            f"--- .•♫•♬•🔥Ｍ𝚟ıııคx🔥•♬•♫•. ---\n\nX∀8ꟽ\n\n--- ||| 🎸 ||| - ⌘•⌘ ꧁☆❤️🅼8🅰🆇❤️☆꧂ ⌘•⌘ - ||| 🎸 ||| ---\n"
        )
        print(
            f"-||| 🎹 ||| --- ░M░A░R░C░O░S░ --- ||| 🎹 |||-\n\n-||| 📷 ||| --- MvIiIaX & M8AX 2025 - 2050 --- ||| 📷 |||-\n"
        )
        print(f"{factores}\n")
        print(
            "---------------------------------------------------------------------------------\n"
        )
        break