
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
            }
        ]
    },
    plugins:[
        new HtmlWebPackPlugin({
            template: "./public/index.html",
            filename: "./index.html"
        })
    ]
};