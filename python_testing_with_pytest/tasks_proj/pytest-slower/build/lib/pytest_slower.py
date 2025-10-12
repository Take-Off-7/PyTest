# conftest.py (plugin implementation)

import time
import pytest
import warnings


SLOW_THRESHOLD_FACTOR = 2.0
CACHE_KEY = "slower/test_durations"

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_call(item):
    start = time.time()
    outcome = yield
    duration = time.time() - start

    cache = item.config.cache
    durations = cache.get(CACHE_KEY, {})

    nodeid = item.nodeid
    prev = durations.get(nodeid)

    if prev is not None and duration > prev * SLOW_THRESHOLD_FACTOR:
        warnings.warn(f"test duration over 2x last duration ({prev:.2f}s -> {duration:.2f}s)")

    durations[nodeid] = duration
    cache.set(CACHE_KEY, durations)
