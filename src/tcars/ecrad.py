import os
import importlib.resources
import jstyleson as json
import f90nml as fnl
from tempfile import TemporaryDirectory
import subprocess as sproc
import numpy as np

ecrad_bin = os.path.join(
        importlib.resources.files("tcars"),
        "ecrad/bin/ecrad"
    )

def ecrad_run(cfg, inp):
    with TemporaryDirectory() as tmpdir:
        cwd = os.getcwd()
        os.chdir(tmpdir)
        fnl.write(cfg, "cfg.nml")
        inp.to_netcdf("input.nc")
        pstat = sproc.run(
            [ecrad_bin, "cfg.nml", "input.nc", "output.nc"],
            capture_output=True,
            text=True,
        )
        flx = xr.open_dataset("output.nc").copy(deep=True)
        flx["ECRAD"] = ((), np.int32(0))
        flx["ECRAD"].attrs = {
            "version": "1.5",
            "config": json.dumps(cfg),
            "stdout": pstat.stdout.splitlines(),
        }
        os.chdir(cwd)
    return flx