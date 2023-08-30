#!/bin/bash

# Almacenar el comando en una variable
python3="/usr/bin/python3"
sherlock="/home/cyberpunk/CyberpunkTools/sherlock/sherlock.py"

# Directorio para almacenar los resultados
resultados="/home/cyberpunk/CyberpunkTools_resultados"

# Verifica si el directorio para almacenar los resultados existe, sino lo crea
if [ ! -d "$resultados" ]; then
    mkdir -p "$resultados"
fi

# Bucle que muestra el menú y espera la selección del usuario
while true; do
    # Menú de opciones
    echo "Seleccione una opción:"
    echo "1. Búsqueda Básica"
    echo "2. Búsqueda en Múltiples Usuarios"
    echo "3. Búsqueda en Modo Verbose"
    echo "4. Búsqueda en Todas las Plataformas"
    echo "0. Salir"

    # Leer la opción del usuario
    read opcion

    # Ejecutar la opción seleccionada
    case $opcion in
        1)
            echo "Ejecutando Búsqueda Básica..."
            echo "Ingrese el nombre de usuario:"
            read usuario
            # Obtener la fecha y hora actual en un formato legible
            fecha_hora=$(date +"%Y%m%d%H%M%S")
            # Crear el nombre del archivo de salida con la fecha y hora
            archivo_salida="$resultados/sherlock_busqueda_basica_$fecha_hora.txt"
            $python3 $sherlock $usuario 2>&1 | tee "$archivo_salida"
            ;;
        2)
            echo "Ejecutando Búsqueda en Múltiples Usuarios..."
            echo "Ingrese una lista de nombres de usuario separados por espacios:"
            read usuarios
            $python3 $sherlock --folderoutput /home/cyberpunk/CyberpunkTools_resultados $usuarios
            ;;
        3)
            echo "Ejecutando Búsqueda en Modo Verbose..."
            echo "Ingrese el nombre de usuario:"
            read usuario
            # Obtener la fecha y hora actual en un formato legible
            fecha_hora=$(date +"%Y%m%d%H%M%S")
            # Crear el nombre del archivo de salida con la fecha y hora
            archivo_salida="$resultados/sherlock_verbose_$fecha_hora.txt"
            $python3 $sherlock --verbose $usuario 2>&1 | tee "$archivo_salida"
            ;;
        4)
            echo "Ejecutando Búsqueda en Todas las Plataformas..."
            echo "Ingrese el nombre de usuario:"
            read usuario
            # Obtener la fecha y hora actual en un formato legible
            fecha_hora=$(date +"%Y%m%d%H%M%S")
            # Crear el nombre del archivo de salida con la fecha y hora
            archivo_salida="$resultados/sherlock_todas_las_plataformas_$fecha_hora.txt"
            $python3 $sherlock --print-all $usuario 2>&1 | tee "$archivo_salida"
            ;;
        0)
            echo "Saliendo del menú."
            exit 0
            ;;
        *)
            echo "Opción no válida."
            ;;
    esac
done