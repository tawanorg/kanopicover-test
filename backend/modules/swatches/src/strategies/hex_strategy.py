from ..interfaces.color_swatch import ColorSwatch
from typing import Dict, Union

class HexStrategy(ColorSwatch):
    """
    HexStrategy class for representing a Hex color swatch. It is simple #RRGGBB format.
    Reference: https://en.wikipedia.org/wiki/Web_colors#Hex_triplet
    """
    def __init__(self, name: str, hex_value: str):
        super().__init__(name)
        
        self.type = "hex"
        self._hex_value = self.validate_hex_value(hex_value)
        
    @staticmethod
    def validate_hex_value(hex_value: str) -> str:
        """
        Validate the hex value.
        Hex value must start with '#'.
        """
        if not hex_value.startswith("#"):
            raise ValueError("Hex value must start with '#'")
        return hex_value

    def to_dict(self) -> Dict[str, Union[str, int]]:
        return {
            "type": self.type, 
            "name": self.name, 
            "hex": self._hex_value
        }
