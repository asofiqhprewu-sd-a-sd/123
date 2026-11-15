import React from 'react';
import { spring, useCurrentFrame, useVideoConfig, Img, staticFile } from 'remotion';
import { FONT_STACK, SPRING_CONFIGS } from '../styles/theme';

export const TweetCard = ({
  name = 'Ilya Sutskever',
  handle = '@ilyasut',
  avatar = '',
  text = 'I deeply regret my participation in the board\'s actions.',
  delay = 5,
  width = 540,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const entrance = spring({
    frame: frame - delay,
    fps,
    config: SPRING_CONFIGS.snappy,
  });

  const floatY = Math.sin((frame + delay * 3) * 0.05) * 5;
  const avatarSrc = avatar ? (avatar.startsWith('http') ? avatar : staticFile(avatar)) : null;

  return (
    <div
      style={{
        width: `${width}px`,
        backgroundColor: 'rgba(20, 20, 24, 0.85)',
        backdropFilter: 'blur(20px)',
        border: '1.5px solid rgba(255, 255, 255, 0.12)',
        borderRadius: '32px',
        padding: '36px 38px',
        boxSizing: 'border-box',
        boxShadow: '0 24px 60px rgba(0, 0, 0, 0.6)',
        opacity: entrance,
        transform: `translateY(${(1 - entrance) * 60 + floatY}px) scale(${entrance})`,
        zIndex: 6,
      }}
    >
      {/* Header with avatar & name */}
      <div style={{ display: 'flex', alignItems: 'center', marginBottom: '22px' }}>
        {avatarSrc ? (
          <Img
            src={avatarSrc}
            style={{
              width: 56,
              height: 56,
              borderRadius: '50%',
              marginRight: 16,
              objectFit: 'cover',
            }}
          />
        ) : (
          <div
            style={{
              width: 56,
              height: 56,
              borderRadius: '50%',
              backgroundColor: '#374151',
              marginRight: 16,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              color: '#fff',
              fontSize: 22,
              fontWeight: 700,
            }}
          >
            {name[0]}
          </div>
        )}

        <div>
          <div
            style={{
              fontFamily: FONT_STACK,
              fontSize: '28px',
              fontWeight: 700,
              color: '#ffffff',
              lineHeight: 1.2,
            }}
          >
            {name}
          </div>
          {handle && (
            <div
              style={{
                fontFamily: FONT_STACK,
                fontSize: '20px',
                color: '#9ca3af',
              }}
            >
              {handle}
            </div>
          )}
        </div>
      </div>

      {/* Tweet Body */}
      <div
        style={{
          fontFamily: FONT_STACK,
          fontSize: '32px',
          fontWeight: 500,
          lineHeight: 1.4,
          color: '#e5e7eb',
          letterSpacing: '-0.01em',
        }}
      >
        {text}
      </div>
    </div>
  );
};
