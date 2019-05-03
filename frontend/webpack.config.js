const HtmlWebPackPlugin = require("html-webpack-plugin");

module.exports = {
    module:{
        rules:[
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                loader:"babel-loader"
            },
            {
                test: /\.html$/,
                loader:"html-loader"
            },
            {
                test: /\.css$/,
                use:["style-loader","css-loader"]
            },
            // {
            //     test: /\.(jpg|png|svg)$/,
            //     loader: 'url-loader',
            //     options: {
            //         name: '[hash].[ext]',
            //         limit: 10000,
            //     },
            // },
            {
                test: /\.(jpg|png|svg)$/,
                loader: 'file-loader',
                options: {
                  name: '[path][name].[hash].[ext]',
                },
            }
        ]
    },
    plugins:[
        new HtmlWebPackPlugin({
            template: "./src/template/index.html",
            filename: "./index.html"
        })
    ],
    devServer: {
        inline: true,
        port: 3000,
        historyApiFallback: true
    },
}