
.. i18n: .. index::
.. i18n:    single: database; create
.. i18n:    single: database
..

.. index::
   single: database; create
   single: database

.. i18n: .. _sect-dbcreate:
.. i18n: 
.. i18n: Database Creation
.. i18n: =================
..

.. _sect-dbcreate:

Database Creation
=================

.. i18n: Use the technique outlined in this section to create a new database, \ ``openerp_ch01`` \. This
.. i18n: database will contain the demonstration data provided with OpenERP and a large proportion of the
.. i18n: core OpenERP functionality. You will need to know your super administrator password for this – or
.. i18n: you will have to find somebody who does have it to create this database.
..

Use the technique outlined in this section to create a new database, \ ``openerp_ch01`` \. This
database will contain the demonstration data provided with OpenERP and a large proportion of the
core OpenERP functionality. You will need to know your super administrator password for this – or
you will have to find somebody who does have it to create this database.

.. i18n: .. index::
.. i18n:    single: password; super-administrator
.. i18n:    single: password; superadmin
..

.. index::
   single: password; super-administrator
   single: password; superadmin

.. i18n: .. note:: The Super-administrator Password
.. i18n: 
.. i18n:    Anyone who knows the super-administrator password has complete access to the data on the server
.. i18n:    – able to read, change and delete any of the data in any of the databases there.
.. i18n: 
.. i18n:    After first installation, the password is ``admin``. This is the hard-coded default, and
.. i18n:    is used if there is no accessible server configuration file. If your system has been 
.. i18n:    set up so that the server configuration file can be written to by the server, then
.. i18n:    you can change the password through the client. Or you could deliberately make the 
.. i18n:    configuration file read-only so that there is no prospect of changing it from the client.
.. i18n:    Either way, a server systems administrator can change it if you forget it.
.. i18n:    
.. i18n:    So if your system is set to allow it, you can change the superadmin password through the GTK client
.. i18n:    from the menu :menuselection:`File --> Databases --> Administrator Password`, or through the
.. i18n:    web client by logging out (click the :guilabel:`Logout` link), clicking :guilabel:`Databases` on the
.. i18n:    login screen, and then clicking the :guilabel:`Password` button on the Management screen. 
.. i18n:    
.. i18n:    The location of the server configuration file is typically defined by starting the server with 
.. i18n:    the ``--config`` command line option.
..

.. note:: The Super-administrator Password

   Anyone who knows the super-administrator password has complete access to the data on the server
   – able to read, change and delete any of the data in any of the databases there.

   After first installation, the password is ``admin``. This is the hard-coded default, and
   is used if there is no accessible server configuration file. If your system has been 
   set up so that the server configuration file can be written to by the server, then
   you can change the password through the client. Or you could deliberately make the 
   configuration file read-only so that there is no prospect of changing it from the client.
   Either way, a server systems administrator can change it if you forget it.
   
   So if your system is set to allow it, you can change the superadmin password through the GTK client
   from the menu :menuselection:`File --> Databases --> Administrator Password`, or through the
   web client by logging out (click the :guilabel:`Logout` link), clicking :guilabel:`Databases` on the
   login screen, and then clicking the :guilabel:`Password` button on the Management screen. 
   
   The location of the server configuration file is typically defined by starting the server with 
   the ``--config`` command line option.

.. i18n: .. figure:: images/change_superadmin_pwd.png
.. i18n:    :scale: 65
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Changing the super-administrator password through the web client*
..

.. figure:: images/change_superadmin_pwd.png
   :scale: 65
   :align: center

   *Changing the super-administrator password through the web client*

.. i18n: .. _sect-creatingdb:
.. i18n: 
.. i18n: Creating the Database
.. i18n: ---------------------
..

.. _sect-creatingdb:

Creating the Database
---------------------

.. i18n: If you are using the GTK client, choose :menuselection:`File --> Databases --> New database`  in
.. i18n: the menu at the top left. Enter the super-administrator password, then the name of the new database
.. i18n: you are creating.
..

