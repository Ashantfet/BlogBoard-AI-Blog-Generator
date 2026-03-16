# <a href="https://kalyanm45.github.io/BlogBoard-AI-Blog-Generator/">BlogBoard — Autonomous AI Article Generator</a>

<p align="center"> <img src="https://img.shields.io/github/license/KalyanM45/BlogBoard-AI-Blog-Generator?style=ROUND" alt="License" /> <img src="https://img.shields.io/github/stars/KalyanM45/BlogBoard-AI-Blog-Generator?style=ROUND" alt="Stars" /> <img src="https://img.shields.io/github/forks/KalyanM45/BlogBoard-AI-Blog-Generator?style=ROUND" alt="Forks" /> <img src="https://img.shields.io/github/issues/KalyanM45/BlogBoard-AI-Blog-Generator?style=ROUND"alt="Issues" />
</p>

# BlogBoard — AI Blog Generator

BlogBoard is an **AI-powered blogging platform** that automatically generates high-quality articles using Large Language Models and organizes them into a clean, static website.

Originally designed as a scheduled AI article generator using **LangGraph workflows**, this project has been extended to support **dynamic blog generation from any topic via a web interface**.

The system combines:

* Automated AI content generation
* Static blog website rendering
* A backend API for real-time article creation

This makes BlogBoard a lightweight **AI blogging platform** that can generate and publish articles instantly.

---

# Overview

BlogBoard uses a modular pipeline where a backend AI system generates blog content and the frontend displays it as a modern blog website.

### Core Workflow

```
User enters topic (UI or CLI)
        ↓
FastAPI Backend API
        ↓
LangGraph Workflow Pipeline
        ↓
LLM Content Generation (Groq API)
        ↓
Markdown Article Generation
        ↓
Update articles.json
        ↓
Frontend loads and displays the blog
```

Articles are stored as **Markdown files** and automatically indexed in JSON files for the frontend to render.

---

# Key Features

## AI Blog Generation

Automatically generate complete blog posts including:

* SEO-friendly titles
* Descriptions
* Tags
* Markdown formatted content
* Estimated read time

## Dynamic Topic Generation

Users can generate blogs for **any topic** directly from the UI or CLI.

Examples:

```
Virat Kohli Biography
Artificial Intelligence in Healthcare
India vs Pakistan Cricket Rivalry
History of SpaceX
```

## LangGraph AI Pipeline

The project uses **LangGraph** to orchestrate the content generation workflow:

1. Schedule consolidation
2. Topic selection
3. Metadata generation
4. Blog generation
5. Markdown export
6. Website update

## Static Blog Website

The frontend renders articles dynamically using:

* HTML
* CSS
* JavaScript
* Markdown parsing

Categories include:

* Machine Learning
* Deep Learning
* NLP
* Computer Vision
* Generative AI
* AI News
* Statistics

## Custom Topic Category (Added Feature)

A new **Custom Blogs** category was introduced to support blogs generated from arbitrary topics.

Generated blogs are stored in:

```
frontend/blogs/custom/
```

## Web-Based Blog Generator (Added Feature)

A web interface allows users to generate blogs directly from the website without running CLI commands.

Users simply enter a topic and click **Generate Blog**.

## Unified Backend Server (Added Feature)

A FastAPI backend now serves:

* The frontend website
* The blog generation API

This allows the entire platform to run from **a single server command**.

---

# Project Structure

```
BlogBoard-AI-Blog-Generator
│
├── backend
│   ├── api.py                # FastAPI backend server
│   ├── run.py                # Blog generation pipeline entry
│   ├── graph
│   │   ├── graph.py
│   │   ├── nodes.py
│   │   └── state.py
│   ├── prompts
│   │   ├── blog_generation.txt
│   │   └── metadata_generation.txt
│   └── data
│
├── frontend
│   ├── index.html
│   ├── category.html
│   ├── post.html
│   ├── css
│   ├── js
│   │   ├── blogs-data.js
│   │   ├── home.js
│   │   └── post.js
│   └── blogs
│       ├── ml
│       ├── dl
│       ├── nlp
│       ├── cv
│       ├── genai
│       ├── ainews
│       ├── statistics
│       └── custom
│
└── README.md
```

---

# Installation

Clone the repository:

```
git clone https://github.com/ashantfet/BlogBoard-AI-Blog-Generator.git
cd BlogBoard-AI-Blog-Generator
```

Create a virtual environment:

```
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

The system uses the Groq API for LLM inference.

---

# Running the Platform

Start the unified backend server:

```
uvicorn backend.api:app --reload --port 9000
```

Open the website:

```
http://localhost:8000
```

The server will:

* Serve the frontend website
* Handle blog generation requests
* Automatically update the blog database

---

# Generating Blogs

## From Website

1. Open the homepage
2. Enter a topic
3. Click **Generate Blog**

The article will automatically appear under the **Custom Blogs** category.

## From CLI

You can also generate blogs from the command line:

```
python backend/run.py --topic "Virat Kohli Biography"
```

---

# Example Generated Output

```
frontend/blogs/custom/virat-kohli-bio.md
frontend/blogs/custom/articles.json
```

The frontend automatically loads these files and displays the blog.

---

# Improvements Added

The following features were implemented to extend the original project:

### Custom Topic Support

Added CLI argument:

```
--topic
```

This allows generating blogs on any subject.

### Custom Blog Category

Created a new category for dynamically generated articles.

```
frontend/blogs/custom
```

### FastAPI Backend

Introduced a backend API to handle blog generation requests.

### Website Blog Generator

Added UI elements enabling users to generate blogs directly from the website.

### Unified Server

The platform now runs as a single web server instead of separate backend and frontend processes.

---

# Future Enhancements

Possible improvements include:

* AI generated blog thumbnails
* Automatic SEO analysis
* RSS feed generation
* Auto-publishing scheduler
* User accounts and authentication
* Deployment to cloud hosting platforms

---

# License

This project is released under the MIT License.

---

# Author

Ashant Kumar

GitHub
https://github.com/ashantfet

LinkedIn
https://www.linkedin.com/in/ashant-kumar-21a0941a5/

---

# Acknowledgment

Thanks to the original BlogBoard project contributors for the base architecture and AI pipeline implementation.
