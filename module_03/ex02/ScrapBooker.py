import numpy as np

# (x, y) x => nb lignes, y => nb de colonnes

class ScrapBooker:

    def are_all_int(self, tpl):
        return all(isinstance(el, int) for el in tpl)

    def crop(self, array, dim, position=(0,0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width of the image) from the coordinates given by position arguments.
        Args:
        -----
            array: numpy.ndarray
            dim: tuple of 2 integers.
            position: tuple of 2 integers.
        Return:
        -------
            new_arr: the cropped numpy.ndarray.
            None (if combinaison of parameters not compatible).
        Raise:
        ------
            This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray) or not isinstance(dim, tuple) or not isinstance(position, tuple):
            return None
        if not self.are_all_int(dim) or not self.are_all_int(position):
            return None
        return array[position[0]:dim[0]+1, position[1]:dim[1]]

    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis (0: vertical, 1: horizontal)
        Args:
        -----
            array: numpy.ndarray.
            n: non null positive integer lower than the number of row/column of the array
            (depending of axis value).
            axis: positive non null integer.
        Return:
        -------
            new_arr: thined numpy.ndarray.
            None (if combinaison of parameters not compatible).
        Raise:
        ------
            This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray) or not isinstance(n, int) or n <= 0 or axis not in [0, 1]:
            return None
        n-=1
        new = np.delete(array, n, axis)
        return new

    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
        -----
            array: numpy.ndarray.
            n: positive non null integer.
            axis: integer of value 0 or 1.
        Return:
        -------
            new_arr: juxtaposed numpy.ndarray.
            None (combinaison of parameters not compatible).
        Raises:
        -------
            This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray) or not isinstance(n, int) or n <= 0 or axis not in [0, 1]:
            return None
        if axis == 0:
            return np.tile(array, (n,1))
        if axis == 1:
            return np.tile(array, (1,n))

    def mosaic(self, array, dim):
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetition along each dimensions.
        Args:
        -----
            array: numpy.ndarray.
            dim: tuple of 2 integers.
        Return:
        -------
            new_arr: mosaic numpy.ndarray.
            None (combinaison of parameters not compatible).
        Raises:
        -------
            This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray) or not self.are_all_int(dim):
            return None
        array = self.juxtapose(array, dim[0], 0)
        return self.juxtapose(array, dim[1], 1)