If you are using the GTK client, choose :menuselection:`File --> Databases --> New database`  in
the menu at the top left. Enter the super-administrator password, then the name of the new database
you are creating.

.. i18n: .. figure:: images/create_new_db_GTK.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Creating a new database through the GTK client*  
..

.. figure:: images/create_new_db_GTK.png
   :scale: 75
   :align: center

   *Creating a new database through the GTK client*  

.. i18n: If you are using the web client, click :guilabel:`Databases` on the login screen, then
.. i18n: :guilabel:`Create` on the database management page. Enter the super-administrator password, and the
.. i18n: name of the new database you are creating.
.. i18n:   
.. i18n: In both cases, you will see a checkbox that determines whether you load demonstration data or not.
.. i18n: The consequences of checking this box or not affect the **whole use** of this database.
..

If you are using the web client, click :guilabel:`Databases` on the login screen, then
:guilabel:`Create` on the database management page. Enter the super-administrator password, and the
name of the new database you are creating.
  
In both cases, you will see a checkbox that determines whether you load demonstration data or not.
The consequences of checking this box or not affect the **whole use** of this database.

.. i18n: In both cases, you will also see that you can choose the Administrator password. This makes your 
.. i18n: database quite secure because you can ensure that it is unique from the outset.
.. i18n: (In fact many people find it hard to resist ``admin`` as their password!)
..

In both cases, you will also see that you can choose the Administrator password. This makes your 
database quite secure because you can ensure that it is unique from the outset.
(In fact many people find it hard to resist ``admin`` as their password!)

.. i18n: Database openerp_ch01
.. i18n: ---------------------
..

Database openerp_ch01
---------------------

.. i18n: .. index::
.. i18n:    pair: account; user
..

.. index::
   pair: account; user

.. i18n: Wait for the message showing that the database has been successfully created, along with the user
.. i18n: accounts and passwords (\ ``admin/XXXX``\   and \ ``demo/demo``\  ). Now that you have created this
.. i18n: database, you can extend it without having to know the super-administrator password.
..

Wait for the message showing that the database has been successfully created, along with the user
accounts and passwords (\ ``admin/XXXX``\   and \ ``demo/demo``\  ). Now that you have created this
database, you can extend it without having to know the super-administrator password.

.. i18n: .. index::
.. i18n:    single: access; LDAP
.. i18n:    single: LDAP
.. i18n:    pair: password; username
.. i18n:    single: access; user
..

.. index::
   single: access; LDAP
   single: LDAP
   pair: password; username
   single: access; user

.. i18n: .. tip::   User Access
.. i18n: 
.. i18n: 	The combination of username/password is specific to a single database. If you have administrative
.. i18n: 	rights to a database you can modify all users.
.. i18n: 
.. i18n:  	.. index::
.. i18n: 	   single: module; users_ldap
.. i18n: 
.. i18n: 	Alternatively, you can install the :mod:`users_ldap` module, which manages the authentication of users
.. i18n: 	in LDAP (the Lightweight Directory Access Protocol, a standard system), and connect it to several
.. i18n: 	OpenERP databases. Using this, many databases can share the same user account details.
..

.. tip::   User Access

	The combination of username/password is specific to a single database. If you have administrative
	rights to a database you can modify all users.

 	.. index::
	   single: module; users_ldap

	Alternatively, you can install the :mod:`users_ldap` module, which manages the authentication of users
	in LDAP (the Lightweight Directory Access Protocol, a standard system), and connect it to several
	OpenERP databases. Using this, many databases can share the same user account details.

