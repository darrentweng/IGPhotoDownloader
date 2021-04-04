""" Instagram Photo Downloader
----------------------------------------
"""
import instaloader
L = instaloader.Instaloader()

for post in instaloader.Hashtag.from_name(L.context, 'tbt').get_posts():
    # post is an instance of instaloader.Post
    L.download_post(post, target='tbt')