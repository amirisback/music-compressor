#!/usr/bin/env python

import os
from os.path import basename

from pydub import AudioSegment

# folder path
dir_path = input("Enter dir path: ")

# list file and directories
list_files = os.listdir(dir_path)

# Directory
dir_compressed = "compressed"
# Path
path = os.path.join(dir_path, dir_compressed)

try:
    os.makedirs(path, exist_ok=True)
    print("Directory '%s' created successfully" % dir_compressed)
except OSError as error:
    print("Directory '%s' can not be created" % dir_compressed)


def compress_mp3_file(mp3_file_path):
    if not mp3_file_path.endswith(".mp3"): return

    output_file_path = dir_path + "/" + dir_compressed + "/" + "{}.mp3".format(
        os.path.splitext(basename(mp3_file_path))[0])
    print("\nProcessing {} ==> {}".format(mp3_file_path, output_file_path))

    audio_file = AudioSegment.from_file(mp3_file_path, "mp3")
    frame_rate = audio_file.frame_rate
    bytes_per_sample = audio_file.sample_width

    if frame_rate == 11025:
        print("frame rate is already 11025, ignore.")
        return

    print("frame_rate {} ==> {}".format(frame_rate, "11025"))
    audio_file.export(output_file_path, format="mp3", parameters=["-ar", "11025"])


if len(list_files) == 0:
    print("No mp3 source")
else:
    for list_file in list_files:
        data = dir_path + "/" + list_file
        compress_mp3_file(data)