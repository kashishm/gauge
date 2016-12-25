from response.result import Result

why = Result(message="""
The communication breakdowns between Developers and Business Stakeholders is a common risk of software development.
Gauge is an advanced automation tool that allows requirements to be written in a way that will be understood by
all roles in a project and help bridge the gap.

Some of the key features of Gauge that make it stand unique include:

* A rich markup based on markdown
* Simple, Flexible and Rich Syntax
* Business Language Tests : Supports the concept of executable documentation
* Consistent Cross Platform/Language Support for writing test code. Currently supported languages.
* Open Source, so it could be shared freely and improved by others as well
* A modular architecture with plugin support.
* Extensible through plugins and Hackable
* Supports External Data Sources
* Helps you create Maintainable and Understandable test suites
* IDE Support
""")


def gauge_info(args, query):
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


def why_gauge(args, query):
    return why


def examples(args, query):
    return Result(message="Following are the links to examples", links={
        "Java Selenium": "https://github.com/getgauge/gauge-example-java",
        "Java Sahi": "https://github.com/getgauge/gauge-example-sahi",
        "CSharp Selenium": "https://github.com/getgauge/gauge-example-csharp",
        "Ruby Selenium": "https://github.com/getgauge/gauge-example-ruby",
        "Groovy Selenium": "https://github.com/getgauge/gauge-example-groovy",
        "Python Selenium": "https://github.com/kashishm/gauge-example-python",
        "JS Selenium": "https://github.com/getgauge-contrib/gauge-js/blob/master/examples",
    })


def getting_started(args, query):
    return Result(message="""
The following links can help you get started.
""", links={
        "Getting Started": "http://getgauge.io/documentation/user/current/getting_started/",
        "Getting Started in 3 Steps": "http://getgauge.io/documentation/user/current/examples/getting_started_3_minutes.html",
        "Examples": "http://getgauge.io/documentation/user/current/examples/",
    })
