# Week 2 worksheet
The goal of today is to explore **your own** use and energy data demand of the digital infrastructures and appliances you use, and put this into contrast with other household appliances.  The focus today is on *direct energy* and how this links to *active use patterns* (i.e. *what we do everyday constitutes our energy footprint*).

## Startup task (homework prep)

Spend a few minutes writing a list of the digital and electronic technology you *most use* in the home.  You should aim for 3-5 technology enabled appliances (i.e. with a digital processor and/or Internet or WiFi connected).  This could include smart TVs, computers, smart speakers,games consoles, Wifi routers, and of course mobile phones, etc.

1. Take a photo of it to remind yourself of your inventory while doing the lab
2. If possible / safe to do so, take a picture of the label which explains it's energy use requirement in Watts (this might be listed on a power adapter in some cases or on a small label on the back of the device) - if you can't find it, that's ok, we can look it up online
3. Write down the item, make notes of any attached speaker systems, external hardrives, displays or other items that are needed to enable it to work (e.g. a PC will normally have an external monitor, maybe speakers, and so on) - you'll want to include all the devices that you use in an ensemble like this as one device

You will need to have done this prep work to help you with the in lab task *this week and next*.

## Task

Time available: 1 hour:

Make sure you have an up to date copy of your coursework repo available (`git clone` or `git pull` as needed to ensure you are up to date with the server).  In the '`week2`' folder (make one if you don't already have one) create a new markdown document called `username-week2-labnotes.md` with your markdown editor of choice (where 'username' is of course your windows username, not username ;).

1. For each photo, and while you have time in the lab, put a subheading that describes it
2. Add a little detail on how often you use it and for how long (estimate hours per day, week and year)
3. Using your photos and the resources below, look up how much active power the device uses when in active use and add this to a markdown table under the appropriate heading - [markdown has a special syntax for tables](https://www.markdownguide.org/extended-syntax/#tables)
4. If the device has a different power level when not in use (e.g. on standby or use 0W when powered off when not in use), find out what this is and add it to the table
5. Finally, add a row that calculates the number of kilowatt/hours (divide total in Watts by 1,000 to get kilowatts and multiply by the number of hours of use) based on your estimate of use per day, week and year.  For example, if you had a smart speaker that takes 5W all year round this would be:

$$
\frac{5 \times 365 \times 24}{1000} = 43.8kWh
$$ 

- i.e. 365 days in a year by 24 hours per day to get total hours used, multiplied by the power demand in Watts to get Watt-hours
- divide by 1000 to get kilowatt hours 

6. The task should be time bounded, i.e. you should *not spend* much more than 40 minutes of concentrated time on this task.  I would expect you to find and calculate the power for 3-5 assets in detail in this time.
7. Add a subsection `## Reflections` with a short paragraph on your thoughts on how the various assets compare with one another.  Which uses most energy, which uses least, how does this relate to use time or overall powered on time.  Were there any surprises?

Don't forget to `git add` your new markdown file and week 2 folder, `commit` with a suitable meaningful commit message, and `push` to the server at least at the end of the task.  *The basic rule is to commit whenever sensible milestones on the files have been reached.  You push whenever you want to update the server copy with what you've committed.*

## Extension task

If you want to go further, you could try to approximate:

1. the amount of energy used by network traffic arising from your use of the Internet
2. add further to your reflections paragraph discussing how this compares to the direct energy use of your device
3. how does this compare to a typical washing machine, refrigerator or domestic oven with the use pattern found in your household?

We will not worry yet about the cloud computing data centres, AI workloads or other energy demands that might be triggered by your device use for now.  For example, most of the smart speaker's workload will be outside the device itself!

## Learning outcomes
* You should have an appreciation of the direct energy requirements of the devices you use most often
* You should appreciate their relative energy requirements and how this relates to use
* How the impact of time affects the cumulative energy requirement (i.e. amount over a year)
* You should be increasing your energy literacy and how significant or otherwise an individual's actions are in energy terms

## Starting points
Here are some useful digital resources to help.  As before, very interested in which ones (or others) you actually use.

* [Comprehensive spreadsheet](https://assets.publishing.service.gov.uk/media/62d6de498fa8f50c06b95a3c/2021_Electrical_Products_tables_March_2022_update.xlsx) of typical UK appliance energy demands from gov.uk
* [Typical UK home appliance energy demand summary sheet](https://www.nea.org.uk/wp-content/uploads/2022/03/Electricity-Consumption-Around-the-Home.pdf)
* Climate Savers Computing Initiative [on Wikipedia](https://en.wikipedia.org/wiki/Climate_Savers_Computing_Initiative)
* [What appliances use the most electricity?](https://energysavingtrust.org.uk/top-five-energy-consuming-home-appliances/)
* Energy ratings [on energysavings trust](https://energysavingtrust.org.uk/advice/home-appliances/)
* What is a kilowatt/hour (kWh)? ([YouTube video](https://www.youtube.com/watch?v=SMPhh8gT_1E))
