const {sequelize, authenticate} = require('./models/model.js')
const Genshin = require('./models/genshins.js');
const express = require('express');

const path = require('path');
const http = require('http');
const socketio = require('socket.io');
const formatMessage = require('./utils/messages');
const {
    userJoin,
    getCurrentUser,
    userLeave,
    getRoomUsers
} = require('./utils/users');

const app = express();
// const hostname = '127.0.0.1';
// const port = 347;
const server = http.createServer(app);
const io = socketio(server);

// M. Natasya Ramadana

app.use(express.static('views'))
app.use(express.json());
app.use(express.urlencoded({extended:true}));
app.set('view engine', 'ejs');

// TAMBAHAN : syarat biar gbs asal nambah data kosong
const syaratSupplier = (req, res, next) => {
    if ((req.body.icon.trim() == "") || (req.body.name.trim() == "") || (req.body.weapontype.trim() == "") || (req.body.base.trim() == "") || (req.body.substat.trim() == "") ){
        console.log("Data tidak sesuai format");
        res.json({ status: 400 })
    }
    else {
        next()
    }
}

// biar tabel otomatis terbuat dulu
try {
    authenticate()
    Genshin.sync()
    console.log("Tabel Katalog Genshin berhasil dibuat");
} catch {
    console.error("ERROR!!!!");
}

app.get('/weaponlist', (req,res) => {
    Genshin.findAll().then((results) => {
        res.render('index', { genshins: results })
    })
})

app.get('/create', (req, res) => {
    res.render('create')
})

app.get('/edit/:id', (req, res) => {
    Genshin.findOne({ where: { id: req.params.id } }
    ).then((results) => {
        res.render('edit', { genshin: results });
    })
})

app.post('/api/genshins', syaratSupplier, (req, res, next) => {
    Genshin.create({ 
        icon : req.body.icon, 
        name : req.body.name,
        weapontype : req.body.weapontype,
        base : req.body.base, 
        substat : req.body.substat
    }).then((results) => {
        res.json({ status: 200, error: null, Response: results });
    }).catch(err => {
        res.json({ status: 502, error: err });
    })
})

app.put('/api/genshin/:id', syaratSupplier, (req, res, next) => {
    Genshin.update({ 
        icon : req.body.icon, 
        name : req.body.name,
        weapontype : req.body.weapontype,
        base : req.body.base, 
        substat : req.body.substat
    }, { where: { id: req.params.id } 
    }).then((results) => {
        res.json({ status: 200, error: null, Response: results });
    }).catch(err => {
        res.json({ status: 502, error: err });
    })
})

app.delete('/api/genshin/:id', (req, res) => {
    Genshin.destroy({ where: { id: req.params.id } }
    ).then(() => {
        res.json({ status: 200, error: null, Response: results });
    }).catch(err => {
        res.json({ status: 500, error: err, Response: {} });
    })
})

app.get("/", (req, res) => {
    res.sendFile(__dirname + "/public/homepage.html");
});

app.use(express.static(path.join(__dirname, 'public')));
app.get("/livechat", (req, res) => {
    res.sendFile(__dirname + "/public/index.html");
});

const botName = 'Game Master';
// Run when client connects
io.on('connection', socket => {
    socket.on('joinRoom', ({ username, room }) => {
        const user = userJoin(socket.id, username, room);
        socket.join(user.room);
        // Welcome current user
        socket.emit('message', formatMessage(botName, 'Welcome The Traveler'));
        // Send users and room info
        io.to(user.room).emit('roomUsers', {
            room: user.room,
            users: getRoomUsers(user.room)
        });
        socket.broadcast.emit('message', formatMessage(botName, `${user.username} arive`))
    });
    // Listen for chatMessage
    socket.on('chatMessage', msg => {
        const user = getCurrentUser(socket.id);
        io.to(user.room).emit('message', formatMessage(user.username, msg));

    });
    // Runs when client disconnects
    socket.on('disconnect', () => {
        const user = userLeave(socket.id);
        if (user) {
            // Send users and room info
            io.to(user.room).emit('roomUsers', {
                room: user.room,
                users: getRoomUsers(user.room)
            });
        }
        socket.broadcast.emit('message', formatMessage(botName, `${user.username} Leave`))
    });
});

//Server Port

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => console.log(`Server running on port ${PORT}`));


// app.listen(port, () => {
//     console.log(`Server running at http://${hostname}:${port}`);
// })