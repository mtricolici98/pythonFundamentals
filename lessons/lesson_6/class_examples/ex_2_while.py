should_run = True
while should_run:
    print('Something is runnning')
    stop = input('Should I keep running ? Type stop to stop:')
    if stop == 'stop':
        should_run = False
