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

import tcars

logger = logging.getLogger(__name__)

DEFAULT_CONFIG = fn_config = os.path.join(
        importlib.resources.files("tcars"),
        "config/tcars_config.json"
    )

# initialize commandline interface
@click.version_option()
@click.group("tcars")
def cli():
    pass
