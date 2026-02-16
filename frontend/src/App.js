import React from "react";
import axios from "axios";

function App() {

  const handlePredict = async () => {
    const response = await axios.post(
        "http://127.0.0.1:8001/predict",
        {
          transcript: {"Calculus 3": 3.7},
          target_course: "Physics 1"
        }
    );

    alert(JSON.stringify(response.data));
  };

  return (
      <div>
        <h1>Course Compass</h1>
        <button onClick={handlePredict}>
          Predict Grade
        </button>
      </div>
  );
}

export default App;
