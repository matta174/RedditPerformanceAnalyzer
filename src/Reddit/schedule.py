import schedule
import sqlite3

class scheduler:


    def insert_job_in_queue(self,id,batchId,submissionId,scheduledTime,jobType='collect25new',subreddit='all'):
        try:
                conn = sqlite3.connect('src\\Data\\submissions.db')
                sql = ''' INSERT INTO process_queue(id, jobType, subreddit, batchId, submissionId, scheduledTime)
                          Values(?,?,?,?) '''
                cur = conn.cursor()
                cur.execute(sql,(id,jobType,subreddit,batchId,submissionId,scheduledTime))
                conn.commit()
                return cur.lastrowid
        except Exception as e:
                print(e)