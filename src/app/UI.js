export class UI{

    constructor(){
        this.location = document.getElementById('weather-location');
        this.desc = document.getElementById('weather-description');
        this.string = document.getElementById('weather-string');
        this.temp_max = document.getElementById('weather-max');
        this.temp_min = document.getElementById('weather-min');       
        this.humidity = document.getElementById('weather-humidity');
        this.wind = document.getElementById('weather-wind');
    }

    render(weather){
        this.location.textContent = weather.name + ' / '+ weather.sys.country;
        this.desc.textContent = weather.weather[0].description;
        this.string.textContent = ' Temp.Act :' + weather.main.temp + ' ºC ';
        this.temp_max.textContent = 'temp.Max :' + weather.main.temp_max + ' ºC ';
        this.temp_min.textContent = 'temp.Min :' + weather.main.temp_min + ' ºC ';
        this.humidity.textContent = ' Humedad: ' + weather.main.humidity + '%';
        this.wind.textContent = ' Viento: ' + weather.wind.speed + ' m/s ';
    }

}