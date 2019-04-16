import data_collection
import praw

reddit = praw.Reddit('bot1',user_agent='bot1 user agent')
submission_dict = { "id":[], \
                    "title":[], \
                    "author":[], \
                    "subreddit":[], \
                    "score":[], \
                    "comment_number":[], \
                    "time":[]}

def submission_by_id(sub_id):   #creates the object based on the submission id given
    submission = reddit.submission(id = sub_id)
    return submission

def get_submission(sub_id):
    return submission_dict

def set_submission(sub_id):
    submission = submission_by_id(sub_id)

    submission_dict["id"].append(sub_id)
    submission_dict["title"].append(submission.title)
    submission_dict["author"].append(submission.author)
    submission_dict["subreddit"].append(submission.subreddit)
    submission_dict["score"].append(submission.score)
    submission_dict["comment_number"].append(submission.num_comments)
    submission_dict["time"].append(submission.created_utc)

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
