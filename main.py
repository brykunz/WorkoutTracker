userchoice = input("Type 'N' for new workout. 'E' to edit a workout. 'D' to delete a workout").lower()

if userchoice == 'n':
    # New workout
    workout = input("Enter your workout: ")
elif userchoice == 'e':
    # Edit workout
    workout = input("Enter the workout you want to edit: ")
    new_workout = input("Enter the new workout: ")
    print(f"Edited {workout} to {new_workout}")
elif userchoice == 'd':
    # Delete workout
    workout = input("Enter the workout you want to delete: ")
    print(f"Deleted {workout}")
else:   
    print("Invalid choice. Please enter 'N', 'E', or 'D'.")