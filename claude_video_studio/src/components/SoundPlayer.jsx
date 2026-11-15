import React from 'react';
import { Audio, Sequence, staticFile } from 'remotion';

export const SoundPlayer = ({
  voiceAudio = null,
  bgMusic = 'music/ambient_tech.wav',
  sfxEvents = [], // [{ file: 'sfx/pop.wav', frame: 0, volume: 0.7, duration: 60 }]
  sceneVoices = [], // [{ file: 'audio/paris/voice_1.mp3', frame: 0, volume: 1.0 }]
  bgMusicVolume = 0.15,
  voiceVolume = 1.0,
}) => {
  return (
    <>
      {/* Background Ambient Music */}
      {bgMusic && (
        <Audio
          src={staticFile(bgMusic)}
          volume={bgMusicVolume}
          loop
        />
      )}

      {/* Main Global Voiceover Audio */}
      {voiceAudio && (
        <Audio
          src={staticFile(voiceAudio)}
          volume={voiceVolume}
        />
      )}

      {/* Per-Scene Synchronized Voice Clips */}
      {sceneVoices.map((v, idx) => (
        <Sequence key={`voice-${idx}`} from={v.frame}>
          <Audio
            src={staticFile(v.file)}
            volume={v.volume ?? voiceVolume}
          />
        </Sequence>
      ))}

      {/* Synchronized SFX Triggers */}
      {sfxEvents.map((sfx, idx) => (
        <Sequence key={`sfx-${idx}`} from={sfx.frame} durationInFrames={sfx.duration || 60}>
          <Audio
            src={staticFile(sfx.file)}
            volume={sfx.volume ?? 0.7}
          />
        </Sequence>
      ))}
    </>
  );
};
