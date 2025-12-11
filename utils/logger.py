import logging
import pathlib

audit_dir = pathlib.Path('logs')
# si existe audit_dir entonces crea la carpeta
audit_dir.mkdir(exist_ok=True)

log_file = audit_dir/ 'suite.log'

logger = logging.getLogger('TalentoTech') # Se crea el objeto logger con el nombre TalentoTech
logger.setLevel(logging.INFO) 

# Si ya existe un logger con el nombre TalentoTech, entonces no hace nada
if not logger.handlers:
  # En nuestro archivo logger lo que se hará es ir sobreescribiendo los nuevos logs sobre los viejos (en general se van escribiendo en un nuevo archivo identificados por la fecha en que se corrió el test). El mode="a" es por "append"
  file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
  
  formatter = logging.Formatter(
    "%(asctime)s %(levelname)s %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
  )
  
  file_handler.setFormatter(formatter)
  logger.addHandler(file_handler)
  