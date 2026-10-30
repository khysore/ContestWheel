# Facebook Comment Fetcher

A standalone Python script to fetch all comments and commenter names from a Facebook Page post using the Meta Graph API.

## Setup

1. **Install requirements**:
   ```powershell
   pip install -r requirements.txt
   ```

2. **Graph API Credentials**:
   - Go to [Meta for Developers](https://developers.facebook.com/).
   - In the **Graph API Explorer**, generate a **Page Access Token** with the permissions:
     - `pages_read_engagement`
     - `pages_read_user_content`
   - Find your **Post ID** (formatted as `{page_id}_{post_id}`).

3. **Running**:
   Pass values via environment variables:
   ```powershell
   $env:FB_PAGE_ACCESS_TOKEN = "your_token_here"
   $env:FB_POST_ID = "your_post_id_here"
   python get_fb_comments.py
   ```
   Or edit `get_fb_comments.py` directly to set your default values.
