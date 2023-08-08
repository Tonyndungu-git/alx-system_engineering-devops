import requests

def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}

    headers = {'User-Agent': 'CustomUserAgent'}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after} if after else {}

    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        if 'data' in data and 'children' in data['data']:
            hot_posts = data['data']['children']
            for post in hot_posts:
                post_title = post['data']['title'].lower()

                for word in word_list:
                    if f" {word.lower()} " in f" {post_title} ":
                        counts[word] = counts.get(word, 0) + 1

            # Check for pagination (more posts available)
            after = data['data']['after']
            if after:
                count_words(subreddit, word_list, after=after, counts=counts)

        else:
            return None

    except requests.RequestException as e:
        print("An error occurred:", e)

    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")
