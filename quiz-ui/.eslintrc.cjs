/* eslint-env node */
module.exports = {
  plugins: ["tailwindcss"],
  root: true,
  extends: [
    "plugin:vue/vue3-essential",
    "eslint:recommended",
    "plugin:tailwindcss/recommended",
  ],
  parserOptions: {
    ecmaVersion: "latest",
  },
};
