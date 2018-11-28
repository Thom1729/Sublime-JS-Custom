import os
from contextlib import contextmanager
from tempfile import NamedTemporaryFile


@contextmanager
def atomic_replace(dest):
    with NamedTemporaryFile(
        mode="r+",
        dir=str(dest.parent),
        encoding='utf-8',
        delete=False,
    ) as temp:
        yield temp

        temp.flush()
        os.fsync(temp.fileno())
        temp.close()

        os.replace(
            temp.name,
            str(dest)
        )
