//checkout
var form = document.getElementById("form");
form.addEventListener("submit", function (e) {
    e.preventDefault();
    console.log("Form Submitted...");
    document.getElementById("form-button").classList.add("hidden");
    document.getElementById("payment-info").classList.remove("hidden");
});



$(document).ready(function() {
  $("#sidebarCollapse").on("click", function() {
    $("#sidebar").addClass("active");
  });

  $("#sidebarCollapseX").on("click", function() {
    $("#sidebar").removeClass("active");
  });

  $("#sidebarCollapse").on("click", function() {
    if ($("#sidebar").hasClass("active")) {
      $(".overlay").addClass("visible");
      console.log("it's working!");
    }
  });

  $("#sidebarCollapseX").on("click", function() {
    $(".overlay").removeClass("visible");
  });
});
 

