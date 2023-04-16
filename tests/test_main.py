from core.infrastructure.modules.decorators import memoize
from core.tools.suite_runner.suite_runner import TestSuite


@memoize
def test_run_suite() -> None:
    run = TestSuite()
    run.execute(report=False)
