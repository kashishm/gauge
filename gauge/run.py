from response.result import Result

tools = {'maven': {
    'execution': Result(
        message='Run the following command to execute specs using Maven', code="mvn test"),
    'validation': Result(
        message='Run the following command to get all parse and validation errors using Maven',
        code='mvn -Dflags="--validate"'),
    'parallel execution': Result(
        message='Run the following command to execute specs in parallel using Maven',
        code="mvn gauge:execute -DspecsDir=specs -DinParallel=true -Dnodes=3"),
    'environment': Result(
        message='Run the following command to execute against a specific environment using Maven',
        code='mvn gauge:execute -DspecsDir=specs -Denv="dev"'),
    'profile': Result(
        message='Run the following command to execute specs that correspond to a particular test profile in pom.xml',
        code='mvn gauge:execute -P {profile-name}'),
    'tags': Result(
        message='Run the following command to execute specs by tags using Maven',
        code='mvn gauge:execute -DspecsDir=specs -Dtags="!in-progress"'),
    'flags': Result(
        message='Run the following command to add additional gauge flags to execution using Maven',
        code='mvn gauge:execute -DspecsDir=specs -Dflags="--verbose"'),
    'spec path': Result(
        message='Run the following command to specify specs directory using Maven',
        code='mvn gauge:execute -DspecsDir=specs'),
}, 'gradle': {
    'execution': Result(
        message='Run the following command to execute specs using Gradle',
        code="gradle gauge"),
    'validation': Result(
        message='Run the following command to get all parse and validation errors using Gradle',
        code='gradle gauge -PadditionalFlags="--validate"'),
    'parallel execution': Result(
        message='Run the following command to execute specs in parallel using Gradle',
        code='gradle gauge -PspecsDir=specs -PinParallel=true -Pnodes=3'),
    'environment': Result(
        message='Run the following command to execute against a specific environment using Gradle',
        code='gradle gauge -PspecsDir=specs -Penv="dev"'),
    'profile': Result(message='Not available in Gradle plugin'),
    'tags': Result(
        message='Run the following command to execute specs by tags using Gradle',
        code='gradle gauge -PspecsDir=specs -Ptags="!in-progress"'),
    'flags': Result(
        message='Run the following command to add additional gauge flags to execution using Gradle',
        code='gradle gauge -PadditionalFlags="--verbose"'),
    'spec path': Result(
        message='Run the following command to specify specs directory using Gradle',
        code='gradle gauge -PspecsDir=specs'),
}, 'commandline': {
    'execution': Result(
        message='Run the following command to execute specs',
        code='gauge <path_to_specs>'),
    'validation': Result(
        message='Run the following command to get all parse and validation errors',
        code='gauge --validate <path_to_specs>'),
    'parallel execution': Result(
        message='Run the following command to execute specs in parallel',
        code='gauge -p -n <number_of_nodes> <path_to_specs>'),
    'environment': Result(
        message='Run the following command to execute against a specific environment',
        code='gauge --env="dev" <path_to_specs>'),
    'tags': Result(
        message='Run the following command to execute specs by tags',
        code='gauge --tags="!in-progress" <path_to_specs>'),
    'format': Result(
        message='Run the following command to format specs',
        code='gauge --format <path_to_specs>'),
    'refactor': Result(
        message='Run the following command to refactor step',
        code='gauge --refactor <old_step> <new_step>'),
    'update': Result(
        message='Run the following command to update all or specific plugin',
        code="""
gauge --update-all // update all plugins

gauge --update <plugin_name> // update specific plugin
        """),
    'version': Result(
        message='Run the following command to print gauge and plugins version',
        code='gauge -v'),
    'install': Result(
        message="Use one of the following command to update plugin(s).",
        code="""
gauge --install-all // install all plugins mentioned in manifest.json

gauge --install <plugin_name> //install specific plugin
"""),
    'init': Result(
        message="Run the following command to initialize a project.",
        code='gauge --init <template>'),
    'rerun': Result(
        message="Run the following command to rerun failed specs in previous execution.",
        code='gauge --failed'),
}}


def run_tool(args, q):
    if args['runTool'] in tools and args['operation'] in tools[args['runTool']]:
        return tools[args['runTool']][args['operation']]
    return Result(message="Operation {} is not supported in {}".format(args['operation'], args['runTool']))
