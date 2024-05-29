
# FastAPI Blog Application

This is a FastAPI-based blog application with user authentication, CRUD operations for posts, and a basic frontend setup using React and Tailwind CSS.

## Features

- User Registration and Authentication
- JWT-based Token Authentication
- CRUD Operations for Blog Posts
- Frontend built with React and Tailwind CSS

## Table of Contents

- [Installation](#installation)
- [Database Setup](#database-setup)
- [Environment Variables](#environment-variables)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Frontend Setup](#frontend-setup)
- [License](#license)

## Installation

### Backend

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/Alan69/blog_api.git
    cd fastapi-blog
    ```

2. **Create a Virtual Environment:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Frontend

1. **Navigate to the frontend directory:**

    ```bash
    cd frontend
    ```

2. **Install Node.js Dependencies:**

    ```bash
    npm install
    ```

## Database Setup

1. **Initialize the Database:**

    Ensure that your database URL is correctly set in the `.env` file (see Environment Variables section). Then, run the following commands to create the database tables:

    ```bash
    alembic upgrade head
    ```

## Environment Variables

Create a `.env` file in the root directory of the project and add the following environment variables:

```
DATABASE_URL=sqlite:///./test.db
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Running the Application

### Backend

1. **Start the FastAPI Server:**

    ```bash
    uvicorn main:app --reload
    ```

    This will start the server at `http://127.0.0.1:8000`.

### Frontend

1. **Navigate to the frontend directory:**

    ```bash
    cd frontend
    ```

2. **Start the React Development Server:**

    ```bash
    npm start
    ```

    This will start the frontend at `http://localhost:3000`.

## API Endpoints

- **POST** `/token`: Login and obtain JWT token
- **POST** `/register`: Register a new user
- **POST** `/posts/`: Create a new post
- **GET** `/posts/`: Get a list of posts
- **GET** `/posts/{post_id}`: Get a specific post by ID
- **PUT** `/posts/{post_id}`: Update a specific post by ID
- **DELETE** `/posts/{post_id}`: Delete a specific post by ID

## Frontend Setup

### Project Structure

```
frontend/
├── public/
├── src/
│   ├── components/
│   ├── pages/
│   ├── App.js
│   ├── index.js
│   └── ...
├── tailwind.config.js
├── postcss.config.js
├── package.json
└── ...
```

### Installing Tailwind CSS

Tailwind CSS is already set up in the `package.json`. Ensure you have the following configuration in `tailwind.config.js`:

```javascript
module.exports = {
  purge: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],
  darkMode: false,
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
```

### Sample Component

```jsx
// src/components/PostList.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';

const PostList = () => {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    axios.get('/api/posts')
      .then(response => {
        setPosts(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the posts!', error);
      });
  }, []);

  return (
    <div className="container mx-auto px-4">
      <h1 className="text-2xl font-bold my-4">Posts</h1>
      <ul>
        {posts.map(post => (
          <li key={post.id} className="my-2">
            <h2 className="text-xl">{post.title}</h2>
            <p>{post.content}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PostList;
```

### Key Points

- **Installation Instructions**: Detailed steps to set up both backend and frontend environments.
- **Database Setup**: Instructions on how to initialize the database.
- **Environment Variables**: Clear information on required environment variables.
- **Running the Application**: Steps to start both backend and frontend servers.
- **API Endpoints**: List of available API endpoints with brief descriptions.
- **Frontend Setup**: Instructions on setting up Tailwind CSS and a sample React component.
- **License**: Standard MIT License section.

Ensure you update the repository URL and any specific paths or configurations according to your actual project setup. This README provides a solid foundation for anyone setting up and using your FastAPI blog application.
