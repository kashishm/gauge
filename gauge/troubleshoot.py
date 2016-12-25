from response.result import Result


def troubleshoot(args, query):
    return Result(message="Troubleshooting links", links={
        "Logs": "http://getgauge.io/documentation/user/current/troubleshooting/logs.html",
        "Installation": "http://getgauge.io/documentation/user/current/troubleshooting/installation.html",
        "Execution": "http://getgauge.io/documentation/user/current/troubleshooting/execution.html",
        "Intellij IDE plugin": "http://getgauge.io/documentation/user/current/troubleshooting/intellij.html",
    })
