from gauge.constants import DOCUMENTATION
from response.fallback import fallback
from response.result import Result

types = {
    "parallel": Result(message="Run the following command to execute specs in parallel.",
                       code="gauge -p -n {number of streams} {path to specs dir}"),
    "serial": Result(message="Run the following command to execute specs in serial.", code="gauge {path_to_specs_dir}"),
    "tagged": Result(message="""
Tags allow you to filter the specs and scenarios quickly for execution.
To execute all the specs and scenarios which are labelled with certain tags, use the following command.
""", code='gauge --tags "tag1,tag2" specs'),
    "table driven": Result(message="""
When scenarios in a specification are to be executed for multiple sets of data then Data table execution can be used.
The header names from the table can be used in the steps by specifying in angular brackets `<>`(dynamic parameters).
On execution each scenario will be executed for every data row from the table.
""", links={
        DOCUMENTATION: "http://getgauge.io/documentation/user/current/advanced_readings/execution_types/table_driven_execution.html"
    })
}


def execution(args, query):
    return types[args["type"]] if args["type"] in types else fallback(query)
