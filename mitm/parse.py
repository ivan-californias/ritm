import datetime


def response(flow):
    print ("")
    print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print (">>>> Request:")
    print (flow.request.method + " " + flow.request.url)
    for k,v in flow.request.headers.items():
        print (k + ": " + v)
    print ("")
    print (flow.request.raw_content)
    print ("")
    print ("<<<< Response:")
    print (flow.response.http_version + " " + str(flow.response.status_code) + " " + flow.response.reason)
    for k,v in flow.response.headers.items():
        print (k + ": " + v)
    print ("")
    print (flow.response.raw_content)
    print ("")
    print ("---- Info:")
    time = int((flow.response.timestamp_end - flow.request.timestamp_start) * 1000)
    print ("Time Elapsed: " + str(time) + "ms")
    print ("")

