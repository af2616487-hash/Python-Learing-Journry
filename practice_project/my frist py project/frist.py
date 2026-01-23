import random

subjects = [
    "Sharma Ji",
    "Angry Uncle",
    "Local Chaiwala",
    "WhatsApp University Professor",
    "Auto Rickshaw Driver",
    "Neighbour Aunty",
    "Government Clerk",
    "YouTube Baba",
    "Gym Trainer Bhaiya",
    "Startup Founder Bhai",
    "College Student",
    "Society Secretary",
    "Traffic Police Constable"
]

actions = [
    "started giving free gyaan to everyone",
    "went viral on WhatsApp in 5 minutes",
    "created traffic jam without any reason",
    "announced holiday without permission",
    "broke the internet with shocking statement",
    "fell asleep during important meeting",
    "blamed the system for everything",
    "became motivational speaker overnight",
    "launched startup with zero idea",
    "demanded chai instead of salary",
    "called himself national hero",
    "confused everyone with half knowledge"
]

places = [
    "Delhi Metro",
    "Mumbai Local Train",
    "Galli ka Nukkad",
    "Hostel Mess",
    "Shaadi ka Mandap",
    "Railway Platform No. 3",
    "Bangalore Traffic Signal",
    "Village Panchayat",
    "Parliament Canteen",
    "Coaching Centre",
    "Tea Stall",
    "Government Office"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)
    headline = f"BREAKING NEWS: {subject} {action} at {place}."
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()
    if user_input != 'yes':
        print("Thank you for using the headline generator. Have a great day!")
        break
