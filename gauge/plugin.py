from response.result import Result


def install_location(a, q):
    return Result(message="""
By default the plugins are stored at `%APPDATA%\gauge\plugins` for windows and `~/.gauge/plugins` in mac and linux.

To install plugins at different location, set `GAUGE_HOME` environment variable to the custom location.
After setting the GAUGE_HOME env, run the install command.
The plugin will get installed at the `GAUGE_HOME` custom location.
""")


def offline_installation(a, q):
    return Result(message="""
If plugin installation fails due to a network connection issue, you can manually download the plugin distributable.
Install it using the -f flag. Example:
""", code="""
gauge --install {plugin_name} -f {path_to_zip_file}

gauge --install html-report -f html-report-1.0.3-darwin.x86.zip
""")
