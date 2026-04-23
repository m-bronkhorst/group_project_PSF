import numpy as np
from simulation_params_module import Setup, Object, Camera
from scipy.special import erf


class PSF:
    """
    Base PSF class
    """

    def __new__(cls, setup: Setup, obj: Object, cam: Camera, psf_model: str = "", **kwargs):
        """
        Overridden __new__ method to allow for runtime subclass selection based on the "psf_model" parameter. Note that the
        variable "model_type" will be automatically added to the kwargs and passed to the __init__ of child classes.
        :param pattern_type: str, psf_model name eg: Gaussian, Vectorial, ...
        :param kwargs: other keyword arguments to pass to child class.
        """
        subclass_map = {subclass.__name__.lower(
        ): subclass for subclass in cls.__subclasses__()}

        # If there are no subclasses avoid the rest of the code.
        # This allows us to instantiate child classes without having to specify psf_model argument.
        if not subclass_map:
            return super(PSF, cls).__new__(cls)

        # better error handling for readability. KeyError is not descriptive here.
        try:
            subclass = subclass_map[psf_model.lower()]
        except KeyError:
            raise RuntimeError(
                f"psf_model not recognised. Got {psf_model}. Available psf_model {list(subclass_map.keys())}.")

        # once we find a subclass we can instantiate it.
        return super(PSF, subclass).__new__(subclass)

    def __init__(self, setup: Setup, obj: Object, cam: Camera, **kwargs):
        self.setup = setup
        self.obj = obj
        self.camera = cam

    def compute_psf(self):
        raise NotImplementedError()


class GaussianPSF(PSF):
    """
    Gaussian PSF model that computes the 2D Gaussian PSF. The class also computes the intermediate terms
    useful to compute derivatives of the expected photon count with respect to the emitter parameters.
    """

    def __init__(self, setup: Setup, obj: Object, cam: Camera, *args, **kwargs):
        super().__init__(setup, obj, cam, **kwargs)

    def compute_psf(self):
        """
        Computes the 2D Gaussian PSF and its derivatives.
        The PSF is integrated over pixel areas using error functions, and partial derivatives of the PSF
        are also calculated.

        Returns:
        --------
        psf : ndarray
            The computed 2D Gaussian PSF of shape (num_emitters, grid_size, grid_size).
        """

        pass

    def compute_DeltaEx(self):
        """
        Computes the Integrated x-component of the PSF with the use of error functions

        Returns:
        --------
        DeltaEx : ndarray
            Integrated x-component of the PSF, shape (num_emitters, grid_size, grid_size).
        """
        pass

    def compute_DeltaEy(self):
        """
        Computes the Integrated y-component of the PSF with the use of error functions

        Returns:
        --------
        DeltaEy : ndarray
            Integrated y-component of the PSF, shape (num_emitters, grid_size, grid_size).
        """
        pass

    def compute_dEx(self):
        """
            Computes the intermediate term used to compute partial derivative of the expected
             pixel count with respect to theta_x,

        Returns:
        --------
        dEx : ndarray
            Term used to compute partial derivative of the PSF with respect to theta_x,
            shape (num_emitters, grid_size, grid_size).
        """
        pass

    def compute_dEy(self):
        """
            Computes the intermediate term used to compute partial derivative of the expected
             pixel count with respect to theta_y,

        Returns:
        --------
        dEx : ndarray
            Term used to compute partial derivative of the PSF with respect to theta_y,
            shape (num_emitters, grid_size, grid_size).
        """
        pass


