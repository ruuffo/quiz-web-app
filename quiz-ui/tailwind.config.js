/** @type {import('tailwindcss').Config} */

const plugin = require("tailwindcss/plugin");
module.exports = {
  purge: { content: ["./src/**/*.{vue,js,ts,jsx,tsx,html}"] },
  content: [],
  theme: {
    container: { center: true },
    extend: {
      colors: {
        primary: "#FF00FF",
      },
      textShadow: {
        sm: "0 1px 2px var(--tw-shadow-color)",
        DEFAULT: "0 2px 4px var(--tw-shadow-color)",
        lg: "0 8px 16px var(--tw-shadow-color)",
        none: "none",
      },
      fontFamily: {
        body: ["Anuphan"],
        question: ["Montserrat"],
      },
      backgroundImage: {
        "gif-pattern": "url('./src/assets/spirited-away-funny.gif')",
      },
    },
    plugins: [
      require("tailwindcss"),
      require("autoprefixer"),
      plugin(function ({ matchUtilities, theme }) {
        matchUtilities(
          {
            "text-shadow": (value) => ({
              textShadow: value,
            }),
          },
          { values: theme("textShadow") }
        );
      }),
    ],
  },
};
