document.addEventListener('DOMContentLoaded', () => {
    const movieTableBody = document.getElementById('movie-table-body');
    const watchLaterFilter = document.getElementById('watch-later-filter');
    const movieListContainer = document.getElementById('movie-list-container');
    const movieDetailContainer = document.getElementById('movie-detail-container');
    const movieDetailContent = document.getElementById('movie-detail-content');
    const backButton = document.getElementById('back-button');

    let movies = [];
    const WATCH_LATER_KEY = 'watch_later_movies';

    // Fetch movies data
    fetch('movies.json')
        .then(response => response.json())
        .then(data => {
            movies = data;
            renderTable();
        })
        .catch(error => console.error('Error loading movies:', error));

    // Render table
    function renderTable() {
        movieTableBody.innerHTML = '';
        const watchLaterList = getWatchLaterList();
        const isFilterActive = watchLaterFilter.checked;

        movies.forEach(movie => {
            const isWatchLater = watchLaterList.includes(movie.id);

            // Filter logic
            if (isFilterActive && !isWatchLater) {
                return;
            }

            const row = document.createElement('tr');
            row.addEventListener('click', () => showDetail(movie));

            // Watch Later Checkbox Cell
            const checkboxCell = document.createElement('td');
            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.className = 'watch-later-checkbox';
            checkbox.checked = isWatchLater;

            // Prevent row click when clicking checkbox
            checkbox.addEventListener('click', (e) => {
                e.stopPropagation();
                toggleWatchLater(movie.id);
            });

            checkboxCell.appendChild(checkbox);
            row.appendChild(checkboxCell);

            // Title
            const titleCell = document.createElement('td');
            titleCell.textContent = movie.title || movie.original_title || 'No Title';
            row.appendChild(titleCell);

            // Director
            const directorCell = document.createElement('td');
            directorCell.className = 'col-director';
            directorCell.textContent = movie.director || '-';
            row.appendChild(directorCell);

            // Country
            const countryCell = document.createElement('td');
            countryCell.className = 'col-country';
            countryCell.textContent = movie.country || '-';
            row.appendChild(countryCell);

            // Year
            const yearCell = document.createElement('td');
            yearCell.className = 'col-year';
            yearCell.textContent = movie.release_year || '-';
            row.appendChild(yearCell);

            // Genre
            const genreCell = document.createElement('td');
            genreCell.className = 'col-genre';
            const genres = Array.isArray(movie.genre) ? movie.genre.join(', ') : (movie.genre || '-');
            genreCell.textContent = genres;
            row.appendChild(genreCell);

            movieTableBody.appendChild(row);
        });
    }

    // Toggle Watch Later
    function toggleWatchLater(id) {
        let list = getWatchLaterList();
        if (list.includes(id)) {
            list = list.filter(item => item !== id);
        } else {
            list.push(id);
        }
        localStorage.setItem(WATCH_LATER_KEY, JSON.stringify(list));

        // Re-render if filter is active to immediately remove unchecked items
        if (watchLaterFilter.checked) {
            renderTable();
        }
    }

    function getWatchLaterList() {
        const stored = localStorage.getItem(WATCH_LATER_KEY);
        return stored ? JSON.parse(stored) : [];
    }

    // Filter Event Listener
    watchLaterFilter.addEventListener('change', renderTable);

    // Show Detail View
    function showDetail(movie) {
        movieListContainer.classList.add('hidden');
        document.querySelector('header .controls').style.display = 'none'; // Hide filter in detail view
        movieDetailContainer.classList.remove('hidden');

        // Render Metadata
        let metadataHtml = '<div class="metadata-grid">';

        // Priority keys to display first
        const priorityKeys = ['title', 'original_title', 'director', 'country', 'release_year', 'genre'];
        const ignoredKeys = ['content', 'id'];

        // Add priority keys first
        priorityKeys.forEach(key => {
            if (movie[key]) {
                const value = Array.isArray(movie[key]) ? movie[key].join(', ') : movie[key];
                metadataHtml += createMetadataItem(key, value);
            }
        });

        // Add other keys
        Object.keys(movie).forEach(key => {
            if (!priorityKeys.includes(key) && !ignoredKeys.includes(key)) {
                 const value = Array.isArray(movie[key]) ? movie[key].join(', ') : movie[key];
                 metadataHtml += createMetadataItem(key, value);
            }
        });

        metadataHtml += '</div>';

        // Render Markdown Content
        const markdownHtml = marked.parse(movie.content || '');

        movieDetailContent.innerHTML = `
            <h1>${movie.title}</h1>
            ${metadataHtml}
            <div class="markdown-body">${markdownHtml}</div>
        `;

        // Scroll to top
        window.scrollTo(0, 0);
    }

    function createMetadataItem(key, value) {
        // Format key for display (e.g., rating_child -> Rating Child)
        const displayKey = key.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
        return `
            <div class="metadata-item">
                <span class="metadata-label">${displayKey}</span>
                <span class="metadata-value">${value}</span>
            </div>
        `;
    }

    // Back Button
    backButton.addEventListener('click', () => {
        movieDetailContainer.classList.add('hidden');
        movieListContainer.classList.remove('hidden');
        document.querySelector('header .controls').style.display = 'flex'; // Show filter again
    });
});
