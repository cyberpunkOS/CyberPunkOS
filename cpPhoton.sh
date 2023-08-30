#!/bin/bash

# Almacenar el comando en una variable
python3="/usr/bin/python3"
photon="/home/cyberpunk/CyberpunkTools/Photon/photon.py"

# Directorio para almacenar los resultados
resultados="/home/cyberpunk/CyberpunkTools_resultados"

# Verifica si el directorio para almacenar los resultados existe, sino lo crea
if [ ! -d "$resultados" ]; then
    mkdir -p "$resultados"
fi

while true; do
    clear
    echo "=============================================================================="
    echo "Photon Scanner:"
    echo "=============================================================================="
    echo "1. Escanear sitio web"
    echo "2. Clonar sitio web"
    echo "3. Volver al menú principal"

    read -p "Seleccione una opción (1-3): " opcion

    if [ "$opcion" == "1" ]; then
        read -p "Ingrese la URL del sitio web a escanear: " url
        sitio_web=$(basename "$url")
        directorio_destino="$resultados/$sitio_web"
        
        echo "Creando el directorio $directorio_destino y escaneando $url ..."
        mkdir -p "$directorio_destino"
        "$python3" "$photon" -u "$url" -o "$directorio_destino"
        read -p "Presione Enter para continuar..."
    elif [ "$opcion" == "2" ]; then
        read -p "Ingrese la URL del sitio web a clonar: " url
        sitio_web=$(basename "$url")
        directorio_destino="$resultados/$sitio_web"
        
        echo "Creando el directorio $directorio_destino y clonando $url ..."
        mkdir -p "$directorio_destino"
        "$python3" "$photon" -u "$url" --clone -o "$directorio_destino"
        read -p "Presione Enter para continuar..."
    elif [ "$opcion" == "3" ]; then
        break
    else
        echo "Opción no válida. Por favor, seleccione una opción válida."
        read -p "Presione Enter para continuar..."
    fi
done