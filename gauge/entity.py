# -*- coding: utf-8 -*-
from gauge.constants import DOCUMENTATION
from response.fallback import fallback
from response.result import Result

gauge = Result(message="""
Gauge is an open source, light-weight cross-platform test automation tool with the ability to author test cases in the business language.
It has multi language and multi IDE support. Please visit http://getguage.io for more info.
""")

specification = Result(message="""
A specification describes a particular feature of the application under test and
contains test cases which can also act as your feature documentation.
""")

scenario = Result(message="""
A scenario represents a single flow/test case in a particular specification.
A specification must contain at least one scenario.
""")

context = Result(message="""
Contexts or Context steps are steps defined in a spec before any scenario.
They allow you to specify a set of conditions that are necessary for executing scenarios in a spec.
Context steps can be used to set up data before running scenarios.
""")

tag = Result(message="""
Tags are used to associate labels with specifications or scenarios.
Tags are written as comma separated values in the spec with a prefix `Tags:`.
""")

teardown = Result(message="""
Tear Down Steps are the steps defined in a spec after the last scenario.
They allow you to specify a set of clean-up steps after every execution of scenario in a spec.
They are used to perform a tear down function.
""")

concept = Result(message="""
Concepts provide the ability to combine re-usable logical groups of steps into a single unit.
It provides a higher level abstraction of a business intent by combining steps.
""")

step = Result(message="""
Steps are the executable components of your specification.
steps are the actions you want to perform in a scenario.
They are written as markdown unordered list items (bullet points).
""")

parameter = Result(message="""
Steps can be defined to take values as parameters so that they can be re-used with different parameter values.

The parameters passed into a step can be of different types:

* simple/static parameter
* dynamic parameter
* table parameter
* special parameter
""", links={
    DOCUMENTATION: "http://getgauge.io/documentation/user/current/gauge_terminologies/parameters/",
})

simple_parameter = Result(message="They are values passed into the steps in double quotes. Examples:",
                          code="""
* Create a “gauge-java” project
* Write “100” line specification
""")

table_parameter = Result(message="Markdown table passed into the steps as parameter. Example:",
                         code="""
* Create the following users
    |id| name |
    |--|------|
    |1 | john |
    |2 | mike |
""")

special_parameter = Result(message="""
Special parameters provide the ability to pass larger and richer data into the steps as parameters.
They are entered in angular brackets - <> in the step.
They contain 2 parts separated by a colon :

    <prefix:value>

* Prefix : This defines the type of special parameter. e.g. file, table.
* Value : This defines the value for the type of special parameter.


There are 2 types of special parameters available in Gauge
* File: These are used to read files and pass the file content as a string parameter to the underlying steps. Example: <file:email.txt>

* CSV: Tables are used to pass table value into steps read from an external CSV file. Example: <table:data.csv>
""")

dynamic_parameter = Result(message="They are values passed into the steps in angular brackets. Examples:",
                           code="* Create a <project> project")

plugins = Result(message="""
Plugins are an easy way to extend the features of gauge
There are various types of plugins that gauge currently supports.

* Language Plugins
* IDE Plugins
* Reporting Plugins
* Build Tool Plugins
""", links={
    DOCUMENTATION: "http://getgauge.io/documentation/user/current/plugins/"
})

config = Result(message="""
All the Gauge specific internal configurations are stored in gauge.properties file.
This file is present in the Gauge install location (GAUGE_ROOT).
These properties are key value pairs. Following are the different configurations available:

* gauge_repository_url
* gauge_templates_url
* runner_connection_timeout
* plugin_kill_timeout
* runner_request_timeout
* gauge_exclude_dirs
""", links={
    DOCUMENTATION: "http://getgauge.io/documentation/user/current/advanced_readings/configuration/"
})

entities = {
    "gauge": gauge,
    "specification": specification,
    "scenario": scenario,
    "context": context,
    "tag": tag,
    "teardown": teardown,
    "concept": concept,
    "step": step,
    "parameter": parameter,
    "simple parameter": simple_parameter,
    "table parameter": table_parameter,
    "special parameter": special_parameter,
    "dynamic parameter": dynamic_parameter,
    "plugins": plugins,
    "config": config,
}


def define(args, query):
    entity = args['entity'].lower()
    return entities[entity] if entity in entities else fallback(query)
