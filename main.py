# Volleyball Varsity / Seatwork 1
from pyscript import document


# List of Volleyball Varsity members
varsity_members = ["Kailey Gayas", "Johanna Ramos", "Julienne Miranda",  "Hope Benitez",]

def verify_candidate(event):

    first_name = document.getElementById(
        "first_name"
    ).value.strip()

    last_name = document.getElementById(
        "last_name"
    ).value.strip()


    full_name = f"{first_name} {last_name}"


    is_member = full_name.lower() in [
        member.lower() for member in varsity_members
    ]


    messages = {
        True: (
            f"Congratulations, {full_name}! "
            "You are now part of the OBFV Volleyball Varsity!"
        ),
        False: (
            f"Sorry, {full_name}, your name is not "
            "on the varsity list."
        )
    }

    document.getElementById(
        "result"
    ).innerText = messages[is_member]