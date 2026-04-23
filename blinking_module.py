import numpy as np
from simulation_params_module import Setup, Object, Camera


class BlinkingEmitters:
    """
    Class to simulate the blinking of the emitters over time. 
    Here, the blinking is the variation in intensity of fluorescence.
    """

    def __init__(self, setup: Setup, obj: Object, cam: Camera):
        self.setup = setup
        self.obj = obj
        self.cam = cam

    def get_emitter_intensities(self):
        """
        Generates the intensity of the emitters over time (frames).
        The blinking is modeled by a Markov chain with two states: ON and OFF.

        Returns:
        --------
        intensity : ndarray
            The computed intensity of all emitters over time (num_emitters, num_frames).
        """
        pass
