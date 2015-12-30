Using the Script:
================

How to run the python script just on its own.

* :ref:`quick-start`
	* :ref:`phone-num`
	* :ref:`email-auth`
	* :ref:`red-auth`
	* :ref:`account-add`
* :ref:`job-types`
* :ref:`job-edit`
	* :ref:`job-add`
	* :ref:`job-del`
	* :ref:`job-custom`
* :ref:`running`


_stuff()


.. _quick-start:

Quick Start:
------------

First :ref:`download` the script.
Check that you have the :ref:`required-software`

Then run it with python!
	Code Exerpt
	python3 RedAlert.py
	>>you win!!!!

Then theres just some first time setup.



.. _phone-num:

Formatting your Phone Number:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In order to get text messages, you have to tell it where to send them!
RedAlert sends text messages through emails to your phone. So you need to format your phone number into an email address. You can look up the carriers on your own `Google "Email to text provider list" <https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=email+to+text+provider+list>`_
Here's the top hits I found at http://www.textsendr.com/emailsms.php:

===============  ===========================
Cell Provider    Email Address
===============  ===========================
AT&T             [phone number]@txt.att.net
Qwest            [phone number]@qwestmp.com
Sprint           [phone number]@messaging.sprintpcs.com
T Mobile         [phone number]@tmomail.net
T Mobile (Ger)   [phone number]@T-D1-SMS.de
T Mobile UK      [phone number]@t-mobile.uk.net
V Mobile CA      [phone number]@vmobile.ca
Verizon          [phone number]@vtext.com
Virgin Mobile    [phone number]@vmobl.com
Vodacom Africa   [phone number]@voda.co.za
Vodafone         [phone number]@vodafone.net
===============  ===========================

.. _email-auth:

Enabling Email Authorization:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

RedAlert sends email through a gmail account. But you need to enable less secure apps in Gmail first.
https://www.google.com/settings/security/lesssecureapps

Follow that link, log into your email, and turn on access for less secure apps.
There you go!
Now when RedAlert logs in with your information, Google won't reject it.
(Yes, this method is horribly insecure, but it works alright. Will be changed on future update.)


.. _red-auth:

Authenticating Reddit
---------------------

Now it's time to let RedAlert see your messages!
To do that, go to the link presented by RedAlert on startup.

Todo Figure 1.

It'll be different every time. Each time you start up RedAlert you'll need to do this.
Login into Reddit and then allow the app. Your browser will then redirect to a dead webpage. Copy the access token there and paste it into the script.

Todo Figure 2.

And there you go, you are ready to start recieving messages!



.. _account-add:

Adding More Reddit Accounts
---------------------------
You may have more than one reddit account you'd like to recieve messages from.
Just enter the 
      code snippet: 3.Add User
And you'll repeat the steps in :ref:`red-auth`
Once that is done you'll be able to choose which user gets checked. Hooray! Alt mail checked!


.. _job-types:

Types of Jobs:
--------------
There are currently three tasks RedAlert can accomplish (And I think you'll find they getcha where you need to go)

* Message Checker
	* Exactly what it sounds like. It checks your messages! If you have multiple accounts logged in you'll be able to choose which account you want checked. You can even have two message checkers on the same account. Why would you want that? I don't know!
* Subreddit Keyword Monitor
	* Monitors a specific subreddit for keywords that you specify. Want to always know when someone mentions an app you wrote? I sure do. I use RedAlert to monitor when people talk about RedAlert!
	* To use it, just enter a subreddit and enter your keywords. Seperate them with spaces. Like this: You're Awesome.
* Subbmission Monitor
	* This one is handy for keeping tabs on how one of your posts is doing. Updates consist of:
		* Number of Up votes and Down votes
		* Number of comments the post has.
	* Start by entering the subreddit where you posted your submission. This will display all the recent posts in a subreddit and their post IDs. Find yours and copy it.
	* Paste your post ID (or directly enter it if you already knew it) where it asks
	* Enter how frequently you'd like to recieve updates about this post. Only integer values accepted, don't be cheeky!


.. _job-edit:

Editing your Jobs:
------------------
The script is pretty strait forward.
There are three :ref:`job-types` that you can choose from when initializing RedAlert.
Choose which ones you want and the script should walk you through what you need.

Jobs persist after you close RedAlert. So once you get things how you like them, you'll never have to worry about it again.

.. _job-add:

Adding Jobs:
^^^^^^^^^^^^
How to add a job.


.. _job-del:

Removing Jobs:
^^^^^^^^^^^^^^
How to remove a job.

.. _job-custom:

Custom Job Commands:
^^^^^^^^^^^^^^^^^^^^
Entering customs jobs.


.. _running:

Running the Program!:
---------------------
Turn it on!
