import React from 'react';
import { spring, useCurrentFrame, useVideoConfig, Img, staticFile } from 'remotion';
import { FONT_STACK, SPRING_CONFIGS } from '../styles/theme';

export const PersonCard = ({
  name = '',
  image = '',
  delay = 0,
  width = 320,
  height = 420,
  scale = 1.0,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Spring entrance
  const entrance = spring({
    frame: frame - delay,
    fps,
    config: SPRING_CONFIGS.snappy,
  });

  // Ambient floating
  const floatOffset = Math.sin((frame + delay * 5) * 0.05) * 6;

  // Resolve image source (either external URL or local staticFile)
  const imageSrc = image.startsWith('http') ? image : staticFile(image);

  return (
    <div
      style={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        opacity: entrance,
        transform: `translateY(${(1 - entrance) * 60 + floatOffset}px) scale(${entrance * scale})`,
        zIndex: 5,
      }}
    >
      {/* Photo Frame */}
      <div
        style={{
          width: `${width}px`,
          height: `${height}px`,
          borderRadius: '32px',
          overflow: 'hidden',
          backgroundColor: '#18191c',
          border: '1.5px solid rgba(255, 255, 255, 0.15)',
          boxShadow: '0 20px 50px rgba(0, 0, 0, 0.5), inset 0 1px 1px rgba(255, 255, 255, 0.2)',
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
        }}
      >
        <Img
          src={imageSrc}
          style={{
            width: '100%',
            height: '100%',
            objectFit: 'cover',
          }}
        />
      </div>

      {/* Name Label */}
      {name && (
        <div
          style={{
            marginTop: '22px',
            fontFamily: FONT_STACK,
            fontSize: '40px',
            fontWeight: 700,
            letterSpacing: '-0.02em',
            color: '#f3f4f6',
            textTransform: 'lowercase',
            textShadow: '0 2px 10px rgba(0,0,0,0.5)',
          }}
        >
          {name}
        </div>
      )}
    </div>
  );
};
