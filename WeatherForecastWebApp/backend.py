import requests

API_KEY = ""

def get_data(place, forecast_days):
    # API call from openweathermap.org
    request_url = f"api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(request_url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == '__main__':
    get_data(place="Tokyo", forecast_days=3)