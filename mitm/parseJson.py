from datetime import datetime
import json
import base64
import uuid
import time
import pytz
import re
from elasticsearch import Elasticsearch

def response(flow):
    es = Elasticsearch()
    d = {}
    d["uuid"] = str(uuid.uuid4())
    d["timestamp"] = datetime.now(tz=pytz.utc).isoformat()
    d["duration_ms"] = (flow.response.timestamp_end - flow.request.timestamp_start) * 1000
    d["client"] = flow.client_conn.__repr__()
    d["client_net_address_port"] = str(flow.client_conn.address)
    d["client_net_address"] = re.sub(r':.*','',str(flow.client_conn.address))
    d["server"] = flow.server_conn.__repr__()
    d["server_net_address_port"] = str(flow.server_conn.address)
    d["server_net_address"] = re.sub(r':.*','',str(flow.server_conn.address))
    try:
        rqText = flow.request.text
    except:
        rqText = str(flow.request.raw_content)
    d["request"] = {
        "duration_ms": (flow.request.timestamp_end - flow.request.timestamp_start) * 1000,
        "timestamp_start": datetime.fromtimestamp(flow.request.timestamp_start, tz=pytz.utc).isoformat(),
        "timestamp_end": datetime.fromtimestamp(flow.request.timestamp_end, tz=pytz.utc).isoformat(),
        "method": flow.request.method,
        "url": flow.request.url,
        "host": flow.request.host,
        "http_version": flow.request.http_version,
        "query": [],
        "query_params": {},
        "scheme": flow.request.scheme,
        "text": rqText,
        "headers": {},
        "cookies": []
    }
    for k,v in flow.request.cookies.items():
        d["request"]["cookies"] = (k + "=" + v)
    for k,v in flow.request.headers.items():
        d["request"]["headers"][k.lower()] = v
    for p in flow.request.query:
        d["request"]["query"].append(p + "=" + flow.request.query[p])
        keyVal = re.sub(r'[\.:]','',p)
        d["request"]["query_params"][keyVal] = flow.request.query[p]
    try:
        rqText = flow.response.text
    except:
        rqText = str(flow.response.raw_content)
    d["response"] = {
        "delay_ms": (flow.response.timestamp_start - flow.request.timestamp_end) * 1000,
        "duration_ms": (flow.response.timestamp_end - flow.response.timestamp_start) * 1000,
        "timestamp_start": datetime.fromtimestamp(flow.response.timestamp_start, tz=pytz.utc).isoformat(),
        "timestamp_end": datetime.fromtimestamp(flow.response.timestamp_end, tz=pytz.utc).isoformat(),
        "cookies": [],
        "http_version": flow.response.http_version,
        "reason": flow.response.reason,
        "status_code": flow.response.status_code,
        "text": rqText,
        "headers": {}
    }
    for k,v in flow.response.cookies.items():
        d["response"]["cookies"] = (k + "=" + str(v))
    for k,v in flow.response.headers.items():
        d["response"]["headers"][k.lower()] = v
    print("{::..::}:" + json.dumps(d))
    res = es.index(index="mitmproxy", doc_type="request", body=d)
    print("es.index.res: " + str(res))
