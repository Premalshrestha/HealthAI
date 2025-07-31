function toggleEmergencyModal() {
    const modal = document.getElementById('emergency-modal');
    modal.classList.toggle('hidden');
}

function toggleMap() {
    const mapModal = document.getElementById('mapModal');
    mapModal.classList.toggle('hidden');
}

// Optional: Close modal when "Cancel" button is clicked
document.getElementById("close-emergency").addEventListener("click", () => {
    document.getElementById("emergency-modal").classList.add("hidden");
});