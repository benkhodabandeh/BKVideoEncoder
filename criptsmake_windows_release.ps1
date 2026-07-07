warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/analysis.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/app.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/config.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/gui_callbacks.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/utils.py', LF will be replaced by CRLF the next time Git touches it
[1mdiff --git a/README.md b/README.md[m
[1mindex a9f578d..ae1ab70 100644[m
[1m--- a/README.md[m
[1m+++ b/README.md[m
[36m@@ -1,137 +1,122 @@[m
[31m-# Ben. Khodabandeh Video Encoder[m
[31m-[m
[31m-**A professional video encoding toolbox powered by FFmpeg.**  [m
[31m-Wrap x264, x265, and aac into preset-based workflows — no CLI gymnastics.[m
[31m-[m
[31m-![Python](https://img.shields.io/badge/python-3.9+-blue) ![License](https://img.shields.io/badge/license-GPLv3-green) ![Platform](https://img.shields.io/badge/platform-win%20%7C%20linux%20%7C%20macos-lightgrey)[m
[31m-[m
 <p align="center">[m
[31m-  <img src="logo.png" alt="BK Video Encoder" width="128">[m
[32m+[m[32m  <img src="logo.png" alt="BK Video Encoder" width="760">[m
 </p>[m
 [m
[31m-## Screenshots[m
[31m-[m
 <p align="center">[m
[31m-  <img src="screenshots/main_window.png" alt="Main window" width="80%">[m
[32m+[m[32m  <strong>Cinema-grade FFmpeg encoding with a smooth Windows 11 desktop workflow.</strong><br>[m
[32m+[m[32m  Preset-driven x264/x265 encoding, batch development, scene-aware tuning, preview stills, crop tools, metadata, and VMAF QC.[m
 </p>[m
[32m+[m
 <p align="center">[m
[31m-  <img src="screenshots/presets.png" alt="Preset selection" width="45%">[m
[31m-  <img src="screenshots/qc_tool.png" alt="VMAF Quality Control Tool" width="45%">[m
[32m+[m[32m  <a href="https://github.com/benkhodabandeh/BKVideoEncoder/releases"><img alt="Releases" src="https://img.shields.io/github/v/release/benkhodabandeh/BKVideoEncoder?style=for-the-badge"></a>[m
[32m+[m[32m  <img alt="Python" src="https://img.shields.io/badge/python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white">[m
[32m+[m[32m  <img alt="Windows 11" src="https://img.shields.io/badge/Windows_11-optimized-0078D4?style=for-the-badge&logo=windows11&logoColor=white">[m
[32m+[m[32m  <img alt="License" src="https://img.shields.io/github/license/benkhodabandeh/BKVideoEncoder?style=for-the-badge">[m
 </p>[m
 [m
 ---[m
 [m
[31m-## Features[m
[32m+[m[32m## Why BK Video Encoder[m
[32m+[m
[32m+[m[32mBK Video Encoder is a professional creator-focused encoder front-end. It removes repetitive command-line FFmpeg work while keeping the important creative controls visible: source type, target quality, crop, audio handling, metadata, batch queue, still generation, and VMAF comparison.[m
[32m+[m
[32m+[m[32m### Premium workflow highlights[m
 [m
[31m-- **Preset-driven encoding** — pick from curated presets (The Capo, The Soldier, The Ghost, The Hitman, The Rocket, The Heist, The Job) or mix and match[m
[31m-- **Source-aware tuning** — adjusts encoder params for clean, modern, vintage, or animation source material[m
[31m-- **Three quality levels** — Lean, Standard, Prime Cut[m
[31m-- **Batch queue** — stack jobs with different presets and process them in one run[m
[31m-- **VMAF QC Tool** — compare original vs. encoded with perceptual quality scoring[m
[31m-- **Preview stills** — auto-generated snapshots with dominant-color palette bars[m
[31m-- **Metadata tagging** — embed title, artist, year, syndicate into output files[m
[31m-- **Audio mixdown** — dual-track: original multichannel + stereo downmix[m
[31m-- **Scene detection** — via PySceneDetect or FFmpeg[m
[31m-- **Crop detection** — auto-detect letterbox/pillarbox or choose from common aspect ratios[m
[32m+[m[32m| Area | What it does |[m
[32m+[m[32m|---|---|[m
[32m+[m[32m| Preset system | Curated workflows for theatrical masters, web encodes, HEVC compression, social vertical output, and target-size delivery. |[m
[32m+[m[32m| Smooth UI | Background FFmpeg execution, debounced estimate/preview updates, bounded UI queue pumping, and non-blocking routine notifications. |[m
[32m+[m[32m| Batch queue | Queue multiple jobs, reopen/edit queued jobs, reorder jobs, and process them as a development plan. |[m
[32m+[m[32m| Video analysis | FFprobe metadata, source complexity suggestion, crop detection, scene detection, and preview stills. |[m
[32m+[m[32m| Quality control | VMAF comparison tool for checking perceptual quality against the original. |[m
[32m+[m[32m| Windows 11 polish | High-DPI awareness, bundled FFmpeg build support, refined dark theme, and professional icon/branding assets. |[m
 [m
 ---[m
 [m
[31m-## Quick Start[m
[32m+[m[32m## Screenshots[m
[32m+[m
[32m+[m[32m> Add current screenshots to `screenshots/` and keep these filenames for a polished GitHub landing page.[m
[32m+[m
[32m+[m[32m<p align="center">[m
[32m+[m[32m  <img src="screenshots/main-window.png" alt="Main window" width="880"><br>[m
[32m+[m[32m  <em>Main encoding workspace</em>[m
[32m+[m[32m</p>[m
[32m+[m
[32m+[m[32m<p align="center">[m
[32m+[m[32m  <img src="screenshots/preset-selection.png" alt="Preset selection" width="430">[m
[32m+[m[32m  <img src="screenshots/vmaf-qc.png" alt="VMAF QC tool" width="430">[m
[32m+[m[32m</p>[m
 [m
[31m-### Download[m
[32m+[m[32m---[m
 [m
[31m-Grab the latest portable archive for your platform from the [Releases page](https://github.com/benkhodabandeh/BKVideoEncoder/releases).[m
[32m+[m[32m## Quick start on Windows 11[m
 [m
[31m-- **Windows**: `BKVideoEncoder.*.windows.7z` → extract and run `BKVideoEncoder.exe`[m
[31m-- **Linux**: `BKVideoEncoder.*.linux.7z` → extract and run `./BKVideoEncoder`[m
[31m-- **macOS**: `BKVideoEncoder.*.macos.7z` → extract and run `./BKVideoEncoder`[m
[32m+[m[32m### Portable release[m
 [m
[31m-No installation required. The FFmpeg binary is bundled.[m
[32m+[m[32m1. Open the [Releases](https://github.com/benkhodabandeh/BKVideoEncoder/releases) page.[m
[32m+[m[32m2. Download the Windows archive.[m
[32m+[m[32m3. Extract it to a normal user folder, for example `C:\Apps\BKVideoEncoder`.[m
[32m+[m[32m4. Run `BKVideoEncoder.exe`.[m
 [m
[31m-### Build from Source[m
[32m+[m[32m### Build from source[m
 [m
[31m-```bash[m
[32m+[m[32m```powershell[m
 git clone https://github.com/benkhodabandeh/BKVideoEncoder.git[m
 cd BKVideoEncoder[m
[32m+[m[32mpy -3.11 -m venv .venv[m
[32m+[m[32m.\.venv\Scripts\Activate.ps1[m
[32m+[m[32mpython -m pip install --upgrade pip[m
 pip install -r requirements.txt pyinstaller[m
[31m-[m
[31m-# On Windows:[m
[31m-python build.py[m
[31m-[m
[31m-# On Linux/macOS:[m
 python build.py[m
 ```[m
 [m
[31m-The built binary + FFmpeg bundle lands in `dist/`.[m
[32m+[m[32mThe portable build lands in `dist/`.[m
 [m
 ---[m
 [m
[31m-## How It Works[m
[32m+[m[32m## Preset reference[m
 [m
[31m-1. **Load a video** — sets the source.[m
[31m-2. **Enter metadata** — title, year, artist (used for filenames and output folders).[m
[31m-3. **Select preset(s)** — each preset targets a specific encoder/resolution/workflow.[m
[31m-4. **Adjust quality** — Lean (smaller), Standard (balanced), Prime Cut (highest).[m
[31m-5. **Queue or Go** — add multiple jobs to The Plan or hit MAKE THE HIT.[m
[32m+[m[32m| Preset | Codec | Mode | Best for |[m
[32m+[m[32m|---|---|---|---|[m
[32m+[m[32m| The Capo | x264 | CRF | High-quality theatrical / compatibility master |[m
[32m+[m[32m| The Soldier | x264 | 2-pass ABR | Web distribution with predictable size and quality |[m
[32m+[m[32m| The Ghost | x265 | 2-pass ABR | Efficient HEVC compression |[m
[32m+[m[32m| The Hitman | x264 | CRF | Fast x26