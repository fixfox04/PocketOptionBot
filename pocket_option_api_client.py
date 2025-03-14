import requests
import json
import time
import os

class PocketOptionAPI:
    def __init__(self, api_key, base_url="https://api.pocketoption.com/v1"):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}

    def get_market_data(self, asset="EURUSD", timeframe=60):
        """ Получает рыночные данные по указанному активу """
        endpoint = f"{self.base_url}/market-data/{asset}/{timeframe}"
        response = requests.get(endpoint, headers=self.headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Ошибка запроса: {response.status_code}, {response.text}")
            return None

    def save_data_to_file(self, data, filename="market_data.json"):
        """ Сохраняет рыночные данные в файл """
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Данные сохранены в {filename}")


if __name__ == "__main__":
    API_KEY = os.getenv("POCKET_OPTION_API_KEY", "your_api_key_here") 
    api = PocketOptionAPI(API_KEY)
    
    market_data = api.get_market_data("EURUSD", 60)
    if market_data:
        api.save_data_to_file(market_data, "eurusd_data.json")
