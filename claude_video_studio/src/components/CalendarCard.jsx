import React from 'react';
import { spring, useCurrentFrame, useVideoConfig } from 'remotion';
import { FONT_STACK, SPRING_CONFIGS } from '../styles/theme';

export const CalendarCard = ({
  month = 'ноябрь',
  day = '30',
  delay = 0,
  size = 280,
  headerColor = '#ef4444',
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const entrance = spring({
    frame: frame - delay,
    fps,
    config: SPRING_CONFIGS.snappy,
  });

  const floatY = Math.sin((frame + delay * 3) * 0.05) * 8;
  const dayFontSize = String(day).length > 2 ? size * 0.26 : size * 0.44;

  return (
    <div
      style={{
        width: `${size}px`,
        backgroundColor: '#f8fafc',
        borderRadius: '36px',
        overflow: 'hidden',
        boxShadow: '0 25px 60px rgba(0, 0, 0, 0.6)',
        border: '2px solid rgba(255, 255, 255, 0.15)',
        opacity: entrance,
        transform: `translateY(${(1 - entrance) * 70 + floatY}px) scale(${entrance})`,
        zIndex: 6,
      }}
    >
      {/* Month Bar */}
      <div
        style={{
          backgroundColor: headerColor,
          color: '#ffffff',
          fontFamily: FONT_STACK,
          fontSize: `${size * 0.16}px`,
          fontWeight: 700,
          textAlign: 'center',
          padding: '16px 0',
          letterSpacing: '-0.02em',
        }}
      >
        {month}
      </div>

      {/* Day Body */}
      <div
        style={{
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          padding: '30px 10px 36px 10px',
          color: '#1e293b',
          fontFamily: FONT_STACK,
          fontSize: `${dayFontSize}px`,
          fontWeight: 800,
          lineHeight: 1,
        }}
      >
        {day}
      </div>
    </div>
  );
};
