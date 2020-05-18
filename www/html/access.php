<!DOCTYPE html>
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
  <li><a class = "active" href="/access.php">Access</a></li>
  <li><a href="/licenceinfo.php">History</a></li>
  <li style="float:right"><a href="/about.php">About</a></li>
  <li style="float:right"><a href="/contact.php">Contact</a></li>  
</ul>


<?php

if (isset($_POST['submit'])){
	if (in_array('approved', $_POST)) {
		addApproved($_POST);
	} elseif (in_array('blocked', $_POST)) {
		addBlocked($_POST);
	}
}
?>

<form action="" method="POST">
	<p>
		<b>Add a New Plate<br /></b>
		<a>Licence Plate: <input type="text" name="LicencePlate"><br /></a>
		<label for "access">Access Type</label>
		<select id="access" name="access">
    			<option value="approved">Approve</option>
    			<option value="blocked">Block</option>
  		</select>
		<input type="submit" name="submit" value="addPlates">
	</p>
	<?php
	$access_plates = file_get_contents ("../../approved.json");
        $access = json_decode($access_plates, true);
	$blocked_plates = file_get_contents ("../../blocked.json");
	$blocked =json_decode($blocked_plates, true);
	?>
	<b>Approved Plates</b>
	<table>
		<thead>
			<tr>
				<th>Plate</th>
				<th>Date</th>
			</tr>
		</thead>
		<tbody>
			<?php
			echo '<pre>';
			foreach($access as $row)
			{
				echo '<tr><td>'.$row["plate"].'</td><td>'.$row["date"].'</td></tr>';
			}
			echo '</pre>';
			?>
		</tbody>
	</table>
	<br />
	<br />
	<b>Blocked Plates</b>
	<table>
		<thead>
			<tr>
				<th>Plate</th>
				<th>Date</th>
			</tr>
		</thead>
		<tbody>
			<?php
			echo '<pre>';
			foreach($blocked as $row)
			{
				echo '<tr><td>'.$row["plate"].'</td><td>'.$row["date"].'</td></tr>';
			}
			echo '</pre>';
			?>
		</tbody>
	</table
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
	<script src="global.js"></script>
</body>
	
<?php

function pre_r( $array ) {
	echo '<pre>';
	print_r( $array );
	echo '</pre>';

}


function prepareData ( $dataarray ) {

	$d = date("Y-m-d"); 
	$new_array = array (
		"plate"	=> $dataarray['LicencePlate'],
		"date" => $d
	);
	return $new_array;
}

function addApproved ( $array ) {
	$currentdata = file_get_contents ("../../approved.json");
        $file = json_decode($currentdata, true);
	$d = date("Y-m-d"); 
        $formattedData = array (
                "plate" => $array['LicencePlate'],
                "date" => $d
        );
	$file[] = $formattedData;
	$finaldata = json_encode($file);
	file_put_contents('../../approved.json', $finaldata);
}

function addBlocked ( $array ) {
	$currentdata = file_get_contents ("../../blocked.json");
        $file = json_decode($currentdata, true);
        $d = date("Y-m-d"); 
        $formattedData = array (
                "plate" => $array['LicencePlate'],
                "date" => $d
        );
        $file[] = $formattedData;
        $finaldata = json_encode($file);
        file_put_contents('../../blocked.json', $finaldata);

}

?>

