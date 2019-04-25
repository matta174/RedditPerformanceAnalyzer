from Reddit import data_collection, database_interactions
import praw

reddit = praw.Reddit('bot1',user_agent='bot1 user agent')
submission_dict = {}

def submission_by_id(sub_id):   #creates the object based on the submission id given
    submission = reddit.submission(id = sub_id)
    return submission

def get_submission_dict():
    return submission_dict

def set_submission(sub_id):
    submission_dict = {}
    submission = submission_by_id(sub_id)
    submission_dict[sub_id] = {}
    submission_dict[sub_id]['title']=submission.title
    submission_dict[sub_id]['author']=submission.author
    submission_dict[sub_id]["subreddit"]=submission.subreddit
    submission_dict[sub_id]['score']=submission.score
    submission_dict[sub_id]["comment_number"]=submission.num_comments
    submission_dict[sub_id]["time"]=submission.created_utc

def get_title(sub_id):
    submission = submission_by_id(sub_id)
    return submission.title

def get_author(sub_id):
    submission = submission_by_id(sub_id)
    return submission.author

def get_subreddit(sub_id):
    submission = submission_by_id(sub_id)
    return submission.subreddit

def get_score(sub_id):
    submission = submission_by_id(sub_id)
    return submission.score

def get_comment_num(sub_id):
    submission = submission_by_id(sub_id)
    return submission.num_comments

def get_time(sub_id):
    submission = submission_by_id(sub_id)
    return submission.created_utc

def get_ratio(sub_id):
    submission = submission_by_id(sub_id)
    return submission.upvote_ratio

def get_link(sub_id):
    submission = submission_by_id(sub_id)
    return submission.url

def is_adult(sub_id):
    submission = submission_by_id(sub_id)
    return submission.over_18

def get_batch_score(batchID):
        batch_score = 0
        batch = database_interactions.select_submissions_by_batchId_from_db(batchID[0])
        for submission in batch:
            batch_score += get_score(submission[0])
        return batch_score

