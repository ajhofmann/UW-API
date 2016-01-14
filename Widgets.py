from uwaterlooapi import UWaterlooAPI
uw = UWaterlooAPI(api_key="INSERT API KEY")
from Tkinter import *

# Initialize Graphics
root = Tk()
root.geometry("1920x1000")

# Create button bar
selectionBar = Frame(root, relief = RAISED)
selectionBar.pack(fill=X)
selectionBar.config(background = '#ffffff')

# Create info box
infoBox = Frame(root)
infoBox.pack(fill=BOTH, expand = 1)

def initWeather():
    for widget in infoBox.winfo_children():
        widget.destroy()
    weather = uw.current_weather()
    tempBox = Frame(infoBox)
    tempBox.pack(fill = BOTH, expand = 1)
    windBox = Frame(infoBox)
    windBox.pack(fill = BOTH, expand = 1)
    percipBox = Frame(infoBox)
    percipBox.pack(fill = BOTH, expand = 1)
    tempLbl = ['', '', '' , '']
    windLbl = ['', '']
    percipLbl = ['', '', '']
    tempinfo = [u'temperature_current_c', u'windchill_c', u'temperature_24hr_max_c', u'temperature_24hr_min_c']
    tempheader = ["Current Temperature: ", "Current Windchill: ", "24 Hour Maximum: ", "24 Hour Minimum: "]
    tempcolor = ["#b3d8ff", "#99cbff"]
    windinfo = [u'wind_speed_kph', u'wind_direction_degrees']
    windheader = ["Wind Speed: ", "Wind Direction: "]
    windcolor = ["#ccffcc", "#b3ffb3"]
    percipinfo = [u'precipitation_15min_mm', u'precipitation_1hr_mm', u'precipitation_24hr_mm']
    percipheader =["Precipitation (Last 15 min): ", "Percipitation (Last Hour): ", "Percipitation (Last Day): "]
    percipcolor = ["#0051cc", "#0065ff"]
    for i in range(4):
        tempLbl[i] = Label(tempBox)
        tempLbl[i].pack(fill = BOTH, side = LEFT, expand = 1)
        tempLbl[i].config(text = tempheader[i] + str(weather[tempinfo[i]]), font = 20, background = tempcolor[i%2])
    for i in range(2):
        windLbl[i] = Label(windBox)
        windLbl[i].pack(fill = BOTH, side = LEFT, expand = 1)
        windLbl[i].config(text = windheader[i] + str(weather[windinfo[i]]), font = 20, background = windcolor[i])
    for i in range(3):
        percipLbl[i] = Label(percipBox)
        percipLbl[i].pack(fill = BOTH, side = LEFT, expand = 1)
        percipLbl[i].config(text = percipheader[i] + str(weather[percipinfo[i]]), font = 20, background = percipcolor[i%2])


def initRev():
    for widget in infoBox.winfo_children():
        widget.destroy()
    day = ['', '', '', '', '']
    meals = [u'lunch', u'dinner']
    menu = [[], [], [], [], []]
    for i in range(5):
        day[i] = uw.menu()[u'outlets'][0][u'menu'][i][u'meals']
    for h in range(5):
        for i in range(2):
            for j in range(len(day[h][meals[i]])):
                menu[h].append(day[h][meals[i]][j][u'product_name'].encode('utf-8'))
                if menu[h][len(menu[h])-1][0:4] == "R - ":
                    menu[h][len(menu[h])-1] = menu[h][len(menu[h])-1][4:]
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
    colors = ["#ff4d4d", "#ff8080"]
    labels = []
    for i in range(5):
            labels.append(Label(days[i]))
            labels[len(labels) - 1].pack(fill = BOTH)
            labels[len(labels) - 1].config(text = names[i], background = "#cce0ff")
    for i in range(5):
        for j in range(len(menu[i])):
            labels.append(Label(days[i]))
            labels[len(labels) - 1].pack(fill = BOTH, expand = 1)
            labels[len(labels) - 1].config(text = menu[i][j], background = colors[(i+j)%2])
            if j == 2:
                labels.append(Label(days[i]))
                labels[len(labels) - 1].pack(fill = BOTH)
                labels[len(labels) - 1].config(text = "Dinner: ", background = "#cce0ff")



# Create option buttons
weatherBut = Button(selectionBar, relief = RAISED, text = " Weather ", command = lambda: initWeather())
weatherBut.pack(side = LEFT, fill = X, padx = 15, expand = 1)
weatherBut.config(background = '#80ffff')

revmenuBut = Button(selectionBar, relief = RAISED, text = " REVelations Cafe ")
revmenuBut.pack(side = LEFT, fill = X, padx = 15, expand = 1)
revmenuBut.config(background = '#ff944d')

v1But = Button(selectionBar, relief = RAISED, text = " Village 1 Cafe ", command = lambda: initRev())
v1But.pack(side = LEFT, fill = X, padx = 15, expand = 1)
v1But.config(background = '#ffff80')

infoBut = Button(selectionBar, relief = RAISED, text = " Information Sessions ")
infoBut.pack(side = LEFT, fill = X, padx = 15, expand = 1)
infoBut.config(background = '#b3ffcc')

mainloop()