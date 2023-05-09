def generate_hashtag(text: str) -> str:
    _list: list = []
    new_text = text.split(' ')

    for each in new_text:
        result = each.title()
        _list.append(result.replace(' ', ''))
        result = "".join(_list)
        if len(new_text) == 1:
            return f'#{result.upper()}'
        return f'#{result}'


if __name__ == '__main__':
    print(generate_hashtag('sdfsd fdf'))
