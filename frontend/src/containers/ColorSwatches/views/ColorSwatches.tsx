
 
import { Loader } from "../../../design";
import useColorSwatches from '../hooks/useColorSwatches';
import useRandomColorSwatch from '../hooks/useRandomColorSwatch';

function ColorSwatches() {
  const [
    getRandomColorSwatch,
    { isPending: isRandomColorSwatchPending, error: randomColorSwatchError },
  ] = useRandomColorSwatch();
  const { colorSwatches } = useColorSwatches();

  if (isRandomColorSwatchPending) {
    return <Loader />;
  }

  if (randomColorSwatchError) {
    return <div>Error: {randomColorSwatchError.message}</div>;
  }

  return (
    <div className="App">
      <ul className="color-swatches-list" data-testid="color-swatches-list">
        {colorSwatches.map((colorSwatch, index) => (
          <li key={index} className="color-swatch-item" data-testid="color-swatch-item">
            <div className="color-swatch-color" style={{ backgroundColor: colorSwatch.color }}>
              <p data-testid="color-swatch-color">{colorSwatch.color}</p>
            </div>
            <div className="color-swatch-name">
              <p data-testid="color-swatch-name">{colorSwatch.name}</p>
            </div>
          </li>
        ))}
      </ul>
      <button
        className="App-link btn btn-primary btn-xl float-button"
        onClick={() => {
          getRandomColorSwatch();
        }}
      >
        {/* Add pointing right emoji */}
        <span role="img" aria-label="pointing right">
          👉
        </span>
        Random Color
      </button> 
    </div>
  );
}



export default ColorSwatches;
