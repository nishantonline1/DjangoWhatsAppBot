from django.http import HttpResponse
from rest_framework.decorators import api_view,renderer_classes
from twilio.twiml.messaging_response import MessagingResponse
from rest_framework.renderers import JSONRenderer
"""
The first thing we need to do in our chatbot is obtain the message entered by the user. This message comes in the payload of the POST request with a key of ’Body’. We can access it through Django’s request object:
"""

@api_view(['POST'])
@renderer_classes([JSONRenderer])
def whatsAppmsg(request):
    incoming_msg = request.data['Body'].lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if incoming_msg:
    
    #change below code for automated response
    
        if 'hi' in incoming_msg:
            quote = 'Hello'
            msg.body(quote)
            responded = True
        if 'order' in incoming_msg:
            quote = 'order details'
            msg.body(quote)
            # return a cat pic
            # msg.media('https://cataas.com/cat')
            responded = True
    if not responded:
        msg.body('Sorry!')
    return HttpResponse(str(resp))
