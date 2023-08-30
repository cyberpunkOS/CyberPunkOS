#!/usr/bin/env python3

import subprocess
import webbrowser
import os
import time

# Constantes para las rutas de las aplicaciones
TOR_BROWSER_PATH = "/usr/bin/torbrowser-launcher"
PROTONVPN_PATH = "/usr/bin/protonvpn"

titulo = """
   ______        __                                      __        ____  _____
  / ____/__  __ / /_   ___   _____ ____   __  __ ____   / /__     / __ \/ ___/
 / /    / / / // __ \ / _ \ / ___// __ \ / / / // __ \ / //_/    / / / /\__ \ 
/ /___ / /_/ // /_/ //  __// /   / /_/ // /_/ // / / // ,<      / /_/ /___/ / 
\____/ \__, //_.___/ \___//_/   / .___/ \__,_//_/ /_//_/|_|     \____//____/  
      /____/                   /_/                                            
"""
def recopilacion_y_verificacion():
    while True:
        print("\n" + "="*80)
        print("Recopilación y verificación:")
        print("="*80)
        print("1. Goris - Búsqueda inversa de imágenes en Google")
        print("2. ExifTool - Analizar metadata de un archivo")
        print("3. SpiderFoot - OSINT Automático")
        print("4. HTTrack - Clonador de sitios web")
        print("5. IntelTechniques Toolkit - Colección de herramientas OSINT")
        print("6. Bellingcat - Online Investigation Toolkit")
        print("7. Volver al menú principal")

        opcion = input("Seleccione una opción (1-7): ")

        if opcion == '1':
            ejecutar_goris()  # Llama a la función que ejecuta Goris
        elif opcion == '2':
            print("Abriendo Exiftool...")
            ejecutar_exiftool()  # Llama a la función que ejecuta ExifTool
        elif opcion == '3':
            # Ejecutar SpiderFoot en segundo plano
            subprocess.Popen(["spiderfoot", "-l", "127.0.0.1:8989"])
            print("En un momento se abrirá la interfaz web...")
            time.sleep(5)  # Espera 5 segundos
            # Abrir la URL en el navegador
            webbrowser.open("http://127.0.0.1:8989")
        elif opcion == '4':
            # Ejecutar webhttrack
            subprocess.Popen(["/usr/bin/webhttrack"])
        elif opcion == '5':
            print("Abriendo IntelTechniques Toolkit...")
            webbrowser.open("https://inteltechniques.com/tools/")
        elif opcion == '6':
            print("Abriendo Bellingcat's Online Investigation Toolkit...")
            webbrowser.open("https://docs.google.com/spreadsheets/d/18rtqh8EG2q1xBo2cLNyhIDuK9jrPGwYr9DI2UncoqJQ/edit#gid=930747607")
        elif opcion == '7':
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def ejecutar_goris():
    # Solicitar al usuario la URL
    url = input("Ingrese la URL de la imagen: ")
    # Ejecutar el comando "goris s -u" con la URL proporcionada
    try:
        subprocess.run(["goris", "s", "-u", url], check=True)
    except subprocess.CalledProcessError:
        print("Error al ejecutar el comando. Asegúrese de que 'goris' esté instalado y sea ejecutable.")
    
    input("Presiona Enter para volver al menú anterior.")