.. i18n: .. note::  Failure to Create a Database
.. i18n: 
.. i18n: 	How do you know if you have successfully created your new database?
.. i18n: 	You are told if the database creation has been unsuccessful.
.. i18n: 	If you have entered a database name using prohibited characters (or no name, or too short a name),
.. i18n: 	you will be alerted by the dialog box :guilabel:`Bad database name!` explaining how to correct the error.
.. i18n: 	If you have entered the wrong super-administrator password or a name already in use
.. i18n: 	(some names can be reserved without your knowledge), you will be alerted by the dialog box
.. i18n: 	:guilabel:`Error during database creation!`.
..

.. note::  Failure to Create a Database

	How do you know if you have successfully created your new database?
	You are told if the database creation has been unsuccessful.
	If you have entered a database name using prohibited characters (or no name, or too short a name),
	you will be alerted by the dialog box :guilabel:`Bad database name!` explaining how to correct the error.
	If you have entered the wrong super-administrator password or a name already in use
	(some names can be reserved without your knowledge), you will be alerted by the dialog box
	:guilabel:`Error during database creation!`.

.. i18n: Since this is the first time you have connected to this database, you will be asked a series of questions to
.. i18n: define the database parameters. You may choose to :guilabel:`Skip Configuration Wizards` or
.. i18n: :guilabel:`Start Configuration`. If you choose to configure your application, you may proceed with the
.. i18n: following steps:
..

Since this is the first time you have connected to this database, you will be asked a series of questions to
define the database parameters. You may choose to :guilabel:`Skip Configuration Wizards` or
:guilabel:`Start Configuration`. If you choose to configure your application, you may proceed with the
following steps:

.. i18n: 	#.  :guilabel:`Configure Your Interface` : select \ ``Simplified`` \ and click :guilabel:`Next`.
.. i18n: 
.. i18n: 	#.  :guilabel:`Configure Your Company Information` : replace the proposed default of \ ``OpenERP S.A.`` \
.. i18n: 	    by your own company name, complete as much of your address as you like. You can set the currency that
.. i18n: 	    your company uses or leave the default setting. You may also add your company logo which will
.. i18n: 	    be visible on reports and other documents. Click :guilabel:`Next`.
.. i18n: 
.. i18n: 	#.  :guilabel:`Install Applications` : check the applications you need and then click :guilabel:`Install`.
.. i18n: 	    For now, do not install any application.
..

	#.  :guilabel:`Configure Your Interface` : select \ ``Simplified`` \ and click :guilabel:`Next`.

	#.  :guilabel:`Configure Your Company Information` : replace the proposed default of \ ``OpenERP S.A.`` \
	    by your own company name, complete as much of your address as you like. You can set the currency that
	    your company uses or leave the default setting. You may also add your company logo which will
	    be visible on reports and other documents. Click :guilabel:`Next`.

	#.  :guilabel:`Install Applications` : check the applications you need and then click :guilabel:`Install`.
	    For now, do not install any application.

.. i18n: Once configuration is complete, you are connected to your OpenERP system. Its functionality is very
.. i18n: limited because you have selected a :guilabel:`Simplified` interface with no application installed,
.. i18n: but this is sufficient to demonstrate that your installation is working.
..

Once configuration is complete, you are connected to your OpenERP system. Its functionality is very
limited because you have selected a :guilabel:`Simplified` interface with no application installed,
but this is sufficient to demonstrate that your installation is working.

.. i18n: .. figure:: images/define_main_co_dlg.png
.. i18n:    :align: center
.. i18n:    :scale: 80
.. i18n: 
.. i18n:    *Defining your company during initial database configuration*
..

.. figure:: images/define_main_co_dlg.png
   :align: center
   :scale: 80

   *Defining your company during initial database configuration*

.. i18n: .. index::
.. i18n:    single: database; manage
..

.. index::
   single: database; manage

.. i18n: .. _sect-dbmanage:
.. i18n: 
.. i18n: Managing Databases
.. i18n: ------------------
..

.. _sect-dbmanage:

Managing Databases
------------------

.. i18n: As a super-administrator, you do not only have rights to create new databases, but also to:
..

