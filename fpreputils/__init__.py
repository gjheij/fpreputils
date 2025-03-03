# fpreputils/__init__.py
from importlib.metadata import version

__version__ = version("fpreputils")

# Now import core functionality (optional, but typical in __init__.py)
from . import fmriprep

__all__ = ["fmriprep"]
