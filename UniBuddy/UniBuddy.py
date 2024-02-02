"""
[Case Study Story] 
Imagine the first day of university for a freshman named Alex. 
Alex is excited but also overwhelmed by the vast campus, numerous courses, and the sea of new faces. 
To aid new students like Alex, the university's IT department has developed a personalised chatbot. 
This chatbot, named "UniBuddy", is designed to make the transition smoother for freshmen.
Upon accessing the chatbot, Alex is prompted to enter their name, favourite colour, and age. 
Based on this input, UniBuddy offers a personalised greeting.
For instance, if Alex's favourite colour is blue,
    UniBuddy might suggest joining the university's "Blue Art Club".
If Alex is 18, the chatbot might provide information about freshman-specific events.
The chatbot also offers a feature where Alex can input specific queries, like "Where is the library?"
    or "How do I join the debate club?", 
        and UniBuddy responds with relevant information, all while adhering to a friendly tone,
        using string transformation methods to ensure the responses feel personalised and engaging.
"""
import os
print("Current working directory:", os.getcwd())

print('''
Welcome to UniBuddy! Your all-in-one app that makes your freshman journey a bit easier to navigate!
      
      Please enter your details to get started: 
      ''')

while True:
    try:
        name = input("Please enter your name: ").capitalize()
        if not name.isalpha():
            print("Please enter a valid name.")
            continue
        
        fav_colour = input("Please enter your favourite colour: ")
        if not fav_colour.isalpha():
            print("Please enter a valid colour.")
            continue
        
        age = input("Please enter your age: ")
        if not age.isdigit():
            print("Please enter a valid age.")
            continue

        print(f"Hi {name}! Welcome to UniBuddy.")
        break

    except ValueError:
        print("You have entered an invalid value. Please try again.")

if int(age) < 18:
    print("You might be too young to be in university. Unless you skipped a grade or two, in that case, Welcome!")

elif int(age) >= 18 and int(age) <= 19:
    print('''
          Based on your age, I think you have just joined the university so welcome! Here are some activities I'd recommend for you to get settled in: \n
          1. There is a freshers fair happening in the main sports hall which will give you information on all the societies you can join (there will also be some freebies!).
          2. In the Great Hall there are information sessions every hour each day. You can also collect your student ID card from here.
          3. There are a few parties happening on campus throughout the week. It's a greaat place to meet new people!
          ''')
elif int(age) == 20:
    print('''
        Based on your age, I think you are in second year. Welcome back! \n
          Here are some activities you may be interested in:
          1. There is a freshers fair for returners in the main hall.
          2. The cinema club is having a pizza and movie night as a chance to relax before the academic year starts. You should check it out!
          3. The university is looking for volunteers to be a friendly face to the freshers.
        ''')
    answer = input("Would you be interested in volunteering? Type 'yes' for yes or anything else for no: ").lower()
    if answer == 'yes':
        print("That's great! I will add you to the list.")
    else:
        print("No worries! There are other things you can get involved with.")
else:
    print("Based on your age, I think you are in third year or above. You must be very familiar with the university. Welcome back!")

faq = open("UniBuddy_faq.txt", "r")

faq_list = []

for lines in faq:
    temp = lines.strip('\n')
    temp = temp.split()

    joined = " ".join(temp)
    faq_list.append(joined)

while True:
    print("Here is a list of our most frequently asked questions : ")
    for count, quest in enumerate(faq_list, start=1):
        print(f"{count}. {quest}")

    choice = int(input("Please enter the number question you'd like to ask : "))
    index = choice - 1

    if index == 0:
        print(f"You have chosen : {faq_list[index]}")
        print("The campus tour is happening on Monday, Wednesday and Friday at 11am, starting at the library.")
    elif index == 1:
        print(f"You have chosen : {faq_list[index]}")
        print("Download the app 'university' and sign in with your student number. Click the calendar icon to see your timetable. ")
    elif index == 2:
        print(f"You have chosen : {faq_list[index]}")
        print('''Welcome week: 18 September 2023 - 22 September 2023
            Autumn Term: 25 September 2023 - 8 December 2023
            Spring Term: 8 January 2024 - 22 March 2024
            Summer Term: 22 April 2024 – 21 June 2024''')
    elif index == 3:
        print(f"You have chosen : {faq_list[index]}")
        print("Go to the main sports hall where the freshers fair is taking place. You can also check online at 'societies.uni.com'.")
    elif index == 4:
        print(f"You have chosen : {faq_list[index]}")
        print("There are lots of transport links to get to the city centre from campus. The best way to travel troughout the city is any 'A' buses like 'A1', 'A4' etc.")
    elif index == 5:
        print(f"You have chosen : {faq_list[index]}")
        print("You can collect it in person from the Great Hall any time.")
    elif index == 6:
        print(f"You have chosen : {faq_list[index]}")
        print("Contact the Student Union at 'studentunion@university.ac.uk'.")
    else:
        print(" ")

    new_q = input("Would you like to ask another question? (y=yes, n=no): ")
    if new_q == "yes":
        continue
    else:
        print("Thank you for using this service.")
        break
