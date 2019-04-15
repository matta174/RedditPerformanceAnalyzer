import pygal


# bar_chart = pygal.Bar()                                            # Create a bar graph object
# bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])  # Add some values
# bar_chart.render_to_file('src\\Data\\bar_chart.svg')               # Save the svg to a file


def create_bar_chart():
    b_chart = pygal.Bar()
    b_chart.title = "Matt's test bchart"
    b_chart.add("test column", [.84])
    b_chart.add('test column',[.4])
    b_chart.render_in_browser()


def create_radar_chart():
    radar_chart = pygal.Radar()
    radar_chart.title = 'V8 benchmark results'
    radar_chart.x_labels = ['Richards', 'DeltaBlue', 'Crypto', 'RayTrace', 'EarleyBoyer', 'RegExp', 'Splay', 'NavierStokes']
    radar_chart.add('Chrome', [6395, 8212, 7520, 7218, 12464, 1660, 2123, 8607])
    radar_chart.add('Firefox', [7473, 8099, 11700, 2651, 6361, 1044, 3797, 9450])
    radar_chart.add('Opera', [3472, 2933, 4203, 5229, 5810, 1828, 9013, 4669])
    radar_chart.add('IE', [43, 41, 59, 79, 144, 136, 34, 102])
    radar_chart.render_in_browser()


create_radar_chart()