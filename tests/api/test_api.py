import requests
from faker import Faker
import pytest
import time

fake = Faker()

@pytest.fixture(scope='module')
def created_post():
  """Crea un post y devuelve sus datos para otros tests"""
  # payload = {
  # 'title': 'Post para testing',
  # 'body': 'Contenido de prueba',
  # 'userId': 1
  # }
  payload = {
    'title': fake.street_name(),
    'body': fake.street_address(),
    'id': fake.random_number()
  }
  
  response = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload)
  assert response.status_code == 201
  print(response)
  return response.json()

@pytest.mark.e2e
def test_update_delete_post(created_post):
  """Usa el post creado en la fixture"""
  post_id = created_post['id']
  
  # validacion de tiempo de respuesta
  init_time = time.time()
  
  #  update
  update_payload = {'title': 'Título actualizado'}
  response = requests.patch(f'https://jsonplaceholder.typicode.com/posts/{post_id}', json=update_payload)
  diff_time = time.time() - init_time
  
  assert response.status_code == 200
  assert response.json()['title'] == 'Título actualizado'
  assert diff_time < 2, f"El tiempo de respuesta fue demasiado lento:{diff_time}"
  
  # delete
  response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
  assert response.status_code == 200
 