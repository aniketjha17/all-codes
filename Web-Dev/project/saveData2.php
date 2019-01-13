<?php 

    #CHECKING WHICH MODE IS THE REQUEST SET TO
if($_SERVER['REQUEST_METHOD'] === "POST"){
	# INCLUDE THE CONNECTION CODE BELOW
	include ('config.php');
	#COLLECT ALL POST ARRAY VALUES BELOW IN LOCAL VARIABLE
	$bname =$_POST['bname'];
   $bdesc=$_POST['bdesc'];
   $bcategory=$_POST['bcategory'];

   
   if(!empty($_FILES['picture']['name'])){
   	// file attribute
   	$filename=$_FILES['picture']['name'];
   	$filesize=$_FILES['picture']['size'];
   	$filetype=$_FILES['picture']['type'];
    
   	#server directory where the file will get uploaded
   	#create a directory first

   	if(!file_exists("private")){
   		#CREATE A DIRECTORY
   		mkdir("private");

   	}
   	#SET SERVER PATH
   	
   		$serverpath="private/".rand(000,999).$filename;
   		# file upload
   		$tmp_file = $_FILES['picture']['tmp_name'];
   		#move the temp file
   		$move=move_uploaded_file($tmp_file, $serverpath) or die ($_FILES['picture']['error']);
   	}
   	else{
          $serverpath= '';
   	}
   

   #PREPARE SQL STATEMENTS 
	$sql ="INSERT INTO book VALUES ('0','$bname','$bdesc','$bcategory','$serverpath')";

	 #execute the above statement
	$ex=mysqli_query($con,$sql) or die (mysqli_error($con));

	#check if properly executed
	if ($ex == 1) {
			?><script>
		alert('book uploaded successfully')
		window.location.href="homepage.php";
		</script>
		<?php
	}
// if($ex==1){
   
//     header('location:login.php');
// }



}

?>
