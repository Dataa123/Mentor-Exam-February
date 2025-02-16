import { useEffect, useState } from 'react'

function App() {
  const [inputValue, setInputValue] = useState("");
  const [weathers, setWeather] = useState([]);

  const key = "b267c0add690d4d5d51b2e499de2039c";

  const fetching = (x) => {
    fetch(`https://api.openweathermap.org/data/2.5/weather?q=${x}&appid=${key}`)
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
    fetching(inputValue);
  }, [inputValue])


  return (
    <>
      <form>
        <input type="text" placeholder='City...' name='city' onChange={(e) => { setInputValue(e.target.value) }} />
        <input type="submit" />
      </form>

    {
      Object.keys(weathers).map((i) => {
        return weathers[i] == "weather" ? <p>{weathers[i].main}</p> : undefined
      })
    }
    </>
  )
}

export default App