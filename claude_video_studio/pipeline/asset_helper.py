"""Asset Manager and Reference Asset Extractor for Claude Video Studio.
Extracts clean reference icons & portraits from the reference video,
and provides SVG/canvas fallback generators for new projects.
"""

import json
import os
import subprocess
import shutil
import urllib.request

FFMPEG_PATH = shutil.which("ffmpeg") or shutil.which("ffmpeg.cmd") or "C:\\Users\\Admin\\AppData\\Local\\Microsoft\\WinGet\\Packages\\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\\ffmpeg-9.0.2-full_build\\bin\\ffmpeg.exe"


def extract_reference_assets(ref_video_path, output_dir):
    """Crops key visual assets from the reference video for instant demo use."""
    os.makedirs(os.path.join(output_dir, "icons"), exist_ok=True)
    os.makedirs(os.path.join(output_dir, "avatars"), exist_ok=True)

    # Asset definitions: (name, category, timestamp, crop_filter)
    # Video resolution is 464x848
    assets = [
        # OpenAI 3D Icon (centered at 2.0s)
        (
            "openai.png",
            "icons",
            2.0,
            "crop=240:240:(in_w-240)/2:(in_h-240)/2+40",
        ),
        # Clock 3D Icon (at 5.0s)
        ("clock.png", "icons", 5.0, "crop=200:200:(in_w-200)/2:440"),
        # Brain 3D Icon (at 20.0s)
        ("brain.png", "icons", 20.0, "crop=240:200:(in_w-240)/2:430"),
        # Building 3D Icon (at 70.0s)
        ("building.png", "icons", 70.0, "crop=100:170:70:460"),
        # Microsoft Icon (at 70.0s)
        ("microsoft.png", "icons", 70.0, "crop=110:110:295:485"),
        # Calendar Card (at 95.0s)
        ("calendar.png", "icons", 95.0, "crop=110:110:177:475"),
        # Anthropic Claude Star Icon (at 155.0s)
        ("claude.png", "icons", 155.0, "crop=110:110:177:365"),
        # xAI Logo (at 155.0s)
        ("xai.png", "icons", 155.0, "crop=100:100:310:370"),
        # Elon Musk Avatar (at 10.0s)
        ("musk.jpg", "avatars", 10.0, "crop=150:175:(in_w-150)/2:265"),
        # Ilya Sutskever Avatar (at 45.0s)
        ("sutskever.jpg", "avatars", 45.0, "crop=145:180:68:385"),
        # Greg Brockman Avatar (at 45.0s)
        ("brockman.jpg", "avatars", 45.0, "crop=145:180:250:385"),
        # Dario Amodei Avatar (at 80.0s)
        ("amodei.jpg", "avatars", 80.0, "crop=140:175:50:395"),
        # Sam Altman Avatar (at 110.0s)
        ("altman.jpg", "avatars", 110.0, "crop=130:170:78:425"),
    ]

    for filename, cat, timestamp, crop in assets:
        target_path = os.path.join(output_dir, cat, filename)
        cmd = [
            FFMPEG_PATH,
            "-y",
            "-ss",
            str(timestamp),
            "-i",
            ref_video_path,
            "-vf",
            crop,
            "-vframes",
            "1",
            "-q:v",
            "2",
            target_path,
        ]
        try:
            subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True,
            )
            print(f"Extracted {cat}/{filename}")
        except Exception as e:
            print(f"Failed to extract {filename}: {e}")


def generate_svg_icon(name, output_path):
    """Generates clean SVG icons when custom assets are requested."""
    svgs = {
        "sparkles": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#60a5fa" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"/></svg>""",
        "cpu": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#34d399" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="16" height="16" x="4" y="4" rx="2"/><rect width="6" height="6" x="9" y="9" rx="1"/><path d="M15 2v2"/><path d="M15 20v2"/><path d="M2 15h2"/><path d="M2 9h2"/><path d="M20 15h2"/><path d="M20 9h2"/><path d="M9 2v2"/><path d="M9 20v2"/></svg>""",
        "zap": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#fbbf24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>""",
        "trending_up": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#f87171" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/></svg>""",
    }
    if name in svgs:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(svgs[name])
        print(f"Generated SVG: {output_path}")


if __name__ == "__main__":
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ref_path = os.path.join(os.path.dirname(base), "референс.mp4")
    out_dir = os.path.join(base, "assets")
    if os.path.exists(ref_path):
        extract_reference_assets(ref_path, out_dir)
    else:
        print(f"Reference video not found at {ref_path}")
