.. _first-time:

First Time Setup
=================

.. _getSoft:

Get the software
------------------

First :ref:`download` the RedAlert script.


.. _phone-num:

Adding your Phone Number
-------------------------
In order to get text messages, you have to tell RedAlert where to send them!
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

Adding your Email
------------------

RedAlert sends email through a gmail account. But you need to enable less secure apps in Gmail first.
https://www.google.com/settings/security/lesssecureapps

Follow that link, log into your email, and turn on access for less secure apps.
There you go!


Now when RedAlert logs in with your information, Google won't reject it.

.. note:: Yes, this method is gross, but it works alright. If you're worried about being spammed or security, I'd recommend looking through the source code to see how we handle this information. Everything is stored locally, and no bad things are transmitted across the internet. Still, probably not the best idea to use your email attached to your bank account. Will be changed on future release.

