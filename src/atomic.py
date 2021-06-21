import os
import os.path
from contextlib import contextmanager
from tempfile import NamedTemporaryFile
import logging

if False:  # Mypy
    from typing import Iterator, IO


logger = logging.getLogger(__name__)


@contextmanager
def atomic_replace(destination_path: str) -> 'Iterator[IO]':
    """Atomically replace the file at `dest` with a new file.

    If atomic replacement fails, remove `dest` and replace non-atomically.
    If all replacement fails, delete the temporary file.
    """
    destination_directory, destination_name = os.path.split(destination_path)
    with NamedTemporaryFile(
        mode="r+",
        dir=destination_directory,
        encoding='utf-8',
        delete=False,
        prefix=destination_name + '.temp-'
    ) as temp:
        temp_path = temp.name

        try:
            yield temp

            temp.flush()
            os.fsync(temp.fileno())
            temp.close()

            try:
                os.replace(temp_path, destination_path)
            except PermissionError:
                logger.warn('Could not atomically replace {}.'.format(destination_path))
                os.unlink(destination_path)
                os.replace(temp_path, destination_path)
        finally:
            try:
                os.unlink(temp_path)
            except FileNotFoundError:
                pass
