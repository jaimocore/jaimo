"""
jaimo - Python library and toolkit for data science applications.
"""

# Current Version Number
__version__ = "0.1.0"

# Import the main functions into the top-level namespace.
from .numerical import f
from .numerical import zero

# Content permitted for secondary import / wildcard import.
__all__ = ["f", "zero"]