<?php 

// Server name must be localhost 
$servername = "localhost"; 

// In my case, user name will be root 
$username = "root"; 

// Password is empty 
$password = ""; 

// Creating a connection 
$conn = new MongoClient($servername, 
			$username, $password); 

// Check connection 
if ($conn->connect_error) { 
	die("Connection failure: "
		. $conn->connect_error); 
} 

// Creating a database named NGDB_Project 
$sql = "CREATE DATABASE NGDB"; 
if ($conn->query($sql) === TRUE) { 
	echo "Database with name NGDB_Project"; 
} else { 
	echo "Error: " . $conn->error; 
} 

// Closing connection 
$conn->close(); 
?> 
