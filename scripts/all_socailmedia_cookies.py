social_media_urls = [
    "https://www.facebook.com",
    "https://www.instagram.com",
    "https://www.twitter.com",
    "https://www.linkedin.com",
    "https://www.pinterest.com",
    "https://www.snapchat.com",
    "https://www.tiktok.com",
    "https://www.reddit.com",
    "https://www.youtube.com",
    "https://www.whatsapp.com",
    "https://www.telegram.org",
    "https://www.discord.com",
    "https://www.quora.com",
    "https://www.tumblr.com",
    "https://www.wechat.com",
    "https://www.vk.com",
    "https://www.medium.com",
]

from generic_web_scraper import get_cookies


def all_cookies():
    for url in social_media_urls:
        print(f"url:{url}")
        print(f"cookies:{get_cookies(url=url)}")
        print("\n")

all_cookies()