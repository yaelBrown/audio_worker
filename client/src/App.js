import './App.css';
import ReactAudioPlayer from 'react-audio-player'

import testSong from './Assets/Bad_Bunny_-_Yonaguni.mp3'
import waveForm from './Assets/Bad_Bunny_-_Yonaguni.mp3_waveform.png'
import albumArt from './Assets/Bad_Bunny-Yonaguni-albumArt.webp'


function App() {
  const audioElement = new Audio(testSong)
  // audioElement.play()

  return (
    <div className="App">
      <h1>React Audio player</h1>
      {/* <h2>ReactAudioPlayer component: </h2>
      <ReactAudioPlayer
        src={testSong}
        autoPlay
        controls
      />
      <br/> */}

      {/* <audio src={testSong} controls/> */}

      {/* <h2>Original Waveform output:</h2>
      <img src={waveForm} alt="x" /> */}

      {/* <h2>Modified Waveform with css:</h2>
      <div id="waveformDiv" style={{ backgroundImage: `url(${waveForm})`}} /> */}

      {/* <h2>Album Art</h2>
      <img src={albumArt} alt="x" /> */}


    </div>
  );
}

export default App;
