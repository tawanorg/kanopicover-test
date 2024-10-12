from typing import List, Dict, Union, Optional
from ..interfaces.color_swatch import ColorSwatch
 
class SwatchRepository:
    """
    SwatchRepository is a repository of ColorSwatch objects.
    """
    
    @property
    def types(self) -> List[str]:
        """
        Get all types of swatches.
        """
        return list(set([swatch.type for swatch in self._swatches]))
  
    def __init__(self):
        self._swatches: List[ColorSwatch] = []
          
    def add_swatch(self, swatch: ColorSwatch) -> None:
        """
        Add a swatch to the collection.
        """
        self._swatches.append(swatch)

    def get_swatches(self) -> List[Dict[str, Union[int, str]]]:
        """
        Get all swatches.
        """
        return [swatch.to_dict() for swatch in self._swatches]
    
    def remove_swatch(self, name: str) -> None:
        """
        Remove a swatch by name.
        """
        self._swatches = [swatch for swatch in self._swatches if swatch.name != name]

    def get_swatch_by_name(self, name: str) -> Optional[ColorSwatch]:
        """
        Get a swatch by name.
        """
        return next((swatch for swatch in self._swatches if swatch.name == name), None)

    def get_swatches_by_type(self, type: str) -> List[ColorSwatch]:
        """
        Get all swatches by type.
        """
        return [swatch for swatch in self._swatches if swatch.type == type]