import asyncio
import os
import uuid
from io import BytesIO

from flask import Flask, request, Response


app = Flask(__name__)


@app.route('/animated/webp', methods=['POST'])
async def handle_animated_webp():
    emote_filename = f'{uuid.uuid4().hex}.gif'
    emote_content = request.get_data()

    emote_bytes = BytesIO(emote_content)

    pipe = await asyncio.create_subprocess_exec('convert', '-', '-coalesce', emote_filename, stdin=asyncio.subprocess.PIPE)

    await pipe.communicate(emote_bytes.read())

    with open(emote_filename, 'rb') as f:
        converted_emote = f.read()

    os.remove(emote_filename)

    return Response(converted_emote, status=200)


@app.route('/static/webp', methods=['POST'])
async def handle_static_webp():
    emote_filename = f'{uuid.uuid4().hex}.png'
    emote_content = request.get_data()

    emote_bytes = BytesIO(emote_content)

    pipe = await asyncio.create_subprocess_exec('convert', '-', emote_filename, stdin=asyncio.subprocess.PIPE)

    await pipe.communicate(emote_bytes.read())

    with open(emote_filename, 'rb') as f:
        converted_emote = f.read()

    os.remove(emote_filename)

    return Response(converted_emote, status=200)


@app.route('/animated/gif', methods=['POST'])
async def handle_animated_gif():
    emote_filename = f'{uuid.uuid4().hex}.gif'
    emote_content = request.get_data()

    emote_bytes = BytesIO(emote_content)

    pipe = await asyncio.create_subprocess_exec('convert', '-', '-coalesce', emote_filename, stdin=asyncio.subprocess.PIPE)
    await pipe.communicate(emote_bytes.read())

    with open(emote_filename, 'rb') as f:
        converted_emote = f.read()

    os.remove(emote_filename)

    return Response(converted_emote, status=200)


if __name__=='__main__':
    app.run(host='0.0.0.0', port=9000)
