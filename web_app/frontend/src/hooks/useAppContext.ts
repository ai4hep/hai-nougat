import { useContext } from 'react';
import AppContext from '../contexts/AppContext';
import { AppContextValue } from '../types/app.types';

export const useAppContext = (): AppContextValue => {
  const context = useContext(AppContext);
  if (!context) {
    throw new Error('useAppContext must be used within AppProvider');
  }
  return context;
};
