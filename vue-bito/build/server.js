const path = require("path");

//引入：json-server模块
const jsonServer = require("json-server");
//用jsonserver创建服务对象
const server = jsonServer.create();
//创建路由
const router = jsonServer.router(path.join("mock", "db.json"));
//定义中间件
const middlewares = jsonServer.defaults();

//nodejs的思路，每次请求服务器是，都会执行middlewares中间件
server.use(middlewares);
// 为了操作 POST, PUT 和 PATCH 需要使用 body-parser
// server.use(jsonServer.bodyParser)
server.use((req, res, next) => {
  req.method = "GET";
  next();
})
// Add this before server.use(router)
let routes = require('../mock/routes')
server.use(jsonServer.rewriter(routes))
//路由，会根据请求，找对应的数据，如：books或者readers
server.use(router);
//启动服务器
server.listen(3000,()=>{
    console.log("JSON Server is running");
});
