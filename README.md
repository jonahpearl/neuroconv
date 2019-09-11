# nwbn-conversion-tools
Shared tools for converting data from various formats to NWB:N 2.0

## Installation
To clone the repository and set up a conda environment, do:
```
$ git clone https://github.com/NeurodataWithoutBorders/nwbn-conversion-tools
$ conda env create -f nwbn-conversion-tools/make_env.yml
$ source activate nwbn_conversion
```

Alternatively, to install **nwbn_conversion_tools** directly in an existing environment:
```
$ pip install git+https://github.com/NeurodataWithoutBorders/nwbn-conversion-tools
```

## GUI
After activating the correct environment, nwbn_conversion_tools GUI can be imported and run from the python interpreter.
```python
from nwbn_conversion_tools.gui.main_gui import main

main()
```



## optical physiology
### processing
* [CELLMax](https://github.com/NeurodataWithoutBorders/nwbn-conversion-tools/blob/master/nwbn_conversion_tools/ophys/processing/CELLMax/README.md)
