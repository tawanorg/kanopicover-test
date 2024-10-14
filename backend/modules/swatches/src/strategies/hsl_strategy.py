from typing import Dict, Union
from ..interfaces.color_swatch import ColorSwatch

class HSLStrategy(ColorSwatch):
    """
    HSLStrategy stores the hue, saturation, and lightness components as values between 0 and 360 (hue) and 0 and 100 (saturation and lightness).
    Reference: https://www.w3.org/TR/css-color-3/#hsl-color
    """
    def __init__(self, name: str, hue: int, saturation: int, lightness: int): 
        """
        Initialize the HSLStrategy.
        """
        super().__init__(name)
        
        self.type = "hsl"
        self._hue = self.validate_hue_value(hue)
        self._saturation = self.validate_saturation_lightness_value(saturation)
        self._lightness = self.validate_saturation_lightness_value(lightness)
        
    def to_color(self) -> str:
        return f"hsl({self._hue}, {self._saturation}%, {self._lightness}%)"
         
    def to_dict(self) -> Dict[str, Union[int, str]]:
        """
        Convert the color swatch to an object.
        """
        return {
            "type": self.type,
            "name": self.name,
            "hue": self._hue,
            "saturation": self._saturation,
            "lightness": self._lightness,
            "color": self.to_color()
        }
     