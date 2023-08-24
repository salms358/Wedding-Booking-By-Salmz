$(document).ready(function() {
    var successMessage = $('.container');
    
    if (successMessage.length) {
        successMessage.show();
        
        setTimeout(function() {
            successMessage.fadeOut();
        }, 5000);
    }
});