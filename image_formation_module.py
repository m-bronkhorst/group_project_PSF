import numpy as np
import matplotlib.pyplot as plt
from simulation_params_module import Object, Setup, Camera
from illumination_pattern_module import IlluminationPattern
from background_module import Background
from blinking_module import BlinkingEmitters


class ImageFormation:
    """
    Class to generate the expected image. It also generates the expected photon count for each pixel,
     together with its partial derivatives with respect to the emitter parameters.

    Parameters:
    -----------
    setup: dataclass
        Parameters related to the setup
    object: dataclass
        Parameters related to the object, i.e. the emitters
    camera: dataclass
        Parameters related to the camera
    PSF: class
        Parameters related to the PSF class
    IlluminationPattern: class
        Generates the illumination pattern
    Background: class
        Generates the pattern-dependent background
    BlinkingEmitters: class
        Generates the intensity of the emitters over time
    """

    def __init__(self, setup: Setup, obj: Object, cam: Camera, PSF, illumination_pattern, effective_background, blinking):
        self.setup = setup
        self.object = obj
        self.camera = cam
        self.PSF = PSF
        self.illumination_pattern = illumination_pattern
        self.effective_background = effective_background
        self.blinking = blinking

    def compute_photons_per_pixel(self, theta=None):
        """
        Computes the expected photon count per pixel

        Parameters:
        -----------
        illumination : ndarray
            Illumination pattern
        x_grid, y_grid : ndarray
            Grid of the simulation
        x_grid_camera, y_grid_camera : ndarray
            Grid of the camera pixels
        psf : ndarray
            The PSF from the different general PSF model
        setup_background : ndarray
            The effective background
        emitter_intensity :ndarray
            Photon budget of the emitter
        background_intensity : ndarray
            The expected pattern-dependent background count

        Returns:
        --------
        photons_per_pixel : ndarray
            The expected photon count for each pixel
        """

        # if theta is None:
        #     xemit = self.object.xemit
        #     yemit = self.object.yemit
        #     zemit = self.object.zemit
        #     intensity = self.object.emitter_intensity
        #     background = self.object.background_intensity
        # else:
        #     xemit, yemit, zemit, intensity, background = theta
        #
        # psf = self.PSF.compute_psf(xemit=xemit, yemit=yemit)

        pass

    def derive_expected_photons_to_x(self):
        """
        Computes the derivative of the expected photon count per pixel with respect to the x-position of the emitter

        Parameters:
        -----------

        Returns:
        --------
        dmu_dx : ndarray
            The derivative of the expected photon count with respect to x
        """
        pass

    def derive_expected_photons_to_y(self):
        """
        Computes the derivative of the expected photon count with respect to the y-position of the emitter


        Returns:
        --------
        dmu_dy : ndarray
            The derivative of the expected photon count with respect to y
        """
        pass

    def derive_expected_photons_to_z(self):
        """
        Computes the derivative of the expected photon count with respect to the z-position of the emitter

        Returns:
        --------
        dmu_dz : ndarray
            The derivative of the expected photon count with respect to z
        """
        pass

    def derive_expected_photons_to_intensity(self):
        """
       Computes the derivative of the expected photon count with respect to the emitter intensity

        Returns:
        --------
        dmu_dI : ndarray
            The derivative of the expected photon count with respect to the emitter intensity
        """
        pass

    def derive_expected_photons_to_background(self):
        """
       Computes the derivative of the expected photon count with respect to the effective background intensity

        Returns:
        --------
        dmu_dbg : ndarray
            The derivative of the expected photon count with respect to the background intensity
        """
        pass

    def compute_image(self):
        """
        Computes the noisy image expected on the detector by adding Poisson noise to the expected photon count

        Returns:
        --------
        image : ndarray
            The noisy image expected on the detector
        """
        pass
