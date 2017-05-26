# Be sure to import the helper gateway class
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
# Specify your login credentials
username = 'MyUsername'
apikey   = 'MyApikey'
# NOTE: If connecting to the sandbox, please use your sandbox login credentials
# Create a new instance of our awesome gateway class
gateway = AfricasTalkingGateway(username, apikey)
# NOTE: If connecting to the sandbox, please add the sandbox flag to the constructor:
#*************************************************************************************
#             ****SANDBOX****
#gateway    = AfricasTalkingGateway(username, apiKey, "sandbox");
# **************************************************************************************
# Any gateway errors will be captured by our custom Exception class below, 
# so wrap the call in a try-catch block
try:
    # Our gateway will return 10 messages at a time back to you, starting with
    # what you currently believe is the lastReceivedId. Specify 0 for the first
    # time you access the gateway, and the ID of the last message we sent you
    # on subsequent results
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



# @login_required(login_url='/login/')
# def sms_fetch_list(request):
#     lastReceivedId = 0
#     while True:
#         messages = gateway.fetchMessages(lastReceivedId)
#         for sms_message in messages:
#             sms_from = message['from']
#             sms_to = message['to']
#             sms_date = message['date']
#             sms_text = message['text']
#             sms_linkID = message['linkID']  
#     return render(request, 'sms_list.html', {'sms_message': sms_message})