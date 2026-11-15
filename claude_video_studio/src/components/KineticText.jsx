import React from 'react';
import { FONT_STACK } from '../styles/theme';

export const KineticText = ({
  text = '',
  words = [],
  currentTimeSec = 0,
  fontSize = 52,
  position = 'bottom', // default to bottom as requested!
}) => {
  // If word timestamps are provided, highlight dynamically
  const wordList =
    words.length > 0
      ? words
      : text
          .split(' ')
          .filter(Boolean)
          .map((w, i, arr) => ({
            text: w,
            start: i * 0.4,
            end: (i + 1) * 0.4,
          }));

  // Clean positioning at the bottom with dark readable glass plate
  return (
    <div
      style={{
        position: 'absolute',
        bottom: '80px',
        left: 0,
        width: '100%',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        padding: '0 48px',
        boxSizing: 'border-box',
        zIndex: 20,
      }}
    >
      <div
        style={{
          display: 'flex',
          flexWrap: 'wrap',
          justifyContent: 'center',
          alignItems: 'center',
          gap: '12px 16px',
          padding: '24px 38px',
          borderRadius: 28,
          background: 'rgba(10, 10, 14, 0.88)',
          backdropFilter: 'blur(20px)',
          border: '1.5px solid rgba(255, 255, 255, 0.16)',
          boxShadow: '0 20px 50px rgba(0, 0, 0, 0.8), 0 0 30px rgba(0, 0, 0, 0.5)',
          maxWidth: 960,
        }}
      >
        {wordList.map((item, idx) => {
          const itemText = item.text || item.word || '';
          const isActive =
            currentTimeSec >= item.start && currentTimeSec <= item.end;
          const isPast = currentTimeSec > item.end;

          // High-contrast, maximum readability
          const color = isActive
            ? '#38bdf8' // active word glowing vibrant cyan
            : isPast
            ? '#ffffff' // spoken words bright white
            : 'rgba(255, 255, 255, 0.45)'; // upcoming words semi-transparent white

          const scale = isActive ? 1.08 : 1.0;
          const textShadow = isActive
            ? '0 0 20px rgba(56, 189, 248, 0.8), 0 2px 8px rgba(0,0,0,0.9)'
            : '0 2px 8px rgba(0,0,0,0.8)';

          return (
            <span
              key={idx}
              style={{
                fontFamily: FONT_STACK,
                fontSize: `${fontSize}px`,
                fontWeight: 800,
                lineHeight: 1.3,
                letterSpacing: '-0.02em',
                color,
                transform: `scale(${scale})`,
                transition: 'all 0.08s ease',
                textShadow,
                textTransform: 'lowercase',
              }}
            >
              {itemText}
            </span>
          );
        })}
      </div>
    </div>
  );
};
