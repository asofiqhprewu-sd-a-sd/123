#!/usr/bin/env python3
"""Claude Video Studio - Master CLI Orchestrator.
Automates high-impact motion graphics videos for tech explainers, reels, and shorts.

Usage:
    python studio.py list
    python studio.py new <project_name>
    python studio.py voice <project_name> [--voice ru-RU-DmitryNeural]
    python studio.py render <project_name> [--out output.mp4]
    python studio.py preview <project_name>
    python studio.py create <project_name>
"""

import argparse
import json
import os
import shutil
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECTS_DIR = os.path.join(BASE_DIR, "projects")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
FFMPEG_PATH = (
    shutil.which("ffmpeg")
    or shutil.which("ffmpeg.cmd")
    or "C:\\Users\\Admin\\AppData\\Local\\Microsoft\\WinGet\\Packages\\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\\ffmpeg-9.0.2-full_build\\bin\\ffmpeg.exe"
)


def cmd_list(args):
    print("\n--- Available Studio Projects ---")
    if not os.path.exists(PROJECTS_DIR):
        print("No projects directory found.")
        return

    projects = [
        d
        for d in os.listdir(PROJECTS_DIR)
        if os.path.isdir(os.path.join(PROJECTS_DIR, d))
    ]
    if not projects:
        print("No projects found.")
        return

    for p in projects:
        p_dir = os.path.join(PROJECTS_DIR, p)
        script_file = os.path.join(p_dir, "script.json")
        status = "configured" if os.path.exists(script_file) else "empty"
        scenes_count = 0
        total_sec = 0.0
        if os.path.exists(script_file):
            try:
                with open(script_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    scenes = data.get("scenes", [])
                    scenes_count = len(scenes)
                    fps = data.get("fps", 30)
                    total_frames = sum(
                        s.get("durationInFrames", 90) for s in scenes
                    )
                    total_sec = total_frames / fps
            except Exception:
                pass
        mp4_files = [f for f in os.listdir(p_dir) if f.endswith(".mp4")]
        rendered = f"rendered ({mp4_files[0]})" if mp4_files else "not rendered"
        print(
            f" * {p:24} | Scenes: {scenes_count:2} | Duration: {total_sec:5.1f}s | Status: {rendered}"
        )
    print()


def cmd_new(args):
    project_name = args.name.strip().replace(" ", "_").lower()
    target_dir = os.path.join(PROJECTS_DIR, project_name)
    if os.path.exists(target_dir):
        print(f"Error: Project '{project_name}' already exists.")
        return

    os.makedirs(target_dir, exist_ok=True)
    template = {
        "title": args.title or project_name.replace("_", " ").title(),
        "fps": 30,
        "width": 1080,
        "height": 1920,
        "bgMusic": "music/ambient_tech.wav",
        "bgMusicVolume": 0.12,
        "narrator": "avatars/amodei.jpg",
        "scenes": [
            {
                "id": "scene_1",
                "durationInFrames": 90,
                "theme": "dark",
                "text": "заголовок вашей новой истории",
                "icon": "icons/openai.png",
                "sfx": "sfx/pop.wav",
            },
            {
                "id": "scene_2",
                "durationInFrames": 90,
                "theme": "blue",
                "text": "главный персонаж или событие",
                "person": {"name": "имя героя", "image": "avatars/musk.jpg"},
                "sfx": "sfx/whoosh.wav",
            },
            {
                "id": "scene_3",
                "durationInFrames": 90,
                "theme": "red",
                "text": "неожиданный поворот сюжета",
                "diagram": {
                    "leftIcon": "icons/building.png",
                    "rightIcon": "icons/microsoft.png",
                    "leftLabel": "проблема",
                    "rightLabel": "решение",
                },
                "sfx": "sfx/drop.wav",
            },
        ],
    }
    script_path = os.path.join(target_dir, "script.json")
    with open(script_path, "w", encoding="utf-8") as f:
        json.dump(template, f, ensure_ascii=False, indent=2)
    print(f"Created new project at: {target_dir}")
    print(f"Edit the script at: {script_path}")


def cmd_voice(args):
    project_dir = os.path.join(PROJECTS_DIR, args.name)
    script_path = os.path.join(project_dir, "script.json")
    if not os.path.exists(script_path):
        print(f"Error: Script not found at {script_path}")
        return

    from pipeline.tts_engine import generate_speech

    with open(script_path, "r", encoding="utf-8") as f:
        project = json.load(f)

    fps = project.get("fps", 30)
    scenes = project.get("scenes", [])
    voice = args.voice or "ru-RU-DmitryNeural"

    print(f"Generating voiceover for {len(scenes)} scenes using voice '{voice}'...")
    audio_clips = []
    for i, scene in enumerate(scenes):
        text = scene.get("text", "")
        if not text:
            continue
        audio_name = f"voice_scene_{i+1}.mp3"
        audio_path = os.path.join(project_dir, audio_name)
        print(f"[{i+1}/{len(scenes)}] Synthesizing: '{text}'")
        res = generate_speech(text, audio_path, voice=voice)

        # Update scene duration and words timing
        duration_sec = res["duration"]
        # Add 0.3s padding for visual rhythm
        padded_frames = int((duration_sec + 0.35) * fps)
        scene["durationInFrames"] = max(scene.get("durationInFrames", 60), padded_frames)
        scene["words"] = res.get("words", [])
        audio_clips.append(audio_path)

    # Save updated script
    with open(script_path, "w", encoding="utf-8") as f:
        json.dump(project, f, ensure_ascii=False, indent=2)
    print("Voice generation complete! Script timings updated.")


def cmd_render(args):
    project_dir = os.path.join(PROJECTS_DIR, args.name)
    script_path = os.path.join(project_dir, "script.json")
    if not os.path.exists(script_path):
        print(f"Error: Script not found at {script_path}")
        return

    output_path = args.out
    if not output_path:
        output_path = os.path.join(project_dir, f"{args.name}.mp4")

    # Read project
    with open(script_path, "r", encoding="utf-8") as f:
        project_data = json.load(f)

    # Update src/Root.jsx to load this project
    root_jsx_path = os.path.join(BASE_DIR, "src", "Root.jsx")
    total_frames = sum(s.get("durationInFrames", 90) for s in project_data.get("scenes", []))
    fps = project_data.get("fps", 30)

    # Write temporary Root.jsx with current project props
    escaped_json = json.dumps(project_data, ensure_ascii=False)
    root_code = f"""import React from 'react';
import {{ Composition }} from 'remotion';
import {{ VideoComposition }} from './VideoComposition';

const project = {escaped_json};

export const RemotionRoot = () => {{
  return (
    <Composition
      id="MainVideo"
      component={{VideoComposition}}
      durationInFrames={{{total_frames}}}
      fps={{{fps}}}
      width={{{project_data.get('width', 1080)}}}
      height={{{project_data.get('height', 1920)}}}
      defaultProps={{{{ project }}}}
    />
  );
}};
"""
    with open(root_jsx_path, "w", encoding="utf-8") as f:
        f.write(root_code)

    print(f"Rendering '{args.name}' ({total_frames} frames @ {fps}fps = {total_frames/fps:.1f}s)...")
    cmd = [
        "npx.cmd" if sys.platform == "win32" else "npx",
        "remotion",
        "render",
        "src/index.jsx",
        "MainVideo",
        output_path,
        f"--browser-executable={CHROME_PATH}",
    ]
    try:
        subprocess.run(cmd, cwd=BASE_DIR, check=True)
        print(f"\nRender Complete! Output saved to:\n{output_path}\n")
    except subprocess.CalledProcessError as e:
        print(f"Render failed: {e}")


def cmd_preview(args):
    project_dir = os.path.join(PROJECTS_DIR, args.name)
    script_path = os.path.join(project_dir, "script.json")
    if not os.path.exists(script_path):
        print(f"Error: Script not found at {script_path}")
        return

    # Update Root.jsx
    with open(script_path, "r", encoding="utf-8") as f:
        project_data = json.load(f)

    root_jsx_path = os.path.join(BASE_DIR, "src", "Root.jsx")
    total_frames = sum(s.get("durationInFrames", 90) for s in project_data.get("scenes", []))
    fps = project_data.get("fps", 30)
    escaped_json = json.dumps(project_data, ensure_ascii=False)
    root_code = f"""import React from 'react';
import {{ Composition }} from 'remotion';
import {{ VideoComposition }} from './VideoComposition';

const project = {escaped_json};

export const RemotionRoot = () => {{
  return (
    <Composition
      id="MainVideo"
      component={{VideoComposition}}
      durationInFrames={{{total_frames}}}
      fps={{{fps}}}
      width={{{project_data.get('width', 1080)}}}
      height={{{project_data.get('height', 1920)}}}
      defaultProps={{{{ project }}}}
    />
  );
}};
"""
    with open(root_jsx_path, "w", encoding="utf-8") as f:
        f.write(root_code)

    print(f"Launching Remotion Studio preview for '{args.name}'...")
    cmd = [
        "npx.cmd" if sys.platform == "win32" else "npx",
        "remotion",
        "studio",
        "src/index.jsx",
        f"--browser-executable={CHROME_PATH}",
    ]
    subprocess.run(cmd, cwd=BASE_DIR)


def cmd_create(args):
    """One-stop shop: voice generation + render."""
    cmd_voice(args)
    cmd_render(args)


def main():
    parser = argparse.ArgumentParser(description="Claude Video Studio CLI")
    sub = parser.add_subparsers(dest="command")

    p_list = sub.add_parser("list", help="List all video projects")

    p_new = sub.add_parser("new", help="Create a new video project")
    p_new.add_argument("name", help="Project identifier")
    p_new.add_argument("--title", help="Human-readable project title")

    p_voice = sub.add_parser("voice", help="Generate neural speech for project")
    p_voice.add_argument("name", help="Project identifier")
    p_voice.add_argument("--voice", default="ru-RU-DmitryNeural", help="TTS voice name")

    p_render = sub.add_parser("render", help="Render video to MP4")
    p_render.add_argument("name", help="Project identifier")
    p_render.add_argument("--out", help="Output MP4 file path")

    p_preview = sub.add_parser("preview", help="Open Remotion visual preview UI")
    p_preview.add_argument("name", help="Project identifier")

    p_create = sub.add_parser("create", help="Generate audio and render in one step")
    p_create.add_argument("name", help="Project identifier")
    p_create.add_argument("--voice", default="ru-RU-DmitryNeural", help="TTS voice name")
    p_create.add_argument("--out", help="Output MP4 file path")

    args = parser.parse_args()
    if args.command == "list":
        cmd_list(args)
    elif args.command == "new":
        cmd_new(args)
    elif args.command == "voice":
        cmd_voice(args)
    elif args.command == "render":
        cmd_render(args)
    elif args.command == "preview":
        cmd_preview(args)
    elif args.command == "create":
        cmd_create(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
