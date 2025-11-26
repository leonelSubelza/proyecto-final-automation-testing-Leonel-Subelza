import requests

def test_post_users():
  url = "https://reqres.in/api/users"
  header = {"x-api-key": "reqres-free-v1"}
  
  payload = {"name":"Pepe", "age":50}
  
  response = requests.post(url,headers=header,json=payload)
  
  # verificar que el recurso se haya creado
  assert response.status_code == 201, "Respuesta no exitosa"
  
  data = response.json()
  # verificar que el nombre de la respuesta sea el mismo que el enviado
  assert data["name"] == payload["name"]
  print(data)
  