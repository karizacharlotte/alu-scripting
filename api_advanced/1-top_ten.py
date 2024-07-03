<<<<<<< HEAD

=======
>>>>>>> 0e4c101fba24b99c3b9ce2c50dd7dafba36e66b4
#!/usr/bin/python3
"""Script that fetch 10 hot post for a given subreddit."""
import requests


def top_ten(subreddit):
<<<<<<< HEAD
        """Return number of subscribers if @subreddit is valid subreddit.
            if not return 0."""

                headers = {'User-Agent': 'MyAPI/0.0.1'}
                    subreddit_url = "https://reddit.com/r/{}.json".format(subreddit)
                        response = requests.get(subreddit_url, headers=headers)

                            if response.status_code == 200:
                                        json_data = response.json()
                                                for i in range(10):
                                                            print(
                                                                            json_data.get('data')
                                                                                            .get('children')[i]
                                                                                                            .get('data')
                                                                                                                            .get('title')
                                                                                                                                        )
                                                                                                                                            else:
                                                                                                                                                    print(None)

=======
    """Return number of subscribers if @subreddit is valid subreddit.
    if not return 0."""

    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = "https://reddit.com/r/{}.json".format(subreddit)
    response = requests.get(subreddit_url, headers=headers)

    if response.status_code == 200:
        json_data = response.json()
        for i in range(10):
            print(
                json_data.get('data')
                .get('children')[i]
                .get('data')
                .get('title')
            )
    else:
        print(None)
>>>>>>> 0e4c101fba24b99c3b9ce2c50dd7dafba36e66b4
