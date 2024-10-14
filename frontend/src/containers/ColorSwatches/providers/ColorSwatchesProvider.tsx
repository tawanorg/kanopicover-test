import { useQuery } from '@tanstack/react-query';
import React, { useEffect, useState } from 'react';
import { Loader } from '../../../design';
import { ColorSwatch, ColorSwatchContextInterface } from '../../../types';
import { Api } from '../api';
import { ColorSwatchesContext } from '../context';

const ColorSwatchesProvider: React.FC<React.PropsWithChildren<{}>> = ({ children }) => {
  const [colorSwatches, setColorSwatches] = useState<ColorSwatch[]>([]);

  const { data, isLoading, error } = useQuery({
    queryKey: ['colorSwatches'],
    queryFn: Api.getColorSwatches,
  });

  const updateColorSwatches = (data: ColorSwatch[]) => {
    setColorSwatches(data);
  };

  useEffect(() => {
    if (data) {
      setColorSwatches(data);
    }
  }, [data]);

  const value: ColorSwatchContextInterface = {
    colorSwatches,
    setColorSwatches: updateColorSwatches,
  };

  if (isLoading) {
    return <Loader />;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <ColorSwatchesContext.Provider value={value}>
      {children}
    </ColorSwatchesContext.Provider>
  );
};

export default ColorSwatchesProvider;