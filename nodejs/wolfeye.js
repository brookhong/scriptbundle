var express = require('express')
  , path = process.argv[2] || __dirname
  , app = express();

function getLastName(p) {
  var tmp = /.*\/([^\/]*)\//.exec(p);
  return tmp[1];
}
app.set('views', __dirname);
app.set('view engine', 'jade');
app.configure(function() {
  var hourMs = 1000*60*60;
  app.use('/static',express.static(path, { maxAge: hourMs }));
  app.use('/static',express.directory(path));
  app.use('/static',express.errorHandler());
});
app.get('/random', function(req, res){
  var id = Math.round(Math.random()*files.length);
  res.render('random', { file: '/static/'+files[id]});
});
app.get('/', function(req, res){
  res.send("<li><a href='/random'>random</a><li><a href='/static'>"+getLastName(path)+"</a>");
});

app.listen(8080);
console.log("Folder " + path + " is shared at http://localhost:8080\n");

var walk    = require('walk');
var files   = [];
var walker  = walk.walk(path, { followLinks: false });
walker.on('file', function(root, stat, next) {
    files.push(stat.name);
    next();
});