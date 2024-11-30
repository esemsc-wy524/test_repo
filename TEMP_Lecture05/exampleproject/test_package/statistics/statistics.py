import numpy as np

def calculate_mean(data):
    """Calculates the mean of an array.

    Parameters
    ----------
    data : np.ndarray
        Input data array.

    Returns
    -------
    float
        The mean of the data.
    """
    return np.mean(data)

def calculate_median(data):
    """Calculates the median of an array.

    Parameters
    ----------
    data : np.ndarray
        Input data array.

    Returns
    -------
    float
        The median of the data.
    """
    return np.median(data)

def calculate_std(data):
    """Calculates the standard deviation of an array.

    Parameters
    ----------
    data : np.ndarray
        Input data array.

    Returns
    -------
    float
        The standard deviation of the data.
    """
    return np.std(data)