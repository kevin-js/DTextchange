$(document).ready(function(){

	this.menuActive = false;
	// open and close user menu
	$('#menu-button').click(function(){
		this.menuActive = !this.menuActive;
		
		if(this.menuActive){
			$('#user-menu').show(300);
		}else{
			$('#user-menu').hide(300);
		}
	});

});