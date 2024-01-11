import bpy
import os
import sys

# Define the path to the blender-addons directory
addon_directory = '../construction-file_conversion/blender-addons'
sys.path.append(os.path.abspath(addon_directory))

# Function to try to enable an addon
def try_enable_addon(addon_name):
    try:
        bpy.ops.preferences.addon_enable(module=addon_name)
        print(f"Enabled addon: {addon_name}")
    except Exception as e:
        print(f"Failed to enable addon '{addon_name}': {e}")

# Extracted addon names from your directory structure
addon_names = [
    "io_import_dxf", "mesh_tools", "add_mesh_extra_objects", "io_scene_gltf2",
    "node_wrangler", "rigify", "io_mesh_uv_layout", "mesh_looptools",
    "io_anim_camera", "bone_selection_sets", "animation_animall",
    "add_mesh_discombobulator", "io_export_dxf", "magic_uv",
    "development_icon_get", "io_scene_x3d", "btrace", "io_anim_nuke_chan",
    "mesh_tissue", "paint_palette", "object_scatter", "greasepencil_tools",
    "lighting_tri_lights", "measureit", "add_curve_ivygen", "add_camera_rigs",
    "copy_global_transform", "real_snow", "io_anim_bvh", "io_mesh_uv_layout",
    "object_boolean_tools", "archimesh", "object_fracture_cell", "object_carver",
    "space_view3d_stored_views", "object_color_rules", "storypencil",
    "io_import_palette", "object_collection_manager", "system_blend_info",
    "mesh_tiny_cad", "space_view3d_align_tools", "system_demo_mode",
    "io_shape_mdd", "io_mesh_ply", "render_copy_settings", "node_presets",
    "add_curve_extra_objects", "system_property_chart", "development_edit_operator",
    "precision_drawing_tools", "io_export_paper_model", "add_mesh_geodesic_domes",
    "io_mesh_atomic", "ui_translate", "io_curve_svg", "render_ui_animation_render",
    "io_coat3D", "space_view3d_math_vis", "amaranth", "render_povray",
    "mesh_f2", "object_skinify", "io_scene_obj", "space_view3d_3d_navigation",
    "mesh_auto_mirror", "mesh_inset", "io_scene_fbx", "mesh_snap_utilities_line",
    "add_mesh_BoltFactory", "camera_turnaround", "mesh_looptools",
    "space_view3d_brush_menus", "materials_library_vx", "curve_assign_shapekey",
    "io_scene_gltf2", "mesh_tissue", "object_print3d_utils", "materials_utils",
    "animation_add_corrective_shape_key", "space_view3d_copy_attributes",
    "depsgraph_debug", "viewport_vr_preview", "io_export_pc2", "object_color_rules"
]


# Attempt to enable all listed addons
for addon in addon_names:
    try_enable_addon(addon)

# The conversion logic
def convert_file(input_path, output_path):
    # Assuming the DXF import and OBJ export functionality are available
    try:
        # Import DXF file
        bpy.ops.import_scene.dxf(filepath=input_path)

        # Export to OBJ
        bpy.ops.export_scene.obj(filepath=output_path, use_selection=False)
        print(f"Exported OBJ file to {output_path}")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")

# Paths for input DXF file and output OBJ file
input_file = '../construction-file_conversion/files/2-ext_wall.dxf'
output_file = 'files/2-ext_wall_output.obj'

# Perform conversion
convert_file(input_file, output_file)
