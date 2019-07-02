import pygal
from django.views.generic import TemplateView
from pygal.style import DarkStyle
from Reddit import database_interactions, submission_data


# bar_chart = pygal.Bar()                                            # Create a bar graph object
# bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])  # Add some values
# bar_chart.render_to_file('src\\Data\\bar_chart.svg')               # Save the svg to a file

def create_bar_chart(batchId = 'f89d1526-9017-4046-b06c-e4f59c683bb5'):
    b_chart = pygal.Bar()
    b_chart.title = "Matt's test bchart"
    test_batchid = database_interactions.select_submissions_by_batchId_from_db('f89d1526-9017-4046-b06c-e4f59c683bb5')
    votecountlist = list()
    for submission in test_batchid:
        submissionID = submission[0]
        submission = submission_data.submission_by_id(submission[0])
        votecount = submission.score
        votecountlist.insert(0,[submissionID,votecount])
    for item in votecountlist:
        b_chart.add(item[0],item[1])
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


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        # Instantiate our chart. We'll keep the size/style/etc.
        # config here in the view instead of `charts.py`.
        cht_fruits = pygal.Pie(
            height=600,
            width=800,
            explicit_size=True,
            style=DarkStyle
        )

        # Call the `.generate()` method on our chart object
        # and pass it to template context.
        context['cht_fruits'] = cht_fruits.generate()
        return context

