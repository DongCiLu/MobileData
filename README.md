# Speed estimation of cellular network access data
Speed estimation with coarse-grained location information in cellular network access traces and find correlation of user speed and smartphone app / mobile data usage.

See more details in our paper: [Inferring Correlation between User Mobility and App Usage in Massive Coarse-grained Data Traces](http://yunhefeng.me/material/App_Speed.pdf)

## Dataset example:
Our dataset contains mobile network access data of nearly 1 million unique users in three Chinese city for about 3-hour length.
Here is an example of trajectory and the cellular network access records of a single user:

<img src="/example/example.png" width="500px"/>  

## System overview:
In our system, we create a distance estimation filter based on the tower boundary-to-boundary distance lower bound based on Voronoi diagram to filter out poor quality distance estimations. Base on the distance estimates and travel time estimates, we are able to estimate user speed and study its correlation with user smartphone app usage.

<img src="/example/system_overview.png" width="700px"/> 

### Distance lower bound in Voronoi Diagram
Our main idea to improve distance estimation accuracy is the use of distance lower bound filter. Here shows a common scene that why distance estimates can easily fail with coarse-grained location information normally found in cell phone traces. Our distance lower bound filter also helps with cell oscillation problem. Please see more details in our [paper](http://yunhefeng.me/material/App_Speed.pdf).

<img src="/example/distance_lb.png" width="500px"/> 

## Speed estimation error
By filtering out poor quality distance estimates, we are able to achieve higher speed estimation performance. Note that our distance lower bound filter can be applied to any distance estimation algorithm. Here we show the accuracy improvements of our algorithm:

<img src="/example/error_cdf.png" width="450px"/>

## Correlation of user speed and smartphone app usage
Here we shows the correlation of estimated speed and different category of smartphone apps usage. More results can be found in our [paper](http://yunhefeng.me/material/App_Speed.pdf).

<img src="/example/correlation.png" width="900px"/>
