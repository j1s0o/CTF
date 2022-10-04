<?php 
class whu{
	public $a;
	function __destruct(){
		echo "destruct start\n";
		echo PHP_VERSION."\n";
	}
	function __wakeup(){
		die("no hack");
	}
}
unserialize('O:3:"whu":2147483647:{s:1:"a";N;}');
?>