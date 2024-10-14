import { useContext } from "react";
 
import { ColorSwatchContextInterface } from "../../../types";
import { ColorSwatchesContext } from "../context";

const useColorSwatches = (): ColorSwatchContextInterface => {
  const context = useContext(ColorSwatchesContext);
  if (!context) {
    throw new Error(
      "useColorSwatches must be used within a ColorSwatchesProvider"
    );
  }
  return context;
};
 
export default useColorSwatches;