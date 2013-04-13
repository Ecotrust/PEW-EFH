<!doctype html>  

<!--[if IEMobile 7 ]> <html <?php language_attributes(); ?>class="no-js iem7"> <![endif]-->
<!--[if lt IE 7 ]> <html <?php language_attributes(); ?> class="no-js ie6"> <![endif]-->
<!--[if IE 7 ]>    <html <?php language_attributes(); ?> class="no-js ie7"> <![endif]-->
<!--[if IE 8 ]>    <html <?php language_attributes(); ?> class="no-js ie8"> <![endif]-->
<!--[if (gte IE 9)|(gt IEMobile 7)|!(IEMobile)|!(IE)]><!--><html <?php language_attributes(); ?> class="no-js"><!--<![endif]-->
	
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
		
		<title><?php echo wp_title('', true, 'right'); ?></title>
				
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		
		<!-- icons & favicons -->
		<!-- For everything else -->
		<link rel="shortcut icon" href="/media/marco/ico/favicon.ico">
		<link rel="stylesheet" href="http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.9/themes/base/jquery-ui.css" type="text/css" media="all" />
		
		
		<!-- Grab Google CDN's jQuery, with a protocol relative URL; fall back to local if necessary -->
		<script src="//ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
		<script>window.jQuery || document.write(unescape('%3Cscript src="<?php echo get_template_directory_uri(); ?>/library/js/libs/jquery-1.7.1.min.js"%3E%3C/script%3E'))</script>
		
		<script src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.9/jquery-ui.min.js" type="text/javascript"></script>

		<script src="<?php echo get_template_directory_uri(); ?>/library/js/modernizr.full.min.js"></script>
		

		<!-- media-queries.js (fallback) -->
		<!--[if lt IE 9]>
			<script src="<?php echo get_template_directory_uri(); ?>/assets/js/respond.min.js"></script>
			<style>
			
			#feedback-tab {
				-ms-filter: "progid:DXImageTransform.Microsoft.Matrix(M11=-1.836909530733566e-16, M12=-1, M21=1, M22=-1.836909530733566e-16, SizingMethod='auto expand')";
				
				/* IE6 and 7 */ 
				filter: progid:DXImageTransform.Microsoft.Matrix(
				         M11=-1.836909530733566e-16,
				         M12=-1,
				         M21=1,
				         M22=-1.836909530733566e-16,
				         SizingMethod='auto expand');

			  }
			</style>
		<![endif]-->

		<!-- html5.js -->
		<!--[if lt IE 9]>
			<script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
		<![endif]-->
		
		<!--[if IE 7]>
		  <link rel="stylesheet" href="<?php echo get_template_directory_uri(); ?>/css/font-awesome-ie7.css">
		<![endif]-->

  		<link rel="pingback" href="<?php bloginfo('pingback_url'); ?>">
		
		<!-- wordpress head functions -->
		<?php wp_head(); ?>
		<!-- end of wordpress head -->
		
		<link rel="stylesheet" href="<?php echo get_template_directory_uri(); ?>/css/bootstrap.css">

		<link rel="stylesheet" href="<?php echo get_template_directory_uri(); ?>/css/bootstrap-responsive.css">
		<link rel="stylesheet" href="<?php echo get_template_directory_uri(); ?>/style.css">
		
		<!-- marco stylesheet -->
		<link rel="stylesheet" href="<?php echo get_template_directory_uri(); ?>/css/marco_style.css">
		<!--[if lt IE 9]>
				<link rel="stylesheet" href="<?php echo get_template_directory_uri(); ?>/css/marco_style.ie.css">
		<![endif]-->		
		
		<?php 

			// check wp user level
			get_currentuserinfo(); 
			// store to use later
			global $user_level; 
		
		?>
				
	</head>
	
	<body <?php body_class(); ?>>

		<header role="banner">
			<div class="navbar navbar-fixed-top">
			  <div class="navbar-inner">
			    <div class="container">
			    	<div class="row-fluid">
			    		<div class="span5">
					        <a href="<?php echo get_bloginfo('wpurl'); ?>">
					        	<img src="<?php echo get_template_directory_uri(); ?>/img/marco-logo.gif"/>
					        </a>
					    </div>
					    <div class="span7">
					       <!-- .btn-navbar is used as the toggle for collapsed navbar content -->
					      <!-- REMOVING THE FOLLOWING UNTIL WE FIND A SOLUTION -->
                          <!--<a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
					     	 <span class="icon-bar"></span>
					      	 <span class="icon-bar"></span>
					      	 <span class="icon-bar"></span>
					      </a>-->
					      <div class="nav-collapse">
					      	<div>
						        <form class="form-search pull-right" action="<?php echo home_url( '/' ); ?>" method="get">
						          <input type="text" class="input-medium search-box" name="s" id="search" value="<?php the_search_query(); ?>" placeholder="search">
						          <a class="btn">
						              <i class="icon-remove icon-large"></i> 
						          </a>
						          
						        </form>
						        <ul class="nav pull-right">
						          <li class="<?php echo $pagename == 'news' ? 'active' : null ?>"><a href="<?php echo get_bloginfo('wpurl'); ?>/news">News</a></li>
						          <li class="<?php echo $pagename == 'about' ? 'active' : null ?>"><a href="<?php echo get_bloginfo('wpurl'); ?>/about">About the&nbsp;Portal</a></li>
						          <li><a href="http://www.midatlanticocean.org/" target="_blank">Visit MARCO</a></li>
						        </ul>
						      </div><!--/.nav-collapse -->
						  </div>
					    </div>
					  </div>
					</div>
				</div>
			</div>
		</header> <!-- end header -->
	<div id="feedback-tab" class="rounded hidden-phone" data-toggle="modal" data-target="#feedback-modal">
	    feedback
	</div>
	<div id="feedback-modal" class="modal hide fade">
	    <div class="modal-header">
	        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
	        <h3>Feedback</h3>
	    </div>
	    <form class="form-horizontal" id="feedback-form">
	    <div class="modal-body">        
	        <div class="control-group">
	          <label class="control-label" for="name">Full Name</label>
	          <div class="controls">
	            <input class="input-xlarge" type="text" name="name" placeholder="Full Name" required>
	          </div>
	        </div>
	        <div class="control-group">
	          <label class="control-label" for="email">Email Address</label>
	          <div class="controls">
	            <input class="input-xlarge" type="email" name="email" placeholder="Email Address" required>
	          </div>
	        </div>
	        <div class="control-group">
	          <label class="control-label" for="comment">Comment</label>
	          <div class="controls">
	              <textarea class="input-xlarge" rows="3" name="comment" required></textarea>
	          </div>
	        </div>

	    </div>
	    <div class="modal-footer">
	        <button href="#" class="btn" data-dismiss="modal">Close</button>
	        <button type="submit" class="btn btn-primary">Send Feedback</button>
	    </div>
	  </form>
	</div>


		<div class="container">
