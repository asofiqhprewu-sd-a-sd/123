export const THEMES = {
  dark: {
    bg: '#0a0a0c',
    bgGradient: 'radial-gradient(circle at 50% 40%, #15161a 0%, #08080a 100%)',
    gridColor: 'rgba(255, 255, 255, 0.04)',
    accent: '#10b981',
    cardBg: 'rgba(255, 255, 255, 0.05)',
    cardBorder: 'rgba(255, 255, 255, 0.12)',
    textColor: '#ffffff',
    textDim: 'rgba(255, 255, 255, 0.35)',
  },
  red: {
    bg: '#450a0a',
    bgGradient: 'radial-gradient(circle at 50% 40%, #7f1d1d 0%, #450a0a 100%)',
    gridColor: 'rgba(255, 255, 255, 0.06)',
    accent: '#ef4444',
    cardBg: 'rgba(255, 255, 255, 0.08)',
    cardBorder: 'rgba(255, 255, 255, 0.18)',
    textColor: '#ffffff',
    textDim: 'rgba(255, 255, 255, 0.4)',
  },
  blue: {
    bg: '#0284c7',
    bgGradient: 'linear-gradient(180deg, #38bdf8 0%, #0284c7 70%, #0369a1 100%)',
    gridColor: 'rgba(255, 255, 255, 0.12)',
    accent: '#38bdf8',
    cardBg: 'rgba(255, 255, 255, 0.15)',
    cardBorder: 'rgba(255, 255, 255, 0.25)',
    textColor: '#ffffff',
    textDim: 'rgba(255, 255, 255, 0.45)',
  },
  purple: {
    bg: '#3b0764',
    bgGradient: 'radial-gradient(circle at 50% 40%, #581c87 0%, #2e1065 100%)',
    gridColor: 'rgba(255, 255, 255, 0.06)',
    accent: '#a855f7',
    cardBg: 'rgba(255, 255, 255, 0.08)',
    cardBorder: 'rgba(255, 255, 255, 0.15)',
    textColor: '#ffffff',
    textDim: 'rgba(255, 255, 255, 0.4)',
  },
};

export const SPRING_CONFIGS = {
  snappy: { damping: 14, mass: 0.6, stiffness: 120 },
  smooth: { damping: 20, mass: 1.0, stiffness: 80 },
  bouncy: { damping: 10, mass: 0.7, stiffness: 140 },
};

export const FONT_STACK = '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Inter", "Helvetica Neue", Arial, sans-serif';
