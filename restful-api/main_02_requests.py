#!/usr/bin/python3
"""Simple runner for the JSONPlaceholder requests task."""

from task_02_requests import fetch_and_print_posts, fetch_and_save_posts


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
