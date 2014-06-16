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

		this.changeMenuState = function(){
			this.menuActive = !this.menuActive;
		}
	});

})();