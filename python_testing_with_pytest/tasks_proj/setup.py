from setuptools import setup, find_packages

setup(
    name="tasks",
    version="0.1.0",
    package_dir={"": "src"},  # tells setuptools that packages live under /src
    packages=find_packages(where="src"),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "tasks=tasks.cli:tasks_cli",  # enables "tasks list" in terminal
        ]
    },
)
