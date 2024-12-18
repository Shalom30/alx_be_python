task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task but not time bound so consider completing it immediately "
                  f"you have"
                  f"time to spare.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is a medium priority task but it is time bound so make sure to do it as soon as "
                  f"you can"
                  f"since it is time bound.")
        else:
            print(f"Note: '{task}' is a medium priority task so make sure to do it as soon as you can. ")
    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a low priority task but it's time bound so consider doing it some time soon")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time. ")
