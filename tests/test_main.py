from core.infrastructure.modules.decorators import memoize
from core.infrastructure.modules.suite_runner import TestSuite


@memoize
def test_run() -> None:
    run = TestSuite()
    run.execute(report=False)
