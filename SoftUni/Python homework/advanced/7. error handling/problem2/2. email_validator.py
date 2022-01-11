from errors import NameTooShortError, MustContainAtSymbolError, InvalidDomainError
from valid_emails import VALID_EMAILS


def email_validator(email):
    try:
        name, domain = email.split('@')
    except ValueError:
        raise print(MustContainAtSymbolError("Email must contain @"))

    try:
        name_of_domain, extension = domain.split('.')
    except KeyError:
        raise print(InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net"))

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if extension not in VALID_EMAILS:
        raise print(InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net"))

    return 'Email is valid'


while True:
    command = input()

    if command == 'End':
        break

    print(email_validator(command))
