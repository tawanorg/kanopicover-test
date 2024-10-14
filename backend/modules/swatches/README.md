## Swatches

This module is responsible for generating and managing color swatches.

## Folder Structure

```
.
├── modules
│   ├── swatches
│   │   ├── README.md
│   │   ├── src
│   │   │   ├── __init__.py
│   │   │   ├── controllers # Flask blueprint -- controllers for the API
│   │   │   ├── interfaces # Interfaces -- define the interface for the color swatch
│   │   │   ├── repositories # Repositories -- use repository pattern to get data from data sources
│   │   │   ├── strategies # Strategies -- color space strategies
│   │   │   └── tests # Unit tests
│   └── __init__.py
```


## How to add new color swatch 
  
Follow TDD approach: You should add the new strategy to test cases first. Then add the new strategy to the code.

1. Add the new strategy to test cases in `tests/test_swatches_strategies.py`.
 
```python
@pytest.mark.parametrize("name, hex_value, expected", [
    ("SuperRed", "#FF0000", {"type": "hex", "name": "SuperRed", "hex": "#FF0000", "color": "#FF0000}),
    ("SuperGreen", "#00FF00", {"type": "hex", "name": "SuperGreen", "hex": "#00FF00", "color": "#00FF00"}),
])
def test_hex_strategy_valid_values(name, hex_value, expected):
    hex_swatch = HexStrategy(name, hex_value=hex_value)
    assert hex_swatch.to_dict() == expected
```

2. Create new color swatch strategy class in `src/strategies` folder. eg `hex_strategy.py`

```python
class HexStrategy(ColorSwatch):
    """
    A class representing a Hex color swatch.
    """
    def __init__(self, name: str, hex_value: str):
        super().__init__(name)
        
        self.type = "hex"
        self._hex_value = hex_value

    def to_color(self) -> str:
        return self._hex_value
    
    def to_dict(self) -> Dict[str, Union[str, int]]:
        return {
            "type": self.type, 
            "name": self.name, 
            "hex": self._hex_value,
            "color": self.to_color()
        }
```

3. If you want user to able to regenerate swatches then add new strategy to `src/controllers/swatch_controller.py`
