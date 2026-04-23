# simulation_params.py
from dataclasses import dataclass, field
import numpy as np


@dataclass
class Object:
    """
    Parameters related to the object emitter:

    - xemit, yemit, zemit: Arrays representing emitter positions in microns.
    - zstack: Enable/disable z-stacking.
    - zrange: The range of z-stacking in microns.
    - depth: Distance of the object relative to the focal plane.
    - zstage: Z-position of the stage
    - emitter_intensity: The intensity of emitters.
    - background_intensity: The intensity of background noise.
    """
    xemit: np.ndarray
    yemit: np.ndarray
    zemit: np.ndarray = field(default_factory=lambda: np.array([0.0]))
    zstack: bool = False
    zrange: float = 0.0
    depth: float = 0.0
    zstage: float = 0.0
    emitter_intensity: float = 1.0
    background_intensity: float = 1.0


@dataclass
class Camera:
    """
    Parameters related to the camera

    - pixel_size_x, pixel_size_y: The size of the pixels in microns.
    - pixel_count: The number of pixels in the camera.
    - shutter_size_x: The size of the shutter in microns.
    - num_frames: The number of frames to capture.
    """
    pixel_size_x: float
    pixel_size_y: float
    pixel_count: int = 1
    shutter_size_x: int = 1
    num_frames: int = 1
    pass


@dataclass
class Setup:
    """
    Parameters related to the setup

    - grid_size: The size of the grid.
    - pixel_size: The size of the pixels in microns.
    - NA, NA_illum: The numerical aperture of the objective and illumination.
    - Lambda: The wavelength of the light.
    - refmed, refimm, refcov: The refractive index of the medium, immersion, and cover slip.
    - sigma_x, sigma_y, sigma: The standard deviation of the PSF in x, y
    - z_lightsheet: The z-position of the light sheet.
    - calibration: The calibration parameters for the Astigmatic PSF model
    - aberrations: The aberration coefficients to apply to the phase aberration function for the Vectorial PSF model
    """
    grid_size: int
    pixel_size: float = 1.0
    NA: float = 1.0
    NA_illum: float = 1.0
    Lambda: float = 1.0
    refmed: float = 1.0
    refimm: float = 1.0
    refcov: float = 1.0
    sigma_x: float = 1.0
    sigma_y: float = 1.0
    sigma: float = 1.0
    z_lightsheet: float = 0.0
    calibration: np.ndarray = field(
        default_factory=lambda: np.array([
            # sigma0_x, gamma_x, d_x, A_x, B_x
            [1.08, 0.389, 0.531, -0.07081, -0.073],
            # sigma0_y, gamma_y, d_y, A_y, B_y
            [1.01, -0.389, 0.531, 0.164, 0.04017]
        ])
    )
    aberrations: np.ndarray = field(
        default_factory=lambda: np.array([[
            [2, 2, 120]  # shape [batch, Zernike modes, features {n, m, coef}]
        ]])
    )

    def __post_init__(self):
        x = np.linspace(-self.grid_size // 2, self.grid_size //
                        2, self.grid_size)
        y = np.linspace(-self.grid_size // 2, self.grid_size //
                        2, self.grid_size)
        self.simulation_grid = np.meshgrid(x, y)


@dataclass
class Numerical:
    """
    Numerical parameters for the simulation
    """
    # TODO to be determined
