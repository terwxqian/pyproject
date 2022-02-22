import asyncio
import time

'''
# async def main():
#    print('hello')
#    await asyncio.sleep(1)
#    print('world')
# asyncio.run(main())

#------------------------------------------
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")
    await say_after(1, 'hello')
    await say_after(2, 'world')
    print(f"finished at {time.strftime('%X')}")
asyncio.run(main())

async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))
    task2 = asyncio.create_task(
        say_after(2, 'world'))
    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")

# ----------------------awaitable-coroutine
#  We say that an object is an awaitable object if it can be used in an await expression.
#  Many asyncio APIs are designed to accept awaitables.
#  There are three main types of awaitable objects: coroutines, Tasks, and Futures.
# #
async def nested():
    print('inside of the nested()')
    return 42

async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    print('call nested()')
    nested()

    # Let's do it differently now and await it:
    print('call await nested()')
    print(await nested())  # will print "42".
asyncio.run(main())
# -----------Tasks
async def nested():
    print('inside of the nested()')
    await asyncio.sleep(5)
    return 42

async def main():
    # Schedule nested() to run soon concurrently with "main()".
    print(f"started at {time.strftime('%X')}")
    print('create task of nested()')
    task = asyncio.create_task(nested())

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    await task
    print(f"end at {time.strftime('%X')}")
asyncio.run(main())
'''
# -----------futures-------------




