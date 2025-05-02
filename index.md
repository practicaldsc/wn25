---
layout: page
title: 🏡 Home
description: >-
  Course homepage.
nav_order: 1
---

{: .red }
**This is the course website for a previous iteration of the course. If you’re looking for the most recent course website, look at [practicaldsc.org](https://practicaldsc.org).**

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

<!-- 
[Jump to Week 16: Conclusion, Review](#week-16-conclusion-review){: .btn .btn-green } [Announcements 📣](https://edstem.org/us/courses/69737/discussion/5943734){: .btn .btn-purple }
 -->
{% for module in site.modules %}
{{ module }}
{% endfor %}
