import time
import queue
from multiprocessing import Process, Queue


def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.send(None)
        return cr
    return start


def follow(thefile, target):
    thefile.seek(0, 2)      # Go to the end of the file
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)    # Sleep briefly
            continue
        target.send(line)


@coroutine
def grep(pattern, target):
    try:
        while True:
            line = (yield)
            if pattern in line:
                target.send(line)
    except GeneratorExit:
        target.close()


@coroutine
def printer():
    try:
        while True:
            line = (yield)
            print(line)
    except GeneratorExit:
        pass


def data_source(target):
    for i in range(100):
        target.send(i)


@coroutine
def distributer(targets):
    t = 0
    batch = []

    try:
        while True:
            data = (yield)
            batch.append(data)
            if len(batch) == 8:
                if t == len(targets):
                    t = 0
                targets[t].send(batch)
                batch = []
                t = t + 1
    except GeneratorExit:
        if len(batch) > 0:
            if t == len(targets):
                t = 0
            targets[t].send(batch)
        for target in targets:
            target.close()


@coroutine
def processor(input_queue, output_queue):
    def process():
        while True:
            batch = input_queue.get()
            if batch is None:
                output_queue.put(None)
                break
            else:
                print("Process batch: {}".format(batch))
                output_queue.put(sum(batch))
        print("proc done")
        return

    p = Process(target=process)
    p.start()
    try:
        while True:
            batch = (yield)
            input_queue.put(batch)
    except GeneratorExit:
        input_queue.put(None)
        p.join()


@coroutine
def fan_in(output_queue, target):
    while True:
        try:
            print("fan in loop")
            data = output_queue.get(False, 1.0)
            print("got data {}".format(data))
            if data is None:
                print("data is None")
                target.close()
                return
            print(data)
            target.send(data)
        except queue.Empty:
            yield
    print("fan_in done")


@coroutine
def reducer():
    result = 0
    try:
        while True:
            i = (yield)
            result = result + i
    except GeneratorExit:
        pass
    print(result)


def main():
    input_queue = Queue()
    output_queue = Queue()

    r = reducer()
    fan_in(output_queue, r)
    processors = [processor(input_queue, output_queue)]
    d = distributer(processors)
    data_source(d)


if __name__ == "__main__":
    main()
