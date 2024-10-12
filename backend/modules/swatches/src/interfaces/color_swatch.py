from typing import Dict, Union
from abc import ABC, abstractmethod

class ColorSwatch(ABC):
    """
    ColorSwatch is an abstract class that defines the structure for a color swatch.
    """
    
    def __init__(self, name: str):
        if not name:
            raise ValueError("Name cannot be empty or None")
         
        self.name = name

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        self._type = value

    @abstractmethod
    def to_dict(self) -> Dict[str, Union[int, str]]:
        """
        Convert the color swatch to a dictionary.
        """
        raise NotImplementedError("Subclasses must implement this method")
     
    @staticmethod
    def validate_rgb_value(value: int) -> int:
        """
        Validate the RGB value.
        RGB values must be in the range 0-255.
        Reference: https://www.w3.org/TR/css-color-3/#rgb-color
        """
        if not (0 <= value <= 255):
            raise ValueError("RGB values must be between 0 and 255")
        return value
    
    @staticmethod
    def validate_hue_value(value: int) -> int:
        """
        Validate the hue value.
        Hue values must be in the range 0-360.
        Reference: https://www.w3.org/TR/css-color-3/#hsl-color
        """
        if not (0 <= value <= 360):
            raise ValueError("Hue must be between 0 and 360")
        return value

    @staticmethod
    def validate_saturation_lightness_value(value: int) -> int:
        """
        Validate the saturation or lightness value.
        Saturation and Lightness must be in the range 0-100.
        Reference: https://www.w3.org/TR/css-color-3/#hsl-color
        """
        if not (0 <= value <= 100):
            raise ValueError("Saturation and Lightness must be between 0 and 100")
        return value
    
    @staticmethod
    def validate_brgb_value(value: int) -> int:
        """
        Validate the BRGB value.
        BRGB values must be in the range 0-10000.
        Reference: https://doc.clickup.com/p/h/2jfty-17782/74e5fb4127316d9
        """
        if not (0 <= value <= 10000):
            raise ValueError("BRGB values must be between 0 and 10000")
        return value
 