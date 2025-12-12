# 🚀 Proyecto Final – Automatización QA (Talento Tech)

Este proyecto forma parte de la entrega final del curso **Talento Tech – Automatización QA**, donde se implementa una suite de pruebas automatizadas utilizando **Python, Pytest, Selenium y GitHub Actions**.
Las pruebas se realizan sobre la página [Saucedemo](https://www.saucedemo.com) y también se incluye una sección dedicada a pruebas API utilizando [ReqRes](https://reqres.in/) como servicio de prueba.

---

## 🎯 Propósito del Proyecto

El objetivo principal es demostrar la capacidad de:
   - Diseñar y automatizar casos de prueba UI usando el patrón Page Object Model (POM).
   - Implementar pruebas parametrizadas con datos externos desde un archivo CSV.
   - Validar flujos completos como:
      - Login (válido e inválido)
      - Navegación por la página inventory.html
      - Agregar productos al carrito

   - Gestionar logs y capturas de pantalla automáticas en caso de fallo.
   - Generar reportes HTML de ejecución.
   - Automatizar la ejecución completa mediante GitHub Actions.
   - Realizar pruebas de API (GET, POST, DELETE, PUT/PATCH) contra ReqRes.

Es un proyecto que refleja buenas prácticas de automatización usadas en entornos profesionales.

---

## ⚙️ Tecnologías Utilizadas

#### Backend de automatización
- Python 3.12
- Pytest
- Selenium WebDriver
- Requests (para pruebas de API)
- Python Faker (generación de datos)
- CSV para parametrización

#### Ejecución y DevOps
- GitHub Actions (CI)
- pytest-html (reportes)
- logging (logs estructurados)
- WebDriver Manager (manejo automático del driver)

#### Patrón
- Page Object Model (POM)

---
<!--### Notas:
- reports/ y logs/ no se suben al repo (están en .gitignore).
- Los reportes y capturas se generan automáticamente en cada ejecución.

---
-->
## 🧪 Casos de Prueba Automatizados
#### ✔ Login (parametrizado con CSV)
- Login exitoso con credenciales válidas
- Login inválido
- Campos vacíos
- Email/username incorrecto
- Contraseña incorrecta
- Usuario bloqueado, etc.

#### ✔ Navegación en inventory.html
- Validación del título
- Validación de elementos principales
- Verificación de productos visibles
- Validación del primer producto: nombre y precio

#### ✔ Carrito
- Agregar un producto al carrito
- Validar el badge del carrito
- Verificar que el producto se vea en el carrito

#### ✔ Pruebas API (ReqRes)
- GET de usuario
- POST de creación
- PUT/PATCH de actualización
- DELETE de un recurso
- Validación de códigos de estado y estructura de respuesta

--- 
## ⚙️ Integración Continua con GitHub Actions
El archivo ci.yml permite que:
- En cada push o pull request a main o develop:
   - Se instalen dependencias
   - Se ejecuten todos los tests UI + API
   - Se generen reportes HTML y logs
   - Se suban como artefactos al pipeline

Esto simula un entorno CI real de automatización como en una empresa.

--- 
## 📊 Reportes generados
Gracias al archivo pytest.ini, cada vez que se corra pytest se generá automáticamente:
```bash
reports/report.html
```
Este reporte incluye:
- Lista completa de tests ejecutados
- Tests pasados y fallados
- Tiempos de ejecución
- Logs por test

## 📁 Capturas de pantalla
Si un test falla:
- Se guarda una imágen PNG en la carpeta reports/screens con formato:
```bash
testname_FAIL_YYYYMMDD-HHMMSS.png
```
---
### 📦 Instalación de dependencias
1. Clonar el repositorio:
```bash
git clone https://github.com/leonelSubelza/proyecto-final-automation-testing-Leonel-Subelza.git
cd proyecto-final-automation-testing-Leonel-Subelza
```

2. Crear un entorno virtual (opcional pero recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

Eso instalará Selenium, Pytest, Requests, Faker, pytest-html, WebDriver Manager y demás dependencias necesarias.

## ▶️ ¿Cómo ejecutar las pruebas?
Ejecutar todas las pruebas:
```bash
py -m pytest -v
```

Ejecutar solo las pruebas de API:
```bash
pytest -m e2e
```