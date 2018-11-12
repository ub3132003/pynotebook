import faust

app = faust.App(
    'hello-world',
    broker='kafka://192.168.1.201:9092',
    value_serializer='raw',
)

greetings_topic = app.topic('test')

@app.agent(greetings_topic)
async def greet(greetings):
    async for greeting in greetings:
        print(greeting)