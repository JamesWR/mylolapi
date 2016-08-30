<?php
$servername = "localhost";
$username = "root";
$password = "myphp@123";
$dbname = "lolchampdata";
$request = $_REQUEST;

$champnums = array("266","103","84","12","32","34","1","22","268","432","53","63","201","51","69","31","42","122","131","119","36","245","60","28","81","9","114","105","3","41","86","150","79","104","120","74","39","40","59","24","126","222","429","43","30","38","55","10","85","121","203","96","7","64","89","127","236","117","99","54","90","57","11","21","62","82","25","267","75","111","76","56","20","2","61","80","78","133","33","421","58","107","92","68","13","113","35","98","102","27","14","15","72","37","16","50","134","223","91","44","17","412","18","48","23","4","29","77","6","110","67","45","161","254","112","8","106","19","101","5","157","83","154","238","115","26","143");
// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
// for($index = 0; $index < count($champnums); $index++)
// {
// 	$sql = "CREATE TABLE _".$champnums[$index]." (
// 	minute INT UNSIGNED PRIMARY KEY, 
// 	itemData TEXT
// 	)";
// 	echo "sql: ".$sql;
// 	if ($conn->query($sql) === TRUE) {
// 	    echo "Record updated successfully";
// 	} else {
// 	    echo "Error updating record: " . $conn->error;
// 	}
// }

$sql = "CREATE TABLE buydata (
minute INT UNSIGNED,
champ INT UNSIGNED,
item INT UNSIGNED,
count INT UNSIGNED,
PRIMARY KEY (minute,champ,item)
)";
echo "sql: ".$sql;
if ($conn->query($sql) === TRUE) {
    echo "Record updated successfully";
} else {
    echo "Error updating record: " . $conn->error;
}
$sql = "CREATE TABLE recordedgames (
gamesid INT UNSIGNED PRIMARY KEY 

)";
echo "sql: ".$sql;
if ($conn->query($sql) === TRUE) {
    echo "Record updated successfully";
} else {
    echo "Error updating record: " . $conn->error;
}

$conn->close();
?>