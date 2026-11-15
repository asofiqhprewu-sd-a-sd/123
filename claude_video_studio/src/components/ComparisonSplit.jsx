import React from 'react';
import { spring, useCurrentFrame, useVideoConfig } from 'remotion';
import { FONT_STACK, SPRING_CONFIGS } from '../styles/theme';
import { IconHero } from './IconHero';

export const ComparisonSplit = ({
  leftTitle = 'GPT-3 (2020)',
  leftIcon = 'icons/openai.png',
  leftStat = '175 млрд параметров',
  rightTitle = 'GPT-4 (2023)',
  rightIcon = 'icons/brain.png',
  rightStat = '1.8 трлн параметров',
  delay = 5,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const entrance = spring({
    frame: frame - delay,
    fps,
    config: SPRING_CONFIGS.snappy,
  });

  const vsEntrance = spring({
    frame: frame - delay - 6,
    fps,
    config: SPRING_CONFIGS.bouncy,
  });

  return (
    <div
      style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        position: 'relative',
        width: '100%',
        padding: '0 40px',
        boxSizing: 'border-box',
        gap: '40px',
        opacity: entrance,
        transform: `scale(${entrance})`,
        zIndex: 6,
      }}
    >
      {/* Left Card */}
      <div
        style={{
          flex: 1,
          backgroundColor: 'rgba(30, 41, 59, 0.75)',
          borderRadius: '32px',
          border: '2px solid rgba(255, 255, 255, 0.12)',
          padding: '36px 24px',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          boxShadow: '0 20px 50px rgba(0, 0, 0, 0.5)',
        }}
      >
        <div style={{ marginBottom: 20 }}>
          <IconHero icon={leftIcon} size={180} />
        </div>
        <div
          style={{
            fontFamily: FONT_STACK,
            fontSize: '28px',
            fontWeight: 800,
            color: '#ffffff',
            textAlign: 'center',
            marginBottom: 10,
          }}
        >
          {leftTitle}
        </div>
        {leftStat && (
          <div
            style={{
              fontFamily: FONT_STACK,
              fontSize: '20px',
              fontWeight: 600,
              color: '#94a3b8',
              textAlign: 'center',
            }}
          >
            {leftStat}
          </div>
        )}
      </div>

      {/* Center "VS" Badge */}
      <div
        style={{
          position: 'absolute',
          top: '50%',
          left: '50%',
          transform: `translate(-50%, -50%) scale(${vsEntrance})`,
          width: 80,
          height: 80,
          borderRadius: '50%',
          backgroundColor: '#ef4444',
          border: '4px solid #ffffff',
          boxShadow: '0 0 35px rgba(239, 68, 68, 0.75)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          color: '#ffffff',
          fontFamily: FONT_STACK,
          fontSize: '32px',
          fontWeight: 900,
          letterSpacing: '-0.02em',
          zIndex: 10,
        }}
      >
        VS
      </div>

      {/* Right Card */}
      <div
        style={{
          flex: 1,
          backgroundColor: 'rgba(30, 41, 59, 0.75)',
          borderRadius: '32px',
          border: '2px solid rgba(255, 255, 255, 0.12)',
          padding: '36px 24px',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          boxShadow: '0 20px 50px rgba(0, 0, 0, 0.5)',
        }}
      >
        <div style={{ marginBottom: 20 }}>
          <IconHero icon={rightIcon} size={180} />
        </div>
        <div
          style={{
            fontFamily: FONT_STACK,
            fontSize: '28px',
            fontWeight: 800,
            color: '#38bdf8',
            textAlign: 'center',
            marginBottom: 10,
          }}
        >
          {rightTitle}
        </div>
        {rightStat && (
          <div
            style={{
              fontFamily: FONT_STACK,
              fontSize: '20px',
              fontWeight: 600,
              color: '#94a3b8',
              textAlign: 'center',
            }}
          >
            {rightStat}
          </div>
        )}
      </div>
    </div>
  );
};
