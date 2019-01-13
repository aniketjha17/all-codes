<!DOCTYPE html>
<html>
<head>
	<title>Sign Up</title>
</head>
<body>
	<h3>Please sign up to continue</h3>
<form action="saveData.php"  method="POST" enctype="multipart/form-data">
	<table cellspacing="20">
		<tr>
			<td>NAME:</td>
			<td><input type="text" name="name"></td>
		</tr>
		<tr>
			<td>Email:</td>
			<td><input type="email" name="email"></td>
		</tr>
		<tr>
			<td>Password:</td>
			<td><input type="password" name="password"></td>
		</tr>
		<tr>
			<td>Address:</td>
			<td><input type="address" name="address"></td>
		</tr>
		<tr>
			<td>Date Of Birth</td>
			<td><input type="date" name="date"></td>
		</tr>
		<tr>
			<td>Gender:</td>
			<td><input type="text" name="gender"></td>
		</tr>
		<tr>
			<td>About:</td>
			<td><input type="text" name="about"></td>
		</tr>
		<tr>
			<td>Profile Pic:</td>
			<td><input type="file" name="picture"></td>
		</tr>
		<tr>
			<td>Phone no.:</td>
			<td><input type="text" name="phone"></td>
		</tr>
		<tr>
			<td><input type="submit" name="submit" value=signup ></td>
		</tr>
	</table>
</form>
IF EXISTING USER THEN <a href="login.php">LOGIN HERE</a>
<a href="admin.php">Admin Login</a>
</body>
</html>






