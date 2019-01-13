<?php 

#CONNECTION CODE
$host = 'localhost';
$user = 'root';
$pass = '';
$db = 'project1';
 #MAIN CODE
$con = mysqli_connect($host,$user, $pass , $db)  or die(mysqli_error($con));

if ( $con)
{
	echo "Connection established successfully.<br>";
}
 ?>
