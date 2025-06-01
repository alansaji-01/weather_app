# weather/views.py - Add error handling and debug output
import requests
from django.conf import settings
from django.shortcuts import render
import socket

def current_weather(request):
    try:
        # Test DNS resolution first
        socket.gethostbyname('api.openweathermap.org')
        
        api_key = settings.WEATHER_API_KEY
        location = request.GET.get('location', 'London')
        
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={location}"
            f"&appid={api_key}&units=metric",
            timeout=5  # Add timeout
        )
        data = response.json()
        return render(request, 'weather/weather.html', {
            'location': location,
            'temp': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        })
        
    except socket.gaierror:
        return render(request, 'weather/weather.html', 
                    {'error': 'Network error: Could not resolve API hostname'})
    except requests.exceptions.RequestException as e:
        return render(request, 'weather/weather.html', 
                    {'error': f'API error: {str(e)}'})
    except Exception as e:
        return render(request, 'weather/weather.html', 
                    {'error': f'Unexpected error: {str(e)}'})