import React from 'react';
import { interpolate, spring, useCurrentFrame, useVideoConfig } from 'remotion';
import { SPRING_CONFIGS } from '../styles/theme';

export const CodeEditor = ({
  filename = 'agent.py',
  lines = [
    { text: 'import openai, anthropic', color: '#f43f5e' },
    { text: 'def think_and_solve(task):', color: '#38bdf8' },
    { text: '    model = load_reasoning_core()', color: '#a3e635' },
    { text: '    return model.synthesize(task)', color: '#facc15' },
  ],
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
        backgroundColor: '#0d1117',
        borderRadius: '24px',
        border: '1.5px solid rgba(255, 255, 255, 0.15)',
        boxShadow: '0 24px 60px rgba(0, 0, 0, 0.7)',
        overflow: 'hidden',
        opacity: entrance,
        transform: `translateY(${(1 - entrance) * 60}px) scale(${entrance})`,
        zIndex: 6,
      }}
    >
      {/* Window Header */}
      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          backgroundColor: '#161b22',
          padding: '16px 20px',
          borderBottom: '1px solid rgba(255, 255, 255, 0.08)',
        }}
      >
        {/* MacOS Dots */}
        <div style={{ display: 'flex', gap: '8px', marginRight: '20px' }}>
          <div style={{ width: 14, height: 14, borderRadius: '50%', backgroundColor: '#ef4444' }} />
          <div style={{ width: 14, height: 14, borderRadius: '50%', backgroundColor: '#eab308' }} />
          <div style={{ width: 14, height: 14, borderRadius: '50%', backgroundColor: '#22c55e' }} />
        </div>

        {/* Filename tab */}
        <div
          style={{
            fontFamily: 'Consolas, Monaco, "Courier New", monospace',
            fontSize: '20px',
            color: '#cbd5e1',
            fontWeight: 600,
          }}
        >
          {filename}
        </div>
      </div>

      {/* Code Body */}
      <div
        style={{
          padding: '24px 28px',
          fontFamily: 'Consolas, Monaco, "Courier New", monospace',
          fontSize: '24px',
          lineHeight: '1.7',
        }}
      >
        {lines.map((item, idx) => {
          // Line typing delay
          const lineStartFrame = delay + 10 + idx * 12;
          const charCount = Math.floor(
            interpolate(
              frame - lineStartFrame,
              [0, 15],
              [0, item.text.length],
              { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
            )
          );
          const visibleText = item.text.slice(0, charCount);

          return (
            <div key={idx} style={{ display: 'flex', alignItems: 'center' }}>
              <span
                style={{
                  width: '38px',
                  color: '#475569',
                  userSelect: 'none',
                  fontSize: '20px',
                }}
              >
                {idx + 1}
              </span>
              <span style={{ color: item.color || '#e2e8f0', fontWeight: 500 }}>
                {visibleText}
                {charCount < item.text.length && charCount > 0 && (
                  <span style={{ borderRight: '2px solid #38bdf8', marginLeft: 2 }} />
                )}
              </span>
            </div>
          );
        })}
      </div>
    </div>
  );
};
