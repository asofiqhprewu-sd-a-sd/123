import React from 'react';
import { interpolate, spring, staticFile, useCurrentFrame, useVideoConfig } from 'remotion';

export const PhotoComparison = ({
  leftPhoto,
  rightPhoto,
  leftLabel = '1888',
  rightLabel = 'Сегодня',
  tag = 'История создания',
  delay = 0,
}) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  const entrance = spring({
    frame: Math.max(0, frame - delay),
    fps,
    config: { damping: 14, mass: 0.8, stiffness: 100 },
  });

  const zoom = interpolate(frame, [0, durationInFrames], [1.0, 1.1], {
    extrapolateRight: 'clamp',
  });

  return (
    <div
      style={{
        opacity: entrance,
        transform: `scale(${interpolate(entrance, [0, 1], [0.92, 1])})`,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        gap: 20,
        zIndex: 5,
      }}
    >
      <div
        style={{
          position: 'relative',
          display: 'flex',
          gap: 20,
          width: 920,
          height: 820,
        }}
      >
        {/* Left Photo (e.g. Historical 1888) */}
        <div
          style={{
            flex: 1,
            position: 'relative',
            borderRadius: 24,
            overflow: 'hidden',
            border: '1.5px solid rgba(255, 255, 255, 0.2)',
            boxShadow: '0 20px 50px rgba(0,0,0,0.6)',
            backgroundColor: '#111',
          }}
        >
          <img
            src={staticFile(leftPhoto)}
            alt={leftLabel}
            style={{
              width: '100%',
              height: '100%',
              objectFit: 'cover',
              transform: `scale(${zoom})`,
              filter: 'grayscale(0.4) contrast(1.1)',
            }}
          />
          <div
            style={{
              position: 'absolute',
              bottom: 16,
              left: 16,
              padding: '6px 16px',
              borderRadius: 999,
              background: 'rgba(0,0,0,0.75)',
              backdropFilter: 'blur(10px)',
              color: '#facc15',
              fontSize: 22,
              fontWeight: 700,
              border: '1px solid rgba(250, 204, 21, 0.3)',
            }}
          >
            {leftLabel}
          </div>
        </div>

        {/* Center VS or Arrow Badge */}
        <div
          style={{
            position: 'absolute',
            top: '50%',
            left: '50%',
            transform: 'translate(-50%, -50%)',
            width: 72,
            height: 72,
            borderRadius: '50%',
            background: 'linear-gradient(135deg, #ef4444, #f97316)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            boxShadow: '0 0 30px rgba(239, 68, 68, 0.7)',
            border: '3px solid #ffffff',
            color: '#ffffff',
            fontWeight: 900,
            fontSize: 24,
            zIndex: 10,
          }}
        >
          ➔
        </div>

        {/* Right Photo (e.g. Modern) */}
        <div
          style={{
            flex: 1,
            position: 'relative',
            borderRadius: 24,
            overflow: 'hidden',
            border: '1.5px solid rgba(255, 255, 255, 0.2)',
            boxShadow: '0 20px 50px rgba(0,0,0,0.6)',
            backgroundColor: '#111',
          }}
        >
          <img
            src={staticFile(rightPhoto)}
            alt={rightLabel}
            style={{
              width: '100%',
              height: '100%',
              objectFit: 'cover',
              transform: `scale(${zoom})`,
            }}
          />
          <div
            style={{
              position: 'absolute',
              bottom: 16,
              right: 16,
              padding: '6px 16px',
              borderRadius: 999,
              background: 'rgba(0,0,0,0.75)',
              backdropFilter: 'blur(10px)',
              color: '#38bdf8',
              fontSize: 22,
              fontWeight: 700,
              border: '1px solid rgba(56, 189, 248, 0.3)',
            }}
          >
            {rightLabel}
          </div>
        </div>
      </div>
    </div>
  );
};