def ejecutar_exiftool():
    while True:
        print("\n" + "="*80)
        print("ExifTool:")
        print("="*80)
        print("1. Analizar los metadatos del archivo")
        print("2. Exportar metadatos a CSV/JSON")
        print("3. Volver al menú principal")

        opcion = input("Seleccione una opción (1-3): ")

        if opcion == '1':
            archivo = input("Ingrese la ruta y el nombre del archivo para analizar: ")
            try:
                subprocess.run(["exiftool", archivo])
            except subprocess.CalledProcessError:
                print("Error al ejecutar el comando 'exiftool'. Asegúrese de que 'exiftool' esté instalado y sea ejecutable.")
        elif opcion == '2':
            archivo = input("Ingrese el nombre del archivo para exportar metadatos: ")
            formato = input("Seleccione el formato de exportación (CSV o JSON): ").lower()
            
            if formato not in ["csv", "json"]:
                print("Formato no válido. Debe ser CSV o JSON.")
                return
            
            resultado = f"/home/cyberpunk/CyberpunkTools_resultados/metadatos.{formato}"
            
            try:
                subprocess.run(["exiftool", f"-{formato}", archivo], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                output = subprocess.check_output(["exiftool", f"-{formato}", archivo], stderr=subprocess.STDOUT, text=True)
                
                # Guardar el resultado en el archivo
                with open(resultado, "w") as archivo_resultado:
                    archivo_resultado.write(output)
                
                print(f"Metadatos exportados en: {resultado}")
            except subprocess.CalledProcessError as e:
                print(f"Error al exportar los metadatos. Asegúrese de que 'exiftool' esté instalado y sea ejecutable.")
                print(e.output)
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def analisis_y_visualizacion():
    while True:
        print("\n" + "="*80)
        print("Análisis y visualización:")
        print("="*80)
        print("1. Maltego - Inteligencia de fuentes abiertas y forense")
        print("2. Volver al menú principal")

        opcion = input("Seleccione una opción (1-2): ")

        if opcion == '1':
            ejecutar_maltego()  # Llama a la función que ejecuta Maltego
        elif opcion == '2':
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def ejecutar_maltego():
    try:
        subprocess.run(["maltego"], check=True)
    except subprocess.CalledProcessError:
        print("Error al ejecutar el comando 'maltego'. Asegúrese de que 'maltego' esté instalado y sea ejecutable.")
    
    input("Presiona Enter para volver al menú anterior.")

def web_scrapping():
    while True:
        print("\n" + "="*80)
        print("Web Scrapping:")
        print("="*80)
        print("1. Photon Scanner - Web Scrapping")
        print("2. Volver al menú principal")

        opcion = input("Seleccione una opción (1-2): ")

        if opcion == '1':
            ejecutar_photon()  # Llama a la función que ejecuta Photon
        elif opcion == '2':
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def ejecutar_photon():
    # Ruta completa hacia el script cpPhoton.sh
    ruta_script = "/home/cyberpunk/CyberpunkTools/cpPhoton.sh"

    try:
        # Abre una nueva terminal y ejecuta el script
        subprocess.run(["mate-terminal", "--command", f"bash -c '{ruta_script} ; bash'"], check=True)
    except subprocess.CalledProcessError:
        print("Error al ejecutar el script. Asegúrate de que la ruta sea correcta y el archivo tenga permisos de ejecución.")

def redes_sociales_y_analisis():
    while True:
        print("\n" + "="*80)
        print("Redes Sociales y Análisis:")
        print("="*80)
        print("1. Sherlock - Búsqueda por nombres de usuarios en redes sociales")
        print("2. Volver al menú principal")

        opcion = input("Seleccione una opción (1-2): ")

        if opcion == '1':
            ejecutar_sherlock()  # Llama a la función que ejecuta Sherlock
        elif opcion == '2':
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

# Nueva función para ejecutar Sherlock
def ejecutar_sherlock():
    # Ruta completa hacia el script cpSherlock.sh
    ruta_script = "/home/cyberpunk/CyberpunkTools/cpSherlock.sh"

    try:
        # Abre una nueva terminal y ejecuta el script
        subprocess.run(["mate-terminal", "--command", f"bash -c '{ruta_script} ; bash'"], check=True)
    except subprocess.CalledProcessError:
        print("Error al ejecutar el script. Asegúrate de que la ruta sea correcta y el archivo tenga permisos de ejecución.")

def ejecutar_cpNews(palabra_clave):
    print(f"Ejecutando el programa cpNews.py con la palabra clave: {palabra_clave}")
    try:
        subprocess.run(["python3", "cpNews.py", palabra_clave], check=True)
    except subprocess.CalledProcessError:
        print("Error al ejecutar cpNews.py. Asegúrate de que el archivo existe y es ejecutable.")
    input("Presiona Enter para volver al menú principal.")

def busqueda_y_monitoreo_de_noticias():
    while True:
        print("\n" + "="*80)
        print("Búsqueda y Monitoreo de Noticia:")
        print("="*80)
        print("1. CyberpunkOS News - Realizar una búsqueda de noticias utilizando palabra clave")
        print("2. Google News - Buscador de noticias automatizado")
        print("3. Google Alerts - Servicio de supervisión de contenidos")
        print("4. Google Trends - Tendencias de búsquedas")
        print("5. Hoaxy - Rastreador de la difusión de las noticias falsas")
        print("6. FastCheck.org - Verificación veracidad de noticias")
        print("7. Snopes - Verificador de hechos")
        print("8. Volver al menú principal")
        
        opcion = input("Seleccione una opción (1-8): ")
        
        if opcion == '1':
            palabra_clave = input("Ingrese la palabra clave de búsqueda: ")
            ejecutar_cpNews(palabra_clave)
        elif opcion == '2':
            webbrowser.open("https://news.google.com/")
        elif opcion == '3':
            webbrowser.open("https://www.google.com/alerts")
        elif opcion == '4':
            webbrowser.open("https://trends.google.com/home")
        elif opcion == '5':
            webbrowser.open("https://hoaxy.osome.iu.edu/")
        elif opcion == '6':
            webbrowser.open("https://www.factcheck.org/")
        elif opcion == '7':
            webbrowser.open("https://www.snopes.com/")
        elif opcion == '8':
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")



def anonimato_y_privacidad():
    while True:
        print("\n" + "="*80)
        print("Anonimato y Privacidad:")
        print("="*80)
        print("1. Tor Browser - Navegador anónimo")
        print("2. ProtonVPN - Servicio de VPN")
        print("3. Volver al menú principal")

        opcion = input("Seleccione una opción (1-3): ")

        if opcion == '1':
            ejecutar_aplicacion(TOR_BROWSER_PATH, "Tor Browser")
        elif opcion == '2':
            ejecutar_aplicacion(PROTONVPN_PATH, "ProtonVPN")
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def ejecutar_aplicacion(aplicacion_path, nombre_aplicacion):
    print(f"Ejecutando {nombre_aplicacion}...")
    try:
        subprocess.run([aplicacion_path], check=True)
        print(f"{nombre_aplicacion} se ha ejecutado con éxito.")
    except subprocess.CalledProcessError:
        print(f"Error al ejecutar {nombre_aplicacion}. Asegúrate de que esté instalado y configurado correctamente.")
    input("Presiona Enter para volver al menú principal.")


# Función principal del menú
def menu_principal():
    while True:
        print("\n" + "="*80)
        print(titulo)
        print("="*80)
        print(" "*25 + "--- Menú de Categorías OSINT ---")
        print("="*80)
        print("1. Recopilación de Datos y Verificación")
        print("2. Análisis y Visualización")
        print("3. Web Scrapping")
        print("4. Redes Sociales y Análisis")
        print("5. Búsqueda y Monitoreo de Noticia")
        print("6. Anonimato y Privacidad")
        print("0. Salir")
        
        opcion = input("Seleccione una categoría (0-6): ")
        
        if opcion == '1':
            recopilacion_y_verificacion()
        elif opcion == '2':
            analisis_y_visualizacion()
        elif opcion == '3':
            web_scrapping()
        elif opcion == '4':
            redes_sociales_y_analisis()
        elif opcion == '5':
            busqueda_y_monitoreo_de_noticias()
        elif opcion == '6':
            anonimato_y_privacidad()
        elif opcion == '0':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    menu_principal()
