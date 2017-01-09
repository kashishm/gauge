from gauge.constants import DOCUMENTATION
from response.result import Result

intellij = {
    "install": Result(message="""
Plugin can be installed by downloading from Jetbrains plugin repository.

Steps to install Gauge Intellij IDEA plugin from IDE:

* Open the Settings dialog (e.g. ⌘ Comma), select Plugins.
* On the right-hand part of the dialog, click the Browse repositories button.
* In the dialog that opens, search for Gauge.
* Right-click on Gauge and select Download and Install.

""", links={
        DOCUMENTATION: "http://getgauge.io/documentation/user/current/ide_support/intellij_idea.html#installation",
    }),
    "init": Result(message="""
* File -> New Project.
* Choose 'Gauge'
* Choose the project location and java sdk
* Finish

Note: If gauge-java is not installed, it will download it for the first time.
"""),
    "autocomplete": Result(message="""
Steps present in the current project can be listed by invoking the auto completion pop up ctrl+space after the '*'.
After choosing a step, it gets inserted with parameters highlighted, you can press tab to cycle between the parameters.
"""),
    "quick fix": Result(message="""
If you have an unimplemented step in the spec file, it will be annotated saying 'undefined step'.
alt+enter can be pressed to open the quick fix pop up.
The destination of the implementation can be chosen, either a new class or from a list of existing classes.
It will then generate the step with required annotation and parameters.
"""),
    "format": Result(message="""
A spec file can be formatted by pressing ctrl+alt+shift l (in windows and linux) and cmd+alt+shift l(in mac).

This formats all the elements of current spec including indentation of tables and steps.
"""),
    "execution": Result(message="""
Specs can be executed by right click -> Run spec.
Execute all specs inside a directory by right click -> Run specifications
A single scenario can be executed by doing a right click on the scenario which should be executed and choosing the scenario.
right click -> run -> Scenario Name.
"""),
    "debug": Result(message="""
Debugging can be performed the same way spec execution works.

Right click on a specification or specs directory -> Debug. Execution will halt on marked breakpoints.
"""),
    "rename": Result(message="""
* Press Shift+F6 on a step to rename/rephrase it.
* The parameters will be in < > in the rephrase dialog. They can be reordered,removed or new parameters can be added.
* The rephrase/rename change will reflect across all the specs in the project.

"""),
    "find usage": Result(message="Press cmd/ctrl+alt+F7 on step/concept to see the usages."),
    "extract concept": Result(message="""
Concepts provide the ability to combine re-usable logical groups of steps into a single unit.
It provides a higher level abstraction of a business intent by combining steps.

To extract a concept:
* On the main menu or on the context menu of the selection, choose Refactor | Extract to Concept or press ⌥⌘C.
""", links={
        DOCUMENTATION: "http://getgauge.io/documentation/user/current/ide_support/features.html#extract-concept",
    }),
    "go to def": Result(message="Navigation from step to implementation (cmd/ctrl + b)")
}

vs = {
    "install": Result(message="""
* Open Visual Studio Extension Manager from Tools -> Extensions and Updates.
* Go to Visual Studio Gallery and search for Gauge VS2013.
* Click on Download and select Install option.
* Restart Visual Studio in order for the changes to take effect.
"""),
    "init": Result(message="""
* Go to File -> New Project.
* Choose Gauge Test Project under Visual C# Test category.
* Choose the Project location and Project Name.
* Click OK.
"""),
    "autocomplete": Result(message="""
This plugin hooks into VisualStudio Intellisense, and brings in autocompletion of Step text.
The step texts brought in is a union of steps already defined, concepts defined, and step text from implementation.

Hint: Hit Ctrl + Space to bring up the Intellisense menu.
"""),
    "quick fix": Result(message="""
Implement an unimplemented step - generates a method template, with a Step attribute having this Step Text.
"""),
    "format": Result(message="""
In the specification editor, right click -> format to format specification.
"""),
    "execution": Result(message="""
Open the Test Explorer : Menu -> Test -> Windows -> Test Explorer All the scenarios in the project should be listed.
Run one or more of these tests.
"""),
    "debug": Result(message="""
In the test explorer, select the scenarios -> right click -> debug. Execution will halt on marked breakpoints.
"""),
    "rename": Result(message="""
* Press F2 on a step to rephrase it.
* The parameters can also be reordered,removed or new parameters can be added.
* The rephrase change will reflect across all the specs in the project.
"""),
    "find usage": Result(message="Right click on a step -> Find All References"),
    "go to def": Result(message="""
Jump from Step text to it's implementation.

Usage: Right Click -> Go to Declaration or hit F12

"""),
}

ide_support = {
    "intellij": intellij,
    "vs": vs,
}


def ide(a, q):
    return Result(message="Gauge currently supports following IDE's",
                  links={
                      "IntelliJ": "http://getgauge.io/documentation/user/current/ide_support/intellij_idea.html",
                      "Visual Studio": "http://getgauge.io/documentation/user/current/ide_support/visual_studio.html",
                  })


def ide_feature(args, query):
    ide = args["ide"].lower()
    if ide in ide_support and args['ideFeature'] in ide_support[ide]:
        return ide_support[ide][args['ideFeature']]
    return Result(message="Feature {} is not supported in IDE {}.".format(args['ideFeature'], args['ide']))


def ide_feature_list(args, query):
    ide = args["ide_name"].lower()
    if ide in ide_support:
        return Result(message="""
Following are the features:
* """ + "* ".join(ide_support[ide].keys()))
    return Result(message="IDE {} is not supported.".format(args['ide_name']))
