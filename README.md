# RITM: Robot In The Middle

RITM: Robot In The Middle, is a setup of a mitmproxy that pushes all the sniffed web transactions to an EK (Elasticsearch and Kibana) stack, in order to analyse, inspect and discover insigths about the performance of an application running on any client capable to use a web proxy. A robot (using robot framework) can run a set of defined assesments over the web traffic to automatically detect issues. The goal is to make easy to integrate this robot as part of any CI/CD cycle.
