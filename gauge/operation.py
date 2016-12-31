from gauge.constants import DOCUMENTATION
from response.result import Result


def validate(a, q):
    return Result(message="Run the following command to print all the parse and validation errors.",
                  code="gauge --validate {path_to_specs_dir}")


def filter(a, q):
    return Result(message="""
Run the following command to filter your specs based on tags while execution.
""", code="gauge --tags {tag_expression} {path_to_specs_dir}", links={
        DOCUMENTATION: "http://getgauge.io/documentation/user/current/advanced_readings/execution_types/tagged_execution.html."
    })


def parallel(a, q):
    return Result(message="Run the following command to execute specs in parallel.",
                  code="gauge -p -n {number of streams} {path to specs dir}")


def serial(a, q):
    return Result(message="Run the following command to execute specs in serial.",
                  code="gauge {path_to_specs_dir}")
