from functools import lru_cache as cache
from core.infrastructure.modules.suite_runner import TestSuite


@cache
def test_run() -> None:
    run = TestSuite()
    run.execute(report=True)
