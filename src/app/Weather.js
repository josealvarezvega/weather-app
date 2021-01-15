export class Weather {
    constructor(city, countryCode){
        this.apikey ='c872bf23d4fa4250e4419a35446ad440';
            this.city = city;
            this.countryCode = countryCode;
    }

    async getWeather(){
        const URI = `https://api.openweathermap.org/data/2.5/weather?q=${this.city},${this.countryCode}&appid=${this.apikey}&units=metric`;
        const response = await fetch (URI);
        const data = await response.json();
        return data;
    }

    changeLocation(city, countryCode){
        this.city = city;
        this.countryCode= countryCode;

    }
}