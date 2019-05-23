#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from multiprocessing import Process
from threading import Thread
from Reddit import data_collection, schedule
import time



def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')


    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # s = schedule.scheduler()
    # collect_thread = Thread(target=collect_data)
    # check_queue_thread = Thread(target=check_queue)
    
    # check_queue_thread.start() 
    # collect_thread.start()
    execute_from_command_line(sys.argv)




def collect_data():
    while True:
        try:
            data_collection.collect_submission_ids()
        except:
            continue
        time.sleep(60 * 15)


def check_queue():
    while True:
        try:
            s.check_queue()
        except:
            continue
        time.sleep(15)


if __name__ == '__main__':
    main()
