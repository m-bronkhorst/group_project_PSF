import numpy as np
from simulation_params_module import Setup, Object, Camera


class IlluminationPattern:

    def __new__(cls, setup: Setup, obj: Object, cam: Camera, pattern_type: str = "", **kwargs):
        """
        Overridden __new__ method to allow for runtime subclass selection based on the "pattern_type" parameter. Note that the
        variable "pattern_type" will be automatically added to the kwargs and passed to the __init__ of child classes.
        :param pattern_type: str, pattern_type name eg: Widefield, Donut, ...
        :param kwargs: other keyword arguments to pass to child class.
        """
        subclass_map = {subclass.__name__.lower(
        ): subclass for subclass in cls.__subclasses__()}

        # If there are no subclasses avoid the rest of the code.
        # This allows us to instantiate child classes without having to specify hardware_pattern_type argument.
        if not subclass_map and cls != IlluminationPattern:
            return super(IlluminationPattern, cls).__new__(cls)

        # better error handling for readability. KeyError is not descriptive here.
        try:
            subclass = subclass_map[pattern_type.lower()]
        except KeyError:
            raise RuntimeError(
                f"pattern_type not recognised. Got {pattern_type}. Available pattern_types {list(subclass_map.keys())}.")

        # once we find a subclass we can instantiate it.
        return super(IlluminationPattern, subclass).__new__(subclass)

    def __init__(self, setup: Setup, obj: Object, cam: Camera, **kwargs):
        self.setup = setup
        self.obj = obj
        self.camera = cam

    def compute_illumination(self):
        raise NotImplementedError()

    def derive_illumination_to_x(self):
        raise NotImplementedError()

    def derive_illumination_to_y(self):
        raise NotImplementedError()

    def derive_illumination_to_z(self):
        raise NotImplementedError()


class Widefield(IlluminationPattern):
    """
    Class to generate widefield illumination pattern and its partial derivatives with respect to the emitter parameters

    Parameters:
    -----------
    setup : class
        Parameters related to the setup
    object : class
        Parameters related to the object, i.e. the emitters
    camera : class
        Parameters related to the camera

    """

    def __init__(self, setup: Setup, obj: Object, cam: Camera, *args, **kwargs):
        super().__init__(setup, obj, cam, **kwargs)

    def compute_illumination(self):
        """
        Computes the (unitless) intensity of the illumination pattern in 2 dimensions

        Parameters:
        -----------

        Returns:
        --------
        pattern : ndarray
            The unitless intensity of a 2D widefield illumination pattern that illuminates the entire field of view
        """
        pass

    def derive_illumination_to_x(self):
        """
        Derives the unitless intensity of a 2D widefield illumination pattern that illuminates the entire field of
        view with respect to the x-position of the emitter
        Parameters:
        -----------

        Returns:
        --------
       dPdx : ndarray
            The derivative of the unitless intensity of a 2D widefield illumination pattern that illuminates the entire
            field of view to x
        """
        pass

    def derive_illumination_to_y(self):
        """
        Derives the unitless intensity of a 2D widefield illumination pattern that illuminates the entire field of view
        with respect to the y-position of the emitter
        Parameters:
        -----------

        Returns:
        --------
        dPdy : ndarray
            The derivative of the unitless intensity of a 2D widefield illumination pattern that illuminates the entire
            field of view to y
        """
        pass

    def derive_illumination_to_z(self):
        """
        Derives the unitless intensity of a 2D widefield illumination pattern that illuminates the entire field of view
        with respect to the z-position of the emitter
        Parameters:
        -----------

        Returns:
        --------
        dIdz : ndarray
            The derivative of the unitless intensity of a 2D widefield illumination pattern that illuminates the entire
            field of view to z
        """
        pass


