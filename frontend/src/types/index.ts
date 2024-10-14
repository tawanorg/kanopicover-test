export interface ColorSwatch extends Record<string, number | string> {
  name: string;
  type: string;
  color: string;
}
  
export interface ColorSwatchContextInterface {
  colorSwatches: ColorSwatch[];
  setColorSwatches: (colorSwatches: ColorSwatch[]) => void;
}
 