import numpy as np
import matplotlib.pyplot as plt
from simulation_params_module import Setup, Object, Camera
from PSF_module import PSF
from illumination_pattern_module import IlluminationPattern


class Background:
    """
    Class for generating a background term dependent of the illumination pattern and detection PSF.

    Parameters:
    -----------
    setup : class
        Parameters related to the setup
    object : class
        Parameters related to the object, i.e. the emitters
    camera : class
        Parameters related to the camera
    PSF : class
        PSF model related to the detection psf
    IlluminationPattern : class
        Illumination pattern

    """

    def __init__(self, setup: Setup, object: Object, camera: Camera):
        self.setup = setup
        self.object = object
        self.camera = camera

    def compute_background(self):
        """
        Computes the patterned dependent background term

        Parameters:
        -----------
        illumination_pattern : ndarray
            The funciton for the illumination pattern
        x_grid, y_grid : ndarray
            Grid of the simulation
        x_grid_camera, y_grid_camera : float
            Grid of the camera pixels
        pixel_size_x, pixel_size_y : float
            Size of the pixels in the x and y direction
        psf : ndarray
            The function for the detection psf

        Returns:
        --------
        background : ndarray
            Value of the background term
        """
    pass

    def derive_background_to_x(self):
        """
        Derives the pattern dependent background term with respect to x-position of the emitter

        Parameters:
        -----------
        illumination_pattern : ndarray
            The funciton for the illumination pattern
        x_grid, y_grid : ndarray
            Grid of the simulation
        x_grid_camera, y_grid_camera : float
            Grid of the camera pixels
        pixel_size_x, pixel_size_y : float
            Size of the pixels in the x and y direction
        psf : ndarray
            The function for the detection psf

        Returns:
        --------
        dBdx : ndarray
            Value of the derivative of the background term to x
        """
        pass

    def derive_background_to_y(self):
        """
        Derives the pattern dependent background term with respect to y-position of the emitter

        Parameters:
        -----------
        illumination_pattern : ndarray
            The funciton for the illumination pattern
        x_grid, y_grid : ndarray
            Grid of the simulation
        x_grid_camera, y_grid_camera : float
            Grid of the camera pixels
        pixel_size_x, pixel_size_y : float
            Size of the pixels in the x and y direction
        psf : ndarray
            The function for the detection psf

        Returns:
        --------
        dBdy : ndarray
            Value of the derivative of the background term to y
        """
        pass

    def derive_background_to_z(self):
        """
        Derives the pattern dependent background term with respect to z-position of the emitter

        Parameters:
        -----------
        illumination_pattern : ndarray
            The funciton for the illumination pattern
        x_grid, y_grid : ndarray
            Grid of the simulation
        x_grid_camera, y_grid_camera : float
            Grid of the camera pixels
        pixel_size_x, pixel_size_y : float
            Size of the pixels in the x and y direction
        psf : ndarray
            The function for the detection psf

        Returns:
        --------
        dBdz : ndarray
            Value of the derivative of the background term to z
        """
        pass
