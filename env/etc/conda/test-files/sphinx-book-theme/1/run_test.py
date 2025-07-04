import sys
from subprocess import call

FAIL_UNDER = "85"
COV = ["coverage"]
RUN = ["run", "--source=sphinx_book_theme", "--branch", "-m"]
PYTEST = ["pytest", "-vv", "--color=yes", "--tb=long"]
REPORT = ["report", "--show-missing", "--skip-covered", f"--fail-under={FAIL_UNDER}"]

SKIPS = [
    "build_book",
    "custombranch",
    "repository_buttons",
]

SKIP_OR = " or ".join(SKIPS)
K = ["-k", f"not ({SKIP_OR})"]


if __name__ == "__main__":
    sys.exit(
        # run the tests
        call([*COV, *RUN, *PYTEST, *K, "src/tests"])
        # maybe run coverage
        or call([*COV, *REPORT])
    )
