from gauge.constants import DOCUMENTATION
from response.fallback import fallback
from response.result import Result

skeleton_files = {
    "env": """The env directory contains multiple environment specific directories.
Each directory has .property files which define the env variables set during execution for that specific environment.""",
    "specs": "The specs directory contains all the spec files for the project.",
    "manifest": "It contains gauge specific configurations which includes the information of plugins required in the project."
}

structure = """
On initialization of a gauge project for a particular language a project skeleton is created with the following files

* Env Directory - {}

* Specs Directory - {}

* Manifest file - {}

Project Structure:
"""


def project(args, query):
    return Result(message=structure.format(skeleton_files['env'], skeleton_files['specs'], skeleton_files['manifest']),
                  links={
                      DOCUMENTATION: "http://getgauge.io/documentation/user/current/getting_started/project_structure/",
                  },
                  code="""
|--- env --- default --- default.properties
|
|--- manifest.json
|
|--- specs --- example.spec
""")


def skeleton(args, query):
    return Result(message=skeleton_files[args['skeleton']] if args['skeleton'] in skeleton_files else fallback(query))


def initialization(args, query):
    return Result(
        message="Run `gauge --init {}` to initialize a {} project.".format(args['template'], args['template']))
