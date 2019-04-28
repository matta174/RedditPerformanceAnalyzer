import os
import time
import threading
from multiprocessing import Process
from queue import Queue
from Reddit import data_collection, submission_data, database_interactions, schedule

def main():
    x = True
    while x:
        #data_collection.fast_submissions_grab()
        check_queue = schedule.scheduler()
        p = Process(target= data_collection.collect_submission_ids())
        p2 = Process(target = check_queue.check_queue())
        p2.start()
        p2.join()
        p.start()
        p.join()
        #data_collection.collect_submission_ids()
        #time.sleep(300) #sleep for 5 minutes before getting new submissions



if __name__ == '__main__':
        main()