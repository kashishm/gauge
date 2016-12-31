# -*- coding: utf-8 -*-
from response.fallback import fallback
from response.result import Result

refactoring = "Refactoring is supported in {} language."
step = "Every step needs to have a language specific implementation that gets executed on the spec execution."
alias = """Multiple Step names for the same implementation.
The number and type of parameters for all the steps names must match the number of parameters on the implementation."""
custom_screenshot = """This is used when there is need to take CustomScreenshots and not the default one taken by Gauge
because you need only a part of the screen captured."""
data_stores = """Data(Objects) can be shared in steps defined in different classes at runtime using DataStores exposed by Gauge.
Suite, Spec, Scenario are the different type of data stores available in Gauge."""
hooks = """Test execution hooks can be used to run arbitrary test code as different levels during the test suite execution.
Before/After hooks are available at suite, spec, scenario, step in Gauge."""
continue_on_failure = "This feature provides a way to have a particular step implementation not break execution due to failure."

java = {
    "step implementation": Result(message=step, code="""
@Step("Say <greeting> to <product name>")
public void helloWorld(String greeting, String name) {
}
"""), "refactoring": Result(message=refactoring.format("Java")),
    "alias": Result(message=alias, code="""
@Step({"Say <greeting> to <product name>", "Wish <greeting> to <product name>"})
public void helloWorld(String greeting, String name) {
}
"""), "custom screenshot": Result(message=custom_screenshot, code="""
public class CustomScreenGrabber implements ICustomScreenshotGrabber {
    public byte[] takeScreenshot() {
    }
}
"""), "data stores": Result(message=data_stores, code="""
DataStore store = DataStoreFactory.get<type>DataStore();
store.put("element-id", "455678");
store.get("element-id");
"""), "hooks": Result(message=hooks, code="""
@BeforeSuite
public void hook() {
}
"""),
    "continue on failure": Result(message=continue_on_failure, code="""
@ContinueOnFailure
@Step("Say <greeting> to <product name>")
public void helloWorld(String greeting, String name) {
}
"""),
}

ruby = {
    "step implementation": Result(message=step, code="""
step 'Say <greeting> to <product name>' do |greeting, name|
end
"""), "refactoring": Result(message=refactoring.format("Ruby")),
    "alias": Result(message=alias, code="""
step 'Say <greeting> to <product name>', 'Wish <greeting> to <product name>' do |greeting, name|
end
"""), "custom screenshot": Result(message=custom_screenshot, code="""
Gauge.configure do |config|
    config.screengrabber =  -> {
    }
end
"""), "data stores": Result(message=data_stores, code="""
store = DataStoreFactory.<type>_datastore;
store.put("element-id", "455678");
store.get("element-id");
"""), "hooks": Result(message=hooks, code="""
before_spec do
end
"""),
    "continue on failure": Result(message=continue_on_failure, code="""
step 'Say <greeting> to <product_name>', :continue_on_failure => true do |greeting, name|
end
"""),
}

csharp = {
    "step implementation": Result(message=step, code="""
[Step({"Say <greeting> to <product name>", "Wish <greeting> to <product name>"})]
public void HelloWorld(string greeting, string name) {
}
"""), "refactoring": Result(message=refactoring.format("csharp")),
    "alias": Result(message=alias, code="""
[Step("Say <greeting> to <product name>")]
public void HelloWorld(string greeting, string name) {
}
"""), "custom screenshot": Result(message=custom_screenshot, code="""
public class CustomScreenGrabber : IScreenGrabber {
    public byte[] TakeScreenshot() {
    }
}
"""), "data stores": Result(message=data_stores, code="""
var store = DataStoreFactory.<type>DataStore;
store.Add("element-id", "455678");
var elementId = (string) store.Get("element-id");
var anotherElementId = store.Get<string>("element-id");
"""), "hooks": Result(message=hooks, code="""
[AfterSuite]
public void hook() {
}
"""),
    "continue on failure": Result(message=continue_on_failure, code="""
[ContinueOnFailure]
[Step("Say <greeting> to <product name>")]
public void HelloWorld(string greeting, string name) {
}
"""),
}

python = {
    "step implementation": Result(message=step, code="""
@step("Say <greeting> to <product name>")
def hello(a, b):
    #code
"""), "refactoring": Result(message=refactoring.format("Python")),
    "alias": Result(message=alias, code="""
@step(["Say <greeting> to <product name>", "Wish <greeting> to <product name>"])
def hello(a, b):
    #code
"""), "custom screenshot": Result(message=custom_screenshot, code="""
@screenshot
def take_screenshot():
    #code
"""), "data stores": Result(message=data_stores, code="""
DataStoreFactory.<type>_data_store().put(key, value)
DataStoreFactory.<type>_data_store().get(key)
"""), "hooks": Result(message=hooks, code="""
from getgauge.python import before_step

@before_step
def hook():
    #code
"""),
    "continue on failure": Result(message=continue_on_failure, code="""
@continue_on_failure
@step("Create a user <user name>")
def hello(user_name):
    #code
"""),
}

go = {
    "step implementation": Result(message=step, code="""
var _ = gauge.Step("Say <greeting> to <product name>", func (a, b string) {
})
"""), "refactoring": Result(message=refactoring.format("Go")),
    "alias": Result(message="Not supported in Go."),
    "custom screenshot": Result(message=custom_screenshot, code="""
gauge.CustomScreenshotFn = func() []byte {
}
"""), "data stores": Result(message=data_stores, code="""
Get<type>Store()[key] = value
value := Get<type>Store()[key]
"""), "hooks": Result(message=hooks, code="""
var _ = gauge.AfterScenario(function () {
}, []string{}, testsuit.AND)
"""),
    "continue on failure": Result(message="Not supported in Go."),
}

js = {
    "step implementation": Result(message=step, code="""
gauge.step(["Say <greeting> to <product name>", "Wish <greeting> to <product name>"], function (a, b) {
});
"""), "refactoring": Result(message=refactoring.format("JavaScript")),
    "alias": Result(message=alias, code="""
gauge.step("Say <greeting> to <product name>", function (a, b) {
});
"""), "custom screenshot": Result(message=custom_screenshot, code="""
gauge.screenshotFn = function () {
};
"""), "data stores": Result(message=data_stores, code="""
gauge.dataStore.<type>Store.put(key, value);
gauge.dataStore.<type>Store.get(key);
"""), "hooks": Result(message=hooks, code="""
gauge.hooks.beforeScenario(function () {
});
"""),
    "continue on failure": Result(message="Not supported in JavaScript."),
}

language_map = {
    "java": java,
    "ruby": ruby,
    "csharp": csharp,
    "python": python,
    "go": go,
    "javascript": js,
}


def language(a, q):
    return Result(
        message="""
Currently, Gauge supports following languages
""", links={
            'Java': 'http://getgauge.io/documentation/user/current/language_features/',
            'Ruby': 'http://getgauge.io/documentation/user/current/language_features/',
            'C#': 'http://getgauge.io/documentation/user/current/language_features/',
            'Python': 'http://gauge-python.readthedocs.io/en/latest/',
            'JavaScript': 'https://getgauge-contrib.github.io/gauge-js/',
            'Go': 'https://github.com/getgauge-contrib/gauge-go',
        })


def language_features(args, query):
    if args["language"] in language_map and args['feature'] in language_map[args['language']]:
        return language_map[args['language']][args['feature']]
    return fallback(query)
