module.exports = {
  content: [
    "./_drafts/**/*.html",
    "./_includes/**/*.html",
    "./_layouts/**/*.html",
    "./_posts/*.md",
    "./*.md",
    "./*.html",
    "./node_modules/flowbite/**/*.js",
    "./pages/**/*.{html,js}",
  ],
  theme: {
    theme: {
      extend: {},
    },
  },
  plugins: [require("flowbite/plugin")],
};
