<?php
require_once "./BackTracer.php";
// test section
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
