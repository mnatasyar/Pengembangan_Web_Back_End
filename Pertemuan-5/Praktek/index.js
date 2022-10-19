const http = require('http');
const fs = require('fs');
const hostname = '127.0.0.1';
const port = 8081;

const server = http.createServer((req,res) => {
    res.statusCode = 200;
    res.setHeader("Content-Type","text/html");
    const data = fs.readFileSync("index.html");
    res.end(data)

    res.write("<p>Simple Text</p>");
});

server.listen(port,hostname, () =>{
    console.log(`Server running at ${hostname}:${port}`);
});