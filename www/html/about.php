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

p {
  display: block;
  margin-top: 1em;
  margin-bottom: 1em;
  margin-left: 0;
  margin-right: 0;
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
  <li><a href="/licenceinfo.php">History</a></li>
  <li style="float:right"><a class="active" href="/about.php">About</a></li>
  <li style="float:right"><a href="/contact.php">Contact</a></li>   
</ul>

<h3>What is the Premises Security System?</h3>

<p>
For my final year project, I decided to design and build an automatic electric gate system using Automatic Licence Plate Recognition (ALPR) technology. The system is designed to detect approaching vehicles, scan the licence plate, check said licence plate against a pre-approved list of plates designated by the premises owner. The idea came to me one evening when travelling home for work on a wet, stormy night. I had arrived at my house to locked gates. After I had gone through the process of opening and closing the gates behind me, I was drenched. I immediately started to think of a way to automate this process. After spending some time researching, I was pointed towards the direction of ALPR technology used in systems like barrier free toll on the M50. Nearly a year later, Here it is! The Premises Security System! 
</p>

</body>
</html>
