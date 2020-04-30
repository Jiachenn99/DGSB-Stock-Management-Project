$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });
}); 

$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();
    // Animate select box length
    var searchInput = $(".search-box input");
    var inputGroup = $(".search-box .input-group");
    var boxWidth = inputGroup.width();
    searchInput.focus(function(){
      inputGroup.animate({
        width: "300"
      });
    }).blur(function(){
      inputGroup.animate({
        width: boxWidth
      });
    });
});
