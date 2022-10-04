<?php
class Sekai_Game{
    public $start = True;
    public function __destruct(){
        echo "destruct start\n";
		echo PHP_VERSION."\n";
    }
    public function __wakeup(){
        die("no hack");
    }
}
if(isset($_GET['a_b.c'])){
    unserialize($_GET['sekai_game.run']);
}else{
    highlight_file(__FILE__);
}
// a[b.c=0:10:"Sekai_Game":2147483647:{s:5:"start";N;}
// sekai[game.run=C:10:"Sekai_Game":0:{}
?>  