from flask import Flask

from api.discovery import ServiceDiscovery
from api.services import ServiceList, ServiceDefinition

app = Flask(__name__)

@app.route("/services.<format>")
def service_list(format='xml'):
    service_list = ServiceList(format.lower())
    return response_from(service_list.get(), service_list.content_type())

@app.route("/services/<service_code>.<format>")
def service_definition(service_code, format='xml'):
    service_definition = ServiceDefinition(service_code, format.lower())
    return response_from(service_definition.get(), service_definition.content_type())

@app.route("/discovery.<format>")
def discovery(format='xml'):
    if format.lower() not in ['xml', 'json']:
        return "Un-Supported format"       #FIXME This needs to be implemented as per-spec. I am not sure what the spec is at the moment.
    discovery  = ServiceDiscovery(format.lower())
    return response_from(discovery.get(), discovery.content_type())


def response_from(body, content_type):
    response = app.make_response(body)
    response.headers['Content-Type'] = content_type
    return response

if __name__ == "__main__":
    app.run()
