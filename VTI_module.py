import numpy as np
from image_formation_module import ImageFormation
from CRLB_module import CRLB_Calculator


class VTI_Calculator:
    """
    Class for calculating the Van Trees Inequality (VTI) bound for Single Molecule Localization Microscopy (SMLM).

    Parameters:
    ----------
    image_formation: class
        Parameters related to the image formation process
    crlb: class
        Parameters from the CRLB calculation
    """

    def __init__(self, image_formation: ImageFormation, crlb: CRLB_Calculator):
        self.image_formation = image_formation
        self.crlb = crlb

    def compute_prior_information(self):
        """
        Computes the prior information matrix

        Parameters:
        ----------
        CRLB : class
            An instance of the CRLB_Calculator class
        prior : ndarray
            Prior information, comes from CRLB or VTI in (k-1)

        Returns:
        ----------
        prior : ndarray
            Prior information matrix
        """
        pass

    def compute_data_information(self):
        """
        Computes the data information matrix

        Parameters:
        ----------
        CRLB : class
            An instance of the CRLB_Calculator class
        prior : ndarray
            Prior information, comes from CRLB or VTI in (k-1)
        photons_deriv_to_x : ndarray
            Derivative of photon count with respect to x
        photons_deriv_to_y : ndarray
            Derivative of photon count with respect to y
        photons_deriv_to_z : ndarray
            Derivative of photon count with respect to z
        photons_deriv_to_intensity : ndarray
            Derivative of photon count with respect to intensity
        photons_deriv_to_background : ndarray
            Derivative of photon count with respect to background

        Returns:
        ----------
        data_information : ndarray
            Data information matrix
        """
        pass

    def compute_bayesian_fisher_information(self):
        """
        Computes the Bayesian Fisher information matrix

        Parameters:
        ----------
        data_information : ndarray
            Data information matrix
        prior_information : ndarray
            Prior information matrix

        Returns:
        ----------
        bayesian_fisher_information : ndarray
            Bayesian Fisher information matrix
        """
        pass

    def compute_vti(self):
        """
        Computes the VTI bound for the estimated emitter parameters

        Parameters:
        ----------
        bayesian_fisher_information : ndarray
            Bayesian Fisher information matrix

        Returns:
        ----------
        vti : ndarray
            VTI bound for each estimated parameter
        vti_x : ndarray
            VTI bound for x parameter
        vti_y : ndarray
            VTI bound for y parameter
        vti_z : ndarray
            VTI bound for z parameter
        """
        pass
