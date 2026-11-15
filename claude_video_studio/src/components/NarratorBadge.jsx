import React from 'react';
import { Img, staticFile } from 'remotion';

export const NarratorBadge = ({
  avatar = 'avatars/amodei.jpg',
  size = 120,
}) => {
  if (!avatar) return null;
  const avatarSrc = avatar.startsWith('http') ? avatar : staticFile(avatar);

  return (
    <div
      style={{
        position: 'absolute',
        top: 80,
        left: 60,
        width: `${size}px`,
        height: `${size * 1.25}px`,
        borderRadius: '24px',
        overflow: 'hidden',
        border: '2px solid rgba(255, 255, 255, 0.2)',
        boxShadow: '0 10px 30px rgba(0, 0, 0, 0.4)',
        zIndex: 20,
        backgroundColor: '#1f2937',
      }}
    >
      <Img
        src={avatarSrc}
        style={{
          width: '100%',
          height: '100%',
          objectFit: 'cover',
        }}
      />
    </div>
  );
};
