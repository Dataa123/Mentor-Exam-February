import { useEffect, useState } from 'react'

function App() {
  const [city, setCity] = useState("");
  const [weathers, setWeather] = useState([]);

  const key = "b267c0add690d4d5d51b2e499de2039c";

  const fetching = (city) => {
    fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${key}`)
    .then((json1) => {
      return json1.json();
    })
    .then((data) => {
      console.log(data);
      setWeather(data);
    })
    .catch((err) => {console.log(err)});
  }

  useEffect(() => {
    fetching(city)
  }, [city])

  const handleSubmit = (e) => {
    e.preventDefault();

    const cityName = e.target.city.value;
    setCity(cityName);
  }

  return (
    <>
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder='City...' name='city' />
        <input type="submit" />
      </form>
 
      {
        city
      }
    </>
  )
}

export default App