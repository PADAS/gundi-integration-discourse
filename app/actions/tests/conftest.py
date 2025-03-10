import pytest

@pytest.fixture
def mock_response_topics():
    # Mock Discord client setup
    data = {'topic_list': {'can_create_topic': True, 'more_topics_url': '/latest?no_definitions=true&page=1', 'per_page': 30, 'top_tags': ['er-notify', 'training', 'tableau', 'er-admin', 'tableau-site', 'reports', 'cta', 'integration', 'integrations', 'connectivity', 'cybertracker', 'er-mobile', 'eruc23', 'gundi', 'impact', 'radios', 'tech', 'tech4wildlife', 'user-access-control'], 'topics': [{'id': 1, 'title': 'EarthRanger Mobile 2.8.2 Release Notes', 'fancy_title': 'EarthRanger Mobile 2.8.2 Release Notes', 'slug': 'earthranger-mobile-2-8-2-release-notes', 'posts_count': 7, 'reply_count': 3, 'highest_post_number': 7, 'image_url': None, 'created_at': '2025-02-06T17:40:58.750Z', 'last_posted_at': '2025-03-06T07:18:26.344Z', 'bumped': True, 'bumped_at': '2025-03-06T07:29:32.045Z', 'archetype': 'regular', 'unseen': False, 'pinned': False, 'unpinned': None, 'visible': True, 'closed': False, 'archived': False, 'bookmarked': None, 'liked': None, 'tags': ['er-notify'], 'tags_descriptions': {}, 'views': 45, 'like_count': 3, 'has_summary': False, 'last_poster_username': 'someoneelse', 'category_id': 8, 'pinned_globally': False, 'featured_link': None, 'posters': [{'extras': None, 'description': 'Original Poster', 'user_id': 344, 'primary_group_id': 45, 'flair_group_id': 45}, {'extras': None, 'description': 'Frequent Poster', 'user_id': 233, 'primary_group_id': 45, 'flair_group_id': 43}, {'extras': None, 'description': 'Frequent Poster', 'user_id': 863, 'primary_group_id': 44, 'flair_group_id': 44}, {'extras': 'latest', 'description': 'Most Recent Poster', 'user_id': 1256, 'primary_group_id': 45, 'flair_group_id': 45}], 'cooked': '<p>We’re excited to share the latest updates in EarthRanger, including new features, interface improvements, and important bug fixes.</p>\n<p>Here’s what’s new:</p>\n<p><img src="https://community.earthranger.com/images/emoji/apple/star2.png?v=12" title=":star2:" class="emoji" alt=":star2:" loading="lazy" width="20" height="20"> <strong>New Features</strong></p>\n<ul>\n<li><strong>Filter Events by Date and Time</strong> – You can now filter events in the Events Dashboard and on the Map by date and time.</li>\n<li><strong>Zoom to Fit</strong> – A new button on the Map automatically adjusts the zoom to fit all visible Subjects and Events.<br>\n<em>Note: Only unfiltered events and visible Subjects will be included.</em></li>\n<li><strong>Event Type Icons on Android</strong> – Custom Event Type icons now display correctly on the Map in the Android app.</li>\n</ul>\n<p><img src="https://community.earthranger.com/images/emoji/apple/rocket.png?v=12" title=":rocket:" class="emoji" alt=":rocket:" loading="lazy" width="20" height="20"> <strong>Improvements</strong></p>\n<ul>\n<li>The <strong>navigational banner in Subjects Go To mode</strong> has been refined for better clarity.</li>\n<li>When selecting a Subject on the Map, the <strong>icon marker now inverts colors</strong>, making it easier to identify the selected Subject.</li>\n</ul>\n<p><img src="https://community.earthranger.com/images/emoji/apple/hammer_and_wrench.png?v=12" title=":hammer_and_wrench:" class="emoji" alt=":hammer_and_wrench:" loading="lazy" width="20" height="20"> <strong>Bug Fixes</strong></p>\n<ul>\n<li><strong>Event Type Syncing</strong> – Fixed an issue where event types wouldn’t sync when a new category was added.</li>\n<li><strong>Polygon Button Issue</strong> – The “Start Polygon” button is now disabled after an event is submitted.</li>\n<li><strong>Subject Track Syncing</strong> – Fixed an issue where subject tracks didn’t sync at first login.</li>\n<li><strong>Event Draft Timezones</strong> – Fixed an issue where draft event times displayed an incorrect timezone.</li>\n</ul>'}, {'id': 2, 'title': 'We want your feedback!', 'fancy_title': 'We want your feedback!', 'slug': 'we-want-your-feedback', 'posts_count': 4, 'reply_count': 2, 'highest_post_number': 4, 'image_url': None, 'created_at': '2025-02-26T17:48:13.580Z', 'last_posted_at': '2025-03-04T06:58:58.240Z', 'bumped': True, 'bumped_at': '2025-03-04T06:58:58.240Z', 'archetype': 'regular', 'unseen': False, 'pinned': False, 'unpinned': None, 'visible': True, 'closed': False, 'archived': False, 'bookmarked': None, 'liked': None, 'tags': ['not-er-notify'], 'tags_descriptions': {}, 'views': 37, 'like_count': 1, 'has_summary': False, 'last_poster_username': 'username1', 'category_id': 8, 'pinned_globally': False, 'featured_link': None, 'posters': [{'extras': None, 'description': 'Original Poster', 'user_id': 711, 'primary_group_id': 44, 'flair_group_id': 44}, {'extras': 'latest', 'description': 'Most Recent Poster', 'user_id': 863, 'primary_group_id': 44, 'flair_group_id': 44}]}]}}
    return data

@pytest.fixture
def mock_response_posts():
    data = {
        "post_stream": {
            "posts": [
                {
                    "id": 1,
                    "cooked": "This is cooked content"
                }
            ]
        }
    }
    return data

@pytest.fixture
def mock_response_post_without_cooked():
    data = {
        "post_stream": {
            "posts": [
                {
                    "id": 1,
                }
            ]
        }
    }
    return data

