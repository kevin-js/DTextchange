"""
	description: Python script responsible for receiving emails from the
	front-end and sending it to the dartmouthtextchange@gmail.com account
"""
import sys, os

DESTINATION_ADDRESS = 'dartmouthtextchange@gmail.com'

email_sender = sys.argv[1]
email_subject = sys.argv[2]
email_body = sys.argv[3]