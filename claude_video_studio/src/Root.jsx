import React from 'react';
import { Composition } from 'remotion';
import { JobsComposition } from './JobsComposition';
import project from '../projects/steve_jobs/script.json';

const totalDurationInFrames = project.scenes.reduce(
  (acc, scene) => acc + scene.durationInFrames,
  0
);

export const RemotionRoot = () => {
  return (
    <Composition
      id="MainVideo"
      component={JobsComposition}
      durationInFrames={totalDurationInFrames || 1654}
      fps={60}
      width={1080}
      height={1920}
      defaultProps={{ project }}
    />
  );
};
