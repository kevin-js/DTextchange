$(document).ready(function(){

	$('#profile-pic').hover(function(){
		$('#profile-pic').addClass('active');
	}, function(){
		$('#profile-pic').removeClass('active');
	});

	$('#profile-pic').click(function(){
		
	});

	$('#profile-header').hover(function(){
		$('.profile-header').backgroundaddClass('active');
	}, function(){
		$('.profile-header').removeClass('active');
	});
});