class GaussAstigPSF(GaussianPSF):
    """
    Astigmatic Gaussian PSF model that computes the 2D Gaussian PSF with astigmatism along the z-axis. The class
    also computes the intermediate terms useful to compute derivatives of the expected photon count with respect
    to the emitter parameters.
    """

    def __init__(self, setup: Setup, obj: Object, cam: Camera, *args, **kwargs):
        super().__init__(setup, obj, cam, **kwargs)

    def compute_psf(self):
        """
        Computes the Gaussian Astigmatic PSF and its derivatives.
        The PSF is integrated over pixel areas using error functions
         and partial derivatives of the PSF are also calculated.

        Returns:
        --------
        psf : ndarray
            The computed 2D Gaussian PSF of shape (num_emitters, grid_size, grid_size).
        """
        pass

    def compute_DeltaEx(self):
        """
        Computes the Integrated x-component of the PSF with the use of error functions

        Returns:
        --------
        DeltaEx : ndarray
            Integrated x-component of the PSF, shape (num_emitters, grid_size, grid_size).
        """
        pass

    def compute_DeltaEy(self):
        """
        Computes the Integrated y-component of the PSF with the use of error functions

        Returns:
        --------
        DeltaEy : ndarray
            Integrated y-component of the PSF, shape (num_emitters, grid_size, grid_size).
        """
        pass

    def compute_dEx(self):
        """
            Computes the intermediate term used to compute partial derivative of the expected
             pixel count with respect to theta_x,

        Returns:
        --------
        dEx : ndarray
            Term used to compute partial derivative of the PSF with respect to theta_x,
            shape (num_emitters, grid_size, grid_size).
        """
        pass

    def compute_dEy(self):
        """
            Computes the intermediate term used to compute partial derivative of the expected
             pixel count with respect to theta_y,

        Returns:
        --------
        dEx : ndarray
            Term used to compute partial derivative of the PSF with respect to theta_y,
            shape (num_emitters, grid_size, grid_size).
        """
        pass


class VectorialPSF(PSF):
    """
    Vectorial PSF model class
    """

    def __init__(self, setup: Setup, obj: Object, cam: Camera, **kwargs):
        super().__init__(setup, obj, cam, **kwargs)

    def compute_pupil_matrix(self):
        """
        Computes the electric field components in the pupil plane.
        This field incorporates s- and p-polarization components, Fresnel coefficients
        for multiple interfaces, and amplitude factors due to refractive index mismatches.

        Returns
        -------
        pupil_matrix : ndarray
            The electric field in the pupil plane of shape (Npupil, Npupil, 2, 3)
        aperture_mask : ndarray,
            of shape (Npupil, Npupil)
        wavevector : ndarray,
            Wavevector of shape (Npupil, Npupil, 3)
        wavevectorzimm : ndarray
            Wavevector of shape (Npupil, Npupil)
        """
        pass

    def compute_elec_field(self):
        """
        Compute the electric field in the image plane for an emitter at a given position.This is done
        by a 2D Chirp-Z Transform (CZT) to propagate the field from the pupil to the image plane.

        Returns
        -------
        elec_field : ndarray, shape (Mx, My, 2, 3)
            The complex electric field in the image plane, with 2 polarization components
            (s- and p-polarization) and 3 vector components (x, y, z).
        """
        pass

    def compute_psf(self, elec_field):
        """
        Compute the intensity PSF from the electric field.
        The PSF is obtained by summing the squared magnitudes of the electric field
        components over all polarization and vectorial dimensions. The PSF is normalized
        and averaged over the dipole orientations.

        Parameters
        ----------
        elec_field : ndarray, shape (Mx, My, 2, 3)
            The complex electric field in the image plane, with 2 polarization components
            (s- and p-polarization) and 3 vector components (x, y, z).

        Returns
        -------
        psf : ndarray, shape (Mx, My)
            The computed PSF intensity, normalized by the total power (w_n) and averaged
            over dipole orientation and summed over the polarization and vector channels.
        """
        pass


class SplinePSF(PSF):
    """
    Spline PSF model class
    """

    def __init__(self, setup: Setup, obj: Object, cam: Camera, **kwargs):
        super().__init__(setup, obj, cam, **kwargs)

    def compute_psf(self):
        """
        Compute the Spline PSF using the spline coefficients

        Returns:
        --------
            psf: ndarray
                The computed PSF.
        """
        pass
