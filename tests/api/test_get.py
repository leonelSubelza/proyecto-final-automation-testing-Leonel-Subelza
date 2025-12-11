import requests

def test_get_users(url_base_reqres,reqres_api_key):
  url = f"{url_base_reqres}/users?page=2"
  # url = f"{url_base_reqres}?page=2"
  header = {"x-api-key": reqres_api_key}
  response = requests.get(url,headers=header)
  
  # verificar que la respuesta es exitosa
  print(response.status_code)
  assert response.status_code == 200, "Respuesta no exitosa"
  
  data = response.json()
  # verificar que data existe
  assert "data" in data
  
  # verificar que existe data es una lista
  assert isinstance(data["data"],list)
  
  # verificar que haya al menos un usuario en la lista
  assert len(data["data"]) > 0
  