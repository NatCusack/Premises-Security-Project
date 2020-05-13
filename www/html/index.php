<!DOCTYPE html>
<html>
<head>
<style>
body {
  font-size: 28px;
  font-family:arial;
  font-style:bold;

}
.webcam{
  width:400px;
  backgrund:#ccc;
  border:10px solid #ddd;
  margin:0 auto;	
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
  <li><a class="active" href="/index.php">Home</a></li>
  <li><a href="/access.php">Access</a></li>
  <li><a href="/licenceinfo.php">History</a></li>
  <li style="float:right"><a href="/about.php">About</a></li>
  <li style="float:right"><a href="/contact.php">Contact</a></li>   
</ul>


<h3>Welcome to Premises Security System</h3>
<div class="webcam">
	<img src='2020-05-13_12-38-58_pic.jpg'
	<canvis id="canvas" width="400" height="300"></canvas>
</div>

<p></p>
</body>
</html>

