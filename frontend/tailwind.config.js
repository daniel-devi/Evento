/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: {
          light: "#6d28d9", // Custom light theme color
          dark: "#4c1d95", // Custom dark theme color
        },
        background: {
          light: "#f3f4f6", // Light mode background
          dark: "#1f2937", // Dark mode background
        },
        text: {
          light: "#1f2937", // Light mode text color
          dark: "#f3f4f6", // Dark mode text color
        },
      },
    },
  },
  plugins: [],
};
