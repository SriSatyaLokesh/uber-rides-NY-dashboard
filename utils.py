def get_locations():
    # Dictionary of important locations in New York
    list_of_locations = {
        "Madison Square Garden": {"lat": 40.7505, "lon": -73.9934},
        "Yankee Stadium": {"lat": 40.8296, "lon": -73.9262},
        "Empire State Building": {"lat": 40.7484, "lon": -73.9857},
        "New York Stock Exchange": {"lat": 40.7069, "lon": -74.0113},
        "JFK Airport": {"lat": 40.644987, "lon": -73.785607},
        "Grand Central Station": {"lat": 40.7527, "lon": -73.9772},
        "Times Square": {"lat": 40.7589, "lon": -73.9851},
        "Columbia University": {"lat": 40.8075, "lon": -73.9626},
        "United Nations HQ": {"lat": 40.7489, "lon": -73.9680},
    }
    return list_of_locations



def get_selection(month, day, selection):
    xVal = []
    yVal = []
    xSelected = []
    colorVal = [
        "#F4EC15",
        "#DAF017",
        "#BBEC19",
        "#9DE81B",
        "#80E41D",
        "#66E01F",
        "#4CDC20",
        "#34D822",
        "#24D249",
        "#25D042",
        "#26CC58",
        "#28C86D",
        "#29C481",
        "#2AC093",
        "#2BBCA4",
        "#2BB5B8",
        "#2C99B4",
        "#2D7EB0",
        "#2D65AC",
        "#2E4EA4",
        "#2E38A4",
        "#3B2FA0",
        "#4E2F9C",
        "#603099",
    ]

    # Put selected times into a list of numbers xSelected
    xSelected.extend([int(x) for x in selection])

    for i in range(24):
        # If bar is selected then color it white
        if i in xSelected and len(xSelected) < 24:
            colorVal[i] = "#FFFFFF"
        xVal.append(i)
        # Get the number of rides at a particular time
        yVal.append(len(totalList[month][day][totalList[month][day].index.hour == i]))
    return [np.array(xVal), np.array(yVal), np.array(colorVal)]
