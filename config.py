import os
from instaloader import Instaloader
class Config:
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
    USER = os.environ.get("INSTAGRAM_USERNAME", "")
    OWNER = os.environ.get("OWNER_ID", "")
    INSTA_SESSIONFILE_ID = os.environ.get("INSTA_SESSIONFILE_ID", None)
    S = "0"
    STATUS = set(int(x) for x in (S).split())
    L=Instaloader()
    HELP="""
You can Download almost anything From your Instagram Account.

<b>What Can Be Downloaded?:</b>

1. All posts of any Profile. (Both Public and Private,for private profiles you need to be a follower.)
2. All Posts from your feed.
3. Stories of any profile (Both Public and Private,for private profiles you need to be a follower.)
4. DP of any profile (No need to follow)
5. Followers and Followees List of any Profile.
6. List of followees who follows back the given username.
7. List of followees who are not following back the given username.
8. Stories of your Followees.
9. Tagged posts of any profile.
10. Your saved Posts.
11. IGTV videos.
12. Highlights from any profiles.
13. Any Public Post from Link(Post/Reels/IGTV)


<b>How to Download:</b>

Its Easy!!
You Need to login into your account by /login. 

You have two Options:

1. From Username:

Just send any instagram username.

For Example:
<code>samantharuthprabhuoffl</code>
<code>subin_p_s_</code>
<code>_chill_manh_7</code>


2. From URL:

You can also sent a post link to download the post or video.

For Example:
<code>https://www.instagram.com/p/CL4QbUiLRNW/?utm_medium=copy_link</code>


<b>Available Commands and Usage</b>

/start - Check wheather bot alive.
/restart - Restart the bot (If you messed up anything use /restart.)
/help - Shows this menu.
/login - Login into your account.
/logout - Logout of your account.
/account - Shows the details of logged in account.

/posts <username> - Download posts of any username. Use /posts to download own posts or <code> /posts <username> </code>for others.
Example : <code>/posts samantharuthprabhuoffl</code>

/igtv <username> - Download IGTV videos from given username. If no username given, downloads your IGTV.

/feed <number of posts to download> - Downloads posts from your feed.If no number specified all posts from feed will be downloaded.
Example: <code>/feed 10</code> to download latest 10 posts from feed.

/saved <number of posts to download> - Downloads your saved posts. If no number specified all saved posts will be downloaded.
Example: <code>/saved 10</code> to download latest 10 saved posts.

/followers <username> - Get a list of all followers of given username. If no username given, then your list will be retrieved.
Example: <code>/followers samantharuthprabhuoffl</code>

/followees <username> - Get a list of all followees of given username. If no username given, then your list will be retrieved.

/fans <username> - Get a list of of followees who follow back the given username. If no username given, your list will be retrieved.

/notfollowing <username> - Get a list of followees who is not following back the given username.

/tagged <username> - Downloads all posts in which given username is tagged. If nothing given your tagged posts will be downloaded.

/story <username> - Downloads all stories from given username. If nothing given your stories will be downloaded.

/stories - Downloads all the stories of all your followees.

/highlights <username> - Downloads highlights from given username, If nothing given your highlights will be downloaded.


"""
    HOME_TEXT = """
<b>😜 𝙷𝚎𝚕𝚕𝚘, [{}](tg://user?id={})

𝚃𝚑𝚒𝚜 𝚒𝚜 𝚊 𝚋𝚘𝚝 𝚘𝚏 [{}](www.instagram.com/{}) 𝚝𝚘 𝚖𝚊𝚗𝚊𝚐𝚎 𝚑𝚒𝚜 𝙸𝚗𝚜𝚝𝚊𝚐𝚛𝚊𝚖 𝚊𝚌𝚌𝚘𝚞𝚗𝚝. 
𝙸 𝚌𝚊𝚗 𝚘𝚗𝚕𝚢 𝚠𝚘𝚛𝚔 𝚏𝚘𝚛 𝚖𝚢 𝚖𝚊𝚜𝚝𝚎𝚛 [{}](tg://user?id={}).


Use /help to know What I can Do?</b>
"""
    HOME_TEXT_OWNER = """
<b>😜 𝙷𝚎𝚕𝚕𝚘, [{}](tg://user?id={})
𝙸 𝚊𝚖 𝚢𝚘𝚞𝚛 𝚊𝚜𝚜𝚒𝚜𝚝𝚊𝚗𝚝 𝚝𝚘 𝚖𝚊𝚗𝚊𝚐𝚎 𝚢𝚘𝚞𝚛 𝙸𝚗𝚜𝚝𝚊𝚐𝚛𝚊𝚖 𝚊𝚌𝚌𝚘𝚞𝚗𝚝 ⭕.
𝙼𝚢 𝙶𝚛𝚘𝚞𝚙 :- @Tg_Hydra_Galaxy
𝚄𝚜𝚎 /help 𝚝𝚘 𝚔𝚗𝚘𝚠 𝚠𝚑𝚊𝚝 𝙸 𝚌𝚊𝚗 𝚍𝚘 𝚏𝚘𝚛 𝚢𝚘𝚞.</b>
"""

