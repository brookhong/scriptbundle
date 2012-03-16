<?php
/**
 * require_once "/works/scriptbundle/BackTracer.php";
 * function php_trace($showArgs, $logFile);
 * $showArgs -- array to specify whose args are dumped in backtrace
 * $logFile  -- log file path
 * For example here the backtrace will be print out on stdout,
 * and the args of call #0 will be dumped.
 * php_trace(array(0),"php://stdout");
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
function php_trace($showArgs = array(), $logFile = "") {
	ob_start();
	print "\n================traced at ".strftime('%Y-%m-%d %H:%M:%S')."================\n";
	$tmp = debug_backtrace();
	array_walk($tmp,'traceFunction', $showArgs);
	print "\n==================end of php_trace outputs:==================\n";
	$trace = ob_get_contents();
	ob_end_clean();
	if($logFile == "")
		$logFile = dirname(__FILE__)."/php_trace.log";
	file_put_contents($logFile,$trace,FILE_APPEND); 
}
function php_log($varList = array(), $logFile = "")
{
	ob_start();
	if(count($varList)) {
		print "===========================\$varList==========================\n";
		$tmp = debug_backtrace();
		print "logged at {$tmp[0]['file']}:{$tmp[0]['line']}\n";
		foreach ($varList as $value) {
			var_dump($value);
		}
		print "=========================end of \$varList=====================\n";
	}
	$trace = ob_get_contents();
	ob_end_clean();
	if($logFile == "")
		$logFile = dirname(__FILE__)."/php_trace.log";
	file_put_contents($logFile,$trace,FILE_APPEND); 
}
if ('cli' === php_sapi_name() && basename(__FILE__) === $argv[0])
	php_trace(array(0),"php://stdout");
?>
