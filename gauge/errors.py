from response.result import Result


def open_files(a, q):
    return Result(message="""
This error occurs when the upper limit to open the number of files is too low.
To fix the error, increase the upper limit by adding the following command to your ~/.profile file and login again.
""", code="ulimit -S -n 2048")


def start_failed(a, q):
    return Result(message="""
The language plugin installed is not compatible with the gauge version installed.
Run the following command to install the latest compatible version.
""", code="gauge --install {language_plugin}")


def validation_failed(a, q):
    return Result(message="""
These generally occur if step implementation is not found for a particular step.

* Ensure the step implementation for the step has been added.
* The step template marking the step in code is case sensitive and should match the step usage in the spec file.
""")
