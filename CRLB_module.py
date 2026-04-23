import numpy as np
from image_formation_module import ImageFormation
from simulation_params_module import Object, Setup, Camera


class CRLB_Calculator:
    """
    Class for calculating the Cramér-Rao Lower Bound (CRLB) for Single Molecule Localization Microscopy (SMLM).

    Parameters:
    -----------
    setup: class
        Parameters related to the setup
    object: class
        Parameters related to the object, i.e. the emitters
    camera: class
        Parameters related to the camera
    PSF: class
        Parameters related to the PSF model

    """

    def __init__(self, setup: Setup, object: Object, camera: Camera, PSF):
        self.setup = setup
        self.object = object
        self.camera = camera
        self.PSF = PSF

    def compute_fisher_information(self):
        """
        Computes the Fisher information matrix

        Parameters:
        -----------
        photons_per_pixel : ndarray
            The expected photon count for each pixel
        derivs: ndarray
            Partial derivatives of the photon count per pixel w.r.t. emitter parameters

        Returns:
        --------
        fisher_information : ndarray
            Fisher information matrix
        """
        pass

    def compute_crlb(self):
        """
        Computes the Cramer-Rao Lower Bound for the estimated parameters

        Parameters:
        -----------
        fisher_information : ndarray
            Fisher information matrix

        Returns:
        --------
        crlb : ndarray
            Cramer-Rao Lower bound for each estimated parameter
        """
        pass
