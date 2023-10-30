import React, { useState, useRef } from 'react';

const VideoComponent = ({ videoSourceURL }) => {
  const videoRef = useRef(null);
  const [isPlaying, setIsPlaying] = useState(false);

  const togglePlay = () => {
    if (videoRef.current.paused) {
      videoRef.current.play();
      setIsPlaying(true);
    } else {
      videoRef.current.pause();
      setIsPlaying(false);
    }
  };

  return (
    <div>
      <video
        ref={videoRef}
        controls
        width="400"
        height="300"
      >
        <source src={videoSourceURL} type="video/mp4" />
        {/* You can add multiple source elements for different video formats */}
      </video>
      <div>
        <button onClick={togglePlay}>
          {isPlaying ? 'Pause' : 'Play'}
        </button>
      </div>
    </div>
  );
};

export default VideoComponent;
