def validUsername (s):
    ok = ['-', '_']
    for c in s:
        if c not in ok and not c.isalpha() and not c.isdigit():
            return False

    return True

def validDomain (s):
    for c in s:
        if not c.isalpha() and not c.isdigit():
            return False

    return True

def validExt (s):
    if len(s) != 3:
        return False

    for c in s:
        if not c.isalpha() and not c.isdigit():
            return False

    return True


def fun(s):
    try:
        username, url = s.split("@")
        website, extension = url.split(".")
    except ValueError:
        return False
    
    if username.replace("-", "").replace("_", "").isalnum() is False:
        return False
    elif website.isalnum() is False:
        return False
    elif len(extension) > 3:
        return False
    else:
        return True


def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)


