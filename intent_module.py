
import ollama


def detect_intent(user_request):
    """Detect the user's requested blog operation."""

    prompt = f"""
Classify the user's request into exactly one category.

Categories:
BLOG_GENERATION
SUMMARY
KEYWORD_GENERATION
META_DESCRIPTION

Rules:
- Writing or creating a blog means BLOG_GENERATION.
- Summarizing an existing blog means SUMMARY.
- Asking for SEO keywords means KEYWORD_GENERATION.
- Asking for an SEO meta description means META_DESCRIPTION.

Return only the category name.

User request: {user_request}
"""

    try:
        response = ollama.chat(
            model="qwen2.5:0.5b",
            messages=[
                {"role": "user", "content": prompt}
            ],
            options={
                "num_predict": 20,
                "temperature": 0
            }
        )

        result = response["message"]["content"].strip().upper()

        valid_intents = {
            "BLOG_GENERATION",
            "SUMMARY",
            "KEYWORD_GENERATION",
            "META_DESCRIPTION"
        }

        # Match the expected category even if the model adds text.
        for intent in valid_intents:
            if intent in result:
                print(f"\nDetected Intent: {intent}")
                return intent

        print("\nIntent could not be identified.")
        return None

    except Exception as error:
        print(f"Error detecting intent: {error}")
        return None
