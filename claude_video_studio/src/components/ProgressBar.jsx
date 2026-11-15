import React from 'react';
import { useCurrentFrame, useVideoConfig } from 'remotion';

export const ProgressBar = ({
  color = '#38bdf8',
  height = 8,
  position = 'top', // 'top' or 'bottom'
}) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();

  const progressPercent = Math.min(100, Math.max(0, (frame / durationInFrames) * 100));

  return (
    <div
      style={{
        position: 'absolute',
        top: position === 'top' ? 0 : undefined,
        bottom: position === 'bottom' ? 0 : undefined,
        left: 0,
        width: '100%',
        height: `${height}px`,
        backgroundColor: 'rgba(255, 255, 255, 0.08)',
        zIndex: 50,
      }}
    >
      <div
        style={{
          width: `${progressPercent}%`,
          height: '100%',
          backgroundColor: color,
          boxShadow: `0 0 16px ${color}`,
        }}
      />
    </div>
  );
};
