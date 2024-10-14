import pytest
from modules.swatches.src.interfaces.color_swatch import ColorSwatch
from modules.swatches.src.repositories.swatch_repository import SwatchRepository

# Fixture for the Swatch Repository
@pytest.fixture
def swatches():
    return SwatchRepository()

class GenericColorSwatch(ColorSwatch):
    def __init__(self, name: str, swatch_type: str, properties: dict):
        super().__init__(name)
        self.type = swatch_type
        self._properties = properties
    
    def to_color(self):
        return self._properties.get("color")
    
    def to_dict(self):
        return {"name": self.name, "type": self.type, **self._properties}

def test_swatch_repository_operations(swatches):
    # Test adding and retrieving swatches
    rgb_swatch = GenericColorSwatch("white", "rgb", {"red": 255, "green": 255, "blue": 255, "color": "rgb(255, 255, 255)"})
    hsl_swatch = GenericColorSwatch("blue", "hsl", {"hue": 240, "saturation": 100, "lightness": 50, "color": "hsl(240, 100%, 50%)"})
    
    swatches.add_swatch(rgb_swatch)
    swatches.add_swatch(hsl_swatch)
    
    assert swatches.get_swatch_by_name("white") == rgb_swatch
    assert swatches.get_swatch_by_name("blue") == hsl_swatch
    assert swatches.get_swatch_by_name("nonexistent") is None
    
    assert len(swatches.get_swatches_by_type("rgb")) == 1
    assert len(swatches.get_swatches_by_type("hsl")) == 1
    
    # Test removing a swatch
    swatches.remove_swatch("white")
    assert len(swatches.get_swatches()) == 1
    
    # Test dynamic color space
    custom_swatch = GenericColorSwatch("custom", "custom", {"custom_property": "custom_value"})
    swatches.add_swatch(custom_swatch)
    
    assert len(swatches.get_swatches()) == 2
    assert swatches.get_swatch_by_name("custom") == custom_swatch
    assert swatches.get_swatches_by_type("custom") == [custom_swatch]
