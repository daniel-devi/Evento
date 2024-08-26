import { createContext, useContext, useMemo, useState } from "react";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";

// This context will provide a way to toggle color mode across the app
const ColorModeContext = createContext({
  toggleColorMode: () => {},
});

// Custom hook to access the color mode context
export const useColorMode = () => {
  // Use the ColorModeContext and return its value
  // This line was missing the return statement, which has been added
  return useContext(ColorModeContext);
};

// ColorModeProvider component to manage and provide color mode
type ColorModeProviderProps = {
  children: React.ReactNode;
};

export function ColorModeProvider({ children }: ColorModeProviderProps) {
  const systemTheme: string | null = localStorage.getItem("colorMode");
  // State to hold the current color mode
  const [mode, setMode] = useState(systemTheme ? systemTheme : "light");

  // Memoized color mode object with toggle function
  const colorMode = useMemo(
    () => ({
      toggleColorMode: () => {
        const newTheme = mode === "light" ? "dark" : "light";
        localStorage.setItem("colorMode", newTheme);

        setMode(newTheme);
      },
    }),
    [mode]
  );

  // Memoized theme object based on the current mode
  const theme = useMemo(
    () =>
      createTheme({
        palette: {
          mode: mode === "dark" ? "dark" : "light",
          primary: {
            main: mode === "dark" ? "#4c1d95" : "#6d28d9",
          },
          background: {
            default: mode === "dark" ? "#1f2937" : "#f3f4f6",
          },
          text: {
            primary: mode === "dark" ? "#f3f4f6" : "#1f2937",
          },
        },
      }),
    [mode]
  );
  // Provide the color mode context and theme to children components
  return (
    <ColorModeContext.Provider value={colorMode}>
      <CssBaseline />
      <ThemeProvider theme={theme}>{children}</ThemeProvider>
    </ColorModeContext.Provider>
  );
}