As a super-administrator, you do not only have rights to create new databases, but also to:

.. i18n: * backup databases,
.. i18n: 
.. i18n: * delete databases,
.. i18n: 
.. i18n: * restore databases.
..

* backup databases,

* delete databases,

* restore databases.

.. i18n: All of these operations can be carried out from the menu :menuselection:`File --> Databases...`
.. i18n: in the GTK client, or from the :guilabel:`Databases` button in the web client's 
.. i18n: :guilabel:`Login` screen.
..

All of these operations can be carried out from the menu :menuselection:`File --> Databases...`
in the GTK client, or from the :guilabel:`Databases` button in the web client's 
:guilabel:`Login` screen.

.. i18n: .. index::
.. i18n:    single: database; backup
..

.. index::
   single: database; backup

.. i18n: .. tip:: Backup (copy) a Database
.. i18n: 
.. i18n:         To make a copy of a database, go to the web :guilabel:`Login` screen and click the :guilabel:`Databases` button.
.. i18n:         Then click the :guilabel:`Backup` button, select the database you want to copy and enter the super-administrator
.. i18n: 	password. Click the :guilabel:`Backup` button to confirm that you want to copy the database.
..

.. tip:: Backup (copy) a Database

        To make a copy of a database, go to the web :guilabel:`Login` screen and click the :guilabel:`Databases` button.
        Then click the :guilabel:`Backup` button, select the database you want to copy and enter the super-administrator
	password. Click the :guilabel:`Backup` button to confirm that you want to copy the database.

.. i18n: .. index::
.. i18n:    single: database; drop
..

.. index::
   single: database; drop

.. i18n: .. tip:: Drop (delete) a Database
.. i18n: 
.. i18n:         To delete a database, go to the web :guilabel:`Login` screen and click the :guilabel:`Databases` button.
.. i18n:         Then click the :guilabel:`Drop` button, select the database you want to delete and enter the super-administrator
.. i18n: 	password. Click the :guilabel:`Drop` button to confirm that you want to delete the database.
..

.. tip:: Drop (delete) a Database

        To delete a database, go to the web :guilabel:`Login` screen and click the :guilabel:`Databases` button.
        Then click the :guilabel:`Drop` button, select the database you want to delete and enter the super-administrator
	password. Click the :guilabel:`Drop` button to confirm that you want to delete the database.

.. i18n: .. index::
.. i18n:    single: database; restore
..

.. index::
   single: database; restore

.. i18n: .. tip:: Restore a Database
.. i18n: 
.. i18n:         To restore a database, go to the web :guilabel:`Login` screen and click the :guilabel:`Databases` button.
.. i18n:         Then click the :guilabel:`Restore` button, click the :guilabel:`Choose File` button to select the database
.. i18n:         you want to restore. Give the database a name and enter the super-administrator	password.
.. i18n: 	Click the :guilabel:`Restore` button to confirm that you want to install a new copy of the selected database.
.. i18n: 	To restore a database, you need to have an existing copy, of course.
..

.. tip:: Restore a Database

        To restore a database, go to the web :guilabel:`Login` screen and click the :guilabel:`Databases` button.
        Then click the :guilabel:`Restore` button, click the :guilabel:`Choose File` button to select the database
        you want to restore. Give the database a name and enter the super-administrator	password.
	Click the :guilabel:`Restore` button to confirm that you want to install a new copy of the selected database.
	To restore a database, you need to have an existing copy, of course.

.. i18n: .. index::
.. i18n:    single: database; duplicate
..

.. index::
   single: database; duplicate

.. i18n: .. tip::   Duplicating a Database
.. i18n: 
.. i18n: 	To duplicate a database, you can:
.. i18n: 
.. i18n:         #. make a backup file on your PC from this database.
.. i18n: 
.. i18n:         #. restore this database from the backup file on your PC, and give it a new name.
.. i18n: 
.. i18n: 	This can be a useful way of making a test database from a production database. You can try out the
.. i18n: 	operation of a new configuration, new modules, or just the import of new data.
..

