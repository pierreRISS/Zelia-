import blenderproc as bproc
from ast import arg
import argparse
import os
import random
import bpy
import numpy as np
from blenderproc.python.types.EntityUtility import Entity
from blenderproc.python.utility.Utility import reset_keyframes


CAM_X = 648
CAM_Y = 648

def light(light):
    light.set_type("POINT")
    light.set_location(bproc.sampler.shell(
        center=[0, 0, 0],
        radius_min=15,
        radius_max=25,
        elevation_min=40,
        elevation_max=90
    ))
    light.set_energy(random.randint(500, 1000))
    light.set_color([random.randint(200, 255),random.randint(200, 255),random.randint(200, 255)])
    return light

def rand_mat(mat):
    mat.set_principled_shader_value("Specular IOR Level", random.uniform(0, 1))
    mat.set_principled_shader_value("Roughness", random.uniform(0, 1))
    mat.set_principled_shader_value("Metallic", random.uniform(0, 1))

def read_cam_file(camera):
    with open(camera, "r") as f:
        for line in f.readlines():
            line = [float(x) for x in line.split()]
            position, euler_rotation = line[:3], line[3:6]
            matrix_world = bproc.math.build_transformation_mat(position, euler_rotation)
            bproc.camera.add_camera_pose(matrix_world)

def set_ground_material(ground_texture):
    img_ground = bpy.data.images.load(f"{ground_texture}/{random.choice(os.listdir(ground_texture))}")
    materials = bproc.material.collect_all()
    ground_material = bproc.filter.one_by_attr(materials, "name", "ground")
    ground_material.set_principled_shader_value("Base Color", img_ground)
    ground_material.set_displacement_from_principled_shader_value("Base Color", multiply_factor=0.5)
    rand_mat(ground_material)
    
def set_pieces_material(pieces_texture):
    materials = bproc.material.collect_all()
    img_pieces = bpy.data.images.load(f"{pieces_texture}/{random.choice(os.listdir(pieces_texture))}")
    pieces_material = bproc.filter.one_by_attr(materials, "name", "piece")
    pieces_material.set_principled_shader_value("Base Color", img_pieces)
    rand_mat(pieces_material)

def random_pos_cam(nbr_photos, poi):
    for i in range(nbr_photos):
        location = [random.randint(-20, 20), random.randint(-20, 20), random.randint(20, 60)]
        rotation_matrix = bproc.camera.rotation_from_forward_vec(poi - location, inplane_rot=np.random.uniform(-0.7854, 0.7854))
        cam2world_matrix = bproc.math.build_transformation_mat(location, rotation_matrix)
        bproc.camera.add_camera_pose(cam2world_matrix)

def set_ground(obj, ground):
    for obj in ground:
        obj.set_scale([25, 25, 1])
        obj.set_cp("category_id", 0)
        obj.enable_rigidbody(active=False, collision_shape="MESH")

def random_objs(size_piece, pos_piece, objs, nbr):
    for j, obj in enumerate(objs):
        if (j > nbr):
            obj.set_cp("category_id", 0)
            obj.disable_rigidbody()
            obj.hide(True)
        else:
            obj.set_cp("category_id", 1)
            obj.set_scale([size_piece, size_piece, size_piece])
            obj.set_location([random.randint(-pos_piece, pos_piece), random.randint(-pos_piece, pos_piece), ((j+5)/20)])
            obj.set_rotation_euler([0, 0, random.randint(-180, 180)])
            obj.enable_rigidbody(active=True, collision_shape="BOX")
            obj.hide(False)

def load_pieces(nbr_pieces, objs):
    iter = int(nbr_pieces -len(objs))
    for i in range(iter):
        objs.append(random.choice(objs).duplicate())

def cam_move(nbr_images, ground):
    poi = bproc.object.compute_poi(ground)
    random_pos_cam(nbr_images, poi)
    focus_point = bproc.object.create_empty("Camera Focus Point")
    focus_point.set_location(poi)

def write_data(data):
    bproc.writer.write_coco_annotations(os.path.join("./output", 'coco_data'),
                                        instance_segmaps=data["instance_segmaps"],
                                        instance_attribute_maps=data["instance_attribute_maps"],
                                        colors=data["colors"],
                                        camera_resolution = (CAM_X, CAM_Y),
                                        color_file_format="JPEG",
                                        append_to_existing_output = False,
                                        )

bproc.init()

objs = bproc.loader.load_blend("ressources/puzzle_pieces.blend")
ground = bproc.loader.load_blend("ressources/ground.blend")

load_pieces(100, objs)
light0 = bproc.types.Light()

read_cam_file("ressources/cam_pos")

bproc.camera.set_resolution(CAM_X, CAM_Y)

# activate normal rendering
bproc.renderer.enable_normals_output()
bproc.renderer.enable_segmentation_output(map_by=["category_id", "instance", "name"])

def generation_cycles(nbr_sim, nbr_mat_swt, nbr_pictures, size, pos_piece, nbr_pieces):
    for j in range(nbr_sim):
        set_ground(objs, ground)
        random_objs(size, pos_piece, objs, nbr_pieces)
        light(light0)
        bproc.object.simulate_physics_and_fix_final_poses(min_simulation_time=4, max_simulation_time=20, check_object_interval=1)
        for i in range(nbr_mat_swt):
            set_ground_material("ressources/ground_texture/")
            set_pieces_material("ressources/piece_texture/")
            cam_move(nbr_pictures, ground)
            data = bproc.renderer.render()
            write_data(data)
            reset_keyframes()

generation_cycles(4, 4, 10, 0.8, 15, 100)
generation_cycles(10, 5, 10, 1.4, 20, 100)
generation_cycles(10, 10, 10, 1.8, 15, 50)
generation_cycles(4, 4, 10, 0.6, 15, 100)
generation_cycles(4, 4, 10, 0.8, 15, 100)


