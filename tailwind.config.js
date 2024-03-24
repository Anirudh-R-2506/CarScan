/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        primary: "#f3f3f3",
        secondary: "#151517",
        tertiary: "#898990",
        accent: "#cbfb45",
      },
    },
    fontFamily: {
      sans: ["EverettLight", "Helvetica Neue", "Helvetica", "sans-serif"],
    }
  },
}
