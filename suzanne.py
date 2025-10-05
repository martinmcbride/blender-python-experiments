# blender --background --python suzanne.py --render-frame 1 -- </path/to/output/image> <resolution_percentage> <num_samples>

import bpy
import sys
import math
import os

working_dir_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(working_dir_path)

import oldutils

OUTPUT_FILE = "suzanne"
RES_PERCENTAGE = 100
SAMPLES = 5


def set_scene_objects() -> bpy.types.Object:
    num_suzannes = 15
    for index in range(num_suzannes):
        oldutils.create_smooth_monkey(location=((index - (num_suzannes - 1) / 2) * 3.0, 0.0, 0.0),
                                      name="Suzanne" + str(index))
    return bpy.data.objects["Suzanne" + str(int((num_suzannes - 1) / 2))]


# Args
output_file_path = OUTPUT_FILE
resolution_percentage = RES_PERCENTAGE
num_samples = SAMPLES
print(output_file_path, resolution_percentage, num_samples)

# Scene Building

## Reset
oldutils.clean_objects()

## Suzannes
center_suzanne = set_scene_objects()

## Camera
camera_object = oldutils.create_camera(location=(10.0, -7.0, 0.0))

oldutils.add_track_to_constraint(camera_object, center_suzanne)
oldutils.set_camera_params(camera_object.data, center_suzanne, lens=50.0)

## Lights
oldutils.create_sun_light(rotation=(0.0, math.pi * 0.5, -math.pi * 0.1))

# Render Setting
scene = bpy.data.scenes["Scene"]
oldutils.set_output_properties(scene, resolution_percentage, output_file_path)
oldutils.set_cycles_renderer(scene, camera_object, num_samples)
