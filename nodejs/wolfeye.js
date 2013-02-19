var express = require('express')
  , path = process.argv[2] || __dirname
  , app = express();
var path = path.replace(/\\/g,'/');
if(path[path.length-1] != '/'){
  path += '/';
}

function getLastName(p) {
  var tmp = /.*\/([^\/]*)\//.exec(p);
  return tmp[1];
}
app.configure(function() {
  var hourMs = 1000*60*60;
  app.use('/static',express.static(path, { maxAge: hourMs }));
  app.use('/static',express.directory(path));
  app.use('/static',express.errorHandler());
  app.use(express.static(__dirname + '/public'));
  app.set('views', __dirname + '/views');
  app.set('view engine', 'jade');
});
app.get('/random', function(req, res){
  var id = Math.round(Math.random()*files.length);
  res.render('random', { file: '/static/'+files[id]});
});
app.get('/ordered', function(req, res){
  res.render('ordered', { file: '/static/'+files[0]});
});
app.get('/', function(req, res){
  res.send("<li><a href='/static'>"+getLastName(path)+"</a><li><a href='/ordered'>ordered</a><li><a href='/random'>random</a>");
});

app.listen(8080);
console.log("Folder " + path + " is shared at http://localhost:8080\n");

var walk    = require('walk');
var files   = [];
var walker  = walk.walk(path, { followLinks: false });
walker.on('file', function(root, stat, next) {
    var rp = root.replace(path,"");
    files.push(rp+'/'+stat.name);
    next();
});
