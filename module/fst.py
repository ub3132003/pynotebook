# examples/agent.py
import faust

my_topic=App.topic("test")
@app.agent(my_topic)
async def process(stream):
    async for value in s:
        print(value)
if __name__ == '__main__':
    app.main()