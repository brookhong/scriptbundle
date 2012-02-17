<?php

$filename = "mynotepad.txt";

if($_POST){
	$contents = $_POST['notepad'];
	file_put_contents($filename, $contents);
}


if($contents = file_get_contents($filename)){
	$notepad = $contents;
}
else{
	$notepad = "";
}



echo "<form action='".$PHP_SELF."' method='post'>\n";
echo "<textarea name='notepad' cols='120' rows='42'>";
echo $notepad;
echo "</textarea><br />\n";
echo "<input type='submit' value='submit' />";
echo "</form>";

?>
