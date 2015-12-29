$(document).ready(function(){
	$("#loadAll").click(function(){
		var folder = "webcam/";

		$.ajax({
		    url : folder,
		    success: function (data) {
		        $(data).find("a").attr("href", function (i, val) {
		            if( val.match(/\.jpg|\.png|\.gif/) ) { 
		                $("#allImages").append( "<div class='loadedImage col-md-6 col-xs-12'><img class='img-responsive' src='"+ folder + val +"'></div>" );
		            } 
		        });
		    }
		});
	});
});