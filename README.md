SofiaValley RSS Planet
----------------------

This is the RSS Planet at <http://planet.sofiavalley.com>. The purpose of this Planet
is to promote Sofia (and Bulgaria) as a place with many tallented
developers and hackers and make it easier for foreigners to follow tech related
activities in the region.

As an added bonus we also support another Planet in Bulgarian, targeted at the
local IT community. It uses the same infrastructure but is accessible via
different URL.

Add Your Blog
=============

Everyone is welcome to join if you agree to the following rules

* Your blog should be mostly on technical topics;
* You blog about interesting technical problems, experiments, projects, etc.
* You live in Sofia or anywhere else in Bulgaria;
* Posts are either only in English or only in Bulgarian
(category feed for a particular language/tag is also accepted);
* You agree to put the text (or image) "SofiaValley Blog" on your site and
link back to <http://planet.sofiavalley.com> - failure to comply will be made
public;

To add your blog just fork this repo and submit a
[pull request](https://github.com/SofiaValley/planet/pull/1). Configuration
files are in `data/` and are self explanatory. 


Software Stack
==============

The software which runs this Planet is called
[Venus](https://github.com/rubys/venus). This repository structure follows the
directory layout used at Red Hat's OpenShift PaaS. Most of the files are ignored.
We only make use of the cron cartridge at OpenShift.

Venus is in `libs/venus/` with themes under `libs/venus/themes/`. Config files
are in `data/`. 

The cron task which updates this Planet is in `.openshift/cron/hourly/`.
All static files are then synced to Amazon S3 and served from there.

How To Contribute
=================

Fork and send a pull request. Patches are welcome!
