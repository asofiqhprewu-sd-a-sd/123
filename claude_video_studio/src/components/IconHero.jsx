import React from 'react';
import { spring, useCurrentFrame, useVideoConfig, Img, staticFile } from 'remotion';
import { SPRING_CONFIGS } from '../styles/theme';

export const IconHero = ({
  icon = '',
  size = 380,
  delay = 0,
  glowColor = 'rgba(16, 185, 129, 0.25)',
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Snappy spring entrance
  const entrance = spring({
    frame: frame - delay,
    fps,
    config: SPRING_CONFIGS.snappy,
  });

  // Smooth floating and gentle tilt
  const floatY = Math.sin((frame + delay * 4) * 0.06) * 10;
  const rotateDeg = Math.sin((frame + delay * 4) * 0.04) * 4;

  const iconSrc = icon.startsWith('http') ? icon : staticFile(icon);

  return (
    <div
      style={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        opacity: entrance,
        transform: `translateY(${(1 - entrance) * 70 + floatY}px) scale(${entrance}) rotate(${rotateDeg}deg)`,
        filter: `drop-shadow(0 20px 40px ${glowColor})`,
        zIndex: 5,
      }}
    >
      <Img
        src={iconSrc}
        style={{
          width: `${size}px`,
          height: `${size}px`,
          objectFit: 'contain',
          mixBlendMode: 'screen',
        }}
      />
    </div>
  );
};
