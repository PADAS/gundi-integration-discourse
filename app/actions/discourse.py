import asyncio

import backoff
import httpx
from urllib.parse import urljoin


def is_retryable_error(exception: httpx.HTTPStatusError) -> bool:
    """Only retry on 429 (rate limit) or 5xx server errors."""
    return exception.response.status_code == 429 or exception.response.status_code >= 500


@backoff.on_exception(
    backoff.expo,
    httpx.HTTPStatusError,
    max_tries=5,
    giveup=lambda e: not is_retryable_error(e),
    jitter=backoff.full_jitter,
)
async def get_post(*, topic: dict, post_url: str, username: str, apikey: str):
    headers = {
        'Api-key': apikey,
        'Api-Username': username,
        'Content-Type': 'application/json'
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.get(post_url, headers=headers)
        response.raise_for_status()
        post = response.json()
        return (topic, post)


async def get_feed_topics(*, topics_url:str, username:str, apikey: str):
    
    headers = {'Api-key': apikey, 'Api-Username': username, 'Content-Type': 'application/json'}

    async with httpx.AsyncClient() as client:
        response = await client.get(topics_url, headers=headers)
        if response.is_success:
            latest_feed = response.json()
            return latest_feed
        else:
            response.raise_for_status()
        

async def get_topics_per_tag(*, topics_url: str, username: str, apikey: str):

    if feed_data := await get_feed_topics(topics_url=topics_url, username=username, apikey=apikey):

        # Let KeyErrors bubble up through the action runner handler.
        all_topics = feed_data['topic_list']['topics']

        filtered_list = []

        topics = [topic for topic in all_topics if 'er-notify' in topic.get('tags', [])]

        # Limit concurrent requests to avoid rate limiting
        semaphore = asyncio.Semaphore(2)

        async def limited_get_post(**kwargs):
            async with semaphore:
                return await get_post(**kwargs)

        tasks = [
            limited_get_post(
                topic=topic,
                post_url=urljoin(topics_url, f'/t/{topic["id"]}/posts.json'),
                username=username,
                apikey=apikey
            )
            for topic in topics
        ]
        results = await asyncio.gather(*tasks)

        # Filter out topics without 'cooked' content
        for topic, item in results:

            post = item['post_stream']['posts'][0]
            if 'cooked' in post:
                topic['cooked'] = post['cooked']
                filtered_list.append(topic)
    
        feed_data['topic_list']['topics'] = filtered_list

        return feed_data
