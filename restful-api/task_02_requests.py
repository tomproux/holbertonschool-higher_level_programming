#!/usr/bin/python3
"""Fetch posts from JSONPlaceholder and save them to CSV."""

import csv

import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch all posts and print their titles."""
    response = requests.get(API_URL, timeout=10)
    print(f"Status Code: {response.status_code}")

    if response.ok:
        posts = response.json()
        for post in posts:
            print(post.get("title", ""))

    return response


def fetch_and_save_posts():
    """Fetch posts and save a CSV file with selected fields."""
    response = requests.get(API_URL, timeout=10)

    if response.ok:
        posts = response.json()
        simplified_posts = [
            {"id": post.get("id"), "title": post.get("title"), "body": post.get("body")}
            for post in posts
        ]

        with open("posts.csv", "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(simplified_posts)

        return simplified_posts

    return []
