# Week 3 worksheet
The goal of today is to explore the 'carbon footprint' (related to embodied energy) of **your own** digital appliances and devices that you identified last week.  Unlike direct energy use, the energy here is required *at all stages* of the manufacturing pipeline, so the carbon footprint relates to mining of raw materials, processing, transportation, manufacturing, shipping and all the other items that come together to make your products and get them in your hands.  We'll have a lecture on what this really is later in the course!

## Cautionary note
The carbon footprint of each device is at best an estimate of the average or typical embodied energy, as the supply chains are often *very long and complex*.  They also differ between even similar products, and change over time (e.g. a market might source from different suppliers, transport or recycle differently etc.).

1. You may get differences in estimates, or only be able to get an estimate for a device that's as similar as possible to the one you have.  Try to sense check what you find, web searches/AI summaries are notorious for giving you spurious results - try multiple sources to see if they're in the same ball park!
2. Sometimes manufacturers and resellers will list the carbon footprint, there's *always* questions we should ask about whether we can rely on the data - data can be old, contain errors, or it may be in their interest to 'scope' the estimate to make their products look good
3. We may have to start caring more about data quality, e.g. published peer reviews in reputable journals with 'life cycle assessments' (LCA) analysis are likely to be the most reliable sources (more on this in a later lecture) - you may need to find figures that reputable sources rely upon

Since this is just a short lab task, approximate 'ball park' estimates are good enough to 'get an idea'.

## Task

Time available: 1 hour:

Make sure you have an up to date copy of your coursework repo available (`git clone` or `git pull` as needed to ensure you are up to date with the server), as before.  In the '`week3`' folder create a new markdown document called `username-week3-labnotes.md`, where 'username' is of course *your username*!

1. For each photo that you used last week, put a subheading that describes it
2. Look up the carbon footprint of the device's manufacture, if possible you may be able to identify and remove the use phase emissions included in the estimate
3. Add a table.  Bring over the annual energy use of the device based on your use pattern.  Add a column converting energy to CO<sub>2</sub>e by multiplying by a conversion factor representing the UK energy mix (*take care with your units!*).  In UK you can assume the energy mix is **0.35401 KgCO<sub>2</sub>e**^[Figure from 2025, [Department for Energy Security and Net Zero.](https://www.gov.uk/government/publications/greenhouse-gas-reporting-conversion-factors-2025)]
4. Add a column with the carbon footprint for the device
5. Now add a row comparing the annual use energy footprint from last week with the embodied footprint per year (i.e. calculate the 'footprint per year' of embodied CO<sub>2</sub>e by dividing it by the number of years you keep the device).
6. You should add a row for different lifetimes 1, 3 and 5 years, showing the cumulative energy from use emissions vs. the footprint per year.  A crossing point where use overtakes embodied might be evidence for some devices.  In reality, some devices have shorter lifespans than this, but many (e.g. TVs, ovens) could last much longer.
7. Add a subsection `## Reflections` with a short paragraph on your thoughts on how the various assets compare with one another, especially reflecting on the use phase related energy against the manufacturing or embodied energy.

Don't forget to `git add` your new file, `commit` and `push` to the server at least at the end of the task.

## Learning outcomes
* You should have an appreciation of how the embodied energy varies with the appliances and devices you use most often
* You should appreciate how embodied energy is amortised over the life of the device, and how this varies with longevity
* You should see how use phase and embodied phase vary considerably across devices
* You should be gaining some or enhancing your 'carbon literacy' i.e. how 'expensive' different devices are to run and to make.

## Starting points
Here are some useful digital resources to help.  As before, very interested in which ones (or others) you actually use or issues you find.  Don't forget, these are starting points, I'm not guaranteeing their quality!  *You should always have an open and enquring mind when it comes to data sources!!*

* [CO<sub>2</sub> Everything](https://www.co2everything.com) - volunteer effort, I've not checked the data!
* [Cloud carbon footprint calculator](https://www.cloudcarbonfootprint.org)
* [Internet use footprint](https://ecotree.green/en/calculate-digital-co2)
* [University of Oxford IT provided figures](https://www.it.ox.ac.uk/article/environment-and-it) - worth reading anyway
* For fun, Small World [Personal carbon footprint calculator](https://www.sw-consulting.co.uk/carbon-calculator)
* [Ethical consumer guides, including technology](https://www.ethicalconsumer.org)