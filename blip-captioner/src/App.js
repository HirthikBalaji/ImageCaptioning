import React, { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [url, setUrl] = useState("");
  const [caption, setCaption] = useState("");

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("image", file);

    const res = await axios.post("http://localhost:5000/caption", formData);
    setCaption(res.data.caption);
  };

  const handleURL = async () => {
    const res = await axios.post("http://localhost:5000/caption", { url });
    setCaption(res.data.caption);
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h1>BLIP Image Captioning</h1>

      <div>
        <input type="file" onChange={(e) => setFile(e.target.files[0])} />
        <button onClick={handleUpload}>Upload Image</button>
      </div>

      <div style={{ marginTop: "1rem" }}>
        <input
          type="text"
          placeholder="Image URL"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
        />
        <button onClick={handleURL}>Submit URL</button>
      </div>

      {caption && (
        <div style={{ marginTop: "2rem" }}>
          <h3>Caption:</h3>
          <p>{caption}</p>
        </div>
      )}
    </div>
  );
}

export default App;
