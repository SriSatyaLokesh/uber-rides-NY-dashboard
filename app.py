import dash
import dash_html_components as html



app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server

app.layout = html.Div(
   children=[
        html.H1("BUILD SOMETHING AWESOME")
   ]
)


if __name__ == "__main__":
    app.run_server(debug=True)