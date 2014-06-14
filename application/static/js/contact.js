(function(){
	var contact = angular.app('contact', []);
	contact.controller('contactController', function(){

		// Use AJAX to send JSON to sendmail.py script which will take care of sending the email for us
		this.sendBlitz = function(name, subject, message){

		};
	});
})();