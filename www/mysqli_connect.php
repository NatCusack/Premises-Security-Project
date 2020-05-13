<?php
DEFINE ('DB_USER', 'anpr');
DEFINE ('DB_PASSWORD', 'root');
DEFINE ('DB_HOST', '192.168.1.2');
DEFINE ('DB_NAME', 'psp');

$dbc = @mysqli_connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
OR die('Could not connect to MySQL Database'.
		mysqli_connect_error());
?>
