import pytest
import httpx
import respx
from app.actions.discourse import get_topics_per_tag


@pytest.mark.asyncio
async def test_happy_path(mock_response_topics, mock_response_posts):
    mock_url_latest_json = "https://somesite.com/latest.json"
    mock_url_post_1 = "https://somesite.com/t/1/posts.json"
    mock_username = "testuser"
    mock_apikey = "testapikey"

    async with respx.mock() as respx_mock:
        respx_mock.get(mock_url_latest_json).respond(json=mock_response_topics, status_code=200)
        respx_mock.get(mock_url_post_1).respond(json=mock_response_posts, status_code=200)

        result = await get_topics_per_tag(
            topics_url=mock_url_latest_json, username=mock_username, apikey=mock_apikey
        )

        # Assertions
        assert len(result['topic_list']['topics']) == len(mock_response_topics['topic_list']['topics']) - 1


@pytest.mark.asyncio
async def test_uncooked_post(mock_response_topics, mock_response_post_without_cooked):
    mock_url_latest_json = "https://somesite.com/latest.json"
    mock_url_post_1 = "https://somesite.com/t/1/posts.json"
    mock_username = "testuser"
    mock_apikey = "testapikey"

    async with respx.mock() as respx_mock:
        respx_mock.get(mock_url_latest_json).respond(json=mock_response_topics, status_code=200)
        respx_mock.get(mock_url_post_1).respond(json=mock_response_post_without_cooked, status_code=200)

        result = await get_topics_per_tag(
            topics_url=mock_url_latest_json, username=mock_username, apikey=mock_apikey
        )

        # Assertions
        assert len(result['topic_list']['topics']) == 0


@pytest.mark.asyncio
async def test_request_failed_on_feed(mock_response_topics, mock_response_post_without_cooked):
    """Test that HTTPStatusError is raised when get_feed_topics fails."""
    mock_url_latest_json = "https://somesite.com/latest.json"
    mock_username = "testuser"
    mock_apikey = "testapikey"

    async with respx.mock() as respx_mock:
        respx_mock.get(mock_url_latest_json).respond(status_code=500)

        with pytest.raises(httpx.HTTPStatusError):
            await get_topics_per_tag(
                topics_url=mock_url_latest_json, username=mock_username, apikey=mock_apikey
            )


@pytest.mark.asyncio
async def test_request_failed_on_post(mock_response_topics, mock_response_post_without_cooked):
    """Test that HTTPStatusError is raised when get_post fails after retries."""
    mock_url_latest_json = "https://somesite.com/latest.json"
    mock_url_post_1 = "https://somesite.com/t/1/posts.json"
    mock_username = "testuser"
    mock_apikey = "testapikey"

    async with respx.mock() as respx_mock:
        respx_mock.get(mock_url_latest_json).respond(json=mock_response_topics, status_code=200)
        respx_mock.get(mock_url_post_1).respond(status_code=500)

        with pytest.raises(httpx.HTTPStatusError):
            await get_topics_per_tag(
                topics_url=mock_url_latest_json, username=mock_username, apikey=mock_apikey
            )