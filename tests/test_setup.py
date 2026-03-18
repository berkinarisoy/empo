"""Verify that project dependencies are correctly installed."""

import sys

def test_python_version():
    assert sys.version_info[:2] == (3, 10), (
        f"Expected Python 3.10, got {sys.version_info.major}.{sys.version_info.minor}"
    )

def test_nmmo_importable():
    import nmmo  # noqa: F401


def test_torch_importable():
    import torch  # noqa: F401


def test_hydra_importable():
    import hydra  # noqa: F401


def test_omegaconf_importable():
    import omegaconf  # noqa: F401


def test_dill_importable():
    import dill  # noqa: F401


def test_empo_importable():
    import empo  # noqa: F401