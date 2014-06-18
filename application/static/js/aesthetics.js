(function() {
	var aesthetics = angular.module('aesthetics', []);

	aesthetics.controller('NavbarController', function(){
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

	aesthetics.controller('MenuController', function(){
		this.menuActive = false;

		// method is called when menu is clicked; depending on state of menu,
		// will either reveal or hide user menu
		this.changeMenuState = function(){
			this.menuActive = !this.menuActive;

			$(document).ready(function(){
				if(!this.menuActive){
					$('#user-menu').show('fast');
				}else{
					$('#user-menu').hide('fast');
				}
			});
		}
	});

})();