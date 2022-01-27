import sys
import inspect


def get_contiuum_chunks(runes, rune_slf):

    chunks = []

    start = None
    for (index, rune_oth) in enumerate(runes):
        if rune_oth == rune_slf:
            if start is None:
                start = index
            continue
        if start is None:
            continue
        chunks.append(slice(start, index))
        start = None

    if not start is None:
        chunks.append(slice(start, index + 1))

    return chunks


def get_max_continuum(values, rune):

    max_key = lambda chunk: chunk.stop - chunk.start

    max_chunk = slice(0, 0)
    max_size = max_key(max_chunk)
    max_value = None

    for value in values:
        chunks = get_contiuum_chunks(value, rune)
        chunk = max(chunks, key = max_key)
        size = max_key(chunk)
        if size > max_size:
            max_value = value
            max_chunk = chunk
            max_size = size

    return (max_value, max_chunk)


def main(text):

    values = map(bin, map(ord, text))

    fix = lambda value: value[2:].zfill(7)

    values = tuple(map(fix, values))

    runes = ('0', '1')

    results = (get_max_continuum(values, rune) for rune in runes)

    return tuple(zip(runes, results))


def serve():

    path = sys.argv[1]

    with open(path) as file:
        text = file.read()

    text = inspect.cleandoc(text)

    results = main(text)

    for (rune, (value, chunk)) in results:
        print(
            (
            '{0} ({1}) has the largest contiuum '
            'of {2} from index {3} to {4}'
            ).format(
                value,
                chr(int('0b' + value, base = 2)),
                rune, chunk.start, chunk.stop
            )
        )


if __name__ == '__main__':
    serve()
