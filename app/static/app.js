const urlInput = document.getElementById('urlInput');
const scrapeBtn = document.getElementById('scrapeBtn');
const downloadBtn = document.getElementById('downloadBtn');
const errorMsg = document.getElementById('errorMsg');
const previewSection = document.getElementById('previewSection');
const markdownPreview = document.getElementById('markdownPreview');
const loadingSpinner = document.getElementById('loadingSpinner');

const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

let currentMarkdown = '';
let currentUrl = '';

// Enter-Taste im Input
urlInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') scrapeBtn.click();
});

// Scrape Button
scrapeBtn.addEventListener('click', async () => {
    const url = urlInput.value.trim();

    if (!url) {
        showError('Bitte URL eingeben');
        return;
    }

    // UI Reset
    hideError();
    previewSection.classList.add('hidden');
    loadingSpinner.classList.remove('hidden');
    scrapeBtn.disabled = true;

    try {
        const response = await fetch('/scrape', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify({ url })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || 'Fehler beim Scraping');
        }

        currentMarkdown = data.markdown;
        currentUrl = data.url;

        markdownPreview.textContent = currentMarkdown;
        previewSection.classList.remove('hidden');

    } catch (error) {
        showError(error.message);
    } finally {
        loadingSpinner.classList.add('hidden');
        scrapeBtn.disabled = false;
    }
});

// Download Button
downloadBtn.addEventListener('click', async () => {
    try {
        const response = await fetch('/download', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify({
                markdown: currentMarkdown,
                url: currentUrl
            })
        });

        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = response.headers.get('content-disposition')?.split('filename=')[1] || 'output.md';
        a.click();

    } catch (error) {
        showError('Download fehlgeschlagen');
    }
});

function showError(message) {
    errorMsg.textContent = message;
    errorMsg.classList.remove('hidden');
}

function hideError() {
    errorMsg.classList.add('hidden');
}
