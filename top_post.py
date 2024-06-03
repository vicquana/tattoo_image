import time
import random
from itertools import islice
from instaloader import Instaloader, Profile

def download_images(profile_name, npost):
    L = Instaloader()

    profile = Profile.from_username(L.context, profile_name)
    posts_sorted_by_likes = sorted(profile.get_posts(),
                                   key=lambda p: p.likes + p.comments,
                                   reverse=True)

    # Filter out video posts
    image_posts = (post for post in posts_sorted_by_likes if not post.is_video)

    # Download the top n image posts with delays
    for post in islice(image_posts, npost):
        try:
            L.download_post(post, profile_name)
            print(f"Downloaded post: {post}")
            # Add a random delay between requests
            time.sleep(random.uniform(5, 10))  # Delay between 5 to 10 seconds
        except Exception as e:
            print(f"Error downloading post: {e}")
            # Add a longer delay in case of an error
            time.sleep(random.uniform(10, 20))

# Example usage
PROFILE = "endlesstattoo.taipei"  # profile to download from
npost = 10  # number of posts to download
download_images(PROFILE, npost)
