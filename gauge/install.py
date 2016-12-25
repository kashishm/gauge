from response.fallback import fallback
from response.result import Result

install = {'windows': Result(message="""
Two ways to install Gauge on windows
* Run `choco install gauge`.
""", links={
    "Download installer": "http://getgauge.io/documentation/user/current/installations/operating_system/install_on_windows.html"
}),
           'linux': Result(links={
               "linux installation docs": "http://getgauge.io/documentation/user/current/installations/operating_system/install_on_linux.html"
           }),
           'mac': Result(message="""
Two ways to install Gauge on mac
* Run `brew install gauge`.
""", links={
               "Download installer": "http://getgauge.io/documentation/user/current/installations/operating_system/install_on_mac.html"
           }),
           }


def installation(args, query):
    return install[args['platform']] if args['platform'] in install else fallback(query)
