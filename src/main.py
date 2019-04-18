import os
import time
from Reddit import data_collection, submission_data

def main():
    x = True
    while x:
        data_collection.collect_submission_ids()

        #time.sleep(300) #sleep for 5 minutes before getting new submissions

if __name__ == '__main__':
    main()