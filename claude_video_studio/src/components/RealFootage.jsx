import React from 'react';
import { interpolate, spring, staticFile, useCurrentFrame, useVideoConfig } from 'remotion';

export const RealFootage = ({
  src,
  alt = 'Real Footage',
  mode = 'card', // 'card' | 'fullscreen'
  width = 860,
  height = 980,
  glowColor = 'rgba(255, 255, 255, 0.2)',
  tag = null,
  zoomDirection = 'in', // 'in' | 'out'
  delay = 0,
}) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  // Smooth 60fps spring entrance for card mode
  const entrance = spring({
    frame: Math.max(0, frame - delay),
    fps,
    config: {
      damping: 14,
      mass: 0.75,
      stiffness: 110,
    },
  });

  const cardOpacity = interpolate(entrance, [0, 1], [0, 1]);
  const cardScale = interpolate(entrance, [0, 1], [0.9, 1.0]);

  // Cinematic Ken Burns slow zoom (smooth 60fps)
  const zoomStart = zoomDirection === 'in' ? 1.0 : 1.14;
  const zoomEnd = zoomDirection === 'in' ? 1.14 : 1.0;
  const imageZoom = interpolate(frame, [0, durationInFrames], [zoomStart, zoomEnd], {
    extrapolateRight: 'clamp',
  });

  // Slow subtle drift
  const panY = interpolate(frame, [0, durationInFrames], [0, -18], {
    extrapolateRight: 'clamp',
  });

  if (mode === 'fullscreen') {
    return (
      <div
        style={{
          position: 'absolute',
          top: 0,
          left: 0,
          width: '100%',
          height: '100%',
          overflow: 'hidden',
          zIndex: 1,
        }}
      >
        <img
          src={staticFile(src)}
          alt={alt}
          style={{
            width: '100%',
            height: '100%',
            objectFit: 'cover',
            transform: `scale(${imageZoom}) translateY(${panY}px)`,
            filter: 'brightness(0.72) contrast(1.08)',
          }}
        />
        {/* Top/bottom dark gradient overlay for text readability */}
        <div
          style={{
            position: 'absolute',
            inset: 0,
            background:
              'linear-gradient(to bottom, rgba(10,10,12,0.92) 0%, rgba(10,10,12,0.3) 30%, rgba(10,10,12,0.3) 70%, rgba(10,10,12,0.95) 100%)',
          }}
        />
      </div>
    );
  }

  // Card Mode (floating high-retention glass frame)
  return (
    <div
      style={{
        opacity: cardOpacity,
        transform: `scale(${cardScale})`,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        zIndex: 5,
      }}
    >
      <div
        style={{
          position: 'relative',
          width,
          height,
          borderRadius: 32,
          overflow: 'hidden',
          boxShadow: `0 30px 80px rgba(0, 0, 0, 0.8), 0 0 50px ${glowColor}`,
          border: '1.5px solid rgba(255, 255, 255, 0.22)',
          backgroundColor: '#121318',
        }}
      >
        <img
          src={staticFile(src)}
          alt={alt}
          style={{
            width: '100%',
            height: '100%',
            objectFit: 'cover',
            transform: `scale(${imageZoom}) translateY(${panY}px)`,
          }}
        />

        {/* Subtle glass vignette */}
        <div
          style={{
            position: 'absolute',
            inset: 0,
            background:
              'radial-gradient(ellipse at center, rgba(0,0,0,0) 50%, rgba(0,0,0,0.55) 100%)',
            pointerEvents: 'none',
          }}
        />

        {/* Location / Date Pill Tag */}
        {tag && (
          <div
            style={{
              position: 'absolute',
              bottom: 24,
              left: 24,
              display: 'flex',
              alignItems: 'center',
              gap: 10,
              padding: '10px 20px',
              borderRadius: 999,
              background: 'rgba(10, 10, 15, 0.82)',
              backdropFilter: 'blur(16px)',
              border: '1px solid rgba(255, 255, 255, 0.25)',
              color: '#ffffff',
              fontSize: 24,
              fontWeight: 600,
              fontFamily: 'Inter, system-ui, sans-serif',
              boxShadow: '0 8px 24px rgba(0, 0, 0, 0.5)',
            }}
          >
            <span style={{ fontSize: 22 }}>📍</span>
            <span>{tag}</span>
          </div>
        )}
      </div>
    </div>
  );
};