class DonutIllumination(IlluminationPattern):
    """
    Class to generate a donut illumination pattern

    Parameters:
    -----------
    setup : class
        Parameters related to the setup
    object : class
        Parameters related to the object, i.e. the emitters
    camera : class
        Parameters related to the camera

    """

    def __init__(self, setup: Setup, obj: Object, cam: Camera, *args, **kwargs):
        super().__init__(setup, obj, cam, **kwargs)

    def compute_illumination(self):
        """
        Computes the (unitless) intensity of a 2D donut shaped illumination pattern in 2 dimensions

        Parameters:
        -----------
        x_center_donut : float
            x-coordinate of the center of the donut
        y_center_donut : float
            y-coordinate of the center of the donut
        sigma_illum : float
            The standard deviation describing the spatial spread of the illumination pattern

        Returns:
        --------
        donut_pattern : ndarray
            The unitless intensity of a 2D donut shaped illumination pattern centered at
            (x_center_donut, y_center_donut)
        """
        pass

    def derive_illumination_to_x(self):
        """
        Derives the unitless intensity of a 2D donut shaped illumination pattern centered at
        (x_center_donut, y_center_donut) to the x-position of the emitter

        Parameters:
        -----------
        x_center_donut : float
            x-coordinate of the center of the donut
        y_center_donut : float
            y-coordinate of the center of the donut
        sigma_illum : float
            The standard deviation describing the spatial spread of the illumination pattern

        Returns:
        --------
        dIdx : ndarray
            The derivative of the unitless intensity of a 2D donut shaped illumination pattern centered at (x_p, y_p)
            to x
        """
        pass

    def derive_illumination_to_y(self):
        """
        Derives the unitless intensity of a 2D donut shaped illumination pattern centered at
        (x_center_donut, y_center_donut) to the y-position of the emitter

        Parameters:
        -----------
        x_center_donut : float
            x-coordinate of the center of the donut
        y_center_donut : float
            y-coordinate of the center of the donut
        sigma_illum : float
            The standard deviation describing the spatial spread of the illumination pattern

        Returns:
        --------
        dIdy : ndarray
            The derivative of the unitless intensity of a 2D donut shaped illumination pattern centered at
            (x_center_donut, y_center_donut) to y
        """
        pass

    def derive_illumination_to_z(self):
        """
        Derives the unitless intensity of a 2D donut shaped illumination pattern centered at
        (x_center_donut, y_center_donut) to the z-position of the emitter

        Parameters:
        -----------
        x_center_donut : float
            x-coordinate of the center of the donut
        y_center_donut : float
            y-coordinate of the center of the donut
        sigma_illum : float
            The standard deviation describing the spatial spread of the illumination pattern

        Returns:
        --------
        dIdz: ndarray
            The derivative of the unitless intensity of a 2D donut shaped illumination pattern centered at
            (x_center_donut, y_center_donut) to z
        """
        pass


