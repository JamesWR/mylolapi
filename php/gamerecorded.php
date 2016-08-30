<?php
$servername = "localhost";
$username = "root";
$password = "myphp@123";
$dbname = "lolchampdata";
$request = $_REQUEST;
// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

if($request["get"] == "true")
{
	$sql ="SELECT gameid FROM recordedgames WHERE gameid=".$request['gameid'];
	$result = $conn->query($sql);
	// error_log("result is: ".$result);
	if ($result->num_rows > 0)
	{
		echo "true";
	}
	else
	{
		echo "false";
	}
}
else
{

	$sql = "INSERT INTO recordedgames (gameid) 
		VALUES (".$request['gameid'].")";

	if ($conn->query($sql) === TRUE) {
		echo "success";
	}
	else {
		echo "fail";
	}
}

$conn->close();
?>