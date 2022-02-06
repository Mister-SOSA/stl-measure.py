''' A simple, easy to use Python module which allows you to quickly measure STL files.'''



from stl import mesh
from termcolor import colored

accepted_units = ['m', 'cm', 'mm', 'in', 'ft']


def get_dimensions(obj, units):
    '''Accepts a mesh object and desired units of measurement. Returns the X, Y, and Z dimensions of the bounding box of the mesh in a dictionary.'''

    try:
        obj = mesh.Mesh.from_file(obj)
    except Exception as e:
        raise ValueError(e)

    minx = obj.x.min()
    maxx = obj.x.max()
    miny = obj.y.min()
    maxy = obj.y.max()
    minz = obj.z.min()
    maxz = obj.z.max()

    dimension_x = maxx - minx
    dimension_y = maxy - miny
    dimension_z = maxz - minz

    if (units == "m"):
        dimensions_dict = {
            "x": dimension_x,
            "y": dimension_y,
            "z": dimension_z
        }
        return dimensions_dict
    elif (units == "cm"):
        dimensions_dict = {
            "x": dimension_x * 100,
            "y": dimension_y * 100,
            "z": dimension_z * 100
        }
        return dimensions_dict
    elif (units == "mm"):
        dimensions_dict = {
            "x": dimension_x * 1000,
            "y": dimension_y * 1000,
            "z": dimension_z * 1000
        }
        return dimensions_dict
    elif (units == "in"):
        dimensions_dict = {
            "x": dimension_x * 39.37007874,
            "y": dimension_y * 39.37007874,
            "z": dimension_z * 39.37007874
        }
        return dimensions_dict
    elif (units == "ft"):
        dimensions_dict = {
            "x": dimension_x * 3.28084,
            "y": dimension_y * 3.28084,
            "z": dimension_z * 3.28084
        }
        return dimensions_dict
    else:
        raise ValueError(
            'The unit you passed to get_dimensions() \"' + colored(units, 'red') + '\" was invalid. Possible units are ' +
            (', ').join(accepted_units)
        )


def get_box_volume(obj, units):
'''Accepts a mesh object and desired units of measurement. Returns a numeric value which represents the volume of the bounding box of the object.'''
  
    try:
        obj = mesh.Mesh.from_file(obj)
    except Exception as e:
        raise ValueError(e)

    minx = obj.x.min()
    maxx = obj.x.max()
    miny = obj.y.min()
    maxy = obj.y.max()
    minz = obj.z.min()
    maxz = obj.z.max()

    dimension_x = maxx - minx
    dimension_y = maxy - miny
    dimension_z = maxz - minz

    mesh_volume = dimension_x * dimension_y * dimension_z

    if (units == "m"):
        return mesh_volume
    elif (units == "cm"):
        return mesh_volume * 100
    elif (units == "mm"):
        return mesh_volume * 1000
    elif (units == "in"):
        return mesh_volume * 39.37007874
    elif (units == "ft"):
        return mesh_volume * 3.28084
    else:
        raise ValueError(
            'The unit you passed to get_volume() \"' + colored(units, 'red') + '\" was invalid. Possible units are ' +
            (', ').join(accepted_units)
        )
