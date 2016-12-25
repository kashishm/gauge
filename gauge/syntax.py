from response.fallback import fallback
from response.result import Result

syntax = {
    "spec": Result(code="""
Specification name  or # Specification name
==================
"""),
    "scenario": Result(code="""
Scenario name or ## Scenario name
-------------
"""),
    "step": Result(code="* Step Name"),
    "tags": Result(code="Tags: login, admin"),
    "concept": Result(code="""
concept name  or # concept name
============
"""),
    "static parameter": Result(code="\"param\""),
    "dynamic parameter": Result(code="<param>"),
    "table parameter": Result(code="""
| id   |  name   |
|------|---------|
| 123  |  John   |
| 456  | Mcclain |
"""),
    "special parameter": Result(code="<prefix:value>"),
}


def cheat_sheet(args, query):
    return syntax[args["syntax"]] if args["syntax"] in syntax else fallback(query)
