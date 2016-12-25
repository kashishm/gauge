from gauge.constants import DOCUMENTATION
from response.result import Result

ci_tools = {
    "go": "http://getgauge.io/documentation/user/current/advanced_readings/ci_integration/go.html",
    "snap": "http://getgauge.io/documentation/user/current/advanced_readings/ci_integration/snap.html",
    "travis": "http://getgauge.io/documentation/user/current/advanced_readings/ci_integration/travis.html",
    "teamcity": "http://getgauge.io/documentation/user/current/advanced_readings/ci_integration/teamcity.html",
}


def ci(args, query):
    if args["ci"] in ci_tools:
        key = args["ci"].capitalize() + " Gauge " + DOCUMENTATION
        return Result(message="""
Gauge can be easily integrated with {}. Steps to Integrate Gauge with {} tool:

* Install the Gauge and language plugin on CI machine
* Add gauge commands as tasks in CI to run tests. For example, to run the specs use `gauge specs`.
* Gauge returns html-reports, console output as result of execution which can be configured to view on CI.
""".format(args["ci"], args["ci"]), links={
            key: ci_tools[args["ci"]]
        })
    return Result(message="""
Gauge can be easily integrated with any Continuous Integration environment.
Unfortunately, the documentation is missing for {} tool.
""".format(args["ci"]))
