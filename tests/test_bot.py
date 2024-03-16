import pytest
from aiogram import types
from app.main import command_start_handler, echo_handler


@pytest.mark.asyncio
async def test_command_start_handler():
    # Mocking the Message object
    message = types.Message(message_id=1, chat=types.Chat(id=1, type='private'),
                            from_user=types.User(id=1, is_bot=False, first_name='Test', last_name='User'))

    # Call the handler
    response = await command_start_handler(message)

    # Assert the response
    assert response.text == "Hello, Test User!"


@pytest.mark.asyncio
async def test_echo_handler_with_text_message():
    # Mocking the Message object
    message = types.Message(message_id=1, chat=types.Chat(id=1, type='private'), text='Test message',
                            from_user=types.User(id=1, is_bot=False, first_name='Test', last_name='User'))

    # Call the handler
    response = await echo_handler(message)

    # Assert the response
    assert response.text == 'Test message'


@pytest.mark.asyncio
async def test_echo_handler_with_unsupported_message_type():
    # Mocking the Message object with unsupported type (location)
    message = types.Message(message_id=1, chat=types.Chat(id=1, type='private'),
                            location=types.Location(latitude=1.0, longitude=1.0),
                            from_user=types.User(id=1, is_bot=False, first_name='Test', last_name='User'))

    # Call the handler
    response = await echo_handler(message)

    # Assert the response
    assert response.text == 'Nice try!'
