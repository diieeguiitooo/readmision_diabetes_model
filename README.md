# Predicción de readmisión hospitalaria en pacientes diabéticos

Modelo que ordena los ingresos por riesgo de readmisión a 30 días en el momento del alta, para priorizar el
seguimiento, y explica qué factores pesan más. Continúa el proyecto
[readmision_diabetes_eda](https://github.com/diieeguiitooo/readmision_diabetes_eda), que limpió, analizó y preparó
el dataset UCI Diabetes 130-US hospitals.

**Estado:** en desarrollo.

## Evaluación

- **Métrica principal:** PR-AUC.
- **Métrica complementaria:** ROC-AUC.
- **Uso clínico:** recall y precisión en el 20 % de ingresos de mayor riesgo.

## Reproducción

```bash
pip install -r requirements.txt
python scripts/descargar_datos.py
```

El script descarga `train.csv` y `test.csv` en `data/` desde un commit fijo de `readmision_diabetes_eda` y comprueba
su huella SHA-256.

## Licencia

Código bajo licencia MIT.
