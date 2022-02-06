# stl-measure.py | STL 3D Model Measurement Tool

A simple, easy to use Python module which allows you to quickly measure STL files.

## ⚙️ Installation

No support for PyPi yet, and thus you cannot install this module with `pip install`. Maybe I will do this in the future.
For now, just download the repo and place the `stlmeasure.py` file in your project directory.

## 🔧 Usage & Examples

Be sure that you import the module into your project using
```py
import stlmeasure
```
At the current time, the module has two main functions, `get_dimensions(obj, units)` and `get_box_volume(obj, units)`.
`get_dimensions(obj, units)` returns a dictionary with the X, Y, and Z dimensions of the object inside.
`get_box_volume(obj, units)` returns a numeric value representing the volume of the **bounding box** of the object. This does not return the "real" volume of the mesh.

The first parameter, `obj`, is the path to the STL file you wish to measure.
The second parameter, `units`, is the unit of measurement you would like to be returned.
Acceptable inputs for `units` at the moment are `'m', 'cm', 'mm', 'in', 'ft'`.

Below you can find some examples of the module in action. Here are some potential goals, with a code block showing you how to accomplish
that goal.



### **Get the dimensions of an STL object, in centimeters, as a dictionary**

```py
import stlmeasure

dimensions = stlmeasure.get_dimensions('./icosphere.stl', 'cm')

print(dimensions)
```
***Ouput:***
```py
{'x': 342.3, 'y': 360.0, 'z': 360.0}
```

### **Get the volume of the bounding box of an STL object, in inches:**

```py
import stlmeasure

bounds_volume = stlmeasure.get_box_volume('./icosphere.stl', 'in')

print(bounds_volume)
```
***Output:***
```
1746.951
```

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
