<?php
/**
 * 
 */
define('PHP_TRACE_INI',"/home/httpd/zhong/php_trace.ini");
//define('PHP_TRACE_LOG',"/home/httpd/zhong/php_trace.log");
define('PHP_TRACE_LOG',"php://stdout");
$show_args = array();
if(file_exists(PHP_TRACE_INI)) {
	$ini_array = parse_ini_file(PHP_TRACE_INI);
	$GLOBALS['show_args'] = explode(",",$ini_array['show_args']);
}
function traceFunction($a,$flag) {
	static $i=0;
	global $show_args;
	print "#{$i} ";
	if(isset($a['class'])) {
		print "{$a['class']}->";
	}
	print "{$a['function']}() called at [{$a['file']}:{$a['line']}]\n";

	if(in_array($i,$show_args)) {
		var_dump($a['args']);
	}
	$i++;
}
function php_trace() {
	ob_start();
	array_walk(debug_backtrace(),'traceFunction');
	$trace = ob_get_contents();
	ob_end_clean();
	file_put_contents(PHP_TRACE_LOG,$trace); 
}


// test section
class A 
{
	function c($p){
		echo $p."\n";
		php_trace();
	}
}

function a($p) {
	b($p);
}

function b($p) {
	$a = new A();
	$a->c($p);
}

a("abc");

?>
