import sqlite3
from Reddit import data_collection
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


    def update_queue(self, id, status):
        try:
                conn = sqlite3.connect('src\\Data\\submissions.db')
                sql = ''' update process_queue SET status = ? WHERE jobId = ?'''
                cur = conn.cursor()
                cur.execute(sql,(status,id))
                conn.commit()
                return cur.lastrowid
        except Exception as e:
            print(e)


	# Status codes:
	# 0 = In Queue
	# 1 = In progress
	# 2 = Complete
	# 3 = Error / Misc
    def check_queue(self,test =  'test'):
        try:
                conn = sqlite3.connect('src\\Data\\submissions.db')
                sql = '''  SELECT * FROM process_queue where status = '0' ORDER BY ROWID ASC LIMIT 1 '''
                cur = conn.cursor()
                cur.execute(sql)
                conn.commit()
                rows = cur.fetchall()
                final_result = [list(i) for  i in rows]
                return final_result

        except Exception as e:
                print(e)

    


    def schedule_listener(self):
        try: 
                next_in_queue = self.check_queue()
                for value in next_in_queue:
                        if (value[1] == 'Collect'): 
                                data_collection.collect_submission_ids(value[4], value[3],value[2])
                                self.update_queue(value[0],'2')

                        else:
                                self.update_queue(value[0],'3')
                                
        except Exception as e:
                print(e)
