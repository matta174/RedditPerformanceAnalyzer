import praw
import json
import uuid
import sqlite3
import submission_data

#Instantiates the reddit instance
reddit = praw.Reddit('bot1',user_agent='bot1 user agent')


# Returns 25 new posts from a designated subreddit
# If no subreddit is designated it retrieves from all
# Submission title, id, and created unix time are saved in posts_storage.json
def collect_submission_ids(designated_subreddit = 'all'):
    batchid = str(uuid.uuid4())
    for submission in reddit.subreddit(designated_subreddit).new(limit=25):
       with open("src\\Data\\posts_storage.json", "r+") as json_file:
        data = json.load(json_file)
        new_submission = {'title': submission.title,
                          'id': submission.id,
                          'created': submission.created,
                          'batchid': batchid
        }

        data['posts'].append(new_submission)
        json_file.seek(0)
        json.dump(data,json_file,indent=4)
        json_file.truncate()
        insert_submission_into_db(submission.id,submission.title,batchid)
        print(submission.title)



# Returns a specific reddit submission by id
def lookup_specific_submission(id = 'bdazcw'):
    specific_submission = reddit.submission(id)
    return specific_submission

def insert_submission_into_db(submissionID, SubmissionName, BatchID):
        #mySubmission = [submissionID,SubmissionName,BatchID]
        try:
                conn = sqlite3.connect('src\\Data\\submissions.db')
                sql = ''' INSERT INTO submissions(SubmissionID, SubmissionName, BatchId)
                          Values(?,?,?) '''
                cur = conn.cursor()
                cur.execute(sql,(submissionID,SubmissionName,BatchID))
                conn.commit()
                return cur.lastrowid
        except Exception as e:
                print(e)


collect_submission_ids()
lookup_specific_submission()

