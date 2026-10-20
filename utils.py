
from pathlib import Path


OUTPUT_DIR = Path(__file__).parent / "outputs"
OUTPUT_FILE = OUTPUT_DIR / "generated_blog.txt"


def save_blog(blog):
    """Save generated blog content to a text file."""

    try:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
            file.write(blog)

        print(f"\nBlog saved successfully: {OUTPUT_FILE}")
        return True

    except OSError as error:
        print(f"Error saving blog: {error}")
        return False
