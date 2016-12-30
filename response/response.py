# -*- coding: utf-8 -*-
from gauge.ci import ci
from gauge.config import config
from gauge.entity import define
from gauge.errors import open_files, start_failed, validation_failed, gauge_api_error
from gauge.execution import execution
from gauge.ide import ide, ide_feature
from gauge.info import gauge_info, why_gauge, examples, getting_started
from gauge.init import project, initialization
from gauge.init import skeleton
from gauge.install import installation
from gauge.language import language, language_features
from gauge.operation import parallel, serial, validate, filter
from gauge.plugin import install_location, offline_installation
from gauge.reporting import reporting, report_details
from gauge.run import run_tool
from gauge.syntax import cheat_sheet
from gauge.troubleshoot import troubleshoot
from response.fallback import fallback

responses = {
    "ide": ide, "language": language, "reporting": reporting, "validate": validate, "filter": filter,
    "parallel execution": parallel, "serial execution": serial, "gauge info": gauge_info, "run tool": run_tool,
    "initialization": initialization, "installation": installation, "define": define, "why gauge": why_gauge,
    "examples": examples, "project": project, "skeleton": skeleton, "cheat sheet": cheat_sheet,
    "language features": language_features, "troubleshoot": troubleshoot, "report details": report_details,
    "ci": ci, "config": config, "execution": execution, "ide feature": ide_feature, "getting started": getting_started,
    "plugin install location": install_location, "plugin offline installation": offline_installation,
    "too many open files": open_files, "failed to start a runner": start_failed, "validation failed": validation_failed,
    "gauge api error": gauge_api_error,
}


def get_response(req):
    args = req['result']['parameters']
    intent = req['result']['metadata']['intentName'].lower()
    query = req['result']['resolvedQuery']
    return responses[intent](args, query) if intent in responses else fallback(query)
