
#####################################
######## C688 - Assignment 2 ########
#####################################

# Install googleAnalyticsR Package
install.packages("googleAnalyticsR")

# load the googleAnalyticsR Package
library(googleAnalyticsR)
library(ggplot2)

# Authenticate for new user
ga_auth(new_user = TRUE)

# Authorize R to access GA data
ga_auth()

# find your GA viewID
my_accounts <- ga_account_list()

# use my_accounts to find the viewID
my_id <- my_accounts$viewId[1]

# list of possible metrics and dimensions
arguments <- google_analytics_meta()

# Set Date Range
start_date <- "2018-03-18"
end_date <- "2018-03-26"

# list of metrics to use
metrics.topic <- c("pageviews", "sessions", "bounceRate",
                   "totalConversions", "newUsers", "goalCompletionsAll",
                   "users", "sessionDuration", "bounces")

# List of dimensions to use
dimensions.topic <- c("date", "hour", "minute", "pagePath",
                      "source", "medium", "landingPagePath", "deviceCategory")

#Pageview, Sessions, & Bounce Rate Query. Dimension = Date
PageViews <- google_analytics_4(my_id,
                                date_range = c(start_date, end_date),
                                metrics = metrics.topic[1:3],
                                dimensions = dimensions.topic[1])

#Plot of page views by day
ggplot(data=PageViews, aes(x=date, y=pageviews)) +
  geom_line (stat="identity") +
  labs(title = "Page Views by Day")


# filters for device category = desktop
filter1 <- dim_filter("deviceCategory", operator = c("EXACT"), "desktop")
f4 <- filter_clause_ga4(list(filter1), operator = "AND")

# Sessions and Bounces Query with Device category filter
Sessions <- google_analytics_4(my_id, 
                               date_range = c(start_date, end_date),
                               metrics = c("bounces", "sessions"),
                               dimensions = c("source", "deviceCategory"),
                               dim_filters = f4)

# plot of Sessions by Source
barplot(Sessions$sessions, 
        names.arg = c("direct", "onlinecampus.bu.edu",
                      "sites.google.com"),
        xlab = "Source",
        ylab = "Sessions",
        main = "Sessions by Source",
        col = c("royalblue1", "indianred1", "springgreen"))





