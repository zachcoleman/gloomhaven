# Gloomhaven Damage Simulator

Attack modifier deck simulator and probability calculator for the popular board game and Steam game Gloomhaven. The probablity calculations are non-trivial given the re-shuffling logic.


## Installation
To install base dependencies use:
```shell
poetry install
```
To install the additional dependencies for running the example notebooks use:
```shell
poetry install -E analyze
```

## Example
Here's an example of the calculated probabilities for the base modifier deck:

<h3 align=left> Attack PDFs </h3>

![](./assets/base_deck.jpg)

<h3 align=left> Attack CDF Table </h3>

<table border="0" class="dataframe table">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>base_attack_1</th>
      <th>base_attack_2</th>
      <th>base_attack_3</th>
      <th>base_attack_4</th>
      <th>base_attack_5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.3491</td>
      <td>0.1228</td>
      <td>0.0636</td>
      <td>0.0704</td>
      <td>0.0736</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.6407</td>
      <td>0.3576</td>
      <td>0.1115</td>
      <td>0.0704</td>
      <td>0.0736</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.9506</td>
      <td>0.6484</td>
      <td>0.3521</td>
      <td>0.1191</td>
      <td>0.0736</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.0000</td>
      <td>0.8851</td>
      <td>0.6341</td>
      <td>0.3616</td>
      <td>0.1228</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.0000</td>
      <td>1.0000</td>
      <td>0.8768</td>
      <td>0.6456</td>
      <td>0.3635</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1.0000</td>
      <td>1.0000</td>
      <td>0.9266</td>
      <td>0.8805</td>
      <td>0.6453</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1.0000</td>
      <td>1.0000</td>
      <td>1.0000</td>
      <td>0.9289</td>
      <td>0.8840</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1.0000</td>
      <td>1.0000</td>
      <td>1.0000</td>
      <td>0.9289</td>
      <td>0.9310</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1.0000</td>
      <td>1.0000</td>
      <td>1.0000</td>
      <td>1.0000</td>
      <td>0.9310</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1.0000</td>
      <td>1.0000</td>
      <td>1.0000</td>
      <td>1.0000</td>
      <td>1.0000</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1.0000</td>
      <td>1.0000</td>
      <td>1.0000</td>
      <td>1.0000</td>
      <td>1.0000</td>
    </tr>
  </tbody>
</table>

<h3 align=left> Attack Summary Stats Table </h3>


<table border="0" class="dataframe table">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>base_attack_1</th>
      <th>base_attack_2</th>
      <th>base_attack_3</th>
      <th>base_attack_4</th>
      <th>base_attack_5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>min</th>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>median</th>
      <td>1.000000</td>
      <td>2.000000</td>
      <td>3.000000</td>
      <td>4.000000</td>
      <td>5.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>3.000000</td>
      <td>4.000000</td>
      <td>6.000000</td>
      <td>8.000000</td>
      <td>10.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>1.059600</td>
      <td>1.986100</td>
      <td>3.035300</td>
      <td>3.994600</td>
      <td>4.970600</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.923652</td>
      <td>1.192581</td>
      <td>1.451229</td>
      <td>1.769204</td>
      <td>2.104466</td>
    </tr>
    <tr>
      <th>mode</th>
      <td>0.000000</td>
      <td>2.000000</td>
      <td>3.000000</td>
      <td>4.000000</td>
      <td>5.000000</td>
    </tr>
  </tbody>
</table>