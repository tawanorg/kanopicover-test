import pytest
from modules.swatches.src.strategies.rgb_strategy import RGBStrategy
from modules.swatches.src.strategies.hsl_strategy import HSLStrategy
from modules.swatches.src.strategies.brgb_strategy import BRGBStrategy
from modules.swatches.src.strategies.hex_strategy import HexStrategy
# Test for invalid name
@pytest.mark.parametrize("name", ["", None])
def test_invalid_swatch_name(name):
    with pytest.raises(ValueError, match="Name cannot be empty"):
        RGBStrategy(name, red=0, green=0, blue=0)
        
@pytest.mark.parametrize("name", ["Valid Name"])
def test_valid_swatch_name(name):
    rgb_strategy = RGBStrategy(name, red=0, green=0, blue=0)
    assert rgb_strategy.name == name

# Parameterized test for valid RGB values
@pytest.mark.parametrize("name, red, green, blue, expected", [
    ("White", 255, 255, 255, {"type": "rgb", "name": "White", "red": 255, "green": 255, "blue": 255, "color": "rgb(255, 255, 255)"}),
    ("Black", 0, 0, 0, {"type": "rgb", "name": "Black", "red": 0, "green": 0, "blue": 0, "color": "rgb(0, 0, 0)"}),
])
def test_rgb_swatch_valid_values(name, red, green, blue, expected):
    rgb_swatch = RGBStrategy(name, red=red, green=green, blue=blue)
    assert rgb_swatch.to_dict() == expected
    assert rgb_swatch.to_color() == f"rgb({red}, {green}, {blue})"

# Parameterized test for invalid RGB values
@pytest.mark.parametrize("name, red, green, blue, error_message", [
    ("Invalid Red", 256, 0, 0, "RGB values must be between 0 and 255"),
    ("Invalid Red", -1, 0, 0, "RGB values must be between 0 and 255"),
    ("Invalid Green", 0, 256, 0, "RGB values must be between 0 and 255"),
    ("Invalid Green", 0, -1, 0, "RGB values must be between 0 and 255"),
    ("Invalid Blue", 0, 0, 256, "RGB values must be between 0 and 255"),
    ("Invalid Blue", 0, 0, -1, "RGB values must be between 0 and 255"),
])
def test_rgb_swatch_invalid_values(name, red, green, blue, error_message):
    with pytest.raises(ValueError, match=error_message):
        RGBStrategy(name, red=red, green=green, blue=blue)

# Parameterized test for valid HSL values
@pytest.mark.parametrize("name, hue, saturation, lightness, expected", [
    ("Red", 0, 100, 50, {"type": "hsl", "name": "Red", "hue": 0, "saturation": 100, "lightness": 50, "color": "hsl(0, 100%, 50%)"}),
    ("Green", 120, 100, 50, {"type": "hsl", "name": "Green", "hue": 120, "saturation": 100, "lightness": 50, "color": "hsl(120, 100%, 50%)"}),
])
def test_hsl_swatch_valid_values(name, hue, saturation, lightness, expected):
    hsl_swatch = HSLStrategy(name, hue=hue, saturation=saturation, lightness=lightness)
    assert hsl_swatch.to_dict() == expected
    assert hsl_swatch.to_color() == f"hsl({hue}, {saturation}%, {lightness}%)"

# Parameterized test for invalid HSL values
@pytest.mark.parametrize("name, hue, saturation, lightness, error_message", [
    ("Invalid Hue", 361, 50, 50, "Hue must be between 0 and 360"),
    ("Invalid Hue", -1, 50, 50, "Hue must be between 0 and 360"),
    ("Invalid Saturation", 180, 101, 50, "Saturation and Lightness must be between 0 and 100"),
    ("Invalid Saturation", 180, -1, 50, "Saturation and Lightness must be between 0 and 100"),
    ("Invalid Lightness", 180, 50, 101, "Saturation and Lightness must be between 0 and 100"),
    ("Invalid Lightness", 180, 50, -1, "Saturation and Lightness must be between 0 and 100"),
])
def test_hsl_swatch_invalid_values(name, hue, saturation, lightness, error_message):
    with pytest.raises(ValueError, match=error_message):
        HSLStrategy(name, hue=hue, saturation=saturation, lightness=lightness)

# Parameterized test for valid BRGB values
@pytest.mark.parametrize("name, red, green, blue, expected", [
    ("Bright Red", 10000, 0, 0, {"type": "brgb", "name": "Bright Red", "red": 10000, "green": 0, "blue": 0, "color": "rgb(10000, 0, 0)"}),
    ("Dark Green", 0, 10000, 0, {"type": "brgb", "name": "Dark Green", "red": 0, "green": 10000, "blue": 0, "color": "rgb(0, 10000, 0)"}),
])
def test_brgb_swatch_valid_values(name, red, green, blue, expected):
    brgb_swatch = BRGBStrategy(name, red=red, green=green, blue=blue)
    assert brgb_swatch.to_dict() == expected
    assert brgb_swatch.to_color() == f"rgb({red}, {green}, {blue})"

# Parameterized test for invalid BRGB values
@pytest.mark.parametrize("name, red, green, blue, error_message", [
    ("Invalid Red", 10001, 0, 0, "BRGB values must be between 0 and 10000"),
    ("Invalid Red", -1, 0, 0, "BRGB values must be between 0 and 10000"),
    ("Invalid Green", 0, 10001, 0, "BRGB values must be between 0 and 10000"),
    ("Invalid Green", 0, -1, 0, "BRGB values must be between 0 and 10000"),
    ("Invalid Blue", 0, 0, 10001, "BRGB values must be between 0 and 10000"),
    ("Invalid Blue", 0, 0, -1, "BRGB values must be between 0 and 10000"),
])
def test_brgb_swatch_invalid_values(name, red, green, blue, error_message):
    with pytest.raises(ValueError, match=error_message):
        BRGBStrategy(name, blue=blue, green=green, red=red)
        

# Parameterized test for valid Hex Strategy values
@pytest.mark.parametrize("name, hex_value, expected", [
    ("SuperRed", "#FF0000", {"type": "hex", "name": "SuperRed", "hex": "#FF0000", "color": "#FF0000"}),
    ("SuperGreen", "#00FF00", {"type": "hex", "name": "SuperGreen", "hex": "#00FF00", "color": "#00FF00"}),
])
def test_hex_strategy_valid_values(name, hex_value, expected):
    hex_swatch = HexStrategy(name, hex_value=hex_value)
    assert hex_swatch.to_dict() == expected
    assert hex_swatch.to_color() == hex_value
    
# Parameterized test for invalid Hex Strategy values
@pytest.mark.parametrize("name, hex_value, error_message", [
    ("Invalid Hex", "FF0000", "Hex value must start with '#'"), 
])
def test_hex_strategy_invalid_values(name, hex_value, error_message):
    with pytest.raises(ValueError, match=error_message):
        HexStrategy(name, hex_value=hex_value)
