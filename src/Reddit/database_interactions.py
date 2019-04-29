import sqlite3
import re

def insert_submission_into_db(submissionID, SubmissionName, BatchID,created):
        try:
                conn = sqlite3.connect('src\\Data\\submissions.db')
                sql = ''' INSERT INTO submissions(SubmissionID, SubmissionName, BatchId, create_datetime)
                          Values(?,?,?,?) '''
                cur = conn.cursor()
                cur.execute(sql,(submissionID,SubmissionName,BatchID,created))
                conn.commit()
                return cur.lastrowid
        except Exception as e:
                print(e)

def select_submission_from_db(submissionID):
        try:
                conn = sqlite3.connect('src\\Data\\submissions.db')
                sql = "SELECT * FROM submissions WHERE SubmissionID=?"
                cur = conn.cursor()
                cur.execute(sql,(submissionID,))
                conn.commit()
                rows = cur.fetchall()
                return rows
        except Exception as e:
                print(e)

def select_submissions_by_batchId_from_db(batchId):
        try:
                conn = sqlite3.connect('src\\Data\\submissions.db')
                sql = "SELECT * FROM submissions WHERE BatchId=?"
                cur = conn.cursor()
                cur.execute(sql,(batchId,))
                conn.commit()
                rows = cur.fetchall()
                return rows
        except Exception as e:
                print(e)        

def get_all_batchIds_from_db():
        try:
                conn = sqlite3.connect('src\\Data\\submissions.db')
                sql = "select DISTINCT BatchId from submissions"
                cur = conn.cursor()
                cur.execute(sql)
                conn.commit()
                rows = cur.fetchall()
                final_result = [list(i) for  i in rows]
                return final_result
        except Exception as e:
                print(e)        


def insert_multiple_submissions_into_db(values):
        try:
                conn = sqlite3.connect('src\\Data\\submissions.db')
                cur = conn.cursor()
                values_list = list()
                for value in values.values():
                        values_list.append(([str(value.get('id')),str(value.get('title')),str(value.get('batchId')), str(value.get('submission_created'))] ))

                cur.executemany("INSERT INTO submissions(SubmissionID, SubmissionName, BatchId, create_datetime) VALUES(?,?,?,?)",values_list)
                conn.commit()
                return cur.lastrowid
        except Exception as e:
                print(e)