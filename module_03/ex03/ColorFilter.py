import numpy as np
class ColorFilter:

    def invert(self, array):
        """
        Inverts the color of the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        inverted_array = array.copy()
        inverted_array[:, :, :3] = 255 - array[:, :, :3]  # Inverser seulement les trois premiers canaux RGB
        return inverted_array

    def to_blue(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        blue_array = np.zeros_like(array)
        blue_array[:, :, 2] = array[:, :, 2]
        if array.shape[2] == 4:
            blue_array[:, :, 3] = array[:, :, 3]
        return blue_array
    
    def to_green(self, array):
        """
        Applies a green filter to the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        green_array = array.copy()
        green_array[:, :, 0] = array[:, :, 0] * 0
        green_array[:, :, 1] = array[:, :, 1]
        green_array[:, :, 2] = array[:, :, 2] * 0
        return green_array

    def to_red(self, array):
        """
        Applies a red filter to the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        red_array = array.copy()
        green = self.to_green(array)
        blue = self.to_blue(array)
        red_array[:, :, 0] = array[:, :, 0]
        red_array[:, :, 1] = array[:, :, 1] - green[:, :, 1]
        red_array[:, :, 2] = array[:, :, 2] - blue[:, :, 2]
        return red_array

    def to_celluloid(self, array):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
            celluloid filter is also known as cel-shading or toon-shading.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        cel_array = array.copy()
        


    # def to_grayscale(self, array, filter, **kwargs):
    # """
    # Applies a grayscale filter to the image received as a numpy array.
    # For filter = 'mean'/'m': performs the mean of RBG channels.
    # For filter = 'weight'/'w': performs a weighted mean of RBG channels.
    # Args:
    # -----
    #     array: numpy.ndarray corresponding to the image.
    #     filter: string with accepted values in ['m','mean','w','weight']
    #     weights: [kwargs] list of 3 floats where the sum equals to 1,
    #     corresponding to the weights of each RBG channels.
    # Return:
    # -------
    #     array: numpy.ndarray corresponding to the transformed image.
    #     None: otherwise.
    # Raises:
    # -------
    #     This function should not raise any Exception.
    # """