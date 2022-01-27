import sys
import inspect
import collections


def clean(text):

    check = lambda rune: rune.isalpha() or rune == ' '

    text = ''.join(filter(check, text))

    text = text.lower()

    return text


def get_most_common_counter_keys(counter, size):

    common_pairs = counter.most_common(size)

    common_split = zip(*common_pairs)
    common_keys = tuple(common_split)[0]

    return common_keys


def get_most_common(words, amount):

    counter = collections.Counter(words)

    common_values = get_most_common_counter_keys(counter, amount)

    return common_values


def get_most_common_words(words, amount):

    common_words = get_most_common(words, amount)

    return common_words


def get_most_common_words_prefixes(words, amount, size):

    prefixes = (word[:size] for word in words if not len(word) < size)
    prefixes = filter(bool, prefixes)

    common_prefixes = get_most_common(prefixes, amount)

    return common_prefixes


def main(text):

    text = clean(text)

    words = text.split(' ')
    words = filter(bool, words)
    words = tuple(words) # exhaust iterator for multiple usage

    common_words = get_most_common_words(words, 10)

    common_prefixes_2 = get_most_common_words_prefixes(words, 3, 2)

    common_prefixes_3 = get_most_common_words_prefixes(words, 3, 3)

    return (common_words, common_prefixes_2, common_prefixes_3)


def serve():

    path = sys.argv[1]

    with open(path) as file:
        text = file.read()

    text = inspect.cleandoc(text)

    results = main(text)

    for (index, result) in enumerate(results, start = 1):
        print('{0}) {1}'.format(index, ' '.join(result)))


if __name__ == '__main__':
    serve()
