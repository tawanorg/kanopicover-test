 
import React from 'react';
import { ColorSwatch, ColorSwatchContextInterface } from '../../../types';

export const ColorSwatchesContext = React.createContext<ColorSwatchContextInterface>({
    colorSwatches: [],                  
    setColorSwatches: (colorSwatches: ColorSwatch[]) => {}
});