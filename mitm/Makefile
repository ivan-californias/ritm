install-deps:
	sudo pip3.6 install elasticsearch pytz mitmproxy

clean:
	rm -rf out

run:
	mkdir -p out
	mitmdump --insecure --anticomp --stream 10k --script parseJson.py --port 8080 --onboarding-host hbotest.mitm.it | tee -a out/dirty-json.dump

run-view:
	mitmdump --insecure -z --stream 10k -s parse.py -d -p 8080 --onboarding-host hbotest.mitm.it
