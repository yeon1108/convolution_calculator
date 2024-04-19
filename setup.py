from cx_Freeze import setup, Executable
import sys
import scipy.signal

include_files = [scipy.signal.__file__]

setup(
    name="Convolution_Calculator",
    version="1.0",
    description="Convolution Calculator",
    executables=[Executable("convolution_calculator_main.py")],
    options={
        "build_exe": {
            "packages": ["numpy", "scipy"],
            "include_files": include_files,
        }
    }
)



"""
<to make exe file> 
cmd
1. pip install --upgrade cx_Freeze
2. cd directory of your file (setup.py and convolution_calculator_main.py)
3. python setup.py build

"""