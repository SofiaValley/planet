SofiaValley RSS Planet
----------------------

This is the RSS planet at <http://sofiavalley.com>. The purpose of this planet
is to show the world that Sofia (and Bulgaria) is a place with many tallented
developers and hackers and make it easier for foreigners to follow tech related
activity happening in the region.

Add Your Blog
=============

Everyone is welcome to join if you agree to the following rules

* Your blog should be mostly on technical topics;
* You blog about interesting technical problems, experiments, projects, etc.
* You live in Sofia or anywhere else in Bulgaria;
* Posts are either only in English or only in Bulgarian
(you can submit a category feed for any particular language);
* You agree to put the text (or image) "SofiaValley Blog" on your site and
link back to <http://planet.sofiavalley.com> - failure to comply will be made
public;

To add your blog just fork this repo and submit a pull request. Configuration
files are in `data/` and are self explanatory. 


Software Stack
==============

The software which runs this planet is called
[Venus](https://github.com/rubys/venus). This repository structure follows the
directory layout used at Red Hat's OpenShift. Venus is in `libs/venus/` with
themes under `libs/venus/themes/`. Config files are in `data/`.

This planet is hosted at Red Hat's OpenShift PaaS cloud and updated through
cron. The cron task is in `.openshift/cron/hourly/`.

All static files are then synced to Amazon S3 and served from there.

How To Contribute
=================

Fork and send a pull request. Patches are welcome!
