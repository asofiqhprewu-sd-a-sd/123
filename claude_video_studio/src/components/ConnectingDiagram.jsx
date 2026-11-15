import React from 'react';
import { spring, useCurrentFrame, useVideoConfig } from 'remotion';
import { FONT_STACK, SPRING_CONFIGS } from '../styles/theme';

export const ConnectingDiagram = ({
  leftElement,
  rightElement,
  leftLabel = '',
  rightLabel = '',
  delay = 0,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const entrance = spring({
    frame: frame - delay,
    fps,
    config: SPRING_CONFIGS.snappy,
  });

  // Animated dashes
  const dashOffset = -(frame * 2.5);

  return (
    <div
      style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        width: '100%',
        padding: '0 40px',
        boxSizing: 'border-box',
        opacity: entrance,
        transform: `scale(${entrance})`,
        zIndex: 5,
        gap: '24px',
      }}
    >
      {/* Left Item */}
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        {leftElement}
        {leftLabel && (
          <div
            style={{
              marginTop: 18,
              fontFamily: FONT_STACK,
              fontSize: 34,
              fontWeight: 600,
              color: '#ffffff',
            }}
          >
            {leftLabel}
          </div>
        )}
      </div>

      {/* Dashed connecting line */}
      <div style={{ width: 140, height: 10, display: 'flex', alignItems: 'center' }}>
        <svg width="140" height="10" viewBox="0 0 140 10">
          <line
            x1="0"
            y1="5"
            x2="140"
            y2="5"
            stroke="#ffffff"
            strokeWidth="3.5"
            strokeDasharray="14 10"
            strokeDashoffset={dashOffset}
            opacity="0.75"
          />
        </svg>
      </div>

      {/* Right Item */}
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        {rightElement}
        {rightLabel && (
          <div
            style={{
              marginTop: 18,
              fontFamily: FONT_STACK,
              fontSize: 34,
              fontWeight: 600,
              color: '#ffffff',
            }}
          >
            {rightLabel}
          </div>
        )}
      </div>
    </div>
  );
};
