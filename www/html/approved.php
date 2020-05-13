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


</style>
</head>
<body>

<div class="header">
  <h2>Premises Security System</h2>
</div>

<ul>
  <li><a href="/index.php">Home</a></li>
  <li><a class="active" href="/approved.index">Approved Plates</a></li>
  <li><a href="licenceinfo.php">History</a></li>
  <li style="float:right"><a href="/about.php">About</a></li>
  <li style="float:right"><a href="/contact.php">Contact</a></li>  
</ul>

