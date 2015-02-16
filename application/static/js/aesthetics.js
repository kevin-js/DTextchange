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

/*(function() {
	var app = angular.module('app', []);

	app.controller('NavbarController', function(){
		// tells which tab is currently selected
		this.currentActive = 0;

		// determines which tab to set to active
		this.setActive = function(ulIndex){
			this.currentActive = ulIndex;
		}
		// set tab at index ulIndex to the active one
		this.isActive = function(ulIndex){
			return this.currentActive === ulIndex;
		}
	});

	app.controller('MenuController', function(){
		// default to false
		this.menuActive = false;

		// method is called when menu is clicked; depending on state of menu,
		// will either reveal or hide user menu
		this.changeMenuState = function(){
			this.menuActive = !this.menuActive;
			
			$(document).ready(function(){
				if(!this.menuActive)
					$('#user-menu').show('fast');
				else
					$('#user-menu').hide('fast');
			});
		}
	});

	app.controller('profileController', function(){
		this.updateProfilePic = function(){
			// ******* TODO *********
			alert("clicked!");
		}
	});

	app.controller('feedController', function(){
		this.posts = posts;
		if(window.XMLHttpRequest){
			xmlhttp = new XMLHttpRequest();
		}else{
			xmlhttp = new ActiveXObject('Microsoft.XMLHTTP');
		}
		xmlhttp.onreadystatechange = function(){
			if(xmlhttp.readyState = 4 && xmlhttp.status == 200){
			
			}
		}
	});

	var posts = {};

})();*/