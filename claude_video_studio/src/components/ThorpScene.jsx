import React from 'react';
import { interpolate, spring, staticFile, useCurrentFrame, useVideoConfig } from 'remotion';
import { FONT_STACK } from '../styles/theme';

export const ThorpScene = ({
  photo,
  text,
  words = [],
  widget,
  badge,
  sfx,
}) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();
  const currentTimeSec = frame / fps;

  // 1. Subtle 60 FPS Ken Burns drift
  const zoom = interpolate(frame, [0, durationInFrames], [1.0, 1.06], {
    extrapolateRight: 'clamp',
  });
  const panY = interpolate(frame, [0, durationInFrames], [0, -18], {
    extrapolateRight: 'clamp',
  });

  // 2. Snappy smooth crossfade in & out (10 frames)
  const fadeIn = interpolate(frame, [0, 10], [0, 1], { extrapolateRight: 'clamp' });
  const fadeOut = interpolate(frame, [durationInFrames - 10, durationInFrames], [1, 0], {
    extrapolateLeft: 'clamp',
  });
  const sceneOpacity = Math.min(fadeIn, fadeOut);

  // 3. Gentle notification drop-in animation from top
  const notifyEntrance = spring({
    frame: Math.max(0, frame - 4),
    fps,
    config: { damping: 16, mass: 0.6, stiffness: 120 },
  });

  return (
    <div
      style={{
        position: 'relative',
        width: '100%',
        height: '100%',
        overflow: 'hidden',
        backgroundColor: '#0a0a0c',
        opacity: sceneOpacity,
      }}
    >
      {/* 1. FULL-BLEED SLIDE PHOTO */}
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
          src={staticFile(photo)}
          alt="Visual"
          style={{
            width: '100%',
            height: '100%',
            objectFit: 'cover',
            transform: `scale(${zoom}) translateY(${panY}px)`,
            filter: 'brightness(0.85) contrast(1.10)',
          }}
        />

        {/* Cinematic dark gradients for crystal-clear readability */}
        <div
          style={{
            position: 'absolute',
            inset: 0,
            background:
              'linear-gradient(to bottom, rgba(10,10,14,0.72) 0%, transparent 22%, rgba(10,10,14,0.2) 50%, rgba(10,10,14,0.92) 84%, rgba(10,10,14,0.98) 100%)',
          }}
        />
      </div>

      {/* 2. TOP NOTIFICATIONS / ОПОВЕЩЕНИЯ (РАЗМЕЩЕНЫ ВВЕРХУ "ТУТ", ЦЕНТР КАДРА ЧИСТЫЙ) */}
      {widget ? (
        // Rich Notification Banner at the TOP
        <div
          style={{
            position: 'absolute',
            top: 68,
            left: 48,
            right: 48,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            gap: 16,
            padding: '12px 24px',
            borderRadius: 999,
            background: 'rgba(12, 14, 20, 0.88)',
            backdropFilter: 'blur(20px)',
            border: `1.5px solid ${widget.borderColor || 'rgba(245, 158, 11, 0.4)'}`,
            boxShadow: `0 12px 32px rgba(0, 0, 0, 0.65), 0 0 24px ${widget.glowColor || 'rgba(245, 158, 11, 0.2)'}`,
            zIndex: 15,
            opacity: notifyEntrance,
            transform: `translateY(${interpolate(notifyEntrance, [0, 1], [-25, 0])}px)`,
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
            <span style={{ fontSize: 28 }}>{widget.icon || badge?.icon || '🔔'}</span>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
              <span
                style={{
                  fontFamily: FONT_STACK,
                  fontSize: 18,
                  fontWeight: 700,
                  color: widget.labelColor || '#94a3b8',
                  textTransform: 'uppercase',
                  letterSpacing: '0.04em',
                }}
              >
                {badge?.label || widget.title}
              </span>
              <span
                style={{
                  fontFamily: FONT_STACK,
                  fontSize: 24,
                  fontWeight: 800,
                  color: widget.valueColor || '#ffffff',
                }}
              >
                {widget.value || widget.title}
              </span>
            </div>
          </div>

          {badge?.sub && (
            <div
              style={{
                padding: '6px 16px',
                borderRadius: 999,
                background: 'rgba(245, 158, 11, 0.22)',
                border: '1px solid rgba(245, 158, 11, 0.45)',
                color: '#facc15',
                fontSize: 18,
                fontWeight: 700,
                fontFamily: FONT_STACK,
                whiteSpace: 'nowrap',
              }}
            >
              {badge.sub}
            </div>
          )}
        </div>
      ) : badge ? (
        // Standard Badge Pills at the TOP (as in user screenshot)
        <div
          style={{
            position: 'absolute',
            top: 68,
            left: 48,
            right: 48,
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            zIndex: 10,
            opacity: notifyEntrance,
            transform: `translateY(${interpolate(notifyEntrance, [0, 1], [-20, 0])}px)`,
          }}
        >
          <div
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: 12,
              padding: '10px 22px',
              borderRadius: 999,
              background: 'rgba(10, 10, 15, 0.82)',
              backdropFilter: 'blur(16px)',
              border: '1px solid rgba(255, 255, 255, 0.20)',
              color: '#ffffff',
              fontSize: 22,
              fontWeight: 600,
              fontFamily: FONT_STACK,
              boxShadow: '0 8px 24px rgba(0, 0, 0, 0.6)',
            }}
          >
            <span>{badge.icon || '📍'}</span>
            <span>{badge.label}</span>
          </div>

          {badge.sub && (
            <div
              style={{
                padding: '8px 18px',
                borderRadius: 999,
                background: 'rgba(245, 158, 11, 0.22)',
                border: '1px solid rgba(245, 158, 11, 0.45)',
                color: '#facc15',
                fontSize: 20,
                fontWeight: 700,
                fontFamily: FONT_STACK,
              }}
            >
              {badge.sub}
            </div>
          )}
        </div>
      ) : null}

      {/* 3. SUBTITLE TEXT: ON PHOTO IN LOWER THIRD */}
      {text && (
        <div
          style={{
            position: 'absolute',
            bottom: 130,
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
              gap: '10px 16px',
              padding: '24px 38px',
              borderRadius: 26,
              background: 'rgba(10, 11, 16, 0.88)',
              backdropFilter: 'blur(24px)',
              border: '1px solid rgba(255, 255, 255, 0.18)',
              boxShadow: '0 24px 60px rgba(0, 0, 0, 0.85)',
              maxWidth: 980,
            }}
          >
            {words.map((item, idx) => {
              const isActive =
                currentTimeSec >= item.start && currentTimeSec <= item.end;
              const isPast = currentTimeSec > item.end;

              // Golden active word
              const color = isActive
                ? '#facc15'
                : isPast
                ? '#ffffff'
                : 'rgba(255, 255, 255, 0.45)';

              const scale = isActive ? 1.08 : 1.0;
              const textShadow = isActive
                ? '0 0 24px rgba(250, 204, 21, 0.75), 0 2px 8px rgba(0,0,0,0.9)'
                : '0 2px 8px rgba(0,0,0,0.85)';

              return (
                <span
                  key={idx}
                  style={{
                    fontFamily: FONT_STACK,
                    fontSize: 46,
                    fontWeight: 800,
                    lineHeight: 1.3,
                    letterSpacing: '-0.02em',
                    color,
                    transform: `scale(${scale})`,
                    textShadow,
                    transition: 'all 0.06s ease',
                    textTransform: 'lowercase',
                  }}
                >
                  {item.text}
                </span>
              );
            })}
          </div>
        </div>
      )}
    </div>
  );
};
