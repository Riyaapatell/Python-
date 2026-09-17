# to-do list
task = []

def add_task():
    limit = int(input("how many task you want to add: "))

    for i in range(limit):
        tasks = input("Enter task: ")
        task.append(tasks)
    print("Added successfully""\n")

def view_task():
    if len(task) == 0:
        print("There's no task in the list!""\n")
    else:
        for i,taskss in enumerate(task,1):
            print(i,taskss)
def delete_task():


    if len(task) > 0:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(task):
            deleted_task = task.pop(number - 1)
            print("Deleted:", deleted_task,"\n")
        else:
            print("Invalid task number.","\n")

while True:
    print("----To-Do List----""\n")

    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit""\n")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_task()

    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("List exited""\n")
    else:
        print("Invalid choice""\n")

# weather api
import requests

api_key = "8613f15eda2c9291eb0ba3e4d47a823d"

city = input("Enter city: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Feels Like:", data["main"]["feels_like"], "°C")
    print("Minimum Temperature:", data["main"]["temp_min"], "°C")
    print("Maximum Temperature:", data["main"]["temp_max"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Weather:", data["weather"][0]["description"])
    print("Wind Speed:", data["wind"]["speed"], "m/s")
    print("Cloudiness:", data["clouds"]["all"], "%")
    print("Visibility:", data["visibility"], "m")
else:
    print("Entered city DNE./Entered a valid city.")