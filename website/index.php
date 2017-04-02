<?php
	session_start(); 
?>
<!DOCTYPE html>
<html>
<link rel="stylesheet" type="text/css" href="stylesheet.css">
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.0/jquery.min.js"></script>

<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>

<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
<body>



<div class="container-fluid">
    <nav class="navbar navbar-inverse">
	    <div class="navbar-header">
	      <a class="navbar-brand" href="#">Tate's Click Bait</a>
	    </div>
	    <ul class="nav navbar-nav">
	      <li class="active"><a href="#">Home</a></li>
	      <li><a href="#">Gallery</a></li>
	    </ul>
	</nav>
	<div class="row">
	    
		<div class="col-md-12">
			<div class="panel panel-default">
			  <div class="panel-body">
			    <!--<img src="/mlh-prime-europe-regional/website/uploads/dog.jpg" height=100% width=100%"> -->
			    <?php
			    	echo'<img src="/mlh-prime-europe-regional/website/uploads/'.$_SESSION["img"].'" height=100% width=100%">';
			    ?>
			  </div>
			</div>
	    	<h2> Description </h2>
			<div class = "well" id = "opportunity-title-display"> 
			    <?php
			    	echo'$_SESSION["description"]';
			    ?>  	
			</div>
			<form action="upload.php" method="post" enctype="multipart/form-data">
			    Select image to upload:
			    <div class="form-group">
				    <input type="file" name="fileToUpload" id="fileToUpload">
				    <hr>
			    	<input type="submit" class="btn btn-default" value="Upload Image" name="submit">
			    </div>  
			</form>
		</div>		
	</div>
</div>
</body>
</html>