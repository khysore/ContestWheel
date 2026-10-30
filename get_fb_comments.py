import os
import sys
import json
import requests

# Set via environment variables or replace with your actual values
PAGE_ACCESS_TOKEN = os.getenv("FB_PAGE_ACCESS_TOKEN", "YOUR_PAGE_ACCESS_TOKEN")
POST_ID = os.getenv("FB_POST_ID", "YOUR_POST_ID")


def get_post_comments(post_id: str, access_token: str):
    """Fetch comments from a Facebook Page post using the Meta Graph API."""
    if access_token == "YOUR_PAGE_ACCESS_TOKEN" or not access_token:
        print("Error: FB_PAGE_ACCESS_TOKEN is not configured.")
        print("Set the FB_PAGE_ACCESS_TOKEN environment variable or update the script.")
        sys.exit(1)

    if post_id == "YOUR_POST_ID" or not post_id:
        print("Error: FB_POST_ID is not configured.")
        print("Set the FB_POST_ID environment variable or update the script (format: {page_id}_{post_id}).")
        sys.exit(1)

    url = f"https://graph.facebook.com/v19.0/{post_id}/comments"
    params = {
        "fields": "from,message,created_time",
        "access_token": access_token,
        "limit": 100,
    }

    comments = []

    while url:
        response = requests.get(url, params=params if params else None)
        data = response.json()

        if "error" in data:
            print(f"API Error: {data['error'].get('message')}")
            break

        for item in data.get("data", []):
            poster_name = item.get("from", {}).get("name", "Anonymous / Private")
            message = item.get("message", "")
            created_time = item.get("created_time", "")
            comments.append({
                "name": poster_name,
                "comment": message,
                "created_time": created_time,
            })

        # Pagination for posts with more than 100 comments
        url = data.get("paging", {}).get("next")
        params = None

    return comments


def save_to_json(comments, filename="comments.json"):
    """Save retrieved comments to a JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(comments, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(comments)} comments to {filename}")


if __name__ == "__main__":
    print(f"Fetching comments for post: {POST_ID}...")
    comments = get_post_comments(POST_ID, PAGE_ACCESS_TOKEN)

    print(f"\nRetrieved {len(comments)} comment(s):\n")
    for idx, c in enumerate(comments, start=1):
        print(f"{idx}. [{c['name']}]: {c['comment']}")

    if comments:
        save_to_json(comments)
