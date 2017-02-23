library(ggplot2)
library(rCharts)
library(lubridate)
library(plyr)
library(dplyr)
library(stringr)

## Read in data
data   <- read.csv("../data/price_place.csv", stringsAsFactors = FALSE)
data$X <- NULL
data$date <- as.Date(data$time)
## process time
time  <- str_replace(data$time, "T", " ")
time  <- laply(time, function(t) t <- str_split(time, "\\.")[[1]][1])


## data(economics, package = "ggplot2")
## econ <- transform(economics, date = as.character(date))
m1 <- mPlot(x = "date",
           y = c("price", "uempmed"),
           cyl  = "type",
           type = "Line", data = data)
m1$set(pointSize = 0, lineWidth = 1)
##m1$print("chart2")
m1$save('../graphs/priceGas.html', standalone = TRUE)

## Plot
ggplot(data = data,
       aes(x   = minute(time),
           y   = price,
           col = type)) + geom_line()
