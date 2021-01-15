require('./index.css');
const { Weather } = require ('./Weather');

const {UI} = require('./UI');
const ui = new UI();

const {Store} = require('./Store');
const store = new Store();
const {city, countryCode} = store.getLocationData();

const weather = new Weather(city,countryCode);


async function fetchweather(){
    const data = await weather.getWeather();
    console.log(data);
    ui.render(data);
}

document.getElementById('w-change-btn').addEventListener('click', (e) => {
    const city = document.getElementById('city').value;
    const countryCode = document.getElementById('countryCode').value;
    weather.changeLocation(city, countryCode);
    store.setLocationData(city, countryCode);
    fetchweather();
    e.preventDefault();
});



document.addEventListener('DOMContentLoaded', fetchweather);