


def get_api():
    r = requests.get('https://api.github.com/user', auth=('user', 'pass'))

