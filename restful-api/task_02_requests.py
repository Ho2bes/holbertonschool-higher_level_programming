#!/usr/bin/env python3
"""Consuming and processing data from an API using Python"""


import requests
import csv


def fetch_posts_and_titles():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code:", response.status_code)

    if response.status_code == 200:
        posts = response.json()

        with open('posts.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            for post in posts:
                writer.writerow({
                    'id': post['id'],
                    'title': post['title'],
                    'body': post['body']
                    })
                print(post['title'])
