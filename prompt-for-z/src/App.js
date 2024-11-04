import React, { useState } from 'react';
import './App.css';

function App() {
  const [inputText, setInputText] = useState('');
  const [outputText, setOutputText] = useState('Your input will appear here');

  const handleInputChange = async (event) => {
    const newText = event.target.value;
    setInputText(newText);
  };

  const setOuput = async () => {
    try {
      // Make a GET request to the API (replace with your desired API URL)
      const response = await fetch(`http://localhost:5000/api/greet?user_input=This shit is bussin on God`, {
        mode: "no-cors"
      });
      if (!response.ok) throw new Error("API request failed");

      const data = await response.json();

      // Assuming the response contains a 'title' field for demonstration
      setOutputText(data.message || "No title found for this post");
    } catch (error) {
      setOutputText("Error fetching data: " + error.message);
    }

  }


  return (
    <div className="App">
      <div className="container">
        {/* Left Panel for Input and Output */}
        <div className="left-panel">
          <h2>Input and Output</h2>
          <div className="input-section">
            <label htmlFor="inputField">Enter text:</label>
            <input
              type="text"
              id="inputField"
              value={inputText}
              onChange={handleInputChange}
              placeholder="Type something here"
            />
          </div>
          <div className="output-section">
            <h3>Output:</h3>
            <p>{outputText}</p>
          </div>
          <button onClick={setOuput}>
            Generate!
          </button>
        </div>


        {/* Right Panel for Video */}
        <div className="right-panel">
          {/* <h2>Brainrot video</h2> */}
          <video width="50%" height="50%" controls src="Uii6jU.mp4">
            Your browser does not support the video tag.
          </video>
        </div>
      </div>
    </div>
  );
}

export default App;
