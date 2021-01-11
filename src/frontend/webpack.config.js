const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const VueLoaderPlugin = require('vue-loader/lib/plugin');
const {CleanWebpackPlugin} =  require('clean-webpack-plugin')

module.exports = {
  mode: 'production',
  entry: path.resolve(__dirname, './src/main.js'),
  output: {
    path: path.resolve(__dirname, './bundles'),
    filename: 'main.js'
  },

  plugins: [
    new BundleTracker({
      path: __dirname,
      filename: '.webpack-stats.json',
    }),
    new VueLoaderPlugin(),
    new CleanWebpackPlugin(),
  ],

  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
      },
      {
        test: /\.vue$/,
        loader: 'vue-loader',
      },
      {
        test: /.(png|jpg|svg|gif)$/,
        use: ['file-loader']
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader']
      }
    ]
  },

  resolve: {
    extensions: ['.js', '.vue', '.json'],
    alias: {vue: 'vue/dist/vue.js'}
  },

  optimization: {

    // ...
    // Automatically split vendor and commons
    // ...
    splitChunks: {
      chunks: 'async', // from 'all'
      name: true, // from 'false'
    },

    // ...

    runtimeChunk: false //from 'true'

}

};
