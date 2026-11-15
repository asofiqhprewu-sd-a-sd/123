import React from 'react';
import { interpolate, spring, useCurrentFrame, useVideoConfig } from 'remotion';
import { FONT_STACK, SPRING_CONFIGS } from '../styles/theme';

export const StatCounter = ({
  start = 0,
  end = 100000000,
  prefix = '$',
  suffix = '',
  label = 'капитализация компании',
  delay = 5,
  color = '#22c55e',
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const entrance = spring({
    frame: frame - delay,
    fps,
    config: SPRING_CONFIGS.snappy,
  });

  // Count-up progress over 45 frames
  const countProgress = interpolate(
    frame - delay,
    [0, 45],
    [0, 1],
    {
      extrapolateLeft: 'clamp',
      extrapolateRight: 'clamp',
    }
  );

  // Ease-out cubic curve for natural decelerating number tick
  const eased = 1 - Math.pow(1 - countProgress, 3);
  const currentVal = Math.round(start + (end - start) * eased);
  const formattedNumber = currentVal.toLocaleString('en-US');

  return (
    <div
      style={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '36px 48px',
        backgroundColor: 'rgba(15, 23, 42, 0.9)',
        borderRadius: '36px',
        border: '2px solid rgba(255, 255, 255, 0.15)',
        boxShadow: `0 24px 60px rgba(0, 0, 0, 0.6), 0 0 40px ${color}33`,
        opacity: entrance,
        transform: `translateY(${(1 - entrance) * 60}px) scale(${entrance})`,
        zIndex: 6,
      }}
    >
      {/* Big Animated Number */}
      <div
        style={{
          fontFamily: FONT_STACK,
          fontSize: '76px',
          fontWeight: 900,
          letterSpacing: '-0.03em',
          color: color,
          textShadow: `0 0 35px ${color}66`,
          lineHeight: 1,
        }}
      >
        {prefix}{formattedNumber}{suffix}
      </div>

      {/* Description Label */}
      {label && (
        <div
          style={{
            marginTop: '18px',
            fontFamily: FONT_STACK,
            fontSize: '26px',
            fontWeight: 700,
            color: '#94a3b8',
            textTransform: 'uppercase',
            letterSpacing: '0.08em',
          }}
        >
          {label}
        </div>
      )}
    </div>
  );
};
