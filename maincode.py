# -*- coding: utf-8 -*-

if __name__ == "__main__":
    from tweepysentiment import abcd, new_positive_cleaned_tokens_list, new_negative_cleaned_tokens_list, a, l

    abcd(new_positive_cleaned_tokens_list, new_negative_cleaned_tokens_list, a, l)

# import twilio
#
# import os
# from twilio.rest import Client
#
# # https://www.twilio.com/blog/retrieving-twilio-mms-image-urls-in-python
#
# # account_sid = os.environ.get('AC821d0ad24af33fe20a7d0376eefe567d')
# # auth_token = os.environ.get('9833e39ca17f403a3f34c2a7f79bf40b')
#
# # Your Account SID from twilio.com/console
# account_sid = 'AC821d0ad24af33fe20a7d0376eefe567d'
# # Your Auth Token from twilio.com/console
# auth_token = '9833e39ca17f403a3f34c2a7f79bf40b'
#
# # client = Client(account_sid, auth_token)
#
# # client.messages.create(from_=os.environ.get('+13604696761'),
# #                       to=os.environ.get('+19706328993'),
# #                       body='hey tell me something')
#
# client = Client(account_sid, auth_token)
#
# message = client.messages \
#     .create(
#     body='hai ra achyuth',
#     media_url='https://images.cinemaexpress.com/uploads/user/imagelibrary/2020/11/25/original/KGF_Chapter_2.JPG',
#     from_='+13604696761',
#     to='+19706328993'
# )
#
# print(message.sid)

# print(media.content_type)


#
# from flask import Flask, request, redirect
# from twilio.twiml.messaging_response import MessagingResponse
#
# app = Flask(__name__)
#
#
# @app.route("/sms", methods=['GET', 'POST'])
# def sms_reply():
#     # """Respond to incoming calls with a simple text message."""
#     # Start our TwiML response
#     resp = MessagingResponse()
#
#     # Add a message
#     resp.message("The Robots are coming! Head for the hills!")
#
#     return str(resp)
