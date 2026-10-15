import requests

url = "http://localhost:8000/"

soap_request = """<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope
    xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:tns="spyne.examples.students">
    <soapenv:Header/>
    <soapenv:Body>
        <tns:get_all_students/>
    </soapenv:Body>
</soapenv:Envelope>
"""

response = requests.post(
    url,
    data=soap_request.encode("utf-8"),
    headers={"Content-Type": "text/xml; charset=utf-8"}
)

print("Code HTTP :", response.status_code)
print(response.text)

