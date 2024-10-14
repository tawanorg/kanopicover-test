 
import { apiClient } from "../../../client";
import { ColorSwatch } from "../../../types";
 
export const randomColorSwatches = async (): Promise<ColorSwatch[]> => {
  const { data } = await apiClient.get('/swatches/random');
  return data;
};

export const getColorSwatches = async (): Promise<ColorSwatch[]> => {
  const { data } = await apiClient.get('/swatches');
  return data;
};
