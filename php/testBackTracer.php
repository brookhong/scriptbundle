<?php
require_once "./BackTracer.php";
// test section
//require_once "/home/httpd/zhong/BackTracer.php";
//php_trace("/home/httpd/zhong/php_trace.log",array(1));
//
//require_once "/home/httpd/zhong/BackTracer.php";
//php_log("/home/httpd/zhong/php_trace.log",array(__LINE__));
class A 
{
	function c($p){
		echo $p."\n";
		php_trace("php://stdout",array(1,3), array($p));
		php_trace("./php_trace.log");
	}
}

function a($p) {
	b($p);
}

$a = new A();
function b($p) {
	global $a;
	$a->c($p);
}

a("abc", $a);

?>
