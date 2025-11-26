import requests

def test_get_users():
  url = "https://reqres.in/api/users?page=2"
  # header = {"x-api-key": "reqres-free-v1"}
  response = requests.get(url)
  
  # verificar que la respuesta es exitosa
  assert response.status_code == 200, "Respuesta no exitosa"
  
  data = response.json()
  # verificar que data existe
  assert "data" in data
  
  # verificar que existe data es una lista
  assert isinstance(data["data"],list)
  
  # verificar que haya al menos un usuario en la lista
  assert len(data["data"]) > 0
  