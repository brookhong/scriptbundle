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
		if(isset($a['object'])) {
			var_dump($a['object']);
		}
		var_dump($a['args']);
	}
	$i++;
}
function php_trace($logFile, $showArgs = array(), $varList = array()) {
	ob_start();
	print "\n================traced at ".strftime('%Y-%m-%d %H:%M:%S')."================\n";
	if(count($varList)) {
		print "---------------------------\$varList--------------------------\n";
		foreach ($varList as $value) {
			var_dump($value);
		}
		print "-------------------------end of \$varList---------------------\n";
	}
	$tmp = debug_backtrace();
	array_walk($tmp,'traceFunction', $showArgs);
	print "\n==================end of php_trace outputs:==================\n";
	$trace = ob_get_contents();
	ob_end_clean();
	file_put_contents($logFile,$trace,FILE_APPEND); 
}
if ('cli' === php_sapi_name() && basename(__FILE__) === $argv[0])
	php_trace("php://stdout",array(0));
?>
