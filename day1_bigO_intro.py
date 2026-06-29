contacts = {
    347: "Ramesh",
    102: "Sita",
    500: "Aarav"
}

print(contacts[347])






contact_list = ["Aarav", "Sita", "Ramesh", "Priya"]

def find_contact(name):
    for contact in contact_list:      #O(n)
        if contact == name:
            return f"{name} found!"
    return f"{name} not found."

print(find_contact("Ramesh"))