<?php
$servername = "localhost";
$username = "root";
$password = "myphp@123";
$dbname = "lolchampdata";
$request = $_REQUEST;
// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
function getCount($champ,$item,$min,$connection) {
	$sql ="SELECT count FROM buydata WHERE minute=".$min." AND champ=".$champ." AND item=".$item;
	$result = $connection->query($sql);
	if ($result->num_rows > 0)
	{
		$row = $result->fetch_assoc();
		return $row["count"];
	}
	else
	{
		return 0;
	}
}
$count = getCount($request["champID"],$request["itemID"],$request["minute"],$conn);
if($count > 0)
{
	$sql = "UPDATE buydata SET count=".($count+1)." WHERE minute=".$request["minute"]." AND champ=".$request["champID"]." AND item=".$request["itemID"];
	echo "sql: ".$sql;
	if ($conn->query($sql) === TRUE) {
		echo "Record updated successfully";
	} else {
		echo "Error updating record: " . $conn->error;
	}
}
else
{

	$sql = "INSERT INTO buydata (minute,champ,item,count) 
		VALUES (".$request["minute"].", ".$request["champID"].", ".$request["itemID"].", "."1".")";

	if ($conn->query($sql) === TRUE) {
		echo "Record updated successfully";
	}
	else {
		echo "Error updating record: " . $conn->error;
	}
}


$conn->close();
?>