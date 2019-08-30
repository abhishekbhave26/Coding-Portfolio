//setting up the server to handle the requests

const http=require("http");
const url=require("url");

const handlers={};

handlers.newbs= (res)=>{
    res.end('Hello newbs route');
};

handlers.notFound= (res)=>{
    res.writeHead(404);
    res.end('Route does not exist');
};

const router={
    'newbs':handlers.newbs
};

const server=http.createServer((req,res) => {
    
    const parsedReq={};
    parsedReq.parsedUrl=url.parse(req.url,true);
    parsedReq.path=parsedReq.parsedUrl.pathname;
    parsedReq.trimmedPath=parsedReq.path.replace(/^\/+|\/+$/g,'');
    parsedReq.method=req.method.toLowerCase();
    parsedReq.headers=req.headers;
    parsedReq.queryStringObject=parsedReq.parsedUrl.query;

    let body=[];

    req.on('data',(chunk)=>{
        body.push(chunk);
    });

    req.on('end',()=>{
        body=Buffer.concat(body).toString();
        parsedReq.body=body;
        
        const routedHandler=typeof(router[parsedReq.trimmedPath]) !=='undefined' ? router[parsedReq.trimmedPath]:handlers.notFound;
        routedHandler(res)
    });

});

server.listen(3000,()=>console.log("Listening on port 3000"));


    