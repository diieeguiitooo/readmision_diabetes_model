"""Descarga train.csv y test.csv del repositorio readmision_diabetes_eda y comprueba su SHA-256."""

import hashlib
import sys
from pathlib import Path
from urllib.request import urlretrieve

# Commit fijo: un cambio futuro en el repositorio de origen no altera los datos de este proyecto
COMMIT = '4a4f29271142081dc6ff177bd9d39521899a14f8'
URL_BASE = (
    'https://raw.githubusercontent.com/diieeguiitooo/readmision_diabetes_eda/'
    f'{COMMIT}/data/processed'
)
HUELLAS = {
    'train.csv': 'efdaa9283dad2be4f2057cae9d943d4f3db6a70eee9855aac7fa8bd5dca75656',
    'test.csv': '1b8a2214c01099c2db1fa63a1824c8eb3bf9692c784681aba594f6be6c97fef0',
}

# Raíz del proyecto: el script está en scripts/, así que es la carpeta de encima
BASE = Path(__file__).resolve().parent.parent
DATA = BASE / 'data'


def calcular_huella(ruta):
    return hashlib.sha256(ruta.read_bytes()).hexdigest()


def main():
    DATA.mkdir(exist_ok=True)

    for nombre, huella in HUELLAS.items():
        ruta = DATA / nombre

        if ruta.exists() and calcular_huella(ruta) == huella:
            print(f'{nombre}: ya descargado y correcto')
            continue

        print(f'{nombre}: descargando...')
        urlretrieve(f'{URL_BASE}/{nombre}', ruta)

        # Un archivo que no coincide no se conserva: nadie debe entrenar con él por error
        if calcular_huella(ruta) != huella:
            ruta.unlink()
            sys.exit(f'{nombre}: la huella SHA-256 no coincide; archivo eliminado')

        print(f'{nombre}: descargado y correcto')


if __name__ == '__main__':
    main()
