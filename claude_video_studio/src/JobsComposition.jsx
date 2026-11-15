import React from 'react';
import { Audio, Sequence, staticFile, useVideoConfig } from 'remotion';
import { JobsScene } from './components/JobsScene';
import { ProgressBar } from './components/ProgressBar';

export const JobsComposition = ({ project }) => {
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
      let dur = 60;
      if (s.sfx.includes('typewriter')) dur = 210;
      else if (s.sfx.includes('door_creak')) dur = 90;
      else if (s.sfx.includes('bass_drop')) dur = 120;
      else if (s.sfx.includes('cash')) dur = 60;

      sfxEvents.push({
        file: s.sfx,
        frame: s.startFrame,
        duration: dur,
        volume: s.sfxVolume ?? 0.25,
      });
    }
  });

  return (
    <div
      style={{
        width: '100%',
        height: '100%',
        position: 'relative',
        backgroundColor: '#000000',
        overflow: 'hidden',
      }}
    >
      {/* 1. Ultra-thin subtle retention line */}
      <ProgressBar
        color="#ffffff"
        height={3}
        position="top"
      />

      {/* 2. Eugene Voiceover Audio */}
      {project.voiceAudio && (
        <Audio
          src={staticFile(project.voiceAudio)}
          volume={project.voiceVolume ?? 1.0}
        />
      )}

      {/* 3. Cinematic Soundtrack */}
      {project.bgMusic && (
        <Audio
          src={staticFile(project.bgMusic)}
          volume={project.bgMusicVolume ?? 0.12}
        />
      )}

      {/* 4. Scenario SFX Events */}
      {sfxEvents.map((sfx, idx) => (
        <Sequence key={`sfx-${idx}`} from={sfx.frame} durationInFrames={sfx.duration}>
          <Audio src={staticFile(sfx.file)} volume={sfx.volume} />
        </Sequence>
      ))}

      {/* 5. Minimalist Moving Scenes */}
      {timedScenes.map((scene, idx) => (
        <Sequence
          key={scene.id || idx}
          from={scene.startFrame}
          durationInFrames={scene.durationInFrames}
        >
          <JobsScene sceneIndex={idx} sceneData={scene} />
        </Sequence>
      ))}
    </div>
  );
};
