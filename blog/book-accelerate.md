<!--
post_description: Book 📖 Notes 📝: Accelerate
-->
[Josh's Blog](https://github.com/seajoshc) - Book 📖 Notes 📝: Accelerate
---

###### Published on 2021-12-XX

Book is basically a deep analysis of [State of DevOps Report](https://duckduckgo.com/?q=state+of+devops+report&ia=web) data and a bunch of insights that came out of that. 

High performers compared to low in 2017
- 46 times more frequent code deployments
- 440 times faster lead time from commit to deploy
- 170 times faster mean time to recover from downtime
- 5 times lower change failure rate (1/5 as likely for a change to fail)

Software Delivery Performance
- Lead Time
- Deployment Frequency
- Mean Time to Restore
- Change Fail Percentage
    - tl;dr this one is somewhat of an outlier, only the above 3 form a valid and reliable statistical "construct"

Good information flow is critical, duh

Team Dyanmics are still the most important thing, duh

[Westrum Culture](https://cloud.google.com/architecture/devops/devops-culture-westrum-organizational-culture)
- Pathological - power oriented
- Bureaucratic - rule oriented
- Generative - performance oriented * spoiler alert you want this one

Continuous Delivery and Lean Management together impact culture in a positive way, these are the things to go after

## Continuous Delivery

- Build quality in - tools and people can detect issues quickly
- Work in small batches - small commits, small chunks of work
- Automate - computers perform repetitive tasks, humans solve problems
- Strive to get better - relentlessly pursue continuous improvement
- Everyone is responsible - this is the only way you get to a generative culture

CD needs the following foundational things:
- Comprehensive config management - aka version control and automate everything
- Continuous integration - high quality, small changes incorporated constantly
- Continuous testing - testing is integral and should be done all the time at all stages

Implementing Continuous Delivery means creating multiple feedback loops to ensure that high-quality software gets delivered to users more frequently and more reliably.

Impact CD tends to have:
- Help reduce team burnout and deployment pain
- Teams identify more strongly with their org/company
- Directly shown to improve culture, works feels better
- Teams can deploy to prod on demand
- Fast feedback on quality and deployability
- Loosely coupled, well-encapsulated architecture tends to organically happen in CD environments
- Teams can choose their own tools
- Higher levels of software delivery performance (lead time, deploy frequency, time to restore)
- Lower change fail rate
- Generative culture
- Better quality and performance of software 
- Decreased percentage of time spent on rework or unplanned work (break/fix, patches, rollbacks, etc.)
- Decreased percentage of time spent on defects identified by users

Continuous Delivery predicts lower levels of unplanned work and rework in a statistically significant way.

Important takeaways:
- Keeping system and app configuration in version control was more highly correlated with software delivery performance than keeping app code in version control
- Having automated tests that are reliable is important. Flaky tests should be rooted out.
- Automated tests are super important and should run all the time (e.g. on commit/push)
- Trunk based development with few short-lived branches is correlated to higher software delivery performance
- CD requires substantial investment in test and deployment automation combined with relentless work to simplify systems and architecture on an on-going basis
