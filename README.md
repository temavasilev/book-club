# Flask Book Review Hub

This is a simple Flask web application that allows users to explore, add, and review books. Users can search for books, view book details, and submit their reviews.

## Features

- User registration and authentication
- Explore and search for books
- Add new books to the platform
- View book details, including user reviews
- Submit book reviews

## Installation & Usage with Docker

1. Clone the repository:
```bash
git clone https://github.com/temavasilev/book-club.git
```

2. Move into the project directory:
```bash
cd book-club
```

3. Build the Docker image:
```bash
docker build -t book-club .
```

4. Run the Docker container:
```bash
docker run -p 5000:5000 book-club
```

5. Open the application in your browser:
```bash
http://localhost:5000
```

## Potential Todos

- Integrate with external book APIs (e.g., Google Books, Open Library) to fetch book information automatically.
- Implement a rating system for book reviews (e.g., 1-5 stars).
- Add pagination to the search results and book listing pages.
- Implement social features, such as following other users or getting personalized recommendations.
- Improve the user interface with a more modern design and better user experience.
- Add support for uploading book cover images.
- Optimize database queries and indexing for better performance.
- Publish the application to a cloud platform (e.g., Heroku, AWS, GCP).
- Publish the image to a container registry (e.g., Docker Hub, AWS ECR, GCP GCR).


## License

This project is licensed under the MIT License. See the LICENSE file for more information.