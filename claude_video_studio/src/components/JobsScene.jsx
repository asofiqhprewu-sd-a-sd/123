import React from 'react';
import { interpolate, spring, staticFile, useCurrentFrame, useVideoConfig } from 'remotion';
import { FONT_STACK } from '../styles/theme';

export const JobsScene = ({ sceneIndex, sceneData }) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();
  const currentTimeSec = frame / fps;

  // 1. Entrance spring physics
  const enterSpring = spring({
    frame,
    fps,
    config: { damping: 15, mass: 0.8, stiffness: 120 },
  });

  // 2. Idle float animation
  const floatY = Math.sin((frame / fps) * 2.5) * 5;

  // 3. Smooth fade-out at scene exit
  const fadeOut = interpolate(frame, [durationInFrames - 10, durationInFrames], [1, 0], {
    extrapolateLeft: 'clamp',
  });

  const words = sceneData.words || [];

  // Typewriter blinking cursor for scene 0
  const cursorBlink = Math.floor((frame / fps) * 3) % 2 === 0;

  // Animated cursor arrow coordinates for Scene 2 (GUI robbery)
  const cursorX = interpolate(frame, [30, 90, 160, 240], [200, 480, 560, 520], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const cursorY = interpolate(frame, [30, 90, 160, 240], [150, 280, 220, 260], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <div
      style={{
        position: 'relative',
        width: '100%',
        height: '100%',
        overflow: 'hidden',
        backgroundColor: '#000000', // Deep pitch black, matching reference
        opacity: fadeOut,
      }}
    >
      {/* BACKGROUND: Soft studio vignette */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background: 'radial-gradient(circle at 50% 45%, rgba(255, 255, 255, 0.035) 0%, rgba(0, 0, 0, 0.95) 75%)',
          pointerEvents: 'none',
          zIndex: 1,
        }}
      />

      {/* TOP HEADLINE (Pure typography, lowercase, like reference: "как появилась нейросеть") */}
      {sceneIndex !== 5 && (
        <div
          style={{
            position: 'absolute',
            top: 130,
            left: 0,
            width: '100%',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            textAlign: 'center',
            padding: '0 50px',
            boxSizing: 'border-box',
            zIndex: 20,
            opacity: enterSpring,
            transform: `translateY(${interpolate(enterSpring, [0, 1], [-18, 0])}px)`,
          }}
        >
          <h1
            style={{
              fontFamily: FONT_STACK,
              fontSize: 52,
              fontWeight: 800,
              lineHeight: 1.15,
              letterSpacing: '-0.03em',
              color: '#ffffff',
              margin: 0,
              textTransform: 'lowercase',
              textShadow: '0 4px 20px rgba(0, 0, 0, 0.9)',
            }}
          >
            {sceneData.headline}
            {sceneIndex === 0 && cursorBlink && <span style={{ color: '#38bdf8' }}> |</span>}
          </h1>
        </div>
      )}

      {/* CENTER STAGE: DYNAMIC VISUAL BEATS */}
      <div
        style={{
          position: 'absolute',
          top: '48%',
          left: '50%',
          transform: `translate(-50%, -50%) translateY(${floatY}px)`,
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          zIndex: 15,
          width: '100%',
        }}
      >
        {/* BEAT 1: HOOK — MYSTERY (0:00 - 0:10) */}
        {sceneIndex === 0 && (
          <div
            style={{
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              transform: `scale(${enterSpring})`,
            }}
          >
            <div
              style={{
                width: 380,
                height: 480,
                borderRadius: 44,
                overflow: 'hidden',
                background: '#0a0a0c',
                border: '1px solid rgba(255, 255, 255, 0.14)',
                boxShadow: '0 30px 80px rgba(0, 0, 0, 0.95), 0 0 40px rgba(255, 255, 255, 0.05)',
              }}
            >
              <img
                src={staticFile('photos/jobs/steve_jobs_1984_real.jpg')}
                alt="Steve Jobs"
                style={{
                  width: '100%',
                  height: '100%',
                  objectFit: 'cover',
                  objectPosition: 'center top',
                }}
              />
            </div>
            <span
              style={{
                fontFamily: FONT_STACK,
                fontSize: 34,
                fontWeight: 700,
                color: '#ffffff',
                marginTop: 22,
                textTransform: 'lowercase',
                letterSpacing: '-0.02em',
                textShadow: '0 2px 10px rgba(0,0,0,0.9)',
              }}
            >
              стив джобс
            </span>
          </div>
        )}

        {/* BEAT 2: DEAL OF THE CENTURY (0:10 - 0:18) */}
        {sceneIndex === 1 && (
          <div
            style={{
              position: 'relative',
              display: 'flex',
              justifyContent: 'center',
              alignItems: 'center',
              width: 960,
              height: 520,
            }}
          >
            {/* Jobs card on Left */}
            <div
              style={{
                position: 'absolute',
                left: 40,
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                transform: `translateX(${interpolate(enterSpring, [0, 1], [-60, 0])}px)`,
              }}
            >
              <div
                style={{
                  width: 310,
                  height: 380,
                  borderRadius: 38,
                  overflow: 'hidden',
                  background: '#0a0a0c',
                  border: '1px solid rgba(255, 255, 255, 0.14)',
                  boxShadow: '0 25px 60px rgba(0,0,0,0.9)',
                }}
              >
                <img
                  src={staticFile('photos/jobs/steve_jobs_1984_real.jpg')}
                  alt="Jobs"
                  style={{ width: '100%', height: '100%', objectFit: 'cover', objectPosition: 'center top' }}
                />
              </div>
              <span style={{ fontFamily: FONT_STACK, fontSize: 26, fontWeight: 700, color: '#ffffff', marginTop: 14 }}>
                стив джобс
              </span>
            </div>

            {/* Center Floating Apple Rainbow Logo Tile */}
            <div
              style={{
                position: 'absolute',
                zIndex: 25,
                transform: `scale(${spring({ frame: Math.max(0, frame - 10), fps, config: { damping: 12 } })})`,
                background: '#111318',
                border: '1px solid rgba(255, 255, 255, 0.2)',
                borderRadius: 28,
                padding: '20px 28px',
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                gap: 10,
                boxShadow: '0 20px 50px rgba(0, 0, 0, 0.95), 0 0 35px rgba(255, 255, 255, 0.1)',
              }}
            >
              <img
                src={staticFile('photos/jobs/apple_rainbow_logo.png')}
                alt="Apple"
                style={{ width: 64, height: 76, objectFit: 'contain' }}
              />
              <span style={{ fontFamily: FONT_STACK, fontSize: 22, fontWeight: 800, color: '#facc15' }}>
                100 000 АКЦИЙ
              </span>
            </div>

            {/* Xerox PARC on Right */}
            <div
              style={{
                position: 'absolute',
                right: 40,
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                transform: `translateX(${interpolate(enterSpring, [0, 1], [60, 0])}px)`,
              }}
            >
              <div
                style={{
                  width: 310,
                  height: 380,
                  borderRadius: 38,
                  overflow: 'hidden',
                  background: '#0a0a0c',
                  border: '1px solid rgba(255, 255, 255, 0.14)',
                  boxShadow: '0 25px 60px rgba(0,0,0,0.9)',
                }}
              >
                <img
                  src={staticFile('photos/jobs/parc_building.jpg')}
                  alt="Xerox PARC"
                  style={{ width: '100%', height: '100%', objectFit: 'cover' }}
                />
              </div>
              <span style={{ fontFamily: FONT_STACK, fontSize: 26, fontWeight: 700, color: '#ffffff', marginTop: 14 }}>
                лаборатория xerox
              </span>
            </div>
          </div>
        )}

        {/* BEAT 3: ROBBERY — GUI & HOLY GRAIL MOUSE (0:18 - 0:28) */}
        {sceneIndex === 2 && (
          <div
            style={{
              position: 'relative',
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              width: 960,
              gap: 20,
            }}
          >
            {/* Top row: GUI Finder Window + Folders */}
            <div style={{ display: 'flex', alignItems: 'center', gap: 20 }}>
              {/* Window */}
              <div
                style={{
                  width: 280,
                  height: 160,
                  borderRadius: 22,
                  background: '#131822',
                  border: '1px solid rgba(56, 189, 248, 0.5)',
                  padding: 14,
                  boxSizing: 'border-box',
                  boxShadow: '0 16px 40px rgba(0,0,0,0.8), 0 0 24px rgba(56, 189, 248, 0.25)',
                  transform: `scale(${spring({ frame: Math.max(0, frame - 5), fps })})`,
                }}
              >
                <div style={{ display: 'flex', gap: 6, alignItems: 'center' }}>
                  <div style={{ width: 10, height: 10, borderRadius: '50%', background: '#ef4444' }} />
                  <div style={{ width: 10, height: 10, borderRadius: '50%', background: '#eab308' }} />
                  <div style={{ width: 10, height: 10, borderRadius: '50%', background: '#22c55e' }} />
                  <span style={{ fontSize: 13, color: '#94a3b8', marginLeft: 8, fontFamily: FONT_STACK }}>Finder</span>
                </div>
                <div style={{ marginTop: 16, background: '#0284c7', borderRadius: 10, padding: '10px 0', textAlign: 'center' }}>
                  <span style={{ fontFamily: FONT_STACK, fontSize: 22, fontWeight: 800, color: '#ffffff' }}>ОКНА</span>
                </div>
              </div>

              {/* Folders */}
              <div
                style={{
                  width: 220,
                  height: 160,
                  borderRadius: 22,
                  background: '#131822',
                  border: '1px solid rgba(168, 85, 247, 0.5)',
                  display: 'flex',
                  flexDirection: 'column',
                  justifyContent: 'center',
                  alignItems: 'center',
                  gap: 8,
                  boxShadow: '0 16px 40px rgba(0,0,0,0.8), 0 0 24px rgba(168, 85, 247, 0.25)',
                  transform: `scale(${spring({ frame: Math.max(0, frame - 15), fps })})`,
                }}
              >
                <span style={{ fontSize: 44 }}>📁</span>
                <span style={{ fontFamily: FONT_STACK, fontSize: 20, fontWeight: 800, color: '#e9d5ff' }}>ПАПКИ</span>
              </div>
            </div>

            {/* The First Wooden Mouse — HOLY GRAIL CLOSEUP WITH GOLDEN GLOW */}
            <div
              style={{
                width: 440,
                height: 360,
                borderRadius: 40,
                overflow: 'hidden',
                background: '#0e1015',
                border: '2px solid #facc15',
                boxShadow: '0 30px 80px rgba(0, 0, 0, 0.95), 0 0 60px rgba(250, 204, 21, 0.65)',
                transform: `scale(${spring({ frame: Math.max(0, frame - 25), fps, config: { damping: 11, stiffness: 140 } })})`,
              }}
            >
              <img
                src={staticFile('photos/jobs/first_mouse.jpg')}
                alt="First Mouse"
                style={{ width: '100%', height: '100%', objectFit: 'cover' }}
              />
            </div>

            {/* Meme Reaction Callout: «ЭТО ЖЕ ПРОСТО ИГРУШКА» */}
            <div
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: 12,
                padding: '10px 26px',
                borderRadius: 999,
                background: 'rgba(239, 68, 68, 0.18)',
                border: '1px solid rgba(239, 68, 68, 0.5)',
                transform: `scale(${spring({ frame: Math.max(0, frame - 120), fps })})`,
              }}
            >
              <span style={{ fontFamily: FONT_STACK, fontSize: 22, fontWeight: 700, color: '#f87171' }}>
                боссы xerox: «это же просто игрушка» 🤦‍♂️
              </span>
            </div>

            {/* Moving Animated Cursor Arrow */}
            <div
              style={{
                position: 'absolute',
                left: cursorX,
                top: cursorY,
                zIndex: 35,
                pointerEvents: 'none',
                filter: 'drop-shadow(0 4px 12px rgba(0,0,0,0.9))',
                transform: 'scale(1.4)',
              }}
            >
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                <path d="M4 2L20 12L13 14L10 21L4 2Z" fill="#ffffff" stroke="#000000" strokeWidth="1.5" />
              </svg>
            </div>
          </div>
        )}

        {/* BEAT 4: CLIMAX — MEME REACTION (0:28 - 0:32) */}
        {sceneIndex === 3 && (
          <div
            style={{
              position: 'relative',
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              gap: 24,
            }}
          >
            {/* Jobs Freeze-Frame with Dramatic Red Glow and Arrows */}
            <div
              style={{
                width: 400,
                height: 460,
                borderRadius: 44,
                overflow: 'hidden',
                background: '#0a0a0c',
                border: '3px solid #ef4444',
                boxShadow: '0 30px 80px rgba(0,0,0,0.95), 0 0 60px rgba(239, 68, 68, 0.7)',
                transform: `scale(${enterSpring})`,
              }}
            >
              <img
                src={staticFile('photos/jobs/steve_jobs_1984_real.jpg')}
                alt="Steve Jobs"
                style={{ width: '100%', height: '100%', objectFit: 'cover', objectPosition: 'center top' }}
              />
            </div>

            {/* Meme Stamp: «МОМЕНТ ОЗАРЕНИЯ» */}
            <div
              style={{
                position: 'absolute',
                top: -30,
                right: -20,
                transform: 'rotate(12deg) scale(1.1)',
                background: '#ef4444',
                color: '#ffffff',
                fontFamily: FONT_STACK,
                fontSize: 22,
                fontWeight: 900,
                padding: '8px 20px',
                borderRadius: 14,
                boxShadow: '0 10px 30px rgba(239, 68, 68, 0.6)',
                letterSpacing: '0.04em',
              }}
            >
              МОМЕНТ ОЗАРЕНИЯ ⚡
            </div>

            {/* Energetic High-End Typography Quote */}
            <div
              style={{
                transform: `scale(${spring({ frame: Math.max(0, frame - 10), fps, config: { damping: 11 } })})`,
                textAlign: 'center',
                padding: '0 20px',
              }}
            >
              <span
                style={{
                  fontFamily: FONT_STACK,
                  fontSize: 42,
                  fontWeight: 900,
                  color: '#ffffff',
                  textTransform: 'uppercase',
                  letterSpacing: '-0.02em',
                  textShadow: '0 0 35px rgba(255, 255, 255, 0.8), 0 4px 16px rgba(0,0,0,0.9)',
                }}
              >
                «ПОЧЕМУ МЫ ЕЩЁ НЕ ДЕЛАЕМ ЭТО?!»
              </span>
            </div>
          </div>
        )}

        {/* BEAT 5: RESOLUTION — SPLIT-SCREEN EMPIRE VS PAPER (0:32 - 0:39) */}
        {sceneIndex === 4 && (
          <div
            style={{
              display: 'flex',
              justifyContent: 'center',
              alignItems: 'center',
              gap: 30,
              width: 980,
            }}
          >
            {/* LEFT SIDE: APPLE $3 TRILLION EMPIRE */}
            <div
              style={{
                flex: 1,
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                gap: 14,
                transform: `translateX(${interpolate(enterSpring, [0, 1], [-40, 0])}px)`,
              }}
            >
              <div
                style={{
                  width: '100%',
                  height: 420,
                  borderRadius: 38,
                  overflow: 'hidden',
                  background: '#0a0a0c',
                  border: '2px solid #facc15',
                  boxShadow: '0 25px 60px rgba(0,0,0,0.95), 0 0 40px rgba(250, 204, 21, 0.4)',
                }}
              >
                <img
                  src={staticFile('photos/jobs/steve_jobs_macintosh_1984.jpg')}
                  alt="Steve Jobs with Macintosh"
                  style={{ width: '100%', height: '100%', objectFit: 'cover', objectPosition: 'center top' }}
                />
              </div>

              {/* $3 TRILLION BADGE */}
              <div
                style={{
                  padding: '10px 24px',
                  borderRadius: 999,
                  background: 'linear-gradient(135deg, rgba(245, 158, 11, 0.25), rgba(16, 185, 129, 0.25))',
                  border: '1.5px solid #facc15',
                  display: 'flex',
                  alignItems: 'center',
                  gap: 10,
                }}
              >
                <span style={{ fontSize: 24 }}>🏆</span>
                <span style={{ fontFamily: FONT_STACK, fontSize: 24, fontWeight: 900, color: '#facc15' }}>
                  $3 000 000 000 000
                </span>
              </div>
            </div>

            {/* VS DIVIDER */}
            <div
              style={{
                fontFamily: FONT_STACK,
                fontSize: 32,
                fontWeight: 900,
                color: '#64748b',
                letterSpacing: '0.04em',
              }}
            >
              VS
            </div>

            {/* RIGHT SIDE: XEROX SELLING PAPER */}
            <div
              style={{
                flex: 1,
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                gap: 14,
                transform: `translateX(${interpolate(enterSpring, [0, 1], [40, 0])}px)`,
              }}
            >
              <div
                style={{
                  width: '100%',
                  height: 420,
                  borderRadius: 38,
                  overflow: 'hidden',
                  background: '#0a0a0c',
                  border: '1px solid rgba(255, 255, 255, 0.14)',
                  boxShadow: '0 25px 60px rgba(0,0,0,0.95)',
                  display: 'flex',
                  flexDirection: 'column',
                  justifyContent: 'center',
                  alignItems: 'center',
                  gap: 16,
                }}
              >
                <span style={{ fontSize: 84 }}>🖨️</span>
                <span style={{ fontFamily: FONT_STACK, fontSize: 32, fontWeight: 800, color: '#ffffff' }}>
                  XEROX
                </span>
                <span style={{ fontFamily: FONT_STACK, fontSize: 20, color: '#94a3b8' }}>
                  продажа бумаги 📄
                </span>
              </div>

              <div
                style={{
                  padding: '10px 24px',
                  borderRadius: 999,
                  background: 'rgba(239, 68, 68, 0.15)',
                  border: '1px solid rgba(239, 68, 68, 0.4)',
                }}
              >
                <span style={{ fontFamily: FONT_STACK, fontSize: 20, fontWeight: 700, color: '#f87171' }}>
                  упустили триллион 📉
                </span>
              </div>
            </div>
          </div>
        )}

        {/* BEAT 6: FINALE PUNCHLINE (0:39 - 0:44) */}
        {sceneIndex === 5 && (
          <div
            style={{
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              textAlign: 'center',
              padding: '0 60px',
              gap: 36,
              transform: `scale(${enterSpring})`,
            }}
          >
            {/* Apple Rainbow Logo */}
            <img
              src={staticFile('photos/jobs/apple_rainbow_logo.png')}
              alt="Apple"
              style={{ width: 80, height: 96, objectFit: 'contain' }}
            />

            {/* Punchline Typography */}
            <h2
              style={{
                fontFamily: FONT_STACK,
                fontSize: 48,
                fontWeight: 800,
                color: '#ffffff',
                lineHeight: 1.25,
                letterSpacing: '-0.02em',
                maxWidth: 880,
                margin: 0,
                textShadow: '0 0 35px rgba(255, 255, 255, 0.6), 0 4px 20px rgba(0,0,0,0.9)',
              }}
            >
              «Иногда самое дорогое — это то, что вы считаете просто игрушкой.»
            </h2>
          </div>
        )}
      </div>

      {/* BOTTOM KINETIC SUBTITLES: PURE TYPOGRAPHY, ZERO BACKGROUND BOX */}
      {sceneIndex !== 5 && (
        <div
          style={{
            position: 'absolute',
            bottom: 150,
            left: 0,
            width: '100%',
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            padding: '0 60px',
            boxSizing: 'border-box',
            zIndex: 25,
          }}
        >
          <div
            style={{
              display: 'flex',
              flexWrap: 'wrap',
              justifyContent: 'center',
              alignItems: 'center',
              gap: '8px 14px',
              maxWidth: 960,
            }}
          >
            {words.map((item, idx) => {
              const isActive = currentTimeSec >= item.start && currentTimeSec <= item.end;
              const isPast = currentTimeSec > item.end;

              const color = isActive
                ? '#ffffff'
                : isPast
                ? 'rgba(255, 255, 255, 0.85)'
                : 'rgba(255, 255, 255, 0.35)';

              const scale = isActive ? 1.06 : 1.0;
              const textShadow = isActive
                ? '0 0 24px rgba(255, 255, 255, 0.9), 0 2px 8px rgba(0,0,0,0.95)'
                : '0 2px 8px rgba(0,0,0,0.9)';

              return (
                <span
                  key={idx}
                  style={{
                    fontFamily: FONT_STACK,
                    fontSize: 38,
                    fontWeight: 700,
                    color,
                    transform: `scale(${scale})`,
                    textShadow,
                    transition: 'all 0.05s ease',
                    textTransform: 'lowercase',
                    letterSpacing: '-0.02em',
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
