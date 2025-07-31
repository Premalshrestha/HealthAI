
// medimate/mediapp/static/js/profile.js
document.addEventListener("DOMContentLoaded", () => {
  const profileToggle = document.getElementById('profile-toggle');
  const profileDropdown = document.getElementById('profile-dropdown');

  if (profileToggle && profileDropdown) {
    // Toggle dropdown
    profileToggle.addEventListener('click', function (e) {
      e.stopPropagation();
      profileDropdown.classList.toggle('hidden');
    });

    // Close when clicking outside
    window.addEventListener('click', function (e) {
      if (!profileDropdown.contains(e.target)) {
        profileDropdown.classList.add('hidden');
      }
    });
  }
});