.. tip::   Duplicating a Database

	To duplicate a database, you can:

        #. make a backup file on your PC from this database.

        #. restore this database from the backup file on your PC, and give it a new name.

	This can be a useful way of making a test database from a production database. You can try out the
	operation of a new configuration, new modules, or just the import of new data.

.. i18n: .. index::
.. i18n:    single: access
..

.. index::
   single: access

.. i18n: A system administrator can configure OpenERP to restrict access to some of these database functions
.. i18n: so that your security is enhanced in normal production use.
..

A system administrator can configure OpenERP to restrict access to some of these database functions
so that your security is enhanced in normal production use.

.. i18n: You are now ready to use databases from your installation to familiarize yourself with the
.. i18n: administration and use of OpenERP.
..

You are now ready to use databases from your installation to familiarize yourself with the
administration and use of OpenERP.

.. i18n: New OpenERP Functionality
.. i18n: =========================
..

New OpenERP Functionality
=========================

.. i18n: The database you have created and managed so far is based on the core OpenERP functionality that you
.. i18n: installed. The core system is installed in the file system of your OpenERP application server, but
.. i18n: only installed into an OpenERP database as you require it, as is described in the next chapter, :ref:`ch-guided`.
..

The database you have created and managed so far is based on the core OpenERP functionality that you
installed. The core system is installed in the file system of your OpenERP application server, but
only installed into an OpenERP database as you require it, as is described in the next chapter, :ref:`ch-guided`.

.. i18n: What if you want to update what is there, or extend what is there with additional modules?
..

What if you want to update what is there, or extend what is there with additional modules?

.. i18n: * To update what you have, you would install a new instance of OpenERP using the same techniques as
.. i18n:   described earlier in this section, :ref:`sect-dbcreate`.
.. i18n: 
.. i18n: * To extend what you have, you would install new modules in the ``addons`` directory of your current
.. i18n:   OpenERP installation. There are several ways of doing that.
..

* To update what you have, you would install a new instance of OpenERP using the same techniques as
  described earlier in this section, :ref:`sect-dbcreate`.

* To extend what you have, you would install new modules in the ``addons`` directory of your current
  OpenERP installation. There are several ways of doing that.

.. i18n: .. index::
.. i18n:    pair:  system; administrator
..

.. index::
   pair:  system; administrator

.. i18n: In both cases you will need to be a \ ``root`` \ user or \ ``Administrator`` \ of your
.. i18n: OpenERP application server.
..

In both cases you will need to be a \ ``root`` \ user or \ ``Administrator`` \ of your
OpenERP application server.

.. i18n: Extending OpenERP
.. i18n: -----------------
..

Extending OpenERP
-----------------

.. i18n: To extend OpenERP you will need to copy modules into the \ ``addons`` \ directory. That is in
.. i18n: your server's \ ``openerp-server`` \ directory (which differs between Windows, Mac and some of the
.. i18n: various Linux distributions and not available at all in the Windows all-in-one installer).
..

To extend OpenERP you will need to copy modules into the \ ``addons`` \ directory. That is in
your server's \ ``openerp-server`` \ directory (which differs between Windows, Mac and some of the
various Linux distributions and not available at all in the Windows all-in-one installer).

.. i18n: .. index::
.. i18n:    single: module; product
.. i18n:    single: module; purchase
..

.. index::
   single: module; product
   single: module; purchase

.. i18n: If you look there you will see existing modules such as :mod:`product` and :mod:`purchase`. A
.. i18n: module can be provided in the form of files within a directory or a a zip-format file containing
.. i18n: that same directory structure.
..

If you look there you will see existing modules such as :mod:`product` and :mod:`purchase`. A
module can be provided in the form of files within a directory or a a zip-format file containing
that same directory structure.

