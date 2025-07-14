// Function to switch between tabs
function openTab(evt, tabName) {
    var i, tabcontent, tablinks;

    // Hide all tab contents
    tabcontent = document.getElementsByClassName("tab-content");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Remove the 'active' class from all tab links
    tablinks = document.getElementsByClassName("tab-btn");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add 'active' class to the clicked tab
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}

sidebarItems.forEach(item => {
    item.addEventListener('click', (event) => {
        event.preventDefault();
        const targetSectionId = item.getAttribute('data-section');
        showSection(targetSectionId);
    });
});

// Default open tab on load
document.getElementById("all").style.display = "block";
document.getElementsByClassName("tab-btn")[0].classList.add("active");


