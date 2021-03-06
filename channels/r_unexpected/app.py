# encoding: utf-8

from utils import get_url


subreddit = 'unexpected'
t_channel = '@r_unexpected'


NSFW_EMOJI = u'\U0001F51E'


def send_post(submission, r2t):
    what, url, ext = get_url(submission)

    title = submission.title
    link = submission.shortlink
    text = '{title}\n{link}\n\nby {channel}'.format(title=title, link=link, channel=t_channel)

    if submission.over_18:
        url = submission.url
        text = '{emoji}NSFW\n{url}\n{title}\n\n{link}\n\nby {channel}'.format(
            emoji=NSFW_EMOJI, url=url, title=title, link=link, channel=t_channel
        )
        return r2t.send_text(text, disable_web_page_preview=True)

    if r2t.dup_check_and_mark(url) is True:
        return False

    return r2t.send_gif_img(what, url, ext, text)
