def queueRequests(target, wordlists):
 engine = RequestEngine(endpoint=target.endpoint,
                    concurrentConnections=30,
                    requestsPerConnection=100,
                    pipeline=False
                    )

 for i in range(30):
     engine.queue(target.req, str(i), gate='race1')

 engine.openGate('race1')
 engine.complete(timeout=60)
def handleResponse(req, interesting):
 table.add(req)
