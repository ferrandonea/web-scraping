# bs4 alternativas
Probando alternativas a bs4 / BeautifoulSoup o como se escriba

* BS4 es medio lento
* Una alternativa es [parsel](https://pypi.org/project/parsel/parsel), pero está construido sobre lxml, aunque es un poco más liviando que bs4 y tiene selectores específicos de CSS, viene de scrapy parece
* [Selectolax](https://github.com/rushter/selectolax) está programado por debajo en C o similar y es más rápido, viene de [Modest](https://github.com/lexborisov/Modest) (que está en C)
    * los selector son más fáciles de obtener al demás
