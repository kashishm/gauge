from gauge.constants import DOCUMENTATION
from response.fallback import fallback
from response.result import Result

configs = {
    "gauge_repository_url": Result(message="""
This property is set to an url, which acts as plugin repository for Gauge.

Please do not change this url or it will break the installation and update of Gauge plugins.
""", code="gauge_repository_url = http://raw.github.com/getgauge/gauge-repository/master"),
    "gauge_templates_url": Result(message="""
This property is set to an url, which acts as template repository for Gauge.

Please do not change this url or it will break the project initialization using templates.
""", code="gauge_templates_url = https://dl.bintray.com/gauge/Templates"),
    "runner_connection_timeout": Result(message="""
This property sets the timeout in milliseconds for making a connection to the language runner.
""", code="runner_connection_timeout = 30000"),
    "plugin_connection_timeout": Result(message="""
This property sets the timeout in milliseconds for making a connection to plugins (except language runner plugins).
""", code="plugin_connection_timeout = 10000"),
    "plugin_kill_timeout": Result(message="""
This property sets the timeout in milliseconds for a plugin to stop after a kill message has been sent.
""", code="plugin_kill_timeout = 10000"),
    "runner_request_timeout": Result(message="""
This property sets the timeout in milliseconds for requests from the language runner.

If the size of the project is too big, Gauge may timeout before the runner returns the response message.
This value can be configured accordingly.
""", code="runner_request_timeout = 10000"),
    "gauge_exclude_dirs": Result(message="""
This property sets the excluded dirs for gauge.

Gauge always looks for concepts in the whole project, folders starting with dot(.) are excluded and
a user can add folders to the excluded folders list by passing a comma separated paths of folder.
Paths can be relative to the path of directory or absolute.
""", code='gauge_exclude_dirs = "src/test,bin"'),
}


def config(args, query):
    if args['config'] in configs:
        res = configs[args['config']]
        return Result(message=res.message, code=res.code, links={
            DOCUMENTATION: "http://getgauge.io/documentation/user/current/advanced_readings/configuration/",
        })
    return fallback(query)
