# Analytics tags assertions 
*** Settings ***
Library		ElasticSearchLib
Library		Collections

*** Variables ***
${ESHOST}	localhost
${ESPORT}	9200
${ESINDEX}	mitmproxy
# Analytics queries
${QUERY_1}	{"_source":["request.query_params.*","response.status_code"],"query":{"match_phrase":{"request.host":{"query":"hbolag.d2.sc.omtrdc.net"}}}}

*** Test Cases ***
Count the number of documents in ElasticSearch
	${count} =	es count	${ESHOST}	${ESPORT}	${ESINDEX}
	Log	All requests count is ${count}
	Should Be True	${count} > 200

Get list of requests for Analytics
	${docs} =	es search	${ESHOST}	${ESPORT}	${ESINDEX}	${QUERY_1}
	Log List	${docs}
