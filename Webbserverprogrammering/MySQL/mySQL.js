let mysql = require("mysql2")

let connection = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "MySQLDatabas123",
    database: "schema",

});

connection.connect(function(err) {
    if (err) throw err;
   let sql = "INSERT INTO elever (namn, KlassID) VALUES ('Kalle', 1)";
    connection.query(sql, function (err, result) {
         if (err) throw err;
         console.log("Elev tillagd i databasen");
    });
});