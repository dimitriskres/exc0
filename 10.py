import sys
import inspect
import operator
import functools


def main(text):

    values = map(bin, map(ord, text))

    def fix(value):
        value = value[2:].zfill(7)
        value = value[:2] + value[-2:]
        return value

    values = iter(map(fix, values))

    step = 4
    nums = range(step)

    chunks = []
    subvalues = []
    while True:
        # Ensures that the iterator is fully exhausted even if it doesn't yield
        # the full amount. This means that there will be < 4 subvalues on the
        # last chunk if the total amount of values is not exactly divisible by 4
        for _ in nums:
            try:
                subvalues.append(next(values))
            except StopIteration:
                break
        try:
            chunk = functools.reduce(operator.add, subvalues)
        except TypeError:
            # subvalues was empty
            break
        chunks.append(chunk)
        subvalues.clear()

    values = (int(chunk, base = 2) for chunk in chunks)

    size_full = 0
    size_even = 0
    size_divs = ([3, 0], [5, 0], [7, 0])

    for value in values:
        size_full += 1
        size_even += not value % 2
        for size_div in size_divs:
            if value % size_div[0]:
                continue
            size_div[1] += 1

    results = (
        prec / size_full
        for prec
        in (size_even, *tuple(zip(*size_divs))[1])
    )

    return results


def serve():

    path = sys.argv[1]

    with open(path) as file:
        text = file.read()

    text = inspect.cleandoc(text)

    results = main(text)

    names = ('even', 'div3', 'div5', 'div7')

    for (name, result) in zip(names, results):
        print('{0}: ≃{1}%'.format(name, round(result * 100, 2)))


if __name__ == '__main__':
    serve()
