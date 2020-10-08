def applyRules(email):
    emailParts = email.split("@")
    localName = emailParts[0]
    localName = localName.split("+")[0]
    localName = "".join(localName.split("."))
    return localName + "@" + emailParts[1]


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        newEmails = [applyRules(email) for email in emails]
        return len(set(newEmails))
