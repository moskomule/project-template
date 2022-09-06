import contextlib
import time


@contextlib.contextmanager
def timeit(name: str = "") -> None:
    """Context manager to measure time

    >>> with timeit('for loop'):
    >>>     l = []
    >>>     for i in ragen(10):
    >>>         l.append(i)

    """

    t0 = time.perf_counter()
    yield
    t1 = time.perf_counter()
    print(f"block {name} took {(t1-t0):.3f}ms")
