import requests

def test_delete_user(url_base_reqres,reqres_api_key):
  url = f"{url_base_reqres}/users?page=2"
  # url = f"{url_base_reqres}?page=2"
  header = {"x-api-key": reqres_api_key}
  response = requests.delete(url,headers=header)
  
  assert response.status_code == 204, "Respuesta no exitosa"