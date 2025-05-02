---
layout: page
title: 🏡 Home
description: >-
  Course homepage.
nav_order: 1
---

# Practical Data Science 🛠️
{: .no_toc }
{: .mb-2 }
EECS 398, Winter 2025 at the <b><span style="background-color: #FFCB05; color: #00274C">University of Michigan</span></b>
{: .no_toc }
{: .fs-6 .fw-300 .mb-2 }

<!-- 4 credits • Open to all majors • ULCS for Computer Science majors, Advanced Technical Elective or Application Elective for Data Science majors, Flexible Technical Elective for Electrical Engineering majors -->

{% for staffer in site.staffersnobio %}
{{ staffer }}
{% endfor %}

{: .green }
> The Final Exam is on **Monday, April 28th from 10:30AM-12:30PM**. Find your assigned room and other logistics [**here**](https://edstem.org/us/courses/69737/discussion/6600862).
>
> We have one more review session this week, on Saturday 4/26 from 1-3PM in 1670 BBB. Attempt the worksheet (linked below) **before** coming.

[Jump to Week 16: Conclusion, Review](#week-16-conclusion-review){: .btn .btn-green } [Announcements 📣](https://edstem.org/us/courses/69737/discussion/5943734){: .btn .btn-purple }

{% for module in site.modules %}
{{ module }}
{% endfor %}
