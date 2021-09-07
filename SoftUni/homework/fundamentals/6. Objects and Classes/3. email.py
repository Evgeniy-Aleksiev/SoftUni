class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
command = input()

while not command == "Stop":
    senders, receivers, contents = command.split()
    email = Email(senders, receivers, contents)
    emails.append(email)
    command = input()

index = [int(i) for i in input().split(", ")]

for x in index:
    emails[x].send()

for email in emails:
    print(email.get_info())

