/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: 'jit',
  content: ['./app/templates/**/*.html.jinja'],
  theme: {
      extend: {
          fontFamily: {
              source: ['"FiraSans"', "sans-serif"],
            //   bold: ['"Sans Bold"', "sans-serif"]
          },
      }
  },
  plugins: [],
}

