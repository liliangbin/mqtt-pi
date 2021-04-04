const path = require('path')

function resolve(dir) {
    return path.join(__dirname, dir)
}

module.exports = {
    publicPath: './',
    devServer: {
        // can be overwritten by process.env.HOST
        host: '0.0.0.0',
        port: 8080,
        proxy: {
            '/api': {
                target: 'http://localhost:8083',
                changeOrigin: true,
                pathRewrite: {
                    '^/api': '/'
                }
            },
            '/socket.io': {
                target: 'http://localhost:8083', // target host
                changeOrigin: true, // needed for virtual hosted sites
                logLevel: 'debug'
            }
        }
    },
    chainWebpack: config => {
        config.resolve.alias
            .set('@', resolve('src'))
            .set('src', resolve('src'))
            .set('common', resolve('src/common'))
            .set('components', resolve('src/components'))
            .set('static', resolve('public'))
    },
    pluginOptions: {}
}
