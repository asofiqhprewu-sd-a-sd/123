import React from 'react';
import { spring, useCurrentFrame, useVideoConfig } from 'remotion';
import { FONT_STACK, SPRING_CONFIGS } from '../styles/theme';

export const BadgePill = ({
  text = '',
  icon = null,
  color = '#ea580c', // orange/coral
  textColor = '#ffffff',
  delay = 0,
  fontSize = 28,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const entrance = spring({
    frame: frame - delay,
    fps,
    config: SPRING_CONFIGS.snappy,
  });

  return (
    <div
      style={{
        display: 'inline-flex',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '12px 28px',
        backgroundColor: color,
        borderRadius: '9999px',
        border: '1px solid rgba(255, 255, 255, 0.2)',
        boxShadow: '0 10px 25px rgba(0, 0, 0, 0.35)',
        opacity: entrance,
        transform: `scale(${entrance})`,
        zIndex: 8,
      }}
    >
      {icon && <span style={{ marginRight: 10, fontSize: fontSize * 0.9 }}>{icon}</span>}
      <span
        style={{
          fontFamily: FONT_STACK,
          fontSize: `${fontSize}px`,
          fontWeight: 700,
          color: textColor,
          letterSpacing: '-0.01em',
        }}
      >
        {text}
      </span>
    </div>
  );
};
