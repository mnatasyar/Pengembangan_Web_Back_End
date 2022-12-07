import express from 'express';
import { dirname } from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const hostname = 'localhost';
const port = 3000;
const app = express();

app.use(express.static('public'))

app.get("/", (req,res)=> {
    res.sendFile(__dirname+"/public/about.html")
})

const myLog = (req,res,next) => {
    console.log("Params: ", req.params.username, new Date().toLocaleString());
    next();
}

const list_username = ['bunny', 'lola', 'nasa'];

app.get('/:username', myLog, function (req,res,next){
    if ( !list_username.includes(req.params.username.toLowerCase()))
        next('route')
    else
        next()
    }, function (req,res,next) {
        res.sendFile(__dirname+'/public/user.html')
    })

app.get('/:username', function (req, res, next) {
    res.sendFile(__dirname+'/public/unknown.html')
    })

app.listen(port, ()=> {
    console.log(`Server running at ${hostname}:${port}`);
})
