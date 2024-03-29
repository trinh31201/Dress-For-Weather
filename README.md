# Dress For Weather

## Introduction
Dress For Weather is a Python application that helps you decide what to wear based on the current weather conditions. By utilizing the [ClimaCell Weather API](https://www.tomorrow.io/weather-api/), it fetches real-time weather forecasts and processes this data through decision trees to recommend the most suitable outfit for the day.

## Features
- Real-time weather forecast fetching using [ClimaCell Weather API](https://www.tomorrow.io/weather-api/).
- Automated outfit suggestions based on temperature, precipitation, and weather conditions.
- Customizable settings for personalized recommendations.
- Simple and intuitive setup and usage.

## Getting Started

### Prerequisites
- Python 3.x
- requests library

### Installation
1. Clone the repository or download the source code.
2. The Requests library in Python provides abstractions that simplify calling APIs by a lot. The good news is the developer dashboard generates ready to use Python code, so our process is extremely streamlined.

### API Key
- Obtain a free API key from [ClimaCell](https://www.tomorrow.io/weather-api/) by signing up at their dashboard.

### Latitude and Longitude
- Determine your location's latitude and longitude for accurate weather forecasts. Websites like https://www.gps-coordinates.net can help you find these coordinates.

## Usage
1. Open `weather.py` in your preferred text editor.
2. Replace `LAT`, `LON` and `APIKEY` with your latitude, longitude and API key on the last line!
3. Run the script
```bash
python3 weather.py
```
5. Get your outfit suggestion for the next 6 hours.

## How It Works
The application calls the ClimaCell Weather API to retrieve the forecast for your location. It then processes this data through decision trees to determine factors like the day's minimum and maximum temperature, weather code and more. Based on this analysis, it suggests an appropriate outfit.

## Contributing
Contributions to Dress Code Assistant are welcome! Feel free to fork the repository, make your changes, and submit a pull request.
