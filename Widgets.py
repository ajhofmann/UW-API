from uwaterlooapi import UWaterlooAPI
uw = UWaterlooAPI(api_key="YOUR API KEY")
from Tkinter import *
import time


# Initialize Graphics
root = Tk()
root.geometry("1920x1000-5-30")

# Create button bar
selectionBar = Frame(root, relief = RAISED)
selectionBar.pack(fill=X)
selectionBar.config(background = '#ffffff')

# Create info box
infoBox = Frame(root)
infoBox.pack(fill=BOTH, expand = 1)

def initInfo():
    # Clear the infoBox frame
    for widget in infoBox.winfo_children():
        widget.destroy()
    # Gets date data and declares variables
    infoSes = []
    info = uw.infosessions()
    today = time.strptime(time.strftime("%x"), "%x")
    start = 0
    # Finds first info session that hasnt happened
    while today > time.strptime(info[start][u'date'].encode('utf-8'), "%B %d, %Y"):
        start += 1
    # Creates the display
    colors = ["#f2f2f2", "#ffffff"]
    for i in range(start, start+10):
        infoSes.append(Label(infoBox))
        infoSes[i-start].pack(fill = BOTH, expand = 1)
        message = "Day: " + info[i][u'date'] + " | Start Time: " + info[i][u'start_time'] + " | Employer: " +\
                  info[i][u'employer'] + " | Location: " + info[i][u'location']
        infoSes[i-start].config(text = message, background = colors[i%2])


# Creates the weather display
def initWeather():
    # Clear the infoBox frame
    for widget in infoBox.winfo_children():
        widget.destroy()
    # get weather from the API
    weather = uw.current_weather()
    # Create the 3 different rows
    tempBox = Frame(infoBox)
    tempBox.pack(fill = BOTH, expand = 1)
    windBox = Frame(infoBox)
    windBox.pack(fill = BOTH, expand = 1)
    percipBox = Frame(infoBox)
    percipBox.pack(fill = BOTH, expand = 1)
    # Create the boxes in each row
    tempLbl = ['', '', '' , '']
    windLbl = ['', '']
    percipLbl = ['', '', '']
    # All info needed to fill out the boxes
    tempinfo = [u'temperature_current_c', u'windchill_c', u'temperature_24hr_max_c', u'temperature_24hr_min_c']
    tempheader = ["Current Temperature: ", "Current Windchill: ", "24 Hour Maximum: ", "24 Hour Minimum: "]
    colors = ["#ffffff", "#e6e6e6"]
    colorsalt = ["#f2f2f2", "#d9d9d9"]
    windinfo = [u'wind_speed_kph', u'wind_direction_degrees']
    windheader = ["Wind Speed: ", "Wind Direction: "]
    percipinfo = [u'precipitation_15min_mm', u'precipitation_1hr_mm', u'precipitation_24hr_mm']
    percipheader =["Precipitation (Last 15 min): ", "Percipitation (Last Hour): ", "Percipitation (Last Day): "]
    # Create the labels and fill them out
    for i in range(4):
        tempLbl[i] = Label(tempBox)
        tempLbl[i].pack(fill = BOTH, side = LEFT, expand = 1)
        tempLbl[i].config(text = tempheader[i] + str(weather[tempinfo[i]]), font = 20, background = colors[i%2])
    for i in range(2):
        windLbl[i] = Label(windBox)
        windLbl[i].pack(fill = BOTH, side = LEFT, expand = 1)
        windLbl[i].config(text = windheader[i] + str(weather[windinfo[i]]), font = 20, background = colorsalt[(i+1)%2])
    for i in range(3):
        percipLbl[i] = Label(percipBox)
        percipLbl[i].pack(fill = BOTH, side = LEFT, expand = 1)
        percipLbl[i].config(text = percipheader[i] + str(weather[percipinfo[i]]), font = 20, background = colors[i%2])

# Creates the Menu Display, 0 = V1, 1 =Rev
def initMenu(x):
    #Clear the infoBox
    for widget in infoBox.winfo_children():
        widget.destroy()
    # set Arrays to deal with all the data
    day = ['', '', '', '', '']
    meals = [u'lunch', u'dinner']
    menu = [[], [], [], [], []]
    # get the raw data for each day
    for i in range(5):
        day[i] = uw.menu()[u'outlets'][x][u'menu'][i][u'meals']
    # put the data into lists of food
    for h in range(5):
        for i in range(2):
            for j in range(len(day[h][meals[i]])):
                menu[h].append(day[h][meals[i]][j][u'product_name'].encode('utf-8'))
                if menu[h][len(menu[h])-1][0:4] == "R - ":
                    menu[h][len(menu[h])-1] = menu[h][len(menu[h])-1][4:]
    # create the columns holding the menu items
    monday = Frame(infoBox)
    monday.pack(fill = BOTH, expand = 1, side = LEFT)
    tuesday = Frame(infoBox)
    tuesday.pack(fill = BOTH, expand = 1, side = LEFT)
    wednesday = Frame(infoBox)
    wednesday.pack(fill = BOTH, expand = 1, side = LEFT)
    thursday = Frame(infoBox)
    thursday.pack(fill = BOTH, expand = 1, side = LEFT)
    friday = Frame(infoBox)
    friday.pack(fill = BOTH, expand = 1, side = LEFT)
    days = [monday, tuesday, wednesday, thursday, friday]
    names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    colors = ["#ffffff", "#e6e6e6", "#f2f2f2", "#d9d9d9"]
    labels = []
    # Build the labels for each menu item and place them on
    for i in range(5):
            labels.append(Label(days[i]))
            labels[len(labels) - 1].pack(fill = BOTH)
            labels[len(labels) - 1].config(text = names[i], background = "#a6a6a6")
    for i in range(5):
        for j in range(len(menu[i])):
            labels.append(Label(days[i]))
            labels[len(labels) - 1].pack(fill = BOTH, expand = 1)
            labels[len(labels) - 1].config(text = menu[i][j], background = colors[((i+j)%2)+(i%2)*2])
            if j == 2:
                labels.append(Label(days[i]))
                labels[len(labels) - 1].pack(fill = BOTH)
                labels[len(labels) - 1].config(text = "Dinner: ", background = "#a6a6a6")



# Create option buttons
weatherBut = Button(selectionBar, relief = RAISED, text = " Weather ", command = lambda: initWeather())
weatherBut.pack(side = LEFT, fill = X, padx = 15, expand = 1)
weatherBut.config(background = '#80ffff')

revmenuBut = Button(selectionBar, relief = RAISED, text = " REVelations Cafe ", command = lambda: initMenu(1))
revmenuBut.pack(side = LEFT, fill = X, padx = 15, expand = 1)
revmenuBut.config(background = '#ff944d')

v1But = Button(selectionBar, relief = RAISED, text = " Village 1 Cafe ", command = lambda: initMenu(0))
v1But.pack(side = LEFT, fill = X, padx = 15, expand = 1)
v1But.config(background = '#ffff80')

infoBut = Button(selectionBar, relief = RAISED, text = " Information Sessions ", command = lambda: initInfo())
infoBut.pack(side = LEFT, fill = X, padx = 15, expand = 1)
infoBut.config(background = '#b3ffcc')

print(uw.infosessions())
mainloop()