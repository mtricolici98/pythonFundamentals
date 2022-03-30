import multiprocessing


def receiver(conn):
    """
    function to print the messages received from other
    end of pipe
    """
    while 1:
        print("Waiting to receive message")
        msg = conn.recv()
        if msg == "END":
            break
        print("Received the message: {}".format(msg))


if __name__ == "__main__":
    # messages to be sent

    # creating a pipe
    parent_conn, child_conn = multiprocessing.Pipe()

    # creating new processes
    p2 = multiprocessing.Process(target=receiver, args=(child_conn,))

    # running processes
    p2.start()

    while True:
        message = input()
        parent_conn.send(message)
        if message == "END":
            break

    # wait until processes finish
    p2.join()
