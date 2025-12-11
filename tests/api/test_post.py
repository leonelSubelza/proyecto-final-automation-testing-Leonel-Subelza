import requests

def test_post_users(url_base_reqres,reqres_api_key):
  header = {"x-api-key": reqres_api_key}
  
  payload = {"name":"Pepe", "age":50}
  
  response = requests.post(f"{url_base_reqres}/users",headers=header,json=payload)
  
  # verificar que el recurso se haya creado
  assert response.status_code == 201, "Respuesta no exitosa"
  
  data = response.json()
  # verificar que el nombre de la respuesta sea el mismo que el enviado
  assert data["name"] == payload["name"]
  print(data)
  