import time
from app.database import get_db_connection, init_db

def seed_database(num_posts=100000):
    print("Initializing database...")
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM posts")
    count = cursor.fetchone()[0]
    if count > 0:
        print(f"Database already has {count} posts. Skipping seed.")
        conn.close()
        return

    print(f"Seeding {num_posts} dummy blog posts")
    start_time = time.time()
    posts_data = [
        (
            f"Blog Post Title {i}",
            f"This is the detailed content for blog post number {i}. It contains some text to make the payload slightly heavier.",
            f"Author {i % 10}",
        )
        for i in range(1, num_posts + 1)
    ]

    cursor.executemany(
        """
        INSERT INTO posts (title, content, author) 
        VALUES (?, ?, ?)
    """,
        posts_data,
    )

    conn.commit()
    conn.close()

    end_time = time.time()
    print(
        f"Successfully seeded {num_posts} posts in {end_time - start_time:.2f} seconds."
    )


if __name__ == "__main__":
    seed_database(100000000)
