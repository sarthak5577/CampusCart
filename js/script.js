// Search Button Interaction

const searchButton = document.querySelector(".search-box button");

searchButton.addEventListener("click", function() {

    alert("Searching for products...");

});
// Wishlist Interaction

const wishlistButtons = document.querySelectorAll(".wishlist-btn");

wishlistButtons.forEach(function(button) {

    button.addEventListener("click", function() {

        button.innerHTML = "❤️ Added to Wishlist";

        button.style.backgroundColor = "#DBEAFE";

    });

});

// Product Details Modal

const viewButtons = document.querySelectorAll(".product-card button:not(.wishlist-btn)");
const modal = document.querySelector(".product-modal");
const closeModal = document.querySelector(".close-modal");


viewButtons.forEach(function(button) {

    button.addEventListener("click", function() {

        modal.style.display = "flex";

    });

});


closeModal.addEventListener("click", function() {

    modal.style.display = "none";

});

// Sell Item Modal

const sellModal = document.querySelector(".sell-modal");
const closeSell = document.querySelector(".close-sell");

// Navbar Sell Item Link
const navbarSell = document.querySelector(".nav-links li:nth-child(3) a");

// Hero Sell Button
const heroSell = document.querySelector(".sell-btn");

// Open from Navbar
navbarSell.addEventListener("click", function(event) {

    event.preventDefault();

    sellModal.style.display = "flex";

});

// Open from Hero Button
heroSell.addEventListener("click", function() {

    sellModal.style.display = "flex";

});

// Close Modal
closeSell.addEventListener("click", function() {

    sellModal.style.display = "none";

});