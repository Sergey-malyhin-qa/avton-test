import requests

Host = "https://api.pokemonbattle.me/v2"
Trainer_ID = "224"
Trainer_token = "58d888733ce45b57de2789ceffd93e6a"
HEADERS = {"Content-Type" :"application/json",
           "trainer_token" :Trainer_token  }

def test_status_code ():
    response = requests.get(url= f'{Host}/trainers', params = {"trainer_id" : Trainer_ID })  
    assert response.status_code == 200 
 
def test_trainer_name():
    response = requests.get(url= f'{Host}/trainers', params = {"trainer_id" : Trainer_ID }) 
    assert response.json()["data"][0]["trainer_name"] == "Kio"

  