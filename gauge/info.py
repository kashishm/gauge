from gauge.constants import READ_MORE
from response.result import Result


def gauge_info(a, q):
    return Result(message="""
Gauge is an open source, light-weight cross-platform test automation tool.
""", links={
        "Website": "http://getgauge.io",
        "Documentation": "http://getgauge.io/documentation/user/current/",
        "Getting Started": "http://getgauge.io/documentation/user/current/getting_started/",
        "Gitter": "https://gitter.im/getgauge/chat",
        "Twitter": "https://twitter.com/getgauge",
        "Github": "https://github.com/getgauge",
        "Google group": "https://groups.google.com/forum/#!forum/getgauge",
    })


def why_gauge(a, q):
    return Result(message="""
The communication breakdowns between Developers and Business Stakeholders is a common risk of software development.
Gauge is an automation tool that allows requirements to be written in a way that will be understood by all roles in a project and help bridge the gap.
""", links={
        READ_MORE: "http://getgauge.io/documentation/user/current/why_gauge.html"
    })


def examples(a, q):
    return Result(message="Following are the links to examples", links={
        "Java Selenium": "https://github.com/getgauge/gauge-example-java",
        "Java Sahi": "https://github.com/getgauge/gauge-example-sahi",
        "CSharp Selenium": "https://github.com/getgauge/gauge-example-csharp",
        "Ruby Selenium": "https://github.com/getgauge/gauge-example-ruby",
        "Groovy Selenium": "https://github.com/getgauge/gauge-example-groovy",
        "Python Selenium": "https://github.com/kashishm/gauge-example-python",
        "JS Selenium": "https://github.com/getgauge-contrib/gauge-js/blob/master/examples",
    })


def getting_started(a, q):
    return Result(message="""
The following links can help you get started.
""", links={
        "Getting Started": "http://getgauge.io/documentation/user/current/getting_started/",
        "Getting Started in 3 Steps": "http://getgauge.io/documentation/user/current/examples/getting_started_3_minutes.html",
        "Examples": "http://getgauge.io/documentation/user/current/examples/",
    })
