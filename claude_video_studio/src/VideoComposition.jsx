import React from 'react';
import { Sequence, useCurrentFrame, useVideoConfig } from 'remotion';
import { GridBackground } from './components/GridBackground';
import { KineticText } from './components/KineticText';
import { PersonCard } from './components/PersonCard';
import { IconHero } from './components/IconHero';
import { TweetCard } from './components/TweetCard';
import { BadgePill } from './components/BadgePill';
import { ConnectingDiagram } from './components/ConnectingDiagram';
import { CalendarCard } from './components/CalendarCard';
import { NarratorBadge } from './components/NarratorBadge';
import { SoundPlayer } from './components/SoundPlayer';
import { StatCounter } from './components/StatCounter';
import { CodeEditor } from './components/CodeEditor';
import { PhoneMockup } from './components/PhoneMockup';
import { ComparisonSplit } from './components/ComparisonSplit';
import { QuoteCard } from './components/QuoteCard';
import { ProgressBar } from './components/ProgressBar';
import { RealFootage } from './components/RealFootage';
import { PhotoComparison } from './components/PhotoComparison';

export const VideoComposition = ({ project }) => {
  const { fps } = useVideoConfig();
  const scenes = project.scenes || [];

  // Compute start frames for each scene and gather SFX / Voice events
  let currentStart = 0;
  const timedScenes = scenes.map((s) => {
    const startFrame = currentStart;
    currentStart += s.durationInFrames;
    return { ...s, startFrame };
  });

  const sfxEvents = [];
  const sceneVoices = [];

  timedScenes.forEach((s) => {
    if (s.sfx) {
      sfxEvents.push({
        file: s.sfx,
        frame: s.startFrame,
        volume: s.sfxVolume ?? 0.75,
        duration: s.sfxDuration || 60,
      });
    }
    if (s.voiceAudio) {
      sceneVoices.push({
        file: s.voiceAudio,
        frame: s.startFrame,
        volume: s.voiceVolume ?? 1.0,
      });
    }
  });

  return (
    <div
      style={{
        width: '100%',
        height: '100%',
        position: 'relative',
        backgroundColor: '#0a0a0c',
        overflow: 'hidden',
      }}
    >
      {/* 1. Global Constant Grid Background: NEVER CHANGES THROUGHOUT ENTIRE VIDEO */}
      <GridBackground theme="dark" showGrass={false} />

      {/* 2. Retention Progress Bar (top) */}
      {project.showProgressBar !== false && (
        <ProgressBar
          color={project.progressBarColor || '#38bdf8'}
          height={project.progressBarHeight || 8}
          position="top"
        />
      )}

      {/* 3. Global Audio (Background Music + Voiceover + SFX) */}
      <SoundPlayer
        voiceAudio={project.voiceAudio || null}
        sceneVoices={sceneVoices}
        bgMusic={project.bgMusic || 'music/ambient_tech.wav'}
        sfxEvents={sfxEvents}
        bgMusicVolume={project.bgMusicVolume ?? 0.12}
        voiceVolume={project.voiceVolume ?? 1.0}
      />

      {/* 4. Top Narrator Badge (ONLY if explicitly set) */}
      {project.narrator && <NarratorBadge avatar={project.narrator} />}

      {/* 5. Render each scene inside its Sequence */}
      {timedScenes.map((scene, idx) => (
        <Sequence
          key={scene.id || idx}
          from={scene.startFrame}
          durationInFrames={scene.durationInFrames}
        >
          <SceneRenderer scene={scene} fps={fps} />
        </Sequence>
      ))}
    </div>
  );
};

