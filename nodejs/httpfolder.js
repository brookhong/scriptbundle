var express = require('express')
  , path = process.argv[2] || __dirname
  , app = express();

app.configure(function() {
  var hourMs = 1000*60*60;
  app.use(express.static(path, { maxAge: hourMs }));
  app.use(express.directory(path));
  app.use(express.errorHandler());
});

app.listen(8080);
console.log("Folder " + path + " is shared at http://localhost:8080\n");
