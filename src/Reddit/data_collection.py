import praw
import json
import uuid
from Reddit import submission_data, database_interactions
import datetime as dt

#Instantiates the reddit instance
reddit = praw.Reddit('bot1',user_agent='bot1 user agent')
submission_dict = {}

# Returns 25 new posts from a designated subreddit
# If no subreddit is designated it retrieves from all
# Submission title, id, and created unix time are saved in posts_storage.json
def collect_submission_ids(designated_subreddit = 'all', sortBy = 'new', lim = 25):
    batchid = str(uuid.uuid4())
    
    for submission in sorter(designated_subreddit, sortBy, lim):
            set_submission(submission.id,submission.title,batchid,submission.created)
        
    #database_interactions.insert_submission_into_db(submission.id,submission.title,batchid,submission.created)
    flatten(submission_dict)
    database_interactions.insert_multiple_submissions_into_db(submission_dict)
def get_date(created):
        return dt.datetime.fromtimestamp(created)


def sorter(sub, sort, lim):
	sorter = {
        'hot': reddit.subreddit(sub).hot(limit=lim),
		'new': reddit.subreddit(sub).new(limit=lim),
		'rising': reddit.subreddit(sub).rising(limit=lim),
		'controversial': reddit.subreddit(sub).controversial(limit=lim),
		'top': reddit.subreddit(sub).top(limit=lim)
        }
	return sorter[sort]


def fast_submissions_grab():
        for submission in reddit.subreddit('all').new(limit = 25):
                print(submission.title)



def get_submission_dict():
    return submission_dict

def set_submission(sub_id, sub_title, batchId,submission_created):
    submission_dict[sub_id] = {}
    submission_dict[sub_id]['id']=sub_id
    submission_dict[sub_id]['title']=sub_title
    submission_dict[sub_id]["batchId"]=batchId
    submission_dict[sub_id]['submission_created']=str(submission_created)


def flatten(d):
    out = {}
    for key, val in d.items():
        if isinstance(val, dict):
            val = [val]
        if isinstance(val, list):
            for subdict in val:
                deeper = flatten(subdict).items()
                out.update({key + '_' + key2: val2 for key2, val2 in deeper})
        else:
            out[key] = val
    return out