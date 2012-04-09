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
function php_log($varList = array(), $logFile = "", $level = 0)
{
	ob_start();
	if(count($varList)) {
		print "===========================\$varList==========================\n";
		$tmp = debug_backtrace();
		print "logged at {$tmp[$level]['file']}:{$tmp[$level]['line']}\n";
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
//else
	//php_log(array($_SERVER['REQUEST_URI'], "BackTracer.php included"), "");
function php_tick(){
	$backtrace = debug_backtrace();
	$line = $backtrace[0]['line'] - 1;
	$file = $backtrace[0]['file'];

	if ($file == __FILE__) return;

	static $fp, $cur, $buf;
	if (!isset($fp[$file])) {
		$fp[$file] = fopen($file, 'r');
		$cur[$file] = 0;
	}

	if (isset($buf[$file][$line])) {
		$code = $buf[$file][$line];
	} else {
		do {
			$code = fgets($fp[$file]);
			$buf[$file][$cur[$file]] = $code;
		} while (++$cur[$file] <= $line);
	}

	$line++;
	$trace = "$file:$line\n$code";
	$logFile = dirname(__FILE__)."/php_trace.log";
	file_put_contents($logFile,$trace,FILE_APPEND); 
}
//declare(ticks=1);
//register_tick_function("php_tick");
function mock_mysql_query($q, $link = NULL) {
	php_log(array($q),"", 2);
	return mysql_query_original($q, $link);
}
if (!function_exists('mysql_query_original')) {
	runkit_function_copy('mysql_query', 'mysql_query_original');
	//runkit_function_redefine('mysql_query', '$q','php_log(array($q),"", 1);return mysql_query_original($q);');
	//runkit_function_redefine('mysql_query', '$q, $link','php_log(array($q),"", 1);return mysql_query_original($q, $link);');
	runkit_function_redefine('mysql_query', '$q','return mock_mysql_query($q);');
	runkit_function_redefine('mysql_query', '$q, $link','return mock_mysql_query($q,$link);');
}
?>
