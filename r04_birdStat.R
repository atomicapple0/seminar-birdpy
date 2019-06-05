#delete dataframes
ls()
rm(list = ls())

library(readr)
library(dplyr)
library(ggpubr)

years = 2000:2018

#import shit
folder <- "/Users/brian/Desktop/birdPy/c03_robin/"
file_list <- list.files(path=folder, pattern="*.csv")


for (i in 1:length(file_list)){
  
  assign(paste('robin', substr(file_list[i],11,14), sep=''), 
         
         read_csv(paste(folder, file_list[i], sep=''), 
                  col_types = cols(X1 = col_skip(), 
                              date = col_date(format = '%Y-%m-%d'),
                              urban = col_factor(levels = c("0", "1"))
                  )
         )
  )
}


robin = robin2018
head(robin)
levels(robnin$urban)

robinRural = filter(robin,urban == '0')
robinUrban = filter(robin,urban == '1')

vecRural <- rep(robinRural$date, robinRural$count)
vecUrban <- rep(robinUrban$date, robinUrban$count)

df <- data.frame(urban=c(rep("rural", times=length(vecRural)), 
                        rep("urban", times=length(vecUrban))), 
                 date=c(vecRural, vecUrban))

df

gghistogram(df, x = 'date', color = 'urban', fill = "urban",
            palette = c("#00AFBB", "#E7B800"))

ggline(df, x = "urban", y = "date", 
       order = c("rural", "urban"),
       ylab = "date", xlab = "urban")

kruskal.test(date ~ urban, data = robin)

ggplot(df, aes(x = date)) +
  geom_histogram(aes(y = ..density.. * 5), binwidth = 5) +
  facet_grid(urban ~ .) +
  labs(title = "Size by Year", x = "date", y = "frequency") +
  scale_x_continuous(breaks = scales::pretty_breaks(n = 10)) +
  theme_bw() +
  theme(
    text = element_text(size = 16),
    axis.text.y = element_text(size = 12)
  )




