import sys
import inspect
import collections


def main(data):

    lines = data.splitlines()
    lines = filter(bool, lines)

    stores = tuple(map(eval, lines))

    keys = stores[0].keys()

    print('Keys:', ' | '.join(keys))
    key = input('Pick: ')

    values = (store[key] for store in stores)

    counter = collections.Counter(values)

    common_value = counter.most_common(1)[0][0]

    # θεωρώ πως το μεγαλύτερο ή μικρότερο κειμένου είναι με βάση μεγέθους
    decide = lambda value: len(value) if isinstance(value, str) else value

    max_value = max(counter.keys(), key = decide)
    min_value = min(counter.keys(), key = decide)

    return (common_value, max_value, min_value)


def serve():

    path = sys.argv[1]

    with open(path) as file:
        data = file.read()

    data = inspect.cleandoc(data)

    results = main(data)

    names = ('popular ', 'largest ', 'smallest')

    for (name, result) in zip(names, results):
        print('{0}: {1}'.format(name, result))


if __name__ == '__main__':
    serve()
