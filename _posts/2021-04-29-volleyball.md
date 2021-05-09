---
layout: default
title:  "Volleyball"
description: "Teaching volleyball techniques to a machine"
---

# Teaching volleyball in 5 minutes OR VollAIball

Teaching volleyball techniques to a machine


## Data Collection

### Classes
__Techniques__
<figure style="display: inline-block; margin: 0;">
    <img src="{{ '/assets/forearm.gif' | relative_url }}" alt="Forearm passing" width="150"/>
    <figcaption style="text-align: center;">Forearm Passing</figcaption>
</figure>
<figure style="display: inline-block; margin: 0;">
    <img src="{{ '/assets/overhead.gif' | relative_url }}" alt="Overhead passing" width="150"/>
    <figcaption style="text-align: center;">Overhead Passing</figcaption>
</figure>
<figure style="display: inline-block; margin: 0;">
    <img src="{{ '/assets/onearm.gif' | relative_url }}" alt="One arm passing" width="150"/>
    <figcaption style="text-align: center;">One Arm Passing</figcaption>
</figure>
<figure style="display: inline-block; margin: 0;">
    <img src="{{ '/assets/pokey.gif' | relative_url }}" alt="Pokey" width="150"/>
    <figcaption style="text-align: center;">Pokey</figcaption>
</figure>

__Background__
<figure style="display: inline-block; margin: 0;">
    <img src="{{ '/assets/nothing.gif' | relative_url }}" alt="Doing nothing" width="150"/>
    <figcaption style="text-align: center;">Doing Nothing</figcaption>
</figure>
<figure style="display: inline-block; margin: 0;">
    <img src="{{ '/assets/hold.gif' | relative_url }}" alt="Holding the ball" width="150"/>
    <figcaption style="text-align: center;">Holding</figcaption>
</figure>
<figure style="display: inline-block; margin: 0;">
    <img src="{{ '/assets/bounce.gif' | relative_url }}" alt="Bouncing the ball" width="150"/>
    <figcaption style="text-align: center;">Bouncing</figcaption>
</figure>
<figure style="display: inline-block; margin: 0;">
    <img src="{{ '/assets/drop.gif' | relative_url }}" alt="Dropping the ball" width="150"/>
    <figcaption style="text-align: center;">Dropping</figcaption>
</figure>
<figure style="display: inline-block; margin: 0;">
    <img src="{{ '/assets/leave.gif' | relative_url }}" alt="Leaving" width="150"/>
    <figcaption style="text-align: center;">Leaving</figcaption>
</figure>

### Videos

|     | Training   | Validation
| --- | ---------- | -----------
| Forearm Passing | 4 Videos, 69s | 2 Videos, 14s
| Overhead Passing | 4 Videos, 72s | 2 Videos, 20s
| One Arm Passing | 5 Videos, 38s | 2 Videos, 7s
| Pokey | 6 Videos, 28s | 2 Videos, 6s
| Nothing | 1 Video, 12s | 1 Video, 5s
| Holding | 1 Video, 7s | 1 Video, 6s
| Bouncing | 2 Videos, 14s | 1 Video, 4s
| Dropping | 1 Video, 18s | 1 Video, 12s
| Leaving | 1 Video, 12s | 1 Video, 3s
| __Total__ | __25 Videos, 270s__ | __13 Videos, 77s__


## Classification
![Confusion Matrix]({{ '/assets/confusion_matrix.png' | relative_url }})


## Counting
<video width="100%" controls preload="metadata">
  <source src="{{ '/assets/new_counting_1position_1_v4.webm' | relative_url }}" type="video/webm">
Your browser does not support this video element.
</video> 

|     | Target   | Prediction
| --- | ---------- | -----------
| Forearm Passing | 10 | 9
| Overhead Passing | 20 | 19
| One Arm Passing | 3 | 5
| Pokey | 3 | 3
| Bouncing | 3 | 3


[Home]({{ '/' | relative_url }})
