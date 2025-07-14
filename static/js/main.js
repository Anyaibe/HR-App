// Search functionality in Employee Directory
document.querySelector('.directory-search').addEventListener('input', function() {
    const searchValue = this.value.toLowerCase();
    document.querySelectorAll('.employee-table tbody tr').forEach(row => {
        row.style.display = row.innerText.toLowerCase().includes(searchValue) ? '' : 'none';
    });
});

// Mock Pagination functionality
document.querySelectorAll('.pagination-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        document.querySelectorAll('.pagination-btn').forEach(b => b.classList.remove('active'));
        this.classList.add('active');
    });
});

// Show the selected section and hide others
document.querySelectorAll('.dropdown-content a').forEach(link => {
    link.addEventListener('click', (event) => {
        event.preventDefault();

        // Hide all content sections
        document.querySelectorAll('.content-section').forEach(section => {
            section.style.display = 'none';
        });

        // Get the target section ID from the link's data-section attribute
        const sectionID = link.getAttribute('data-section');
        const targetSection = document.getElementById(sectionID);

        // Show the target section
        if (targetSection) {
            targetSection.style.display = 'block';
        }
    });
});


// Function to show profile
function showProfile(name, role, email) {
    // Hide the employee directory section
    document.getElementById('employee-directory-section').style.display = 'none';

    // Populate profile details
    document.querySelector('.profile-info h2').textContent = name;
    document.querySelector('.profile-info p:nth-child(2)').textContent = role;
    document.querySelector('.profile-info p:nth-child(3)').textContent = email;

    // Show the profile section
    document.querySelector('.profile').style.display = 'block';

    // Show the back button to return to the directory
    document.getElementById('back-to-directory').style.display = 'block';
}

// Function to show the employee directory and hide the profile
function showDirectory() {
    // Hide the profile section
    document.querySelector('.profile').style.display = 'none';

    // Show the employee directory section
    document.getElementById('employee-directory-section').style.display = 'block';

    // Hide the back button
    document.getElementById('back-to-directory').style.display = 'none';
}

// Sidebar navigation to handle showing different sections
const sidebarItem = document.querySelectorAll('.sidebar a');
sidebarItem.forEach(item => {
    item.addEventListener('click', (event) => {
        event.preventDefault();
        const targetSectionId = item.getAttribute('data-section');


        // Show the clicked section
        document.getElementById(targetSectionId).style.display = 'block';

        // If Employee Directory is clicked, hide the profile section
        if (targetSectionId === 'employee-directory-section') {
            showDirectory();
        }
    });
});