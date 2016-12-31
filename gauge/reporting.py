from gauge.constants import DOCUMENTATION
from response.fallback import fallback
from response.result import Result

reporting_plugins = {
    "xml": Result(message="""
XML Report plugin creates JUnit XML test result document that can be read by tools such as Go, Jenkins.
When the specs are executed, the xml report is generated in reports directory in the project.
The format of XML report is based on JUnit XML Schema(https://windyroad.com.au/dl/Open%20Source/JUnit.xsd).

To add xml-report plugins to the project, just run the following command:
""", code="gauge --add-plugin xml-report"),
    "spectacle": Result(message="""
This is a Gauge plugin that generates static HTML from Specification/Markdown files.
Ability to filter specifications and scenarios are available.
""", code="gauge --docs spectacle {specs_dir}"),
    "html": Result(message="""
Reports are generated using html-report plugin. By default html-report is added to the project.
When the specs are executed, the html report is generated in reports directory in the project by default.
"""),
}


def reporting(a, q):
    return Result(message="""
Gauge can generate following types of reports:

* spectacle: Static Conversion of specs into html.
* html-report: Generates html reports for current execution.
* xml-report: Generates junit syle xml reports for current execution.

To add above plugins to the project, just run the following command:.
""", code="gauge --add-plugin {plugin_name}", links={
        DOCUMENTATION: "http://getgauge.io/documentation/user/current/reporting_features/"
    })


def report_details(args, query):
    return reporting_plugins[args["plugin"]] if args["plugin"] in reporting_plugins else fallback(query)
