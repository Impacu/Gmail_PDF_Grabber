import imaplib
import email

# Connect to the Gmail IMAP server
imap_server = imaplib.IMAP4_SSL("imap.gmail.com")

# Log in to the account, Substitute "Password123 with a token 
# Or with your actual password"
imap_server.login("Reciever_Email", "Password123")

# Select the inbox- This allows the code to only check your inbox
imap_server.select("inbox")

# Search for unread emails from the sender
#Also helps not download copies of lables sent in the past
status, messages = imap_server.search(None, 'FROM "Sender_Email" UNSEEN')

# Get the list of email IDs
messages = messages[0].split()

# Iterate over the list of email IDs
for msg_id in messages:
    # Fetch the raw email data
    status, msg_data = imap_server.fetch(msg_id, "(RFC822)")

    # Parse the email data
    msg = email.message_from_bytes(msg_data[0][1])

    # Iterate over the attachments
    for part in msg.walk():
        # Check if the attachment is a PDF
        if part.get_content_type() == "application/pdf":
            # Get the filename
            filename = part.get_filename()

            # Save the attachment to the specific directory. Make sure to add the folder Location
            # Where you wish to download the pdfs
            with open(r"Where Ever You want it to download" + filename, "wb") as f:
                f.write(part.get_payload(decode=True))
# Still trying to figure out now how to print files created in the day
#Also want to use Task Scheduler that is preinstalled on Windows to run this code everyday
#So I wont even have to click on a button! It would just auto print
