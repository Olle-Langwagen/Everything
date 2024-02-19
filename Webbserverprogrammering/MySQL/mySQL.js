let mysql = require("mysql2")

let connection = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "password",
    database: "schema",

});

connection.connect(function(err) {
    if (err) throw err;
    console.log("Ansluten till databasen");
});