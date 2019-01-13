<?php include ('config.php') ?>
<!DOCTYPE html>
<html>
<head >
	<link rel="stylesheet" type="text/css" href="logincss.css">
	<title>User Login Page</title>
</head>
<body>
<form method="POST">
	<table cellpadding="10">
		<tr>
			<td>Email:</td>
			<td><input type="email" name="email"></td>
		</tr>
		<tr>
			<td>Password:</td>
			<td><input type="password" name="password"></td>
		</tr>
		<tr>
			<td><input type="submit" name="login" value="Login"></td>
		</tr>
	</table>
</form>
<?php 
if(isset($_POST['login'])){
	$email=$_POST['email'];
	$password=$_POST['password'];
	if(empty($_POST)){
		die("All fields are required");
	}
	#verify user
	$verify=mysqli_query($con,"SELECT * FROM signup WHERE email='$email' AND password='$password'") or die(mysqli_error($con));
	#check if user is valid or not

    if(mysqli_num_rows($verify)==1){
    	#start the session
    	session_start();

    	#store the user data in server temporary cache i.e SESSION
    	$_SESSION['user']=NULL;
    	$userData= mysqli_fetch_array($verify);
    	$_SESSION['user']=$userData;
    	#redirect user to homepage
    	header('location:homepage.php');
    	exit;
       } 
else{
	echo "<p style='color:red'>Invalid email or password</p>";
   }



}
?>
   

</body>
</html>