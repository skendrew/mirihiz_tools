# mirihiz_tools


## What's in this repository

The repository contains a few tools for interacting with MIRISim simulations and analysis performed on them. 

## Dependencies

The following packages are required for running code in this repository:
* mirisim
* numpy
* astropy
* [regions](https://github.com/astropy/regions)

The code requires to have *mirisim.skysim* installed to retrieve sources from a scene. This is typically achieved by installing within the mirisim or miricle environment. The easist way to get the *regions* python package installed is via conda astropy repository:

```
>>> conda install -c astropy regions
```

## Code

The main file is make\_regions.py. This contains the main function, also called make\_regions, which creates a DS9 region file. It currently takes both the coordinates and size of the source to create DS9 Circle regions; this is an approximation in the case of non-circular sources. 

The code supports physical coordinates (i.e. detector pixels), from Sextractor output files.

The code also supports relative coordinates from Mirisim scene.ini

The test_data/ directory contains test files that can be used to test the code.

## Calling examples

From the shell command line:

```
>> python make_regions.py test_data/test_data_xtrac.cat sextractor ds9test.reg

````

From an interactive python session:

```
In [2]: from make_regions import make_regions

In [3]: x = make_regions(file='test_data/test_data_xtrac.cat', filetype='sextractor', outfile='ds9reg.reg')

```

Alternatively, for reading the scene from the shell command line:

```
>> python make_regions.py test_data/scene.ini scene ds9test.reg

````

From an interactive python session:

```
In [4]: from make_regions import make_regions

In [5]: x = make_regions(file='test_data/scene.ini', filetype='scene', outfile='ds9reg.reg')

```
## Questions or requests

Post an issue or email me.

## Author

S. Kendrew & M. Topinka, May 2019 
