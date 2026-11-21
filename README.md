# Redis Caching Demo - Blog Posts API

A hands-on mini-project demonstrating the performance improvements achieved by implementing Redis caching compared to direct database queries.

## 🎯 Objective
The primary goal of this project is to understand and visualize the power of Redis caching. We build a simple Blog Posts API with two distinct endpoints to compare response times and system efficiency.

## ⚡ Endpoints
- **`GET /posts/slow`**: Fetches blog posts directly from the SQLite database. (Simulates a standard, uncached API).
- **`GET /posts/fast`**: Fetches blog posts using a Redis caching layer. Falls back to the database only on a cache miss.

## 🛠️ Tech Stack
- **Backend Framework**: FastAPI (Python)
- **Database**: SQLite
- **Caching Layer**: Redis
- **Benchmarking**: Custom Python script using `time` and `requests`

## 📋 Prerequisites
- Python 3.8+
- Redis Server installed and running locally (or via Docker)

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/vlalit834/Redis-caching-demo.git
cd Redis-caching-demo