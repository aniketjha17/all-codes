<!DOCTYPE html>
<html>
<head>
	<title>Books Course</title>
</head>
<body>
<?php 
if (isset ($_POST ['done'])){
echo "THE BOOKS ARE LISTED BELOW";
}
include ('config.php');
$sql="SELECT * FROM book";
$execute=mysqli_query($con,$sql) or die (mysqli_error($con));
if(mysqli_num_rows($execute)>0){
	echo "no such record: ",mysqli_num_rows($execute);}
 ?>
 <table border=2>
 <thead>
 	<tr>
 		<th>Name</th>
 		<th>Description</th>
 		<th>Category</th>
 		<th>Book</th>
 	</tr>
 </thead>
 <?php 
 while($row=mysqli_fetch_array($execute)){
 	?>
 	<tr>
 		<td><?php echo $row[1] ?></td>
 		<td><?php echo $row['name'] ?></td>
 		<td><?php echo $row['description']?></td>
 		<td><?php echo $row['category'] ?></td>
 		<td><img src="<?php echo $row['path'] ?>" width="150" height="150"></td>
 	</tr>
 <?php } ?>
 </table>
 </body>
</html>