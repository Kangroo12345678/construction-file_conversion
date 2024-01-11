def extract_mesh_names_from_obj(obj_file_path):
    mesh_names = []

    with open(obj_file_path, 'r') as file:
        for line in file:
            # OBJ files denote objects with 'o' and groups with 'g'
            if line.startswith('o ') or line.startswith('g '):
                # Extract the name and strip whitespace
                name = line[2:].strip()
                mesh_names.append(name)

    return mesh_names

# Example usage
obj_file_path = 'files/2-external_wall-obj/external_wall_3d.obj'
mesh_names = extract_mesh_names_from_obj(obj_file_path)
print("Mesh Names in OBJ file:", mesh_names)
