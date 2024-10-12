from typing import Dict, Union
from ..interfaces.color_swatch import ColorSwatch

class BRGBStrategy(ColorSwatch):
    """
    BRGBStrategy stores the red, green, and blue components as values between 0 and 10000 (inclusive).
    Reference: Stage 2 - https://doc.clickup.com/p/h/2jfty-17782/74e5fb4127316d9
    """
    def __init__(self, name: str, blue: int, green: int, red: int):
        """
        Initialize the BRGBStrategy.
        """
        super().__init__(name)

        self.type = "brgb"
        self._blue = self.validate_brgb_value(blue)
        self._green = self.validate_brgb_value(green)
        self._red = self.validate_brgb_value(red)
 
    def to_dict(self) -> Dict[str, Union[int, str]]:
        """
        Convert the color swatch to an object.
        """
        return {
            "type": self.type,
            "name": self.name,
            "red": self._red,
            "green": self._green,
            "blue": self._blue,
        }
  