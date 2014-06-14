(function() {
	var aesthetics = angular.module('aesthetics', []);

	aesthetics.controller('NavbarController', function(){
		// tells which tab is currently selected
		this.currentActive = 0;

		// determines which tab to set to active
		this.setActive = function(ulIndex){
			this.currentActive = ulIndex;
		}

		this.isActive = function(ulIndex){
			return this.currentActive === ulIndex;
		}
	});

})();