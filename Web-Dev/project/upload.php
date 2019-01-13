<!DOCTYPE html>
<html>
<head>
	<title>upload</title>
</head>
<body>
<form action="saveData2.php"  method="POST" enctype="multipart/form-data">
	<table cellspacing="20">
		<tr>
			<td>Book's name:</td>
			<td><input type="text" name="bname"></td>
		</tr>
		<tr>
			<td>Book's Description:</td>
			<td><input type="text" name="bdesc"></td>
		</tr>
		<tr>
			<td>Book's category:</td>
			<td><input type="text" name="bcategory"></td>
		</tr>
		<tr>
			<td>Select Book:</td>
			<td><input type="file" name="picture"></td>
		</tr>
		<tr>
			<td><input type="submit" name="submit" value=upload ></td>
		</tr>
	</table>
</form>
</body>
</html>