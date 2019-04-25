import sqlite3

class scheduler:

	def insert_job_in_queue(self,id,batchId,submissionId,scheduledTime,job='collect', lim=25,sortBy='new',subreddit='all'):
		status = "in queue" 
		try:
				conn = sqlite3.connect('src\\Data\\submissions.db')
				sql = ''' INSERT INTO process_queue(id, job, lim, sortBy, subreddit, batchId, submissionId, status)
						  Values(?,?,?,?,?,?,?,?,?) '''
				cur = conn.cursor()
				cur.execute(sql,(id,job,lim,sortBy,subreddit,batchId,submissionId,scheduledTime,status))
				conn.commit()
				return cur.lastrowid
		except Exception as e:
			print(e)


	def check_queue(self,test =  'test'):
		try:
			conn = sqlite3.connect('src\\Data\\submissions.db')
			sql = ''' SELECT * FROM process_queue ORDER BY ROWID ASC LIMIT 1;
					  INSERT INTO process_queue(status) Values('in progress'); '''
			cur = conn.cursor()
			cur.executescript(sql)
			conn.commit()
			rows = cur.fetchall()
			final_result = [list(i) for  i in rows]
                #code for after check complete logic
                #switch for job type

		except Exception as e:
			print(e)
