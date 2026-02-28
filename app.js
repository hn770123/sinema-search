document.addEventListener('DOMContentLoaded', () => {
    const movieTableBody = document.getElementById('movie-table-body');
    const notInterestedFilter = document.getElementById('not-interested-filter');
    const movieListContainer = document.getElementById('movie-list-container');
    const movieDetailContainer = document.getElementById('movie-detail-container');
    const movieDetailContent = document.getElementById('movie-detail-content');
    const backButton = document.getElementById('back-button');

    let movies = [];
    const NOT_INTERESTED_KEY = 'not_interested_movies';

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
        const notInterestedList = getNotInterestedList();
        const isFilterActive = notInterestedFilter.checked;

        movies.forEach(movie => {
            const isNotInterested = notInterestedList.includes(movie.id);

            // Filter logic
            if (isFilterActive && isNotInterested) {
                return;
            }

            const row = document.createElement('tr');
            row.addEventListener('click', () => showDetail(movie));

            // Not Interested Checkbox Cell
            const checkboxCell = document.createElement('td');
            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.className = 'not-interested-checkbox';
            checkbox.checked = isNotInterested;

            // Prevent row click when clicking checkbox
            checkbox.addEventListener('click', (e) => {
                e.stopPropagation();
                toggleNotInterested(movie.id);
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

    // Toggle Not Interested
    function toggleNotInterested(id) {
        let list = getNotInterestedList();
        if (list.includes(id)) {
            list = list.filter(item => item !== id);
        } else {
            list.push(id);
        }
        localStorage.setItem(NOT_INTERESTED_KEY, JSON.stringify(list));

        // Re-render if filter is active to immediately remove checked items
        if (notInterestedFilter.checked) {
            renderTable();
        }
    }

    function getNotInterestedList() {
        const stored = localStorage.getItem(NOT_INTERESTED_KEY);
        if (!stored) return [];
        try {
            const parsed = JSON.parse(stored);
            return Array.isArray(parsed) ? parsed : [];
        } catch (e) {
            console.warn('Invalid data in localStorage, resetting:', e);
            localStorage.removeItem(NOT_INTERESTED_KEY);
            return [];
        }
    }

    // Filter Event Listener
    notInterestedFilter.addEventListener('change', renderTable);

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
