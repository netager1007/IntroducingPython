# 11.1.2 프로세스
import multiprocessing as mp

def washer(dishes, output):   # 식기 세척기
    for dish in dishes:
        print('Washing', dish, 'dish')
        output.put(dish)

def dryer(input):            # 건조기
    while True:
        dish = input.get()
        print('Drying', dish, 'dish')
        input.task_done()

dish_queue = mp.JoinableQueue()
dryer_proc = mp.Process(target=dryer, args=(dish_queue,))
dryer_proc.daemon = True
dryer_proc.start()
dishes = ['salad', 'bread', 'entree', 'dessert']
washer(dishes, dish_queue)
dish_queue.join()
