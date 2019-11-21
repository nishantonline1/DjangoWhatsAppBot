# DjangoWhatsAppBot

Build a WhatsApp Chatbot With Python, Django and Twilio

A chatbot is a software application that is able to conduct a conversation with a human user through written or spoken language. The level of “intelligence” among chatbots varies greatly. While some chatbots have a fairly basic understanding of language, others employ sophisticated artificial intelligence (AI) and machine learning (ML) algorithms to achieve an almost human conversational level.

In this tutorial I’m going to show you how easy it is to build a chatbot for WhatsApp using the Twilio API for WhatsApp and the Django framework for Python.

## Tutorial Requirements

To follow this tutorial you need the following components:

 * **Python 3.6 or newer.** If your operating system does not provide a Python interpreter, you can go to python.org to download an installer.
  
 * **Django.** We will create a web application that responds to incoming WhatsApp messages with it.
  
 * **ngrok.** We will use this handy utility to connect the Django application running on your system to a public URL that Twilio can connect to. This is necessary for the development version of the chatbot because your computer is likely behind a router or firewall, so it isn’t directly reachable on the Internet. If you don’t have ngrok it installed, you can download a copy for Windows, MacOS or Linux.
  
 * A smartphone with an active phone number and WhatsApp installed.
  
 * A Twilio account. If you are new to Twilio create a free account now. You can review the features and limitations of a free Twilio account.
