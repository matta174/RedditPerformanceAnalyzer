import os
import time
import threading
from multiprocessing import Process
from queue import Queue
from Reddit import data_collection, submission_data, database_interactions, schedule

def main():
    x = True
    while x:
        s = schedule.scheduler()
        # batch_data = database_interactions.select_submissions_by_batchId_from_db('0ce5fcb9-1726-418d-bc7e-912ff128561b')
        # batch_data2 = submission_data.get_batch_data(batch_data)
        # database_interactions.update_value_in_submission_data('1_hour',batch_data2)
        p = Process(target= data_collection.collect_submission_ids())
        p2 = Process(target = s.schedule_listener())
        p2.start()
        p2.join()
        p.start()
        p.join()
        #data_collection.collect_submission_ids()
        time.sleep(300) #sleep for 5 minutes before getting new submissions



if __name__ == '__main__':
        main()