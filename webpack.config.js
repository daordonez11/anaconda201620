//require our dependencies
var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
var ExtractTextPlugin = require("extract-text-webpack-plugin");

var config = module.exports = {
    //the base directory (absolute path) for resolving the entry option
    context: __dirname,
    //the entry point we created earlier. Note that './' means
    //your current directory. You don't have to specify the extension  now,
    //because you will specify extensions later in the `resolve` section
    entry: {
		"main": [
			'./assets/css/main.scss',
			'./assets/js/index.js'
		],
	},

    output: {
        //where you want your compiled bundle to be stored
        path: path.resolve('./assets/bundles/'),
        //naming convention webpack should use for your files
        filename: '[name]-[hash].js', 
    },

    plugins: [
        //tells webpack where to store data about your bundles.
        new BundleTracker({filename: './webpack-stats.json'}),
        //makes jQuery available in every module
        new webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery',
            'window.jQuery': 'jquery'
        }),
        new ExtractTextPlugin("./css/main.css")

    ],

    module: {
        loaders: [
            //a regexp that tells webpack use the following loaders on all
            //.js and .jsx files
            {test: /\.jsx?$/,
                //we definitely don't want babel to transpile all the files in
                //node_modules. That would take a long time.
                exclude: /node_modules/,
                //use the babel loader
                loader: 'babel',
                query: {
                    //specify that we will be dealing with React code
                    presets: ['react','es2015']
                }
            },
            {
				test: /\.scss$/,
				loader: ExtractTextPlugin.extract('style', 'css!sass?indentedSyntax&includePaths[]=' + __dirname +  '/node_modules'),
			},
            {
				test: /\.css$/,
				loader: ExtractTextPlugin.extract("style", "css")
			},
      {
        test: /\.(gif)$/i,
        loaders: [
            'file?hash=sha512&digest=hex&name=[hash].[ext]',
            'image-webpack?bypassOnDebug&optimizationLevel=7&interlaced=false'
        ]
      },
            {
                test: /\.js$/,
                loader: 'babel-loader',
                exclude: /node_modules/,
                query: {
                    presets: ['es2015', 'react']

                }
            },
			{
				test: /\.(woff2|png|svg|jpg)$/,
				loader: "url-loader"
			},
            {
                test   : /\.woff/,
                loader : 'url?prefix=font/&limit=10000&mimetype=application/font-woff'
            }, {
                test   : /\.ttf/,
                loader : 'file?prefix=font/'
            }, {
                test   : /\.eot/,
                loader : 'file?prefix=font/'
            }, {
                test   : /\.svg/,
                loader : 'file?prefix=font/'
            },{
              test: /\.json$/,
              loader: "json-loader"
            }
        ]
    },

    resolve: {
        //tells webpack where to look for modules
        modulesDirectories: ['node_modules'],
        //extensions that should be used to resolve modules
        extensions: ['', '.js', '.jsx','.scss','.css','.ttf','.svg','eot','.jpg','.png']
    }
}

if (process.env.NODE_ENV === 'production') {
  config.plugins.push(
    new webpack.optimize.DedupePlugin(),
    new webpack.optimize.UglifyJsPlugin({ minimize: true })
  );
}
