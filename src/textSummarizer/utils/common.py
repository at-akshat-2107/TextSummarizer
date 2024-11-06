import os  # Provides functions to interact with the operating system
from box.exceptions import BoxValueError  # Exception for handling errors with Box library
import yaml  # For loading and parsing YAML files
from textSummarizer.logging import logger  # Custom logging module for logging messages
from ensure import ensure_annotations  # Decorator for runtime type checking of functions if type defines in function int and passes in value as arguments str raise a alert.
from box import ConfigBox  # Box module allows dict-like access to dictionaries
from pathlib import Path  # Pathlib library to work with file and directory paths
from typing import Any  # To specify data type hints


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object, 
    which allows accessing dictionary keys as attributes.

    Args:
        path_to_yaml (Path): Path object pointing to the YAML file to be read.

    Raises:
        ValueError: Raised if the YAML file is empty.
        e: Any other exceptions encountered during file reading.

    Returns:
        ConfigBox: An instance of ConfigBox with the parsed YAML content.
    """
    try:
        # Open the YAML file in read mode
        with open(path_to_yaml) as yaml_file:
            # Parse YAML file and store its content
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            # Return content as a ConfigBox object for attribute-like access
            return ConfigBox(content)
    except BoxValueError:
        # Raise a ValueError if the YAML file is empty
        raise ValueError("YAML file is empty")
    except Exception as e:
        # Raise any other exceptions encountered
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates directories from a given list of paths.

    Args:
        path_to_directories (list): List containing directory paths to create.
        verbose (bool, optional): If True, logs each directory creation. Defaults to True.
    """
    for path in path_to_directories:
        # Create directory; if it already exists, no error is raised due to exist_ok=True
        os.makedirs(path, exist_ok=True)
        # Log directory creation if verbose is enabled
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Calculates and returns the size of a file in kilobytes (KB).

    Args:
        path (Path): Path object pointing to the file whose size is required.

    Returns:
        str: The file size rounded to the nearest KB, prefixed with '~' to indicate approximation.
    """
    # Get file size in bytes and convert to KB
    size_in_kb = round(os.path.getsize(path) / 1024)
    # Return size as a string with "~" to indicate approximation
    return f"~ {size_in_kb} KB"
