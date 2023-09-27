"""This is summary of the purpose of your module."""
from typing import Union
import numpy as np
import xarray as xr


class XrUtils:
    """Class with different xarray utility functions."""

    def __init__(self, data: xr.DataArray) -> None:
        """Initialize class with DataArray."""
        self.data = data

    def sel_years(self, *years: Union[list, int]) -> xr.DataArray:
        """Select years from data (insensitive to temporal resolution)."""
        return self.data.sel(time=np.isin(self.data.time.dt.year, years))