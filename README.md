# 🌤️ Weather Info Fetcher

A simple Python CLI tool that fetches real-time weather data (temperature, condition, and region) for any city using the [WeatherAPI](https://www.weatherapi.com/).

---

## 📌 Features

- Get real-time weather for any city
- Displays:
  - 🌍 Region
  - 🌡️ Temperature (°C)
  - 🌦️ Weather condition (e.g., Sunny, Cloudy)

---

## 🧰 Technologies Used

- Python 3
- `requests` library
- [WeatherAPI](https://www.weatherapi.com/)

---

## 🚀 How to Run

1. **Clone the repository** (if hosted on GitHub):
   ```bash
   git clone https://github.com/your-username/weather-info-fetcher.git
   cd weather-info-fetcher
Install dependencies:

bash
Copy
Edit
pip install requests
Run the script:

bash
Copy
Edit
python weather.py
Input: Type the name of any city when prompted.

📦 Sample Output
bash
Copy
Edit
Enter the name of the city: Hyderabad
Telangana
31.0
Partly cloudy
🔐 API Key
This script uses a public API key. For production or extensive use, please:

Create a free account at weatherapi.com

Get your own API key.

Replace the key in the script:

python
Copy
Edit
url = f"http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={City}"
📜 License
This project is licensed under the MIT License.

🙋‍♂️ Author
Sai Deepak Kolusu
📫 saideepakkolusu39@gmail.com
🔗 LinkedIn

yaml
Copy
Edit

---

Let me know if you’d like to turn this into a full GUI app, add exception handling, or publish it on GitHub
