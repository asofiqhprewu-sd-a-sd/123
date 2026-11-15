import React from 'react';
import { spring, useCurrentFrame, useVideoConfig } from 'remotion';
import { FONT_STACK, SPRING_CONFIGS } from '../styles/theme';

export const QuoteCard = ({
  quote = 'Искусственный интеллект станет либо лучшим, либо худшим событием в истории человечества.',
  author = 'Стивен Хокинг',
  title = 'физик-теоретик',
  delay = 5,
  width = 680,
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
        width: `${width}px`,
        backgroundColor: 'rgba(15, 23, 42, 0.85)',
        backdropFilter: 'blur(20px)',
        borderRadius: '36px',
        border: '1.5px solid rgba(255, 255, 255, 0.15)',
        padding: '48px 46px',
        boxSizing: 'border-box',
        boxShadow: '0 25px 60px rgba(0, 0, 0, 0.65)',
        opacity: entrance,
        transform: `translateY(${(1 - entrance) * 60}px) scale(${entrance})`,
        zIndex: 6,
        position: 'relative',
      }}
    >
      {/* Giant Neon Quote Symbol */}
      <div
        style={{
          fontFamily: 'Georgia, serif',
          fontSize: '90px',
          lineHeight: 0.6,
          color: '#38bdf8',
          opacity: 0.45,
          marginBottom: '20px',
        }}
      >
        “
      </div>

      {/* Quote Text */}
      <div
        style={{
          fontFamily: FONT_STACK,
          fontSize: '32px',
          fontWeight: 600,
          fontStyle: 'italic',
          lineHeight: 1.45,
          color: '#f8fafc',
          marginBottom: '28px',
          letterSpacing: '-0.01em',
        }}
      >
        {quote}
      </div>

      {/* Author attribution */}
      <div style={{ borderTop: '1px solid rgba(255, 255, 255, 0.1)', paddingTop: '18px' }}>
        <div
          style={{
            fontFamily: FONT_STACK,
            fontSize: '24px',
            fontWeight: 700,
            color: '#38bdf8',
          }}
        >
          {author}
        </div>
        {title && (
          <div
            style={{
              fontFamily: FONT_STACK,
              fontSize: '18px',
              color: '#94a3b8',
              marginTop: 4,
            }}
          >
            {title}
          </div>
        )}
      </div>
    </div>
  );
};
