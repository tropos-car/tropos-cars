# tropos-cars


## Installation

It is recommended to download `environment.yml` and install via conda/mamba:
```bash
$ mamba env create -f environment.yml
```
This create the environment "tcars", installes required dependencies and tcars and compiles ecrad.

Test after installation is to print the tcars and ecrad version:
```bash
$ mamba activate tcars
$ ecrad --version
tcars: <version>, ecrad: <version>
```


### Manual conda/mamba + pip
Before installing this package, ensure you have the following prerequisites:
* netcdf4
* netcdf-fortran
* hdf5
* cmake
* cxx-compiler
* fortran-compiler
* openblas

Install prerequisites while creating environment (recommended)
```bash
$ mamba create -n tcars -c conda-forge netcdf4 netcdf-fortran hdf5 cmake cxx-compiler fortran-compiler openblas
```

Activate the environment
```bash
$ mamba activate tcars
```

Then tcars + ecrad can be installed via:
```bash
$ python -m pip install git+https://github.com/tropos-car/tropos-cars
```

### Developement install

Install prerequisites while creating environment
```bash
mamba create -n tcars -c conda-forge netcdf4 netcdf-fortran hdf5 cmake cxx-compiler fortran-compiler openblas
```

Activate the environment
```bash
$ mamba activate tcars
```
Clone the repository:
```bash
$ git clone https://github.com/tropos-car/tropos-cars
```

Change directory:
```bash
$ cd tropos-cars/
```

Then install in editable mode:
```bash
$ python -m pip install -e .
```

## Usage
### ecrad classic interface

Print version:
```bash
$ ecrad --version
tcars: <version>, ecrad: <version>
```

Print help:
```bash
$ ecrad --help
```

Run ecrad from command line from any directory:
```bash
$ ecrad namfile infile outfile
```
> The ecrad outfile is modified, adding the "ECRAD" variable with stdout, version and configuration information.

### tcars cli
Print version:
```bash
$ tcars --version
tcars: <version>
```