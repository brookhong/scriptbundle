<?php
/**
 * require_once "/works/scriptbundle/BackTracer.php";
 * function php_trace($logFile, $showArgs);
 * $logFile  -- log file path
 * $showArgs -- array to specify whose args are dumped in backtrace
 * For example here the backtrace will be print out on stdout,
 * and the args of call #0 will be dumped.
 * php_trace("php://stdout",array(0));
 *
 */
function traceFunction($a,$i,$show_args) {
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
function php_trace($logFile, $showArgs) {
	ob_start();
	global $argv;
	print "\n================traced at ".strftime('%Y-%m-%d %H:%M:%S')."================\n";
	print "php_sapi_name: $argv[0] ".php_sapi_name()."\n\n";
	array_walk(debug_backtrace(),'traceFunction', $showArgs);
	print "\n==================end of php_trace outputs:==================\n";
	$trace = ob_get_contents();
	ob_end_clean();
	file_put_contents($logFile,$trace,FILE_APPEND); 
}
if($argv[0] == "BackTracer.php")
	php_trace("php://stdout",array(0));
?>
