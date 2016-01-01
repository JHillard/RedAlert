Jobs
===============

.. _job-types:

Types of Jobs
--------------

There are currently three tasks RedAlert can accomplish (And I think you'll find they getcha where you need to go)

* Message Checker
	* Exactly what it sounds like. It checks your messages! If you have multiple accounts logged in you'll be able to choose which account you want checked. You can even have two message checkers on the same account. Why would you want that? I don't know!
* Subreddit Keyword Monitor
	* Monitors a specific subreddit for keywords that you specify. Want to always know when someone mentions an app you wrote? I sure do. I use RedAlert to monitor when people talk about RedAlert!
	* To use it, just enter a subreddit and enter your keywords. Seperate them with spaces. Like this: You're Awesome.
* Subbmission Monitor
	* This one is handy for keeping tabs on how one of your posts is doing. Updates consist of: number of Up votes and Down votes and the number of comments the post has.
	* Start by entering the subreddit where you posted your submission. This will display all the recent posts in a subreddit and their post IDs. Find yours and copy it.
	* Paste your post ID (or directly enter it if you already knew it) where it asks
	* Enter how frequently you'd like to recieve updates about this post. Only integer values accepted, don't be cheeky!


.. _job-edit:

Editing your Jobs
------------------

The script is pretty straight forward.
There are three :ref:`job-types` that you can choose from when initializing RedAlert.
Choose which ones you want and the script should walk you through what you need.

Jobs persist after you close RedAlert. So once you get things how you like them, you'll never have to worry about it again.

.. _job-add:

Adding Jobs
------------
Pretty straight forward.

::

	What would you like to do?
		1.Add job
		2.Delete Job
		3.Add User
		4.Run RedAlert
	1
	What task do you want to add:
		1.Message checker
		2.Subreddit Keyword Monitor
		3.Submission Monitor
		4.Custom Job Entry
		5.Back
	1
	Users: 
		0: AccidentalGyroscope
	None
	User index: 0
	Job made: Message Checker for u/AccidentalGyroscope


.. _job-del:

Deleting Jobs
---------------

Also pretty straight forward. ::

	What would you like to do?
		1.Add job
		2.Delete Job
		3.Add User
		4.Run RedAlert
	2
		0: Message Checker for u/AccidentalGyroscope
		1: Keyword Checker for r/Physicsgifs Keywords: fire
	Enter job index you'd like to delete (Choose out-of-bounds index to exit): 1
	Job File Contents: 
	self.makeJob( userIndex=0, job='M',waitTime ='0',postID='None',subRT='None',keywords="None")


	You are now editing the job file.
	Current jobs:
		0: Message Checker for u/AccidentalGyroscope
	What would you like to do?
		1.Add job
		2.Delete Job
		3.Add User
		4.Run RedAlert

.. _job-custom:

Custom Jobs
------------

Here you can enter arbitrary job commands to be executed on startup. The typical use for this would be::

	self.makeJob( userIndex=0, job='K',waitTime ='0',postID='None',subRT='Physicsgifs',keywords="Fire")

Which is the same as selecting a Subreddit Keyword Monitor for r/PhysicsGifs and looking for the keyword "fire".

This can be handy if you want extremely find control over the values you pass to the jobs.
Any string you type into the custom job input will be executed with the python exec() call. This means that you can add whatever code you might want to run at startup. 

.. note:: This method presents a risk. I added it because it can give you a lot of power in how you use this script. But you could delete systen files or wreak havock on your system if you're not careful. So be careful.
