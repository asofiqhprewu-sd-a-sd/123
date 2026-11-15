import React from 'react';
import { spring, useCurrentFrame, useVideoConfig } from 'remotion';
import { FONT_STACK, SPRING_CONFIGS } from '../styles/theme';

export const PhoneMockup = ({
  contactName = 'Илья Суцкевер',
  messages = [
    { from: 'them', text: 'Сэм, мы должны поговорить о безопасности модели.' },
    { from: 'me', text: 'Мы запускаем релиз в четверг. Это решено.' },
    { from: 'them', text: 'Тогда совет директоров соберётся сегодня вечером...' },
  ],
  delay = 5,
  width = 520,
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
        backgroundColor: '#000000',
        borderRadius: '52px',
        border: '4px solid #334155',
        boxShadow: '0 30px 80px rgba(0, 0, 0, 0.8), inset 0 0 4px rgba(255, 255, 255, 0.2)',
        padding: '24px 20px 36px 20px',
        boxSizing: 'border-box',
        overflow: 'hidden',
        opacity: entrance,
        transform: `translateY(${(1 - entrance) * 70}px) scale(${entrance})`,
        zIndex: 6,
      }}
    >
      {/* Dynamic Island Notch */}
      <div style={{ display: 'flex', justifyContent: 'center', marginBottom: 20 }}>
        <div
          style={{
            width: 140,
            height: 32,
            backgroundColor: '#09090b',
            borderRadius: 20,
            border: '1px solid #27272a',
          }}
        />
      </div>

      {/* Chat Header */}
      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          padding: '12px 14px',
          backgroundColor: '#18181b',
          borderRadius: 24,
          marginBottom: 24,
        }}
      >
        <div
          style={{
            width: 44,
            height: 44,
            borderRadius: '50%',
            backgroundColor: '#2563eb',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            color: '#fff',
            fontWeight: 700,
            fontSize: 20,
            marginRight: 14,
          }}
        >
          {contactName[0]}
        </div>
        <div>
          <div
            style={{
              fontFamily: FONT_STACK,
              fontSize: '22px',
              fontWeight: 700,
              color: '#ffffff',
            }}
          >
            {contactName}
          </div>
          <div
            style={{
              fontFamily: FONT_STACK,
              fontSize: '15px',
              color: '#4ade80',
            }}
          >
            в сети
          </div>
        </div>
      </div>

      {/* Message Bubbles */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
        {messages.map((m, idx) => {
          const msgDelay = delay + 8 + idx * 16;
          const msgEntrance = spring({
            frame: frame - msgDelay,
            fps,
            config: SPRING_CONFIGS.bouncy,
          });

          const isMe = m.from === 'me';

          return (
            <div
              key={idx}
              style={{
                alignSelf: isMe ? 'flex-end' : 'flex-start',
                maxWidth: '82%',
                backgroundColor: isMe ? '#2563eb' : '#27272a',
                color: '#ffffff',
                fontFamily: FONT_STACK,
                fontSize: '20px',
                lineHeight: 1.35,
                fontWeight: 500,
                padding: '16px 20px',
                borderRadius: isMe ? '24px 24px 4px 24px' : '24px 24px 24px 4px',
                opacity: msgEntrance,
                transform: `scale(${msgEntrance}) translateY(${(1 - msgEntrance) * 20}px)`,
                boxShadow: '0 6px 20px rgba(0,0,0,0.3)',
              }}
            >
              {m.text}
            </div>
          );
        })}
      </div>
    </div>
  );
};
