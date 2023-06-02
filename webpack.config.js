const path = require('path');

module.exports = {
  entry: {
    index: './assets/index.js',
    profile: './assets/profile.js',
    login: './assets/login.js',
    navbar: './assets/navbar.js'
  },
  
  output: {
    filename: '[name]-bundle.js',  // output bundle file name
    path: path.resolve(__dirname, './static/js'),  // path to our Django static directory
  },

  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        loader: "babel-loader",
        options: { presets: ["@babel/preset-env", "@babel/preset-react"] }
      },
    ]
  }
};