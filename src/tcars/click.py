import shutil
import os.path
import importlib.resources
import warnings

import click
import logging
import parse
import xarray as xr
import pandas as pd
import numpy as np
import datetime as dt
import subprocess
import jstyleson as json
import f90nml

import tcars
import tcars.ecrad

logger = logging.getLogger(__name__)

DEFAULT_CONFIG = fn_config = os.path.join(
        importlib.resources.files("tcars"),
        "config/tcars_config.json"
    )

#################################################################################################################
# T-CARS CLI
#################################################################################################################
# initialize commandline interface
@click.version_option()
@click.group("tcars")
def cli_tcars():
    pass

#################################################################################################################
# ecrad cli
#################################################################################################################
# init cli
@click.version_option(message=f"tcars: version {tcars.__version__}, ecrad: version {tcars.ecrad.__version__}")
@click.group("ecrad")
@click.argument("namfile",type=click.Path(dir_okay=False, exists=True), nargs=1)
@click.argument("infile",type=click.Path(dir_okay=False, exists=True), nargs=1)
@click.argument("outfile",type=click.Path(dir_okay=False, exists=False), nargs=1)
@click.option("--config", "-c", type=click.Path(dir_okay=False, exists=True),
              help="Config file - will merge and override the default config.")
def cli_ecrad(namfile,infile,outfile,config=None):
    """Run vanilla ecrad on the command line.
    """
    config = tcars.utils.merge_config(config)
    ecrad_bin = os.path.join(
        importlib.resources.files("ecrad"),
        "bin/ecrad"
    )

    namfile_dict = f90nml.read(namfile)

    pstat = subprocess.run(
            [ecrad_bin, namfile, infile, outfile],
            capture_output=True,
            text=True,
        )
    
    flx = xr.load_dataset(outfile)
    flx["ECRAD"] = ((), np.int32(0))
    flx["ECRAD"].attrs = {
        "version": tcars.ecrad.__version__,
        "config": json.dumps(namfile_dict),
        "stdout": pstat.stdout.splitlines(),
    }

    flx.to_netcdf(outfile)

