#!/usr/bin/env bash
set -euo pipefail

/Applications/Blender.app/Contents/MacOS/Blender -b -noaudio --python attach_head.py -- \
  --template "/Users/kubotadaichi/Downloads/original.fbx" \
  --head "/Users/kubotadaichi/dev/learning/hackathons/hackathon202512-pre/model/head.glb" \
  --out "/Users/kubotadaichi/Downloads/out.fbx" \
  --head_bone "mixamorig7:Head" \
  --calib "calib.json" \
  --delete_template_head true \
  --decimate_ratio 0.15

