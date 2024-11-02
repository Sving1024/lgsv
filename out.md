# 【模板】最小生成树
## 题目背景

## 题目描述
如题，给出一个无向图，求出最小生成树，如果该图不连通，则输出 `orz`。

## 输入格式
第一行包含两个整数 $N,M$，表示该图共有 $N$ 个结点和 $M$ 条无向边。

接下来 $M$ 行每行包含三个整数 $X_i,Y_i,Z_i$，表示有一条长度为 $Z_i$ 的无向边连接结点 $X_i,Y_i$。

## 输出格式
如果该图连通，则输出一个整数表示最小生成树的各边的长度之和。如果该图不连通则输出 `orz`。

#### 输入 \#1
```
4 5
1 2 2
1 3 2
1 4 3
2 3 4
3 4 3
```
### 输出 \#1
```
7
```
## 说明/提示
数据规模：

对于 $20\%$ 的数据，$N\le 5$，$M\le 20$。

对于 $40\%$ 的数据，$N\le 50$，$M\le 2500$。

对于 $70\%$ 的数据，$N\le 500$，$M\le 10^4$。

对于 $100\%$ 的数据：$1\le N\le 5000$，$1\le M\le 2\times 10^5$，$1\le Z_i \le 10^4$。


样例解释：

 ![](https://cdn.luogu.com.cn/upload/pic/2259.png) 

所以最小生成树的总边权为 $2+2+3=7$。

# 买礼物
## 题目背景

## 题目描述
又到了一年一度的明明生日了，明明想要买 $B$ 样东西，巧的是，这 $B$ 样东西价格都是 $A$ 元。

但是，商店老板说最近有促销活动，也就是：

如果你买了第 $I$ 样东西，再买第 $J$ 样，那么就可以只花 $K_{I,J}$ 元，更巧的是，$K_{I,J}$ 竟然等于 $K_{J,I}$。

现在明明想知道，他最少要花多少钱。
## 输入格式
第一行两个整数，$A,B$。

接下来 $B$ 行，每行 $B$ 个数，第 $I$ 行第 $J$ 个为 $K_{I,J}$。

我们保证 $K_{I,J}=K_{J,I}$ 并且 $K_{I,I}=0$。

特别的，如果 $K_{I,J}=0$，那么表示这两样东西之间不会导致优惠。

注意 $K_{I,J}$ **可能大于** $A$。
## 输出格式
一个整数，为最小要花的钱数。

#### 输入 \#1
```
1 1
0


```
### 输出 \#1
```
1
```
### 输入 \#1
```
3 3
0 2 4
2 0 2
4 2 0

```
### 输出 \#1
```
7
```
## 说明/提示
样例解释 $2$。

先买第 $2$ 样东西，花费 $3$ 元，接下来因为优惠，买 $1,3$ 样都只要 $2$ 元，共 $7$ 元。

（同时满足多个“优惠”的时候，聪明的明明当然不会选择用 $4$ 元买剩下那件，而选择用 $2$ 元。）

数据规模

对于 $30\%$ 的数据，$1\le B\le 10$。

对于 $100\%$ 的数据，$1\le B\le500,0\le A,K_{I,J}\le1000$。

2018.7.25新添数据一组
# [BJWC2010] 严格次小生成树
## 题目背景

## 题目描述
小 C 最近学了很多最小生成树的算法，Prim 算法、Kruskal 算法、消圈算法等等。正当小 C 洋洋得意之时，小 P 又来泼小 C 冷水了。小 P 说，让小 C 求出一个无向图的次小生成树，而且这个次小生成树还得是严格次小的，也就是说：如果最小生成树选择的边集是 $E_M$，严格次小生成树选择的边集是 $E_S$，那么需要满足：($value(e)$ 表示边 $e$ 的权值) $\sum_{e \in E_M}value(e)<\sum_{e \in E_S}value(e)$。

这下小 C 蒙了，他找到了你，希望你帮他解决这个问题。

## 输入格式
第一行包含两个整数 $N$ 和 $M$，表示无向图的点数与边数。

接下来 $M$ 行，每行 $3$ 个数 $x,y,z$ 表示，点 $x$ 和点 $y$ 之间有一条边，边的权值为 $z$。

## 输出格式
包含一行，仅一个数，表示严格次小生成树的边权和。

#### 输入 \#1
```
5 6
1 2 1 
1 3 2 
2 4 3 
3 5 4 
3 4 3 
4 5 6 
```
### 输出 \#1
```
11
```
## 说明/提示
数据中无向图**不保证无自环**。

对于 $50\%$ 的数据， $N\le 2000$，$M\le 3000$。

对于 $80\%$ 的数据， $N\le 5\times 10^4$，$M\le 10^5$。

对于 $100\%$ 的数据， $N\le 10^5$，$M\le 3\times10^5$，边权  $\in [0,10^9]$，数据保证必定存在严格次小生成树。
# 营救
## 题目背景
“咚咚咚……”“查水表！”原来是查水表来了，现在哪里找这么热心上门的查表员啊！小明感动得热泪盈眶，开起了门……
## 题目描述
妈妈下班回家，街坊邻居说小明被一群陌生人强行押上了警车！妈妈丰富的经验告诉她小明被带到了 $t$ 区，而自己在 $s$ 区。

该市有 $m$ 条大道连接 $n$ 个区，一条大道将两个区相连接，每个大道有一个拥挤度。小明的妈妈虽然很着急，但是不愿意拥挤的人潮冲乱了她优雅的步伐。所以请你帮她规划一条从 $s$ 至 $t$ 的路线，使得经过道路的拥挤度最大值最小。
## 输入格式
第一行有四个用空格隔开的 $n$，$m$，$s$，$t$，其含义见【题目描述】。

接下来 $m$ 行，每行三个整数 $u, v, w$，表示有一条大道连接区 $u$ 和区 $v$，且拥挤度为 $w$。

**两个区之间可能存在多条大道**。
## 输出格式
输出一行一个整数，代表最大的拥挤度。
#### 输入 \#1
```
3 3 1 3
1 2 2
2 3 1
1 3 3
```
### 输出 \#1
```
2

```
## 说明/提示
#### 数据规模与约定

- 对于 $30\%$ 的数据，保证 $n\leq 10$。
- 对于 $60\%$ 的数据，保证 $n\leq 100$。
- 对于 $100\%$ 的数据，保证 $1 \leq n\leq 10^4$，$1 \leq m \leq 2 \times 10^4$，$w \leq 10^4$，$1 \leq s, t \leq n$。且从 $s$ 出发一定能到达 $t$ 区。

--- 

#### 样例输入输出 1 解释

小明的妈妈要从 $1$ 号点去 $3$ 号点，最优路线为 $1$->$2$->$3$。
# 口袋的天空
## 题目背景
小杉坐在教室里，透过口袋一样的窗户看口袋一样的天空。

有很多云飘在那里，看起来很漂亮，小杉想摘下那样美的几朵云，做成棉花糖。

## 题目描述
给你云朵的个数 $N$，再给你 $M$ 个关系，表示哪些云朵可以连在一起。

现在小杉要把所有云朵连成 $K$ 个棉花糖，一个棉花糖最少要用掉一朵云，小杉想知道他怎么连，花费的代价最小。

## 输入格式
第一行有三个数 $N,M,K$。

接下来 $M$ 行每行三个数 $X,Y,L$，表示 $X$ 云和 $Y$ 云可以通过 $L$ 的代价连在一起。



## 输出格式
对每组数据输出一行，仅有一个整数，表示最小的代价。

如果怎么连都连不出 $K$ 个棉花糖，请输出 `No Answer`。

#### 输入 \#1
```
3 1 2
1 2 1

```
### 输出 \#1
```
1
```
## 说明/提示
对于 $30\%$ 的数据，$1 \le N \le 100$，$1\le M \le 10^3$；

对于 $100\%$ 的数据，$1 \le N \le 10^3$，$1 \le M \le 10^4$，$1 \le K \le 10$，$1 \le X,Y \le N$，$0 \le L<10^4$。

# [USACO08OCT] Watering Hole G
## 题目背景

## 题目描述
Farmer John 的农场缺水了。

他决定将水引入到他的 $n$ 个农场。他准备通过挖若干井，并在各块田中修筑水道来连通各块田地以供水。在第 $i$ 号田中挖一口井需要花费 $W_i$ 元。连接 $i$ 号田与 $j$ 号田需要 $P_{i,j}$（$P_{j,i}=P_{i,j}$）元。

请求出 FJ 需要为使所有农场都与有水的农场相连或拥有水井所需要的最少钱数。
## 输入格式
第一行为一个整数 $n$。

接下来 $n$ 行，每行一个整数 $W_i$。

接下来 $n$ 行，每行 $n$ 个整数，第 $i$ 行的第 $j$ 个数表示连接 $i$ 号田和 $j$ 号田需要的费用 $P_{i,j}$。
## 输出格式
输出最小开销。

#### 输入 \#1
```
4
5
4
4
3
0 2 2 2
2 0 3 3
2 3 0 4
2 3 4 0
```
### 输出 \#1
```
9
```
## 说明/提示
对于 $100\%$ 的数据，$1 \leq n \leq 300$，$1 \leq W_i \leq 10^5$，$0 \leq P_{i,j} \leq 10^5$。
# [NOIP2013 提高组] 货车运输
## 题目背景
NOIP2013 提高组 D1T3
## 题目描述
A 国有 $n$ 座城市，编号从 $1$ 到 $n$，城市之间有 $m$ 条双向道路。每一条道路对车辆都有重量限制，简称限重。  

现在有 $q$ 辆货车在运输货物， 司机们想知道每辆车在不超过车辆限重的情况下，最多能运多重的货物。

## 输入格式
第一行有两个用一个空格隔开的整数 $n,m$，表示 A 国有 $n$ 座城市和 $m$ 条道路。  

接下来 $m$ 行每行三个整数 $x, y, z$，每两个整数之间用一个空格隔开，表示从 $x$ 号城市到 $y$ 号城市有一条限重为 $z$ 的道路。    
注意： $x \neq y$，两座城市之间可能有多条道路 。

接下来一行有一个整数 $q$，表示有 $q$ 辆货车需要运货。

接下来 $q$ 行，每行两个整数 $x,y$，之间用一个空格隔开，表示一辆货车需要从 $x$ 城市运输货物到 $y$ 城市，保证 $x \neq y$

## 输出格式
共有 $q$ 行，每行一个整数，表示对于每一辆货车，它的最大载重是多少。  
如果货车不能到达目的地，输出 $-1$。

#### 输入 \#1
```
4 3
1 2 4
2 3 3
3 1 1
3
1 3
1 4
1 3
```
### 输出 \#1
```
3
-1
3
```
## 说明/提示
对于 $30\%$ 的数据，$1 \le n < 1000$，$1 \le m < 10,000$，$1\le q< 1000$；

对于 $60\%$ 的数据，$1 \le n < 1000$，$1 \le m < 5\times 10^4$，$1 \le q< 1000$；

对于 $100\%$ 的数据，$1 \le n < 10^4$，$1 \le m < 5\times 10^4$，$1 \le q< 3\times 10^4$，$0 \le z \le 10^5$。

# 逐个击破
## 题目背景
三大战役的平津战场上，傅作义集团在以北平、天津为中心，东起唐山西至张家口的铁路线上摆起子一字长蛇阵，并企图在溃败时从海上南逃或向西逃窜。为了就地歼敌不让其逃走，指挥官制定了先切断敌人东西两头退路然后再逐个歼灭敌人的战略方针。秉承伟大军事家的战略思想，作为一个有智慧的军长你，遇到了一个类似的战场局面。

## 题目描述
现在有 $N$ 个城市，其中 $K$ 个被敌方军团占领了，$N$ 个城市间有 $N-1$ 条公路相连，破坏其中某条公路的代价是已知的，现在，告诉你 $K$ 个敌方军团所在的城市，以及所有公路破坏的代价，请你算出花费最少的代价将这 $K$ 个地方军团互相隔离开，以便第二步逐个击破敌人。

## 输入格式
第一行包含两个正整数 $N$ 和 $K$。

第二行包含 $K$ 个整数，表示哪个城市被敌军占领。

接下来 $N-1$ 行，每行包含三个正整数 $a,b,c$，表示从 $a$ 城市到 $b$ 城市有一条公路，以及破坏的代价 $c$。城市的编号从 $0$ 开始。

## 输出格式
输出一行一个整数，表示最少花费的代价。

#### 输入 \#1
```
5 3
1 2 4
1 0 4
1 3 8
2 1 1
2 4 3
```
### 输出 \#1
```
4
```
## 说明/提示
对于 $10\%$ 的数据，$N\le 10$。

对于 $100\%$ 的数据，$2\le N\le10^5$，$2\le K\le N$，$1\le c\le 10^6$。

# Shichikuji and Power Grid
## 题目背景

## 题目描述
Shichikuji is the new resident deity of the South Black Snail Temple. Her first job is as follows:

There are $n$ new cities located in Prefecture X. Cities are numbered from $1$ to $n$ . City $i$ is located $x_i$ km North of the shrine and $y_i$ km East of the shrine. It is possible that $(x_i, y_i) = (x_j, y_j)$ even when $i \ne j$ .

Shichikuji must provide electricity to each city either by building a power station in that city, or by making a connection between that city and another one that already has electricity. So the City has electricity if it has a power station in it or it is connected to a City which has electricity by a direct connection or via a chain of connections.

- Building a power station in City $i$ will cost $c_i$ yen;
- Making a connection between City $i$ and City $j$ will cost $k_i + k_j$ yen per km of wire used for the connection. However, wires can only go the cardinal directions (North, South, East, West). Wires can cross each other. Each wire must have both of its endpoints in some cities. If City $i$ and City $j$ are connected by a wire, the wire will go through any shortest path from City $i$ to City $j$ . Thus, the length of the wire if City $i$ and City $j$ are connected is $|x_i - x_j| + |y_i - y_j|$ km.

Shichikuji wants to do this job spending as little money as possible, since according to her, there isn't really anything else in the world other than money. However, she died when she was only in fifth grade so she is not smart enough for this. And thus, the new resident deity asks for your help.

And so, you have to provide Shichikuji with the following information: minimum amount of yen needed to provide electricity to all cities, the cities in which power stations will be built, and the connections to be made.

If there are multiple ways to choose the cities and the connections to obtain the construction of minimum price, then print any of them.
## 输入格式
First line of input contains a single integer $n$ ( $1 \leq n \leq 2000$ ) — the number of cities.

Then, $n$ lines follow. The $i$ -th line contains two space-separated integers $x_i$ ( $1 \leq x_i \leq 10^6$ ) and $y_i$ ( $1 \leq y_i \leq 10^6$ ) — the coordinates of the $i$ -th city.

The next line contains $n$ space-separated integers $c_1, c_2, \dots, c_n$ ( $1 \leq c_i \leq 10^9$ ) — the cost of building a power station in the $i$ -th city.

The last line contains $n$ space-separated integers $k_1, k_2, \dots, k_n$ ( $1 \leq k_i \leq 10^9$ ).
## 输出格式
In the first line print a single integer, denoting the minimum amount of yen needed.

Then, print an integer $v$ — the number of power stations to be built.

Next, print $v$ space-separated integers, denoting the indices of cities in which a power station will be built. Each number should be from $1$ to $n$ and all numbers should be pairwise distinct. You can print the numbers in arbitrary order.

After that, print an integer $e$ — the number of connections to be made.

Finally, print $e$ pairs of integers $a$ and $b$ ( $1 \le a, b \le n$ , $a \ne b$ ), denoting that a connection between City $a$ and City $b$ will be made. Each unordered pair of cities should be included at most once (for each $(a, b)$ there should be no more $(a, b)$ or $(b, a)$ pairs). You can print the pairs in arbitrary order.

If there are multiple ways to choose the cities and the connections to obtain the construction of minimum price, then print any of them.
#### 输入 \#1
```
3
2 3
1 1
3 2
3 2 3
3 2 3

```
### 输出 \#1
```
8
3
1 2 3 
0

```
### 输入 \#1
```
3
2 1
1 2
3 3
23 2 23
3 2 3

```
### 输出 \#1
```
27
1
2 
2
1 2
2 3

```
## 说明/提示
For the answers given in the samples, refer to the following diagrams (cities with power stations are colored green, other cities are colored blue, and wires are colored red):

![](https://cdn.luogu.com.cn/upload/vjudge_pic/CF1245D/251d50cda099f4e4be2994b6b01574cc32a17cd3.png)

For the first example, the cost of building power stations in all cities is $3 + 2 + 3 = 8$ . It can be shown that no configuration costs less than 8 yen.

For the second example, the cost of building a power station in City 2 is 2. The cost of connecting City 1 and City 2 is $2 \cdot (3 + 2) = 10$ . The cost of connecting City 2 and City 3 is $3 \cdot (2 + 3) = 15$ . Thus the total cost is $2 + 10 + 15 = 27$ . It can be shown that no configuration costs less than 27 yen.
# [APIO2008] 免费道路
## 题目背景

## 题目描述
 
新亚（New Asia）王国有 N 个村庄，由 M 条道路连接。其中一些道路是鹅卵石路，而其它道路是水泥路。保持道路免费运行需要一大笔费用，并且看上去 王国不可能保持所有道路免费。为此亟待制定一个新的道路维护计划。

国王已决定保持尽可能少的道路免费，但是两个不同的村庄之间都应该一条且仅由一条 且仅由一条免费道路的路径连接。同时，虽然水泥路更适合现代交通的需 要，但国王也认为走在鹅卵石路上是一件有趣的事情。所以，国王决定保持刚好 K 条鹅卵石路免费。

举例来说，假定新亚王国的村庄和道路如图 3(a)所示。如果国王希望保持两 条鹅卵石路免费，那么可以如图 3(b)中那样保持道路(1, 2)、(2, 3)、(3, 4)和(3, 5) 免费。该方案满足了国王的要求，因为：(1)两个村庄之间都有一条由免费道 路组成的路径；(2)免费的道路已尽可能少；(3)方案中刚好有两条鹅卵石道路 (2, 3)和(3, 4)

 ![](https://cdn.luogu.com.cn/upload/pic/4393.png) 

图 3: (a)新亚王国中村庄和道路的一个示例。实线标注的是水泥路，虚线标注 的是鹅卵石路。(b)一个保持两条鹅卵石路免费的维护方案。图中仅标出了免 费道路。


给定一个关于新亚王国村庄和道路的述以及国王决定保持免费的鹅卵石 道路数目，写一个程序确定是否存在一个道路维护计划以满足国王的要求，如果 存在则任意输出一个方案。

## 输入格式
输入第一行包含三个由空格隔开的整数：

N，村庄的数目(1≤N≤20,000)；

M，道路的数目(1≤M≤100,000)；

K，国王希望保持免费的鹅卵石道路数目(0≤K≤N - 1)。

此后 M 行述了新亚王国的道路，编号分别为 1 到 M。第(i+1)行述了第 i 条 道路的情况。用 3 个由空格隔开的整数述：

ui 和 vi，为第 i 条道路连接的两个村庄的编号，村庄编号为 1 到 N；

ci，表示第 i 条道路的类型。ci = 0 表示第 i 条道路是鹅卵石路，ci = 1 表 示第 i 条道路是水泥路。

输入数据保证一对村庄之间至多有一条道路连接

## 输出格式
如果满足国王要求的道路维护方案不存在，你的程序应该在输出第一行打印 no solution。 否则，你的程序应该输出一个符合要求的道路维护方案，也就是保持免费的 道路列表。按照输入中给定的那样输出免费的道路。如果有多种合法方案，你可 以任意输出一种。

#### 输入 \#1
```
5 7 2 
1 3 0 
4 5 1 
3 2 0 
5 3 1 
4 3 0 
1 2 1 
4 2 1
```
### 输出 \#1
```
3 2 0 
4 3 0 
5 3 1 
1 2 1 
```
## 说明/提示

# Power Tree
## 题目背景

## 题目描述
You are given a rooted tree with $n$ vertices, the root of the tree is the vertex $1$ . Each vertex has some non-negative price. A leaf of the tree is a non-root vertex that has degree $1$ .

Arkady and Vasily play a strange game on the tree. The game consists of three stages. On the first stage Arkady buys some non-empty set of vertices of the tree. On the second stage Vasily puts some integers into all leaves of the tree. On the third stage Arkady can perform several (possibly none) operations of the following kind: choose some vertex $v$ he bought on the first stage and some integer $x$ , and then add $x$ to all integers in the leaves in the subtree of $v$ . The integer $x$ can be positive, negative of zero.

A leaf $a$ is in the subtree of a vertex $b$ if and only if the simple path between $a$ and the root goes through $b$ .

Arkady's task is to make all integers in the leaves equal to zero. What is the minimum total cost $s$ he has to pay on the first stage to guarantee his own win independently of the integers Vasily puts on the second stage? Also, we ask you to find all such vertices that there is an optimal (i.e. with cost $s$ ) set of vertices containing this one such that Arkady can guarantee his own win buying this set on the first stage.
## 输入格式
The first line contains a single integer $n$ ( $2 \le n \le 200\,000$ ) — the number of vertices in the tree.

The second line contains $n$ integers $c_1, c_2, \ldots, c_n$ ( $0 \le c_i \le 10^9$ ), where $c_i$ is the price of the $i$ -th vertex.

Each of the next $n - 1$ lines contains two integers $a$ and $b$ ( $1 \le a, b \le n$ ), denoting an edge of the tree.
## 输出格式
In the first line print two integers: the minimum possible cost $s$ Arkady has to pay to guarantee his own win, and the number of vertices $k$ that belong to at least one optimal set.

In the second line print $k$ distinct integers in increasing order the indices of the vertices that belong to at least one optimal set.
#### 输入 \#1
```
5
5 1 3 2 1
1 2
2 3
2 4
1 5

```
### 输出 \#1
```
4 3
2 4 5 

```
### 输入 \#1
```
3
1 1 1
1 2
1 3

```
### 输出 \#1
```
2 3
1 2 3 

```
## 说明/提示
In the second example all sets of two vertices are optimal. So, each vertex is in at least one optimal set.
