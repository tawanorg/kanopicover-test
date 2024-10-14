import { useMutation } from "@tanstack/react-query";
import { useEffect } from "react";
 
import { ColorSwatch } from "../../../types";
import { Api } from "../api";
import useColorSwatches from "./useColorSwatches";

/**
 * Hook to get a random color swatch from the API and add it to the color swatches context
 * @example
 * const [getRandomColorSwatch, { data, isPending, error }] = useRandomColorSwatch();
 * return <Button onClick={getRandomColorSwatch}>Get Random Color Swatch</Button>;
 */
const useRandomColorSwatch = (): [
  () => void,
  { data: ColorSwatch[]; isPending: boolean; error: Error | null }
] => {
  const { mutate, data, isPending, error } = useMutation({
    mutationFn: Api.randomColorSwatches,
  });

  const getRandomColorSwatch = () => {
    mutate();
  };

  const { setColorSwatches, colorSwatches } = useColorSwatches();

  useEffect(() => {
    if (data) {
      setColorSwatches(data);
    }
  }, [data]);

  return [getRandomColorSwatch, { data: colorSwatches ?? [], isPending, error }];
};

export default useRandomColorSwatch;