import React from 'react';
import { useCurrentFrame } from 'remotion';
import { THEMES } from '../styles/theme';

export const GridBackground = ({ theme = 'dark', showGrass = false }) => {
  const frame = useCurrentFrame();
  const t = THEMES[theme] || THEMES.dark;

  // Subtle ambient drift for the grid pattern
  const gridOffsetY = (frame * 0.4) % 60;
  const gridOffsetX = (Math.sin(frame * 0.02) * 15);

  return (
    <div
      style={{
        position: 'absolute',
        top: 0,
        left: 0,
        width: '100%',
        height: '100%',
        background: t.bgGradient,
        overflow: 'hidden',
        zIndex: 0,
      }}
    >
      {/* Tech Grid Pattern */}
      <div
        style={{
          position: 'absolute',
          top: -60,
          left: -60,
          width: 'calc(100% + 120px)',
          height: 'calc(100% + 120px)',
          backgroundImage: `
            linear-gradient(to right, ${t.gridColor} 1.5px, transparent 1.5px),
            linear-gradient(to bottom, ${t.gridColor} 1.5px, transparent 1.5px)
          `,
          backgroundSize: '80px 80px',
          transform: `translate(${gridOffsetX}px, ${gridOffsetY}px)`,
          opacity: 0.85,
        }}
      />

      {/* Subtle Vignette */}
      <div
        style={{
          position: 'absolute',
          top: 0,
          left: 0,
          width: '100%',
          height: '100%',
          background: 'radial-gradient(circle at 50% 50%, transparent 60%, rgba(0, 0, 0, 0.45) 100%)',
          pointerEvents: 'none',
        }}
      />

      {/* Grass bottom for Frutiger Aero / field scenes */}
      {showGrass && (
        <div
          style={{
            position: 'absolute',
            bottom: 0,
            left: 0,
            width: '100%',
            height: 180,
            background: 'linear-gradient(180deg, #4ade80 0%, #15803d 100%)',
            boxShadow: '0 -10px 40px rgba(0,0,0,0.2)',
          }}
        />
      )}
    </div>
  );
};
