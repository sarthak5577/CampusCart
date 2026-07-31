// Search Button Interaction

const searchButton = document.querySelector(".search-box button");

if (searchButton) {

    searchButton.addEventListener("click", function() {

        alert("Searching for products...");

    });

}


// Wishlist Interaction

const wishlistButtons = document.querySelectorAll(".wishlist-btn");

wishlistButtons.forEach(function(button) {

    button.addEventListener("click", function() {

        button.innerHTML = "❤️ Added to Wishlist";

        button.style.backgroundColor = "#DBEAFE";

    });

});


// Product Details Modal

const viewButtons = document.querySelectorAll(".view-details-btn");

const modal = document.querySelector(".product-modal");

const closeModal = document.querySelector(".close-modal");

const modalTitle = document.getElementById("modal-title");

const modalPrice = document.getElementById("modal-price");

const modalCondition = document.getElementById("modal-condition");

const modalSeller = document.getElementById("modal-seller");


viewButtons.forEach(function(button) {

    button.addEventListener("click", function() {

        const card = button.closest(".product-card");


        modalTitle.textContent = card.dataset.title;

        modalPrice.textContent = "Price: " + card.dataset.price;

        modalCondition.textContent = "Condition: " + card.dataset.condition;

        modalSeller.textContent = "Seller: " + card.dataset.seller;


        modal.style.display = "flex";

    });

});


if (closeModal) {

    closeModal.addEventListener("click", function() {

        modal.style.display = "none";

    });

}


// Sell Item Modal

const sellModal = document.querySelector(".sell-modal");

const closeSell = document.querySelector(".close-sell");


const navbarSell = document.querySelector(".nav-links li:nth-child(3) a");

const heroSell = document.querySelector(".sell-btn");


// Navbar Sell Button

if (navbarSell) {

    navbarSell.addEventListener("click", function(event) {

        event.preventDefault();

        sellModal.style.display = "flex";

    });

}


// Hero Sell Button

if (heroSell) {

    heroSell.addEventListener("click", function() {

        sellModal.style.display = "flex";

    });

}


// Close Sell Popup

if (closeSell) {

    closeSell.addEventListener("click", function() {

        sellModal.style.display = "none";

    });

}