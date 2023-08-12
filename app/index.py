from dash import Output, Input, callback

from app import app


# callbacks are here

@callback(
    Output('menu', 'opened'),
    Output('drawer-menu', 'opened'),
    Input('menu', 'opened'),
    Input('drawer-menu', 'opened'),
    prevent_initial_call=True,
)
def drawer_demo(opened_menu, opened_drawer):
    return (False, False) if not (opened_menu or opened_drawer) else (False, True)


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)
