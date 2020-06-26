# 機器學習
## 蒙地卡羅演算法
- 概念
    - 亂數隨機取樣，紀錄落點處於目標範圍內的點，即可得到範圍值
## 馬可夫系統
- 概念
    - 狀態改變的機率圖
## Gibbs演算法
- 概念
    - 以疊代方式改變初始值的機率取得馬可夫系統穩態
    
        ```py
        p=初始機率
        while True:
            nextp=p*轉換的機率
            if p==nextp:
                p=穩態
                break
            else p=nextp
        ```
## Metropolis-Hasting演算法
- 概念
    - 以疊代方式改變狀態變化的機率取得馬可夫系統穩態

        ```py
        p=初始狀態改變機率
        while True:
            a=流入/流出
            if a<1:
                nextp的流出=p的流出*a
                nextp的流入=p的流入+p的流入*(1-a)
            if p==nextp:
                p=穩態
                break
            else p=nextp
        ```
## 隱馬可夫模型
- 概念
    - 只有外面的特徵，沒有裡面的機率分布
## 維特比演算法
- 概念
    - 以動態規劃演算法求出隱馬可夫模型的表徵的最大可能性

        ```py
        p[0]=表徵的狀態機率
        path+=max(p[0])
        for t in range(1,表徵數):
            for i in 狀態:
                p[t][i]=max(p[t-1][狀態]*狀態改變到i的機率*i是表徵的機率)
            path+=max(p[t])
        path=最高可能性的表徵狀態
        ```
## 遺傳演算法
- 概念
    - 好的基因交配可以有更好的下一代

    ```py
    population = 隨機產生初代
    for i in range(maxgeneration):
        dad=輪盤選擇(population)
        mom=輪盤選擇(population)
        index=random(基因長度)
        newpopulation=dad[:index]+mom[index:]
        number=random(100)
        if(number<突變率*100):
            index=random(基因長度)
            newpopulation=dad[:index]+random(基因種類)+mom[index+1:]   
        population=sort_fitness(newpopulation)
    ```
## EM演算法
- 概念
    - 以疊代更新事件發生的期望值去計算事件源頭產生事件的機率

    ```py
    e=事件
    pa=a源頭初始機率
    pb=b源頭初始機率
    while True:
        for ei in e:
            a=pa^e
            b=pb^e
            wa=a/a+b
            wb=b/a+b
            ea=wa*e
            eb=wb*e
            suma+=ea
            sumb+=eb
        newpa=suma/e的總數
        newpb=sumb/e的總數
        if newp==p: break
    ```

---
- [上課網站](https://gitlab.com/ccckmit/ai2/-/tree/master/python/10-machineLearning)