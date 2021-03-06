<html>
<head>
<style>
body {
  font-size: 28px;
  font-family:arial;
  font-style:bold;

}


ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #7d7d7d;
  position: -webkit-sticky; /* Safari */
  position: sticky;
  top: 0;
}

li {
  float: left;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

li a:hover:not(.active) {
  background-color: #555;
  color: #ffcd42;
}

li a.active {
  background-color: #ffcd42;
  color: white;
}

table {
  width: 100%;
  border: 1px solid black;
  text-align: center;
}


</style>
</head>
<body>

<div class="header">
  <h2>Premises Security System</h2>
</div>

<ul>
  <li><a href="/index.php">Home</a></li>
  <li><a href="/access.php">Access</a></li>
  <li><a class="active" href="/licenceinfo.php">History</a></li>
  <li style="float:right"><a href="/about.php">About</a></li> 
  <li style="float:right"><a href="/contact.php">Contact</a></li> 
</ul>


<?php

require_once('../mysqli_connect.php');

$query = "SELECT licenceplate, accesstime, accessgranted FROM plates";

$response = @mysqli_query($dbc, $query);

if($response){
	echo '<table align="left" cellspacing="5" cellpadding="8">
			<thead>
				<tr>
					<td align="left"><b>Licence Plate</b></td>
					<td align="left"><b>Date</b></td>
					<td align="left"><b>Access</b></td>
				</tr>
			</thead>
			<tbody>';
		
		while($row = mysqli_fetch_array($response)){
			echo '<tr>
					<td align="left">' . $row[licenceplate] . '</td>
					<td align="left">' . $row[accesstime] . '</td>
					<td align="left">' . $row[accessgranted] . '</td>
				</tr>';
		}
		
	echo '</tbody>
	</table>';
	
} else{
	echo "Couldn't issue database query";
	
	echo mysqli_erro($dbc);
}
mysql_close($dbc);
	

?>  
