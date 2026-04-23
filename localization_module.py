import numpy as np
from scipy.optimize import minimize
from simulation_params_module import Object, Setup, Camera


class EmitterLocalization:
    """
    Class for fitting the emitter localization model to the observed noisy image.
    """

    def __init__(self, image_formation):
        self.image_formation = image_formation

    def negative_log_likelihood(self, theta, img):
        """
        Computes the chi-squared negative log-likelihood function for the given parameters by forming an
        expected photon count and comparing it to the observed noisy image.

        Parameters:
        -----------
        theta: ndarray
            The emitter parameters (e.g., positions and intens
        mu: ndarray
            The expected photon count per pixel (mu)
        img: ndarray
            The observed noisy image


        Returns:
        --------
        chi_squared: float
            The negative log-likelihood
        """
        # mu = self.image_formation.compute_expected_photon_count(theta)
        # return 2 * (np.sum(mu - img) - np.sum(img[img > 0] * np.log(mu[img > 0] / img[img > 0])))
        pass

    def Levenberg_Marquardt(self):
        """
        Levenberg-Marquardt algorithm for minimizing the negative log-likelihood.

        Parameters:
        -----------
        initial_value: ndarray
            Initial guess for the emitter parameters (e.g., positions and intensities).

        Returns:
        --------
        fitted_parameters: ndarray
            The fitted parameters
        """
        pass

    def fit_to_image(self, initial_value, img, method='L-BFGS-B'):
        """
        Fits the emitter localization model to the observed noisy image by minimizing the
        negative log-likelihood.

        Parameters:
        -----------
        initial_value: ndarray
            Initial guess for the emitter parameters (e.g., positions and intensities).

        Returns:
        --------
        theta: ndarray
            The fitted emitter parameters
        """
        # result = minimize(
        #     fun=self.negative_log_likelihood,
        #     x0=initial_value,
        #     args=(img,),
        #     method=method,
        #     options={"disp": True}
        # )
        pass
