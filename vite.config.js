module.exports = {
  build: {
    outDir: './static/js',
    emptyOutDir: true, // also necessary
    rollupOptions: {
      input: {
        main: "theme/static_src/src/js/main.js",
      },
      output: [
        {
          dir: './static/js',
          // format: 'es',
          entryFileNames: '[name].js'
        },

      ]
    }
  }
}
