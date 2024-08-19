import pytest
import aiohttp
from unittest.mock import AsyncMock
import asyncio
from four import fetch_status, fetch_all_statuses, main


@pytest.mark.asyncio
async def test_fetch_status():
    mock_response = AsyncMock()
    mock_response.status = 200

    mock_session = AsyncMock()
    mock_session.get = AsyncMock(return_value=mock_response)

    semaphore = asyncio.Semaphore(10)
    status = await fetch_status(mock_session, "https://example.com", semaphore, 1)

    assert status == 200


@pytest.mark.asyncio
async def test_fetch_all_statuses():
    mock_response = AsyncMock()
    mock_response.status = 200

    mock_session = AsyncMock()
    mock_session.get = AsyncMock(return_value=mock_response)

    statuses = await fetch_all_statuses("https://example.com", 50, 10)

    assert len(statuses) == 50
    assert all(status == 200 for status in statuses)


@pytest.mark.asyncio
async def test_main(tmp_path):
    output_file = tmp_path / "statuses.txt"

    await main("https://example.com", 10, 5, output_file)

    with open(output_file, 'r') as file:
        lines = file.readlines()

    assert len(lines) == 10
    assert all("Status 200" in line for line in lines)
