from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
username = 'athmanziri'
apikey   = '6083c1f67ac28d2fb5525ed9be1ffac58a1fcda9998fc9d64ba672ef1baf9414'
gateway = AfricasTalkingGateway(username, apikey)
try:
    lastReceivedId = 0;    
    while True:
        messages = gateway.fetchMessages(lastReceivedId)        
        for message in messages:
            print 'from=%s;to=%s;date=%s;text=%s;linkId=%s;' % (message['from'],
                                                                message['to'],
                                                                message['date'],
                                                                message['text'],
                                                                message['linKId']
                                                               )
            lastReceivedId = message['id']
    if len(messages) == 0:
        break            
except AfricasTalkingGatewayException, e:
    print 'Encountered an error while fetching messages: %s' % str(e)