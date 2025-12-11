import pytest

#lista de archivos de pruebas a ejecutar
tests_files = [
  "tests/test_login.py",
  "tests/test_browsing.py",
  "tests/test_cart.py",
]

# argumentos para ejecutar las pruebas: archivos + reporte html
pytest_args = tests_files + [
    "--html=reports/report.html",  # Ruta correcta
    "--self-contained-html",       # HTML con estilos embebidos
    "-v"                           # Verbose
]

# Ejecutar pytest
pytest.main(pytest_args)