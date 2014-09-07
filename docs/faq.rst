==========================
Frequently Asked Questions
==========================

General
=======

Who is behind this?  Who to contact?
------------------------------------
The immediate involved persons is described in the :ref:`dev-team` section.
The author is a participating member in the :term:`GS Task-Force` on behalf of the EU Commission (JRC).
The contact-emails to use are ...[TBD]


What is this project's status? Is it "official"?
------------------------------------------------
[TBD]


What is the roadmap for this project?
-------------------------------------
* Short-term plans are described in the :ref:`todos-list` section of :doc:`CHANGES`.

* In the longer run, it is expected to incorporate more *WLTP* calculations and reference data so that
  this projects acts as repository for diagrams and technical reports on those algorithms.



Technical
=========

I followed the instructions but i still cannot install/run/do *X*.  What now?
-----------------------------------------------------------------------------
If you have no previous experience in python, setting up your environment and installing a new project
is a demanding, but manageable, task.  Here is a checklist of things that might go wrong:

* Did you send each command to the **appropriate shell/interpreter**?

  You should enter sample commands starting ``$`` into your *shell* (:program:`cmd` or :program:`bash`),
  and those starting with ``>>>`` into the *python-interpreter*
  (but don't include the previous symbols and/or the *output* of the commands).


* Is the correct **version of python** running?

  Certain commands such as :command:`pip` come in 2 different versions *python-2 & 3*
  (:command:`pip2` and :command:`pip3`, respectively).  Most programs report their version-infos
  with :option:`--version`.
  Use :option:`--help` if this does not work.


* Have you **upgraded/downgraded the project** into a more recent/older version?

  This project is still in development, so the names of data and functions often differ from version to version.
  Check the :doc:`CHANGES` for point that you have to be aware of when upgrading.


* Did you `search <https://github.com/ankostis/wltp/issues>`_ whether **a similar issue** has already been reported?

* Did you **ask google** for an answer??

* If the above suggestions still do not work, feel free to **open a new issue** and ask for help.
  Write down your platform (Windows, OS X, Linux), your exact python distribution
  and version, and include the *print-out of the failed command along with its error-message.*

  `This last step will improve the documentation and help others as well.