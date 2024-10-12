from typing import Dict, Union
from ..interfaces.color_swatch import ColorSwatch

class RGBStrategy(ColorSwatch):
    """
    RGBStrategy stores the red, green, and blue components as values between 0 and 255 (inclusive).
    Reference: https://www.w3.org/TR/css-color-3/#rgb-color
    """
    def __init__(self, name: str, red: int, green: int, blue: int):
        """
        Initialize the RGBStrategy.
        """
        super().__init__(name)
         
        self.type = "rgb"
        
        self._red = self.validate_rgb_value(red)
        self._green = self.validate_rgb_value(green)
        self._blue = self.validate_rgb_value(blue)
           
    def to_dict(self) -> Dict[str, Union[int, str]]:
        """
        Convert the color swatch to an object.
        """
        return {
            "type": self.type,
            "name": self.name,
            "red": self._red,
            "green": self._green,
            "blue": self._blue
        }
