
import threading
import time

import requests


def process_request(url, responses):
    response = requests.get(url)
    responses.append(response)


def process_single_thread(urls):
    start = time.time()
    responses = []
    for url in urls:
        responses.append(requests.get(url))
    print(responses)
    print(f'Single took {time.time() - start}')


def process_multi_thread(urls):
    start = time.time()
    responses = []
    threads = []
    for url in urls:
        threads.append(threading.Thread(target=process_request, args=(url, responses)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(responses)
    print(f'Multi-thread took {time.time() - start}')


def main():
    urls = [
        'http://www.example.com',
        'http://www.google.com',
        'http://www.yahoo.com',
        'http://www.stackoverflow.com/',
        'http://www.reddit.com/'
    ]
    process_single_thread(urls)
    process_multi_thread(urls)


main()
