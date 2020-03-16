

# Selected Data in the Histogram updates the Values in the DatePicker
@app.callback(
    Output("bar-selector", "value"),
    [Input("histogram", "selectedData"), Input("histogram", "clickData")],
)
def update_bar_selector(value, clickData):
    holder = []
    if clickData:
        holder.append(str(int(clickData["points"][0]["x"])))
    if value:
        for x in value["points"]:
            holder.append(str(int(x["x"])))
    return list(set(holder))


# Clear Selected Data if Click Data is used
@app.callback(Output("histogram", "selectedData"), [Input("histogram", "clickData")])
def update_selected_data(clickData):
    if clickData:
        return {"points": []}
