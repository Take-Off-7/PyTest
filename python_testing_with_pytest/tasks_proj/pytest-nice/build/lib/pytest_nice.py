import pytest
import getpass

def pytest_addoption(parser):
    parser.addoption(
        "--nice",
        action="store_true",
        help="turn failures into opportunities"
    )

    parser.addini(
        "nice",
        type="bool",
        help="Turn failures into opportunity."
    )

def pytest_report_header(config):
        if config.getoption("--nice") or config.getini("nice"):  # 🎯 safe to access here
            return f"Thanks for running the tests, {getpass.getuser()}!"

def pytest_report_teststatus(report, config):
    if report.when == "call" and report.failed and config.getoption("nice"):
        return report.outcome, "O", "OPPORTUNITY for improvement"

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    if config.getoption("--nice") or config.getini("nice"):
        terminalreporter.write_sep("-", "Keep being amazing! 🚀")