class InclinedGaussian(IlluminationPattern):
    """
    Class to generate an inclined Gaussian illumination pattern

    Parameters:
    -----------
    setup : class
        Parameters related to the setup
    object : class
        Parameters related to the object, i.e. the emitters
    camera : class
        Parameters related to the camera

    """

    def __init__(self, setup: Setup, obj: Object, cam: Camera, *args, **kwargs):
        super().__init__(setup, obj, cam, **kwargs)

    def compute_illumination(self):
        """
        Computes the (unitless) intensity of an inclined Gaussian illumination pattern in 3 dimensions

        Parameters:
        -----------
        x_center_pattern: float
            x-coordinate of the center of the illumination pattern
        z_center_pattern : float
            z-coordinate of the center of the illumination pattern
        N_OIL : float
            Refractive index of the immersion oil
        N_MEDIUM : float
            Refractive index of the medium/sample
        NA_OBJ : float
            Numerical aperture of the objective lens
        NA_LS : float
            Numerical aperture of the light-sheet
        lambda_excitation : float
            Wavelength of the (excitation) light of the illumination pattern

        Returns:
        --------
        pattern : ndarray
            The unitless intensity of a 3D inclined Gaussian light-sheet centered at
            (x_center_pattern, z_center_pattern)
        """
        # x, z =
        # X, Z = np.meshgrid(x, z)
        # r_gau, z_gau = rotate_xz(X, Z, N_OIL, N_MEDIUM, NA_OBJ, NA_LS)

        # w0 =
        # zR =

        # P = ... waist_gaussian
        pass

    def derive_illumination_to_x(self):
        """
        Derives the unitless intensity of an inclined Gaussian illumination pattern centered at
        (x_center_pattern, z_center_pattern) to the x-position of the emitter

        Parameters:
        -----------
        x_center_pattern: float
            x-coordinate of the center of the illumination pattern
        z_center_pattern : float
            z-coordinate of the center of the illumination pattern
        N_OIL : float
            Refractive index of the immersion oil
        N_MEDIUM : float
            Refractive index of the medium/sample
        NA_OBJ : float
            Numerical aperture of the objective lens
        NA_LS : float
            Numerical aperture of the light-sheet
        lambda_excitation : float
            Wavelength of the (excitation) light of the illumination pattern

        Returns:
        --------
        dIdz: ndarray
            The derivative of the unitless intensity of an inclined Gaussian illumination pattern centered at
            (x_center_pattern, z_center_pattern) to x
        """
        pass

    def derive_illumination_to_y(self):
        """
        Derives the unitless intensity of an inclined Gaussian illumination pattern centered at
        (x_center_pattern, z_center_pattern) to the y-position of the emitter

        Parameters:
        -----------
        x_center_pattern: float
            x-coordinate of the center of the illumination pattern
        z_center_pattern : float
            z-coordinate of the center of the illumination pattern
        N_OIL : float
            Refractive index of the immersion oil
        N_MEDIUM : float
            Refractive index of the medium/sample
        NA_OBJ : float
            Numerical aperture of the objective lens
        NA_LS : float
            Numerical aperture of the light-sheet
        lambda_excitation : float
            Wavelength of the (excitation) light of the illumination pattern

        Returns
        -------
        dIdz: float
            The derivative of the unitless intensity of an inclined Gaussian illumination pattern centered at (x_p, z_p) to y
        """
        pass

    def derive_illumination_to_z(self):
        """
        Derives the unitless intensity of an inclined Gaussian illumination pattern centered at
        (x_center_pattern, z_center_pattern) to the z-position of the emitter

        Parameters:
        -----------
        x_center_pattern: float
            x-coordinate of the center of the illumination pattern
        z_center_pattern : float
            z-coordinate of the center of the illumination pattern
        N_OIL : float
            Refractive index of the immersion oil
        N_MEDIUM : float
            Refractive index of the medium/sample
        NA_OBJ : float
            Numerical aperture of the objective lens
        NA_LS : float
            Numerical aperture of the light-sheet
        lambda_excitation : float
            Wavelength of the (excitation) light of the illumination pattern

        Returns:
        --------
        dIdz: float
            The derivative of the unitless intensity of an inclined Gaussian illumination pattern centered at
            (x_center_pattern, z_center_pattern) to z
        """
        pass

    def rotate_xz(self, x, z, N_OIL, N_MEDIUM, NA_OBJ, NA_LS):
        """
        Rotates the x and z coordinates to r_gau and z_gau

        Parameters;
        -----------
        x_center_pattern : float
            x-coordinate of the center of the ilumination pattern
        z_center_pattern : float
            z-coordinate of the center of the illumination pattern
        N_OIL : float
            Refractive index of the immersion oil
        N_MEDIUM : float
            Refractive index of the medium (sample)
        NA_OBJ : float
            Numerical aperture of the objective lens
        NA_LS : float
            Numerical aperture of the light-sheet

        Returns:
        --------
        r_gau : np.ndarray
            The r_gau coordinates
        z_gau : np.ndarray
            The z_gau coordinates
        """
        # theta =
        # r_gau =
        # z_gau =
        pass

    def compute_waist_gaussian(self, z_gau, zR, w0):
        """
        Computes the waist of a Gaussian beam

        Parameters:
        -----------
        z_gau : float
            The z_gau coordinates
        zR : float
            The Rayleigh range
        w0 : float
            The minimum of the waist of the Gaussian beam

        Returns:
        --------
        waist : float
            The waist of the Gaussian beam
        """
        # w =
        pass


class SOLEIL(InclinedGaussian):
    """
    Class to generate SOLEIL illumination where the illumination pattern is scanned through the sample

    Parameters:
    -----------
    setup : class
        Parameters related to the setup
    object : class
        Parameters related to the object, i.e. the emitters
    camera : class
        Parameters related to the camera


    """

    def __init__(self, setup: Setup, obj: Object, cam: Camera, *args, **kwargs):
        super().__init__(setup, obj, cam, **kwargs)

    def compute_illumination(self):
        """
        Computes the (unitless) intensity of a SOLEIL illumination pattern in 3 dimensions

        Parameters:
        -----------

        Returns:
        --------
        pattern : ndarray
            The unitless intensity of a 3D SOLEIL illumination pattern
        """

        # TODO: how to call the method of a parent class without calling the same method of the base class
        # function_value = np.sum(super().compute_illumination(positions))
        pass

    def derive_illumination_to_x(self):
        """
        Computes the derivative of the SOLEIL illumination pattern with respect to the x-position of the emitter

        Parameters:
        -----------

        Returns:
        --------
        dIdx : ndarray
            The derivative of the unitless intensity of a 3D SOLEIL illumination pattern to x
        """
        pass

    def derive_illumination_to_y(self):
        """
        Computes the derivative of the SOLEIL illumination pattern with respect to y-position of the emitter

        Parameters:
        -----------

        Returns:
        --------
        dIdy : ndarray
            The derivative of the unitless intensity of a 3D SOLEIL illumination pattern to y
        """
        pass

    def derive_illumination_to_z(self):
        """
        Computes the derivative of the SOLEIL illumination pattern with respect to z-position of the emitter

        Parameters:
        -----------

        Returns:
        --------
        dIdz : ndarray
            The derivative of the unitless intensity of a 3D SOLEIL illumination pattern to z
        """
        pass