.. i18n: You can add modules in two main ways – through the server, or through the client.
..

You can add modules in two main ways – through the server, or through the client.

.. i18n: .. index::
.. i18n:    pair:  system; administration
..

.. index::
   pair:  system; administration

.. i18n: To add new modules through the server is a conventional system administration task. As \ ``root`` \
.. i18n: user or another suitable user, you would put the module in the \ ``addons`` \ directory and change its
.. i18n: permissions to match those of the other modules.
..

To add new modules through the server is a conventional system administration task. As \ ``root`` \
user or another suitable user, you would put the module in the \ ``addons`` \ directory and change its
permissions to match those of the other modules.

.. i18n: To add new modules through the client you must first change the permissions of the \ ``addons`` \
.. i18n: directory of the server, so that it is writeable by the server. That will enable you to install
.. i18n: OpenERP modules using the OpenERP client (a task ultimately carried out on the application
.. i18n: server by the server software).
..

To add new modules through the client you must first change the permissions of the \ ``addons`` \
directory of the server, so that it is writeable by the server. That will enable you to install
OpenERP modules using the OpenERP client (a task ultimately carried out on the application
server by the server software).

.. i18n: .. index::
.. i18n:    pair:  filesystem; permissions
..

.. index::
   pair:  filesystem; permissions

.. i18n: .. tip:: Changing Permissions
.. i18n: 
.. i18n: 	A very simple way of changing permissions on the Linux system you are using to develop an OpenERP
.. i18n: 	application is to execute the command sudo chmod 777 <path_to_addons> (where <path_to_addons> is
.. i18n: 	the full path to the addons directory, a location like /usr/lib/python2.5/site-packages/openerp-
.. i18n: 	server/addons).
..

.. tip:: Changing Permissions

	A very simple way of changing permissions on the Linux system you are using to develop an OpenERP
	application is to execute the command sudo chmod 777 <path_to_addons> (where <path_to_addons> is
	the full path to the addons directory, a location like /usr/lib/python2.5/site-packages/openerp-
	server/addons).

.. i18n: Any user of OpenERP who has access to the relevant administration menus can then upload any new
.. i18n: functionality, so you would certainly disable this capability for production use. You will see examples of
.. i18n: this uploading as you make your way through this book.
..

Any user of OpenERP who has access to the relevant administration menus can then upload any new
functionality, so you would certainly disable this capability for production use. You will see examples of
this uploading as you make your way through this book.

.. i18n: .. Copyright © Open Object Press. All rights reserved.
..

.. Copyright © Open Object Press. All rights reserved.

.. i18n: .. You may take electronic copy of this publication and distribute it if you don't
.. i18n: .. change the content. You can also print a copy to be read by yourself only.
..

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. i18n: .. We have contracts with different publishers in different countries to sell and
.. i18n: .. distribute paper or electronic based versions of this book (translated or not)
.. i18n: .. in bookstores. This helps to distribute and promote the OpenERP product. It
.. i18n: .. also helps us to create incentives to pay contributors and authors using author
.. i18n: .. rights of these sales.
..

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the OpenERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. i18n: .. Due to this, grants to translate, modify or sell this book are strictly
.. i18n: .. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. i18n: .. written authorisation for this.
..

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. i18n: .. Many of the designations used by manufacturers and suppliers to distinguish their
.. i18n: .. products are claimed as trademarks. Where those designations appear in this book,
.. i18n: .. and Open Object Press was aware of a trademark claim, the designations have been
.. i18n: .. printed in initial capitals.
..

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. i18n: .. While every precaution has been taken in the preparation of this book, the publisher
.. i18n: .. and the authors assume no responsibility for errors or omissions, or for damages
.. i18n: .. resulting from the use of the information contained herein.
..

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. i18n: .. Published by Open Object Press, Grand Rosière, Belgium
..

.. Published by Open Object Press, Grand Rosière, Belgium
