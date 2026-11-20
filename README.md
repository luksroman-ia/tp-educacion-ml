# Priorizacion de Zonas Vulnerables para Nuevos Colegios en Argentina (ML)

## Objetivo
Identificar provincias, municipios/departamentos y zonas de Argentina con mayor vulnerabilidad socioeconomica y rezago/exclusion educativa para priorizar la apertura de colegios de alto nivel orientados a familias de bajos recursos.

## Enfoque de Machine Learning
1. **Segmentacion (No supervisado):** Agrupar municipios/departamentos segun indicadores de vulnerabilidad y educacion (K-means y clustering jerarquico/aglomerativo).
2. **Prediccion de riesgo (Supervisado):** Predecir riesgo de abandono/rezago con validacion temporal (sin fuga de datos), comparando modelos y una regla base simple mediante Precision, Recall y F1-Score.

## Fuentes de datos previstas (pendientes de descarga y licencia)
- INDEC (Censo Nacional 2022 y EPH)
- Ministerio de Capital Humano / Educacion (Relevamiento Anual / Aprender)
- RENABAP (Registro Nacional de Barrios Populares)