const SceneRenderer = ({ scene, fps }) => {
  const frame = useCurrentFrame();
  const currentTimeSec = frame / fps;

  return (
    <div style={{ position: 'relative', width: '100%', height: '100%' }}>
      {/* Category Pills (Top Area under progress bar) */}
      {scene.pills && (
        <div
          style={{
            position: 'absolute',
            top: '70px',
            left: 0,
            width: '100%',
            display: 'flex',
            justifyContent: 'center',
            gap: 16,
            zIndex: 15,
          }}
        >
          {scene.pills.map((pill, i) => (
            <BadgePill
              key={i}
              text={pill.text}
              icon={pill.icon}
              color={pill.color || '#1f2937'}
              delay={i * 3}
            />
          ))}
        </div>
      )}

      {/* Hero Visual Area: Exact Dead Center (фотки по середине!) */}
      <div
        style={{
          position: 'absolute',
          top: '46%',
          left: 0,
          width: '100%',
          transform: 'translateY(-50%)',
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          zIndex: 5,
        }}
      >
        {/* Real Footage Card */}
        {scene.photo && (
          <RealFootage
            src={scene.photo.src}
            alt={scene.photo.alt}
            mode="card"
            width={scene.photo.width || 880}
            height={scene.photo.height || 1020}
            glowColor={scene.photo.glowColor || 'rgba(56, 189, 248, 0.25)'}
            tag={scene.photo.tag}
            zoomDirection={scene.photo.zoomDirection || 'in'}
            delay={scene.photo.delay || 3}
          />
        )}

        {/* Real Photo Comparison (1888 vs Today) */}
        {scene.photoComparison && (
          <PhotoComparison
            leftPhoto={scene.photoComparison.leftPhoto}
            rightPhoto={scene.photoComparison.rightPhoto}
            leftLabel={scene.photoComparison.leftLabel}
            rightLabel={scene.photoComparison.rightLabel}
            tag={scene.photoComparison.tag}
            delay={scene.photoComparison.delay || 3}
          />
        )}

        {scene.counter && (
          <StatCounter
            start={scene.counter.start ?? 0}
            end={scene.counter.end ?? 1000000}
            prefix={scene.counter.prefix ?? '$'}
            suffix={scene.counter.suffix ?? ''}
            label={scene.counter.label}
            color={scene.counter.color || '#22c55e'}
            delay={scene.counter.delay || 5}
          />
        )}

        {scene.code && (
          <CodeEditor
            filename={scene.code.filename || 'main.py'}
            lines={scene.code.lines || []}
            delay={scene.code.delay || 5}
            width={scene.code.width || 680}
          />
        )}

        {scene.phone && (
          <PhoneMockup
            contactName={scene.phone.contactName}
            messages={scene.phone.messages || []}
            delay={scene.phone.delay || 5}
            width={scene.phone.width || 520}
          />
        )}

        {scene.comparison && (
          <ComparisonSplit
            leftTitle={scene.comparison.leftTitle}
            leftIcon={scene.comparison.leftIcon}
            leftStat={scene.comparison.leftStat}
            rightTitle={scene.comparison.rightTitle}
            rightIcon={scene.comparison.rightIcon}
            rightStat={scene.comparison.rightStat}
            delay={scene.comparison.delay || 5}
          />
        )}

        {scene.quote && (
          <QuoteCard
            quote={scene.quote.text}
            author={scene.quote.author}
            title={scene.quote.title}
            delay={scene.quote.delay || 5}
            width={scene.quote.width || 680}
          />
        )}

        {scene.icon && (
          <IconHero
            icon={scene.icon}
            size={scene.iconSize || 380}
            glowColor={scene.glowColor || 'rgba(16, 185, 129, 0.25)'}
          />
        )}

        {scene.person && !scene.tweet && (
          <PersonCard
            name={scene.person.name}
            image={scene.person.image}
            width={scene.person.width || 340}
            height={scene.person.height || 440}
          />
        )}
      </div>

      {/* Kinetic Captions / Subtitles: Exact Bottom, Super Readable (текст снизу. читаемый!) */}
      {scene.text && (
        <KineticText
          text={scene.text}
          words={scene.words || []}
          currentTimeSec={currentTimeSec}
          fontSize={scene.fontSize || 50}
          position="bottom"
        />
      )}
    </div>
  );
};
