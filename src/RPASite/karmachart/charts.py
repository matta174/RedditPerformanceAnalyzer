import pygal

from .models import Submissions
from Reddit import submission_data


class submissionPieChart():

    def __init__(self, **kwargs):
        self.chart = pygal.Pie(**kwargs)
        self.chart.title = 'Amount of submissions'

    def get_data(self):
        '''
        Query the db for chart data, pack them into a dict and return it.
        '''
        data = {}
        subids = []

        for item in Submissions.objects.all():
            subids.append(item.submissionid)
        score_list = submission_data.get_multi_score(subids)
        idx = 0
        for submission in Submissions.objects.all():
            submission.score = score_list[idx] #submission_data.get_score(submission.submissionid)
            idx += 1
            data[submission.submissionname] = submission.score
        return data

    def generate(self):
        # Get chart data
        chart_data = self.get_data()

        # Add data to chart
        for key, value in chart_data.items():
            self.chart.add(key, value)

        # Return the rendered SVG
        return self.chart.render(is_unicode=True)




class batchPieChart():

    def __init__(self,batchid, **kwargs):
        self.chart = pygal.Bar(**kwargs)
        self.chart.title = 'Submissions in ' + batchid
        self.batch = batchid

    def get_data(self):
        '''
        Query the db for chart data, pack them into a dict and return it.
        '''
        data = {}
        subids = []
        submissions = Submissions.objects.filter(batchid = self.batch)
        for item in submissions:
            subids.append(item.submissionid)
        score_list = submission_data.get_multi_score(subids)
        idx = 0
        for submission in submissions:
            submission.score = score_list[idx] #submission_data.get_score(submission.submissionid)
            idx += 1
            data[submission.submissionname] = submission.score
        return data

    def generate(self):
        # Get chart data
        chart_data = self.get_data()
        # Add data to chart
        for key, value in chart_data.items():
            self.chart.add(key, value)

        # Return the rendered SVG
        return self.chart.render(is_unicode=True)