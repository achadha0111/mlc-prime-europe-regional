<!DOCTYPE html>
<html>
<link rel="stylesheet" type="text/css" href="stylesheet.css">
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>

<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
<body>

<div class="container-fluid">
	<div class="row">
		<div class="col-md-12">
	    	<h2> Description </h2>
			<div class = "well" id = "opportunity-title-display" ></div>
			<h2> Best Gallery </h2>
			<div class = "well" id = "opportunity-title-display"></div>
			<form action="upload.php" method="post" enctype="multipart/form-data">
			    Select image to upload:
			    <div class="form-group">
				    <input type="file" name="fileToUpload" id="fileToUpload">
			    	<input type="submit" value="Upload Image" name="submit">
			    </div>  
			</form>
		</div>		
	</div>
</div>
<?php
  	if (isset($_SESSION['image_filename'])) {
    	echo '<img src=$_SESSION["image_filename"] alt="Mountain View" style="width:304px;height:228px;">';
	}
?>


</body>
</html>