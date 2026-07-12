from random import randint
from asyncio import sleep, Queue, run, create_task, to_thread

is_running = True

async def generate_request(queue: Queue):
    request = f"Заявка №{randint(1, 100)}"
    await queue.put(request)
    print(f"➕ {request} згенерована")
    await sleep(0.2)

async def generate_requests_loop(queue: Queue):
    while is_running:
        for _ in range(0, randint(1, 5)):
            if not is_running: 
                break
            await generate_request(queue)
        await sleep(randint(3, 5))

async def process_requests_loop(queue: Queue):
    while is_running or not queue.empty():
        if not queue.empty():
            request = await queue.get()
            print(f"⚙️ {request} опрацьовується...")
            await sleep(randint(1, 2))
            print(f"✅ {request} опрацьована")
            queue.task_done()
        else:
            await sleep(0.2)

async def main():
    global is_running
    queue = Queue()

    producer_task = create_task(generate_requests_loop(queue))
    consumer_task = create_task(process_requests_loop(queue))
    
    await to_thread(input, "Натисніть Enter у будь-який момент для завершення роботи програми...\n")
        
    print("Зупинка системи... Чекаємо доопрацювання черги.")
    is_running = False 
    
    await consumer_task
    producer_task.cancel()
    
    print("Програму успішно завершено.")

if __name__ == "__main__":
    run(main())
