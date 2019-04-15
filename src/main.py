
import time
import data_collection

def main():
    x = True
    while x:
        data_collection.collect_submission_ids()
        print ('Ran collection at: ' + str(time.time()))
        time.sleep(300) #sleep for 5 minutes before getting new submissions



if __name__ == '__main__':
    main()