export default {
  server: {
    port: 3000,
    strictPort: true,
  },

  resolve: {
    alias: {
      '@': '/src',
    }
  },
  build: {
    outDir: '../static'
  }
};
