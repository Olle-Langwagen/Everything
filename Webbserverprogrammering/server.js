const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const http = require('http').Server(app);
const io = require("socket.io")(http);

const mongoose = require('mongoose');

app.use(express.static('./webbsidan'));

app.use(bodyParser.urlencoded({ extended: false }));

//password
const dbUrl = "mongodb+srv://ollelangwagen:MongoDB2020@cluster0.zvrisxo.mongodb.net/?retryWrites=true&w=majority"

let Messege = mongoose.model("Message", {
    name: String,
    message: String
});

let messages = [
    {name: "Kalle", message: "Hej!"},
    {name: "Pelle", message: "Hej då!"}
];

app.get("/meddelanden", (req, res) => {
    res.send(messages);
});

app.post("/meddelanden", (req, res) => {
    let messege = new Messege(req.body);
    messege.save()
    .then(item => {
        io.emit("message", req.body);
        
    })
    .catch(err => {
        res.status(500).send("Kunde inte spara till databasen");
    });
});

io.on("connection", (socket) => {
    console.log("Användare anslöt");
});

try {
    mongoose.connect(dbUrl);
    console.log("Ansluten till databasen MongoDB");
}
catch(error) {
    console.log(error);
}

http.listen(3000, () => {
    console.log('Servern är igång, besök den på http://localhost:3000');
});