#!/bin/bash

# Required Variables (Passed from environment variables)
YOUTUBE_STREAM_URL="rtmp://a.rtmp.youtube.com/live2"
STREAM_KEY="${YOUTUBE_STREAM_KEY}"

VIDEO_INPUT="assets/background.mp4"
AUDIO_INPUT="assets/playlist.concat" # Concatenated list of audio files

# Optimized FFmpeg parameters for YouTube Live 1080p stream
ffmpeg -loglevel info -y \
  -re \
  -stream_loop -1 -i "$VIDEO_INPUT" \
  -f concat -safe 0 -i "$AUDIO_INPUT" \
  -c:v libx264 \
  -preset veryfast \
  -b:v 4500k \
  -maxrate 4500k \
  -bufsize 9000k \
  -pix_fmt yuv420p \
  -g 60 \
  -c:a aac \
  -b:a 128k \
  -ar 44100 \
  -f flv "${YOUTUBE_STREAM_URL}/${STREAM_KEY}"
