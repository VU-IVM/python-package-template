"""Testing functions in your_module.py."""
import numpy as np
import pandas as pd
import pytest
import xarray as xr
from your_package_name.your_module import XrUtils


# Define a fixture for creating sample data
@pytest.fixture
def sample_data():
    # Create sample xr.DataArray objects for testing
    time = pd.date_range(start="2000-01-01", periods=20, freq="Y")
    data = np.arange(20)
    xr_data = xr.DataArray(data, coords={"time": time}, dims=("time",))
    return xr_data


def test_init(sample_data):
    # Test that the class is initialized correctly
    xr_utils = XrUtils(sample_data)
    assert xr_utils.data.identical(sample_data)


def test_sel_years(sample_data):
    # Test that the sel_years function works as expected
    xr_utils = XrUtils(sample_data)
    assert xr_utils.sel_years(*[2000, 2001, 2002]).identical(
        sample_data.sel(time=np.isin(sample_data.time.dt.year, [2000, 2001, 2002]))
    )
