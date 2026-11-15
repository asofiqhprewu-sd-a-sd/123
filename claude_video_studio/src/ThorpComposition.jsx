import React from 'react';
import { Audio, Sequence, staticFile, useVideoConfig } from 'remotion';
import { ThorpScene } from './components/ThorpScene';
import { ProgressBar } from './components/ProgressBar';

export const ThorpComposition = ({ project }) => {
  const { fps } = useVideoConfig();
  const scenes = project.scenes || [];

  let currentStart = 0;
  const timedScenes = scenes.map((s) => {
    const startFrame = currentStart;
    currentStart += s.durationInFrames;
    return { ...s, startFrame };
  });

  const sfxEvents = [];
  timedScenes.forEach((s) => {
    if (s.sfx) {
      sfxEvents.push({
        file: s.sfx,
        frame: s.startFrame,
        volume: s.sfxVolume ?? 0.12, // Quiet, gentle notification sound!
      });
    }
  });

  return (
    <div
      style={{
        width: '100%',
        height: '100%',
        position: 'relative',
        backgroundColor: '#0a0a0c',
        overflow: 'hidden',
      }}
    >
      {/* 1. Golden Retention Progress Bar (Top) */}
      <ProgressBar
        color="#f59e0b"
        height={8}
        position="top"
      />

      {/* 2. Master Voiceover Audio (Evgeny) */}
      {project.voiceAudio && (
        <Audio
          src={staticFile(project.voiceAudio)}
          volume={project.voiceVolume ?? 1.0}
        />
      )}

      {/* 3. Dark Casino Thriller Ambient Music */}
      {project.bgMusic && (
        <Audio
          src={staticFile(project.bgMusic)}
          volume={project.bgMusicVolume ?? 0.14}
        />
      )}

      {/* 4. Synchronized Soft Notification Sounds (Volume 0.12) */}
      {sfxEvents.map((sfx, idx) => (
        <Sequence key={`sfx-${idx}`} from={sfx.frame} durationInFrames={60}>
          <Audio src={staticFile(sfx.file)} volume={sfx.volume} />
        </Sequence>
      ))}

      {/* 5. Render Each Slide Sequence */}
      {timedScenes.map((scene, idx) => (
        <Sequence
          key={scene.id || idx}
          from={scene.startFrame}
          durationInFrames={scene.durationInFrames}
        >
          <ThorpScene
            photo={scene.photo}
            text={scene.text}
            words={scene.words || []}
            widget={scene.widget}
            badge={scene.badge}
            sfx={scene.sfx}
          />
        </Sequence>
      ))}
    </div>
  );
};
