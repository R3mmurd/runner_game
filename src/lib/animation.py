"""
This file contains the implementation of the class Animation.

Author: Alejandro Mujica (aledrums@gmail.com)
"""

from typing import Sequence


class Animation:
    """
    This class represents animations as a sequence of frames. Those
    frames change in a given time interval.
    """

    def __init__(self, frames: Sequence[any], time_interval: float = 0) -> None:
        """
        Initialize a new Animation.

        :param frames: Sequence of frames
        :param time_interval: Duration time (in seconds) of each frame.
        """
        self.__frames: Sequence[any] = frames
        self.__interval: float = time_interval
        self.__size: int = len(self.__frames)
        self.__timer: float = 0
        self.__current_frame_index: int = 0

    def update(self, dt: float) -> None:
        """
        This function updates the animation timer to check whether the frame
        should be changed or not. If the animation has only one frame, then
        this operation does not execute.

        :param dt: Time elapsed (in seconds) since the last time this function has been executed.
        """
        if self.__size <= 1:
            return

        self.__timer += dt

        if self.__timer >= self.__interval:
            self.__timer %= self.__interval
            self.__current_frame_index = (self.__current_frame_index + 1) % self.__size

    def get_current_frame(self) -> any:
        """
        :returns: The current frame of the animation.
        """
        return self.__frames[self.__current_frame_index]
