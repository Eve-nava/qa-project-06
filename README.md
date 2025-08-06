# Proyecto de Automatización: Creación de Kits en Urban Grocers

Este proyecto forma parte del Sprint 6 del Bootcamp de QA Engineering. Tiene como objetivo automatizar la validación del campo `"name"` en la funcionalidad de creación de kits en la aplicación **Urban Grocers**, utilizando Python, Pytest y solicitudes HTTP (API REST).

---

## 🧪 Objetivo

Verificar que la creación de un kit con diferentes tipos de valores para el campo `"name"` cumpla con los requisitos establecidos, tanto en escenarios positivos como negativos.

---

## 🔧 Tecnologías y herramientas utilizadas

- Lenguaje: **Python 3**
- Librerías: `requests`, `pytest`
- Entorno de desarrollo: **PyCharm**
- Control de versiones: **Git + GitHub**
- Pruebas de API: Automatización con `requests`
- Estructura modular de archivos para solicitudes y datos

---

## 📁 Estructura del proyecto

qa-project-06/
│
├── configuration.py # Configuración de endpoints
├── data.py # Datos de entrada para las pruebas
├── sender_stand_request.py # Funciones para envío de solicitudes
├── create_kit_name_kit_test.py # Archivo principal de pruebas
├── README.md # Documentación del proyecto
└── .gitignore # Archivos excluidos del repositorio



---

## ✅ Casos de prueba cubiertos

| Nº | Descripción                                                             | Resultado Esperado |
|----|-------------------------------------------------------------------------|--------------------|
| 1  | Crear kit con 1 caracter                                                | 201 Created        |
| 2  | Crear kit con 511 caracteres                                            | 201 Created        |
| 3  | Crear kit con campo vacío                                               | 400 Bad Request    |
| 4  | Crear kit con más de 512 caracteres                                     | 400 Bad Request    |
| 5  | Crear kit con caracteres especiales                                     | 201 Created        |
| 6  | Crear kit con espacios en el nombre                                     | 201 Created        |
| 7  | Crear kit con nombre numérico (como texto)                              | 201 Created        |
| 8  | Crear kit omitiendo el campo `"name"`                                   | 400 Bad Request    |
| 9  | Crear kit con un valor numérico (sin comillas) como tipo incorrecto     | 400 Bad Request    |

---

## ▶️ Cómo ejecutar las pruebas

1. Asegúrate de tener `pytest` y `requests` instalados:


pip install pytest requests
Ejecuta las pruebas desde la terminal (estando dentro del proyecto):


pytest create_kit_name_kit_test.py
Los resultados mostrarán cuántas pruebas pasaron y cuántas fallaron.

📌 Notas
Algunas pruebas están diseñadas para fallar (por ejemplo, cuando la entrada es inválida). Esto no indica un error en el código, sino que valida el correcto manejo de errores de la API.

El token de autenticación se genera dinámicamente para cada ejecución.

Puedes consultar la documentación de la API proporcionada por el servidor local para mayor referencia.
