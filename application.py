import os
import re
import string

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///data/chinadata.db")

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/display", methods=["GET", "POST"])
def display():
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        #Clear filters
        languagefilter = ""
        followercountfilter = ""
        tweettimefilter = ""
        retweetfilter = ""
        likecountfilter = ""

        #Check for language filter
        if request.form.get("language") != "":
            languagefilter = ("tweet_language=" + "'" + request.form.get("language") + "' and ")
        else:
            languagefilter = ""

        #Follower Count Filter
        followercountfilter = ''.join(["follower_count", ">=" if request.form.get("follower_more_less") == "more" else "<" , request.form.get("follower_count"), " and "])

        #Tweet Time Filter
        tweettimefilter = ''.join(["tweet_time", ">" if request.form.get("date_more_less") == "more" else "<" , request.form.get("tweet_date"), " and "])
        print(tweettimefilter)

        #Is Retweet Filter
        if request.form.get("isretweet") != "":
            if request.form.get("isretweet") == "yes":
                retweetfilter = ("is_retweet='1'" +  " and ")
            else:
                retweetfilter = ("is_retweet='0'" +  " and ")
        else:
            retweetfilter = ""

        #Like Count Filter
        likecountfilter = ''.join(["like_count", ">=" if request.form.get("likes_more_less") == "more" else "<" , request.form.get("like_count")])

        #build filter
        filter = languagefilter + followercountfilter + tweettimefilter + retweetfilter + likecountfilter


        rows = db.execute("SELECT * FROM tweets WHERE " + filter)
        if len(rows) == 0:
            return render_template("displayask.html", error="Sorry - there are no tweets in the database for that set of filters")

        else:
            dictindex = []

            for i in range(len(rows)):

                index = {}
                index['userid'] = rows[i]['userid']
                index['tweetid'] = rows[i]['tweetid']
                index['text'] = rows[i]['tweet_text']
                index['language'] = rows[i]["tweet_language"]
                index['time'] = rows[i]['tweet_time']
                if rows[i]['in_reply_to_userid'] == "None":
                    index['isreply'] = 'Yes'
                else:
                    index['isreply'] = 'No'
                if rows[i]['is_retweet'] == 0:
                    index['isretweet'] = 'No'
                else:
                    index['isretweet'] = 'Yes'
                if (rows[i]['like_count'] != 0 and rows[i]['like_count'] != None):
                    index['likecount'] = int(rows[i]['like_count'])
                else:
                    index['likecount'] = 0

                if (rows[i]['reply_count'] != 0 and rows[i]['reply_count'] != None):
                    index['replycount'] = int(rows[i]['reply_count'])
                else:
                    index['replycount'] = 0

                if (rows[i]['hashtags'] == '[]' or rows[i]['hashtags'] == None):
                    index['hashtags'] = ""
                else:
                    index['hashtags'] = rows[i]['hashtags']
                index['user_display_name'] = rows[i]['user_display_name']

                dictindex.append(index)

            count=len(dictindex)
            return render_template("display.html", dictindex=dictindex, count=count)

    # Else user reached via GET
    else:
        rows = db.execute("select distinct tweet_language from tweets")
        dictindex = []
        for i in range(len(rows)):
            index = {}
            index['tweet_language'] = rows[i]['tweet_language']
            dictindex.append(index)
        return render_template("displayask.html", error="", dictindex=dictindex)

@app.route("/home")
def home():
    return redirect("/")

@app.route("/user", methods=["GET", "POST"])
def user():
    """Show all the tweets by a user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        #Ensure a user ID was submitted
            if not request.form.get("userid"):
                return render_template("userask.html", error="Please enter a User ID")

        #A user ID was submitted
            else:
                userid = request.form.get("userid")

                if request.form.get("orderfield") not in ["tweet_time", "like_count", "reply_count", "hashtags"] :
                    print(request.form.get("orderfield"))
                    orderfield = "tweet_time"
                else:
                    orderfield = request.form.get("orderfield")
                    print(request.form.get("orderfield") + "fail")


                if request.form.get("orderby") not in ["ASC", "DESC"] :
                    print(request.form.get("orderby"))
                    orderby = "ASC"
                else:
                    orderby = request.form.get("orderby")
                    print(request.form.get("orderby"))

                rows = db.execute("SELECT * FROM tweets WHERE userid = :userid ORDER BY " + orderfield + " " + orderby, userid=userid)
                if len(rows) == 0:
                    return render_template("userask.html", error="Sorry - there are no tweets in the database for that user")

                else:
                    dictindex = []

                    for i in range(len(rows)):

                        index = {}
                        index['tweetid'] = rows[i]['tweetid']
                        index['text'] = rows[i]['tweet_text']
                        index['language'] = rows[i]["tweet_language"]
                        index['time'] = rows[i]['tweet_time']
                        if rows[i]['in_reply_to_userid'] == "None":
                            index['isreply'] = 'Yes'
                        else:
                            index['isreply'] = 'No'
                        if rows[i]['is_retweet'] == 0:
                            index['isretweet'] = 'No'
                        else:
                            index['isretweet'] = 'Yes'
                        if (rows[i]['like_count'] != 0 and rows[i]['like_count'] != None):
                            index['likecount'] = int(rows[i]['like_count'])
                        else:
                            index['likecount'] = 0

                        if (rows[i]['reply_count'] != 0 and rows[i]['reply_count'] != None):
                            index['replycount'] = int(rows[i]['reply_count'])
                        else:
                            index['replycount'] = 0

                        if rows[i]['hashtags'] == '[]':
                            index['hashtags'] = ""
                        else:
                            index['hashtags'] = rows[i]['hashtags']
                        index['user_display_name'] = rows[i]['user_display_name']

                        dictindex.append(index)

                    count=len(dictindex)
                    return render_template("user.html", userid=userid, dictindex=dictindex, orderby=orderby, orderfield=orderfield, count=count)


    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("userask.html", error